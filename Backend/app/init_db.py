#!/usr/bin/env python3
"""
Database initialization script for Platziflix
Waits for database to be ready and runs migrations and seeding
"""

import os
import time
import sys
from pathlib import Path

# Add the correct paths to Python path
current_dir = Path(__file__).parent
app_dir = current_dir
parent_dir = current_dir.parent
sys.path.insert(0, str(app_dir))
sys.path.insert(0, str(parent_dir))

# Set the working directory to the app directory
os.chdir(app_dir)

from sqlalchemy import create_engine, text
from sqlalchemy.exc import OperationalError

from core.config import settings
from db.base import Base, engine
from db.seed import seed_database

def wait_for_database(max_retries: int = 30, delay: int = 2) -> bool:
    """
    Wait for database to be ready
    
    Args:
        max_retries: Maximum number of connection attempts
        delay: Delay between attempts in seconds
        
    Returns:
        bool: True if database is ready, False otherwise
    """
    print("🔄 Waiting for database to be ready...")
    
    for attempt in range(max_retries):
        try:
            # Test database connection
            with engine.connect() as conn:
                conn.execute(text("SELECT 1"))
            print("✅ Database is ready!")
            return True
        except OperationalError as e:
            print(f"⏳ Database not ready (attempt {attempt + 1}/{max_retries}): {e}")
            if attempt < max_retries - 1:
                time.sleep(delay)
    
    print("❌ Database failed to become ready after maximum attempts")
    return False

def create_tables():
    """Create all database tables"""
    print("📋 Creating database tables...")
    try:
        Base.metadata.create_all(bind=engine)
        print("✅ Database tables created successfully!")
    except Exception as e:
        print(f"❌ Error creating tables: {e}")
        raise

def initialize_database():
    """Main initialization function"""
    print("🚀 Initializing Platziflix database...")
    print("=" * 50)
    
    # Wait for database to be ready
    if not wait_for_database():
        print("❌ Database initialization failed - database not ready")
        sys.exit(1)
    
    try:
        # Create tables
        create_tables()
        
        # Run seed data
        print("🌱 Running database seed...")
        seed_database()
        
        print("=" * 50)
        print("🎉 Database initialization completed successfully!")
        print("📊 Your Platziflix database is ready with sample data!")
        
    except Exception as e:
        print(f"❌ Database initialization failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    initialize_database() 