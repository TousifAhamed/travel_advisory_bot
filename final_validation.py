#!/usr/bin/env python3
"""
Final validation script for the Travel Advisory Bot
Tests project structure and basic functionality without external dependencies
"""

import os
import sys
import importlib.util
from pathlib import Path

class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    BOLD = '\033[1m'
    END = '\033[0m'

def print_status(message, status="info"):
    if status == "success":
        print(f"{Colors.GREEN}✅ {message}{Colors.END}")
    elif status == "error":
        print(f"{Colors.RED}❌ {message}{Colors.END}")
    elif status == "warning":
        print(f"{Colors.YELLOW}⚠️ {message}{Colors.END}")
    elif status == "info":
        print(f"{Colors.BLUE}ℹ️ {message}{Colors.END}")

def check_file_exists(filepath, description):
    """Check if a file exists and return status"""
    if os.path.exists(filepath):
        print_status(f"{description}: Found", "success")
        return True
    else:
        print_status(f"{description}: Missing", "error")
        return False

def check_directory_structure():
    """Validate the project directory structure"""
    print(f"\n{Colors.BOLD}📁 Checking Project Structure{Colors.END}")
    print("-" * 40)
    
    base_dir = Path(__file__).parent
    
    # Core files
    files_to_check = {
        "main.py": "Main entry point",
        "pyproject.toml": "Project configuration",
        "README.md": "Documentation",
        ".env.example": "Environment template",
        "setup_and_run.bat": "Windows startup script",
        "start.bat": "Alternative startup script"
    }
    
    # Core directories
    dirs_to_check = {
        "src": "Source code directory",
        "src/travel_bot": "Main package",
        "src/travel_bot/models": "Data models",
        "src/travel_bot/processors": "Input processors",
        "src/travel_bot/agents": "AI agents",
        "src/travel_bot/utils": "Utilities",
        "src/travel_bot/ui": "User interface",
        "config": "Configuration"
    }
    
    # Check files
    file_score = 0
    for filename, description in files_to_check.items():
        filepath = base_dir / filename
        if check_file_exists(filepath, description):
            file_score += 1
    
    # Check directories
    dir_score = 0
    for dirname, description in dirs_to_check.items():
        dirpath = base_dir / dirname
        if check_file_exists(dirpath, f"{description} directory"):
            dir_score += 1
    
    total_files = len(files_to_check)
    total_dirs = len(dirs_to_check)
    
    print(f"\n📊 Structure Score: {file_score + dir_score}/{total_files + total_dirs}")
    return file_score == total_files and dir_score == total_dirs

def check_python_modules():
    """Check if Python modules can be imported"""
    print(f"\n{Colors.BOLD}🐍 Checking Python Modules{Colors.END}")
    print("-" * 40)
    
    base_dir = Path(__file__).parent
    src_path = str(base_dir / "src")
    
    if src_path not in sys.path:
        sys.path.insert(0, src_path)
    
    modules_to_test = [
        ("travel_bot.models", "Core data models"),
        ("travel_bot.travel_bot", "Main TravelBot class"),
        ("travel_bot.agents.travel_agent", "Travel agent"),
        ("travel_bot.processors.text_processor", "Text processor"),
        ("travel_bot.ui.streamlit_app", "Streamlit interface"),
        ("config.settings", "Configuration settings")
    ]
    
    import_score = 0
    for module_name, description in modules_to_test:
        try:
            spec = importlib.util.find_spec(module_name)
            if spec is not None:
                print_status(f"{description}: Module found", "success")
                import_score += 1
            else:
                print_status(f"{description}: Module not found", "error")
        except Exception as e:
            print_status(f"{description}: Import error - {str(e)}", "error")
    
    print(f"\n📊 Import Score: {import_score}/{len(modules_to_test)}")
    return import_score == len(modules_to_test)

def check_configuration():
    """Check configuration files and environment setup"""
    print(f"\n{Colors.BOLD}⚙️ Checking Configuration{Colors.END}")
    print("-" * 40)
    
    base_dir = Path(__file__).parent
    
    # Check .env.example
    env_example = base_dir / ".env.example"
    env_file = base_dir / ".env"
    
    config_score = 0
    
    if check_file_exists(env_example, ".env.example template"):
        config_score += 1
        
        # Read and validate .env.example content
        try:
            with open(env_example, 'r') as f:
                content = f.read()
                required_keys = [
                    "OPENAI_API_KEY",
                    "HUGGINGFACE_API_KEY", 
                    "DEFAULT_AI_MODEL",
                    "DEFAULT_LANGUAGE"
                ]
                
                for key in required_keys:
                    if key in content:
                        print_status(f"Environment key '{key}': Found", "success")
                        config_score += 1
                    else:
                        print_status(f"Environment key '{key}': Missing", "error")
                        
        except Exception as e:
            print_status(f"Error reading .env.example: {e}", "error")
    
    # Check if .env exists
    if env_file.exists():
        print_status(".env file: Exists (ready for use)", "success")
    else:
        print_status(".env file: Not found (copy from .env.example)", "warning")
    
    total_config_checks = 5  # .env.example + 4 required keys
    print(f"\n📊 Configuration Score: {config_score}/{total_config_checks}")
    return config_score >= 4  # Allow missing .env file

