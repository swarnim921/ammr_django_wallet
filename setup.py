#!/usr/bin/env python3
"""
Setup script for Django Wallet API
This script helps set up the project environment and dependencies.
"""

import os
import sys
import subprocess
from pathlib import Path

def run_command(command, description):
    """Run a shell command and handle errors."""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed: {e}")
        print(f"Error output: {e.stderr}")
        return False

def check_python_version():
    """Check if Python version is compatible."""
    if sys.version_info < (3, 8):
        print("❌ Python 3.8 or higher is required")
        sys.exit(1)
    print(f"✅ Python {sys.version_info.major}.{sys.version_info.minor} detected")

def create_virtual_environment():
    """Create a virtual environment."""
    if not os.path.exists("venv"):
        return run_command("python -m venv venv", "Creating virtual environment")
    else:
        print("✅ Virtual environment already exists")
        return True

def install_dependencies():
    """Install project dependencies."""
    # Activate virtual environment and install requirements
    if os.name == 'nt':  # Windows
        activate_cmd = "venv\\Scripts\\activate && "
    else:  # Unix/Linux/macOS
        activate_cmd = "source venv/bin/activate && "
    
    return run_command(
        f"{activate_cmd}cd walletsite && pip install -r requirements.txt",
        "Installing dependencies"
    )

def run_migrations():
    """Run Django migrations."""
    if os.name == 'nt':  # Windows
        activate_cmd = "venv\\Scripts\\activate && "
    else:  # Unix/Linux/macOS
        activate_cmd = "source venv/bin/activate && "
    
    return run_command(
        f"{activate_cmd}cd walletsite && python manage.py migrate",
        "Running database migrations"
    )

def create_superuser():
    """Create a superuser account."""
    print("🤔 Would you like to create a superuser account? (y/n): ", end="")
    response = input().lower().strip()
    
    if response in ['y', 'yes']:
        if os.name == 'nt':  # Windows
            activate_cmd = "venv\\Scripts\\activate && "
        else:  # Unix/Linux/macOS
            activate_cmd = "source venv/bin/activate && "
        
        return run_command(
            f"{activate_cmd}cd walletsite && python manage.py createsuperuser",
            "Creating superuser account"
        )
    else:
        print("⏭️ Skipping superuser creation")
        return True

def main():
    """Main setup function."""
    print("🚀 Django Wallet API Setup")
    print("=" * 40)
    
    # Check Python version
    check_python_version()
    
    # Create virtual environment
    if not create_virtual_environment():
        sys.exit(1)
    
    # Install dependencies
    if not install_dependencies():
        sys.exit(1)
    
    # Run migrations
    if not run_migrations():
        sys.exit(1)
    
    # Create superuser
    if not create_superuser():
        sys.exit(1)
    
    print("\n🎉 Setup completed successfully!")
    print("\n📋 Next steps:")
    print("1. Activate the virtual environment:")
    if os.name == 'nt':  # Windows
        print("   venv\\Scripts\\activate")
    else:  # Unix/Linux/macOS
        print("   source venv/bin/activate")
    print("2. Navigate to the project directory:")
    print("   cd walletsite")
    print("3. Start the development server:")
    print("   python manage.py runserver")
    print("4. Open your browser and go to: http://localhost:8000/")
    print("\n📚 For more information, see the README.md file")

if __name__ == "__main__":
    main()
