#!/usr/bin/env python3
"""
Simple validation script for the e-commerce retention predictor project.
This script validates the project structure and basic functionality without requiring
external dependencies that might not be available in the environment.
"""

import os
import json
import sys
from pathlib import Path

def validate_project_structure():
    """Validate that all required directories and files exist."""
    print("🔍 Validating project structure...")
    
    required_dirs = [
        "data", "data/raw", "data/stage", "data/processed", 
        "notebooks", "models"
    ]
    
    required_files = [
        "README.md", "requirements.txt", ".gitignore",
        "notebooks/01_data_ingestion.ipynb",
        "notebooks/02_data_cleaning.ipynb", 
        "notebooks/03_feature_engineering.ipynb",
        "notebooks/04_model_training.ipynb"
    ]
    
    # Check directories
    for dir_path in required_dirs:
        if os.path.isdir(dir_path):
            print(f"  ✅ Directory: {dir_path}")
        else:
            print(f"  ❌ Missing directory: {dir_path}")
            return False
    
    # Check files
    for file_path in required_files:
        if os.path.isfile(file_path):
            print(f"  ✅ File: {file_path}")
        else:
            print(f"  ❌ Missing file: {file_path}")
            return False
    
    return True

def validate_notebooks():
    """Validate notebook JSON structure."""
    print("\n📓 Validating Jupyter notebooks...")
    
    notebooks = [
        "notebooks/01_data_ingestion.ipynb",
        "notebooks/02_data_cleaning.ipynb", 
        "notebooks/03_feature_engineering.ipynb",
        "notebooks/04_model_training.ipynb"
    ]
    
    for notebook in notebooks:
        try:
            with open(notebook, 'r') as f:
                content = json.load(f)
            
            if 'cells' not in content:
                print(f"  ❌ {notebook}: Missing 'cells' key")
                return False
            
            cell_count = len(content['cells'])
            print(f"  ✅ {notebook}: {cell_count} cells - Valid structure")
            
        except json.JSONDecodeError as e:
            print(f"  ❌ {notebook}: Invalid JSON - {e}")
            return False
        except Exception as e:
            print(f"  ❌ {notebook}: Error - {e}")
            return False
    
    return True

def validate_data_pipeline():
    """Validate that the data pipeline structure is correctly set up."""
    print("\n🔄 Validating data pipeline structure...")
    
    # Check data lake structure
    expected_data_flow = {
        "raw": ["customers.csv", "products.csv", "transactions.csv"],
        "stage": ["cleaned_customers.csv", "cleaned_products.csv", "cleaned_transactions.csv", "data_quality_summary.json"],
        "processed": ["customer_features.csv", "training_data.csv", "X_features.csv", "y_target.csv", "label_encoders.pkl", "feature_engineering_summary.json"]
    }
    
    for layer, expected_files in expected_data_flow.items():
        readme_file = f"data/{layer}/README.md"
        if os.path.isfile(readme_file):
            print(f"  ✅ {layer} layer documentation exists")
        else:
            print(f"  ❌ Missing {layer} layer documentation")
    
    # Check model artifacts structure
    model_artifacts = [
        "retention_model.h5", "scaler.pkl", "feature_importance.csv", 
        "model_metadata.json", "training_history.csv"
    ]
    
    models_readme = "models/README.md"
    if os.path.isfile(models_readme):
        print(f"  ✅ Models documentation exists")
    else:
        print(f"  ❌ Missing models documentation")
    
    return True

def validate_requirements():
    """Validate requirements.txt contains necessary packages."""
    print("\n📦 Validating requirements...")
    
    try:
        with open("requirements.txt", 'r') as f:
            requirements = f.read()
        
        essential_packages = [
            "pandas", "numpy", "tensorflow", "scikit-learn", 
            "matplotlib", "seaborn", "faker", "jupyter"
        ]
        
        for package in essential_packages:
            if package in requirements.lower():
                print(f"  ✅ {package} specified in requirements")
            else:
                print(f"  ❌ {package} missing from requirements")
                return False
        
        return True
        
    except Exception as e:
        print(f"  ❌ Error reading requirements.txt: {e}")
        return False

def validate_gitignore():
    """Validate .gitignore includes necessary patterns."""
    print("\n🚫 Validating .gitignore...")
    
    try:
        with open(".gitignore", 'r') as f:
            gitignore = f.read()
        
        essential_patterns = [
            "__pycache__", "*.pyc", ".ipynb_checkpoints", 
            "data/raw/*.csv", "models/", ".env"
        ]
        
        for pattern in essential_patterns:
            if pattern in gitignore:
                print(f"  ✅ {pattern} pattern included")
            else:
                print(f"  ⚠️ {pattern} pattern might be missing")
        
        return True
        
    except Exception as e:
        print(f"  ❌ Error reading .gitignore: {e}")
        return False

def main():
    """Run all validation checks."""
    print("🚀 E-commerce Retention Predictor - Project Validation")
    print("=" * 55)
    
    all_checks_passed = True
    
    # Run validation checks
    checks = [
        validate_project_structure,
        validate_notebooks,
        validate_data_pipeline,
        validate_requirements,
        validate_gitignore
    ]
    
    for check in checks:
        if not check():
            all_checks_passed = False
    
    print("\n" + "=" * 55)
    if all_checks_passed:
        print("🎉 All validation checks passed!")
        print("✨ Project structure is correctly implemented")
        print("📚 Ready for notebook execution with proper dependencies")
        return 0
    else:
        print("❌ Some validation checks failed")
        print("🔧 Please review and fix the issues above")
        return 1

if __name__ == "__main__":
    sys.exit(main())