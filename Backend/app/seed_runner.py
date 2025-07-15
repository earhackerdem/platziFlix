#!/usr/bin/env python3
"""
Seed Runner for Platziflix Platform
Simple script to populate the database with sample data
"""

import os
import sys
import argparse
from pathlib import Path

# Add current directory to Python path
current_dir = Path(__file__).parent
sys.path.insert(0, str(current_dir))

def main():
    """Main function to run the seed"""
    parser = argparse.ArgumentParser(description='Seed the Platziflix database with sample data')
    parser.add_argument('--confirm', '-y', action='store_true', 
                       help='Skip confirmation prompt')
    parser.add_argument('--clear-only', action='store_true',
                       help='Only clear existing data, do not seed')
    
    args = parser.parse_args()
    
    # Import here to avoid issues with path
    from db.seed import seed_database, clear_existing_data
    from db.base import SessionLocal
    
    print("🌱 Platziflix Database Seeder")
    print("=" * 40)
    
    if not args.confirm:
        print("⚠️  This will DELETE all existing data and populate with sample data.")
        response = input("Are you sure you want to continue? (y/N): ")
        if response.lower() not in ['y', 'yes']:
            print("❌ Operation cancelled.")
            return
    
    if args.clear_only:
        print("🧹 Clearing existing data only...")
        db = SessionLocal()
        try:
            clear_existing_data(db)
            print("✅ Data cleared successfully!")
        except Exception as e:
            print(f"❌ Error clearing data: {e}")
        finally:
            db.close()
    else:
        try:
            seed_database()
            print("\n🎉 Seeding completed successfully!")
            print("\nYou can now:")
            print("• Start the FastAPI server")
            print("• Test the API endpoints")
            print("• View the sample data in your database")
        except Exception as e:
            print(f"❌ Error during seeding: {e}")
            sys.exit(1)

if __name__ == "__main__":
    main() 