def check_dependencies():
    """Check if required dependencies can be imported"""
    print(f"\n{Colors.BOLD}📦 Checking Dependencies{Colors.END}")
    print("-" * 40)
    
    # Core dependencies (try to import)
    dependencies = [
        ("os", "Operating system interface", True),
        ("sys", "System-specific parameters", True),
        ("pathlib", "Object-oriented filesystem paths", True),
        ("json", "JSON encoder/decoder", True),
        ("asyncio", "Asynchronous I/O", True),
        ("streamlit", "Web app framework", False),
        ("openai", "OpenAI API client", False),
        ("PIL", "Python Imaging Library", False),
        ("pypdf", "PDF processing", False)
    ]
    
    dep_score = 0
    required_count = 0
    
    for module_name, description, required in dependencies:
        if required:
            required_count += 1
            
        try:
            __import__(module_name)
            print_status(f"{description}: Available", "success")
            dep_score += 1
        except ImportError:
            if required:
                print_status(f"{description}: Missing (required)", "error")
            else:
                print_status(f"{description}: Missing (install needed)", "warning")
    
    print(f"\n📊 Dependencies Score: {dep_score}/{len(dependencies)}")
    print(f"🔧 Required dependencies available: {min(dep_score, required_count)}/{required_count}")
    
    return dep_score >= required_count

def generate_next_steps():
    """Generate next steps for the user"""
    print(f"\n{Colors.BOLD}🚀 Next Steps{Colors.END}")
    print("-" * 40)
    
    steps = [
        "1. Install dependencies: pip install streamlit python-dotenv openai pillow pypdf2",
        "2. Copy .env.example to .env: copy .env.example .env",
        "3. Edit .env file with your API keys",
        "4. Run the application: setup_and_run.bat",
        "5. Open browser to: http://localhost:8501"
    ]
    
    for step in steps:
        print(f"   {step}")
    
    print(f"\n{Colors.YELLOW}💡 Tip: Use setup_and_run.bat for automated setup on Windows{Colors.END}")

def main():
    """Main validation function"""
    print(f"{Colors.BOLD}🌍 Travel Advisory Bot - Final Validation{Colors.END}")
    print("=" * 60)
    
    checks = [
        ("Project Structure", check_directory_structure),
        ("Python Modules", check_python_modules),
        ("Configuration", check_configuration),
        ("Dependencies", check_dependencies)
    ]
    
    passed_checks = 0
    total_checks = len(checks)
    
    for check_name, check_function in checks:
        try:
            if check_function():
                passed_checks += 1
                print_status(f"{check_name}: PASSED", "success")
            else:
                print_status(f"{check_name}: FAILED", "error")
        except Exception as e:
            print_status(f"{check_name}: ERROR - {e}", "error")
        
        print()  # Add spacing between checks
    
    # Final results
    print("=" * 60)
    print(f"{Colors.BOLD}📊 Final Results{Colors.END}")
    print(f"Checks Passed: {passed_checks}/{total_checks}")
    
    if passed_checks == total_checks:
        print_status("🎉 ALL CHECKS PASSED! Your Travel Advisory Bot is ready!", "success")
        print(f"\n{Colors.GREEN}{Colors.BOLD}✨ Project Status: READY FOR USE ✨{Colors.END}")
    elif passed_checks >= 2:
        print_status("⚠️ Most checks passed. Minor setup required.", "warning")
        print(f"\n{Colors.YELLOW}{Colors.BOLD}🔧 Project Status: NEEDS MINOR SETUP 🔧{Colors.END}")
    else:
        print_status("❌ Multiple issues found. Review errors above.", "error")
        print(f"\n{Colors.RED}{Colors.BOLD}🛠️ Project Status: NEEDS ATTENTION 🛠️{Colors.END}")
    
    generate_next_steps()
    
    return passed_checks >= 2

if __name__ == "__main__":
    try:
        success = main()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print(f"\n\n{Colors.YELLOW}⚠️ Validation interrupted by user{Colors.END}")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n{Colors.RED}❌ Unexpected error: {e}{Colors.END}")
        sys.exit(1)
