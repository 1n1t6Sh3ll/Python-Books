#!/usr/bin/env python3
"""
Python Learning Roadmap - Repository Setup Script
This script creates the complete directory structure for the repository
"""

import os
from pathlib import Path

def create_directory_structure():
    """Create the complete directory structure for the Python roadmap"""
    
    # Base structure
    directories = [
        # Beginner Level
        "01-Beginner/Books",
        "01-Beginner/Videos",
        "01-Beginner/PDFs",
        "01-Beginner/Exercises",
        "01-Beginner/Projects",
        
        # Intermediate Level
        "02-Intermediate/Books",
        "02-Intermediate/Videos",
        "02-Intermediate/PDFs",
        "02-Intermediate/Exercises",
        "02-Intermediate/Projects",
        
        # Advanced Level
        "03-Advanced/Books",
        "03-Advanced/Videos",
        "03-Advanced/PDFs",
        "03-Advanced/Exercises",
        "03-Advanced/Projects",
        
        # Specializations
        "04-Specializations/Web-Development/Django",
        "04-Specializations/Web-Development/Flask",
        "04-Specializations/Web-Development/FastAPI",
        "04-Specializations/Data-Science/NumPy-Pandas",
        "04-Specializations/Data-Science/Visualization",
        "04-Specializations/Data-Science/Projects",
        "04-Specializations/Machine-Learning/Scikit-Learn",
        "04-Specializations/Machine-Learning/Deep-Learning",
        "04-Specializations/Machine-Learning/NLP",
        "04-Specializations/Machine-Learning/Computer-Vision",
        "04-Specializations/Automation/Web-Scraping",
        "04-Specializations/Automation/Task-Automation",
        "04-Specializations/Automation/Scripts",
        "04-Specializations/DevOps/Docker",
        "04-Specializations/DevOps/CI-CD",
        "04-Specializations/DevOps/Cloud",
        
        # Interview Prep
        "05-Interview-Prep/Coding-Challenges/Easy",
        "05-Interview-Prep/Coding-Challenges/Medium",
        "05-Interview-Prep/Coding-Challenges/Hard",
        "05-Interview-Prep/System-Design",
        "05-Interview-Prep/Common-Questions",
        
        # Cheatsheets
        "06-Cheatsheets",
        
        # Tools and Setup
        "07-Tools-and-Setup/Installation-Guides",
        "07-Tools-and-Setup/IDE-Configuration",
        "07-Tools-and-Setup/Git-Setup",
    ]
    
    print("Creating directory structure...")
    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)
        print(f"✓ Created: {directory}")
    
    print("\n" + "="*50)
    print("Creating README files for each section...")
    create_readme_files()
    
    print("\n" + "="*50)
    print("✓ Directory structure created successfully!")
    print("\nNext steps:")
    print("1. Add your resources (books, videos, PDFs) to appropriate folders")
    print("2. Initialize git: git init")
    print("3. Add files: git add .")
    print("4. Commit: git commit -m 'Initial commit'")
    print("5. Create GitHub repo and push")

def create_readme_files():
    """Create README.md files for major sections"""
    
    readmes = {
        "01-Beginner/README.md": """# Beginner Level

## What You'll Learn
- Python basics and syntax
- Core programming concepts
- Simple projects to build confidence

## Recommended Order
1. Setup Python environment
2. Learn basic syntax
3. Practice with exercises
4. Build simple projects

## Resources
- Check the `Books/` folder for beginner-friendly books
- Watch tutorials in the `Videos/` folder
- Practice with exercises in the `Exercises/` folder
""",
        
        "02-Intermediate/README.md": """# Intermediate Level

## What You'll Learn
- Object-Oriented Programming
- Working with databases
- Web development basics
- API integration

## Prerequisites
- Completed Beginner level
- Comfortable with Python syntax
- Built at least 2-3 simple projects

## Resources
- Check folders for curated materials
- Focus on building larger projects
""",
        
        "03-Advanced/README.md": """# Advanced Level

## What You'll Learn
- Advanced Python concepts
- Performance optimization
- Design patterns
- Async programming

## Prerequisites
- Strong foundation in Python
- Experience with multiple projects
- Understanding of OOP principles
""",
        
        "04-Specializations/README.md": """# Specialization Tracks

Choose a track based on your career goals:

## Web Development
Full-stack web development with Python frameworks

## Data Science
Data analysis, visualization, and insights

## Machine Learning
AI and ML model development

## Automation
Scripting and task automation

## DevOps
Infrastructure and deployment
""",
        
        "05-Interview-Prep/README.md": """# Interview Preparation

## Contents
- Coding challenges organized by difficulty
- System design questions
- Common Python interview questions
- Tips and strategies

## How to Use
1. Start with Easy challenges
2. Progress to Medium and Hard
3. Practice system design
4. Review common questions regularly
""",
        
        "06-Cheatsheets/README.md": """# Cheatsheets

Quick reference guides for:
- Python syntax
- Data structures
- Common algorithms
- Standard library
- Best practices

Perfect for quick review before interviews or projects!
""",
        
        "07-Tools-and-Setup/README.md": """# Tools and Setup

## Contents
- Python installation guides
- IDE setup and configuration
- Git and GitHub setup
- Virtual environment setup
- Development tools

Start here if you're setting up your development environment!
"""
    }
    
    for filepath, content in readmes.items():
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✓ Created: {filepath}")

def create_gitignore():
    """Create a comprehensive .gitignore file"""
    
    gitignore_content = """# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Virtual Environment
venv/
env/
ENV/
env.bak/
venv.bak/

# IDE
.vscode/
.idea/
*.swp
*.swo
*~
.DS_Store

# Jupyter Notebook
.ipynb_checkpoints

# Environment variables
.env
.env.local

# Database
*.db
*.sqlite3

# Logs
*.log

# OS
.DS_Store
Thumbs.db

# Large files (adjust as needed)
# *.pdf
# *.mp4
# *.zip
"""
    
    with open('.gitignore', 'w', encoding='utf-8') as f:
        f.write(gitignore_content)
    print("✓ Created: .gitignore")

if __name__ == "__main__":
    print("=" * 50)
    print("Python Learning Roadmap - Setup Script")
    print("=" * 50 + "\n")
    
    create_directory_structure()
    create_gitignore()
    
    print("\n" + "=" * 50)
    print("Setup complete! Happy learning! 🐍")
    print("=" * 50)
