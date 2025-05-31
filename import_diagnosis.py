import sys
import os

# Add src to path
sys.path.insert(0, 'src')

print("=== IMPORT DIAGNOSIS ===")

# Test 1: Basic enum import
try:
    print("1. Testing enum import...")
    from enum import Enum
    print("   ✅ Enum imported successfully")
except Exception as e:
    print(f"   ❌ Enum import failed: {e}")

# Test 2: Try importing InputType directly from the models file
try:
    print("2. Testing InputType import...")
    exec("""
class InputType(Enum):
    TEXT = "text"
    IMAGE = "image"
    PDF = "pdf"
    VIDEO = "video"
    AUDIO = "audio"
""")
    print("   ✅ InputType defined successfully")
except Exception as e:
    print(f"   ❌ InputType definition failed: {e}")

# Test 3: Try to load the models __init__.py file content
try:
    print("3. Testing models file read...")
    with open('src/travel_bot/models/__init__.py', 'r') as f:
        content = f.read()
    print(f"   ✅ Models file read successfully ({len(content)} chars)")
    
    # Check for potential issues
    if 'class' in content and 'def' in content:
        print("   ⚠️  Found both classes and functions - potential structure issue")
    
except Exception as e:
    print(f"   ❌ Models file read failed: {e}")

# Test 4: Check for circular imports by examining import statements
try:
    print("4. Checking for circular imports...")
    import ast
    
    with open('src/travel_bot/models/__init__.py', 'r') as f:
        tree = ast.parse(f.read())
    
    imports = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                imports.append(alias.name)
        elif isinstance(node, ast.ImportFrom):
            if node.module:
                imports.append(node.module)
    
    print(f"   Found imports: {imports}")
    
    # Check if any imports might cause circular dependencies
    problematic = [imp for imp in imports if 'travel_bot' in imp]
    if problematic:
        print(f"   ⚠️  Potential circular imports: {problematic}")
    else:
        print("   ✅ No obvious circular imports detected")
        
except Exception as e:
    print(f"   ❌ Circular import check failed: {e}")

print("\n=== DIAGNOSIS COMPLETE ===")
