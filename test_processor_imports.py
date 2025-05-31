#!/usr/bin/env python3
"""
Import validation test for Travel Advisory Bot processors
"""
import os
import sys

# Add the src directory to Python path
project_root = os.path.dirname(os.path.abspath(__file__))
src_path = os.path.join(project_root, 'src')
sys.path.insert(0, src_path)

print("🔍 Testing Travel Bot Processor Imports...")
print("=" * 50)

try:
    from travel_bot.processors.text_processor import TextProcessor
    print("✅ TextProcessor imported successfully")
except Exception as e:
    print(f"❌ TextProcessor import failed: {e}")

try:
    from travel_bot.processors.image_processor import ImageProcessor
    print("✅ ImageProcessor imported successfully")
except Exception as e:
    print(f"❌ ImageProcessor import failed: {e}")

try:
    from travel_bot.processors.audio_processor import AudioProcessor
    print("✅ AudioProcessor imported successfully")
except Exception as e:
    print(f"❌ AudioProcessor import failed: {e}")

try:
    from travel_bot.processors.pdf_processor import PDFProcessor
    print("✅ PDFProcessor imported successfully")
except Exception as e:
    print(f"❌ PDFProcessor import failed: {e}")

try:
    from travel_bot.processors.video_processor import VideoProcessor
    print("✅ VideoProcessor imported successfully")
except Exception as e:
    print(f"❌ VideoProcessor import failed: {e}")

try:
    from travel_bot.processors import ProcessorFactory
    print("✅ ProcessorFactory imported successfully")
except Exception as e:
    print(f"❌ ProcessorFactory import failed: {e}")

try:
    from travel_bot.travel_bot import TravelBot
    print("✅ TravelBot main class imported successfully")
except Exception as e:
    print(f"❌ TravelBot import failed: {e}")

print("\n" + "=" * 50)
print("🎯 Import validation complete!")

# Test creating a processor factory
try:
    from travel_bot.processors import ProcessorFactory
    factory = ProcessorFactory()
    print(f"✅ ProcessorFactory instance created successfully")
    
    # Test getting a text processor
    text_proc = factory.get_processor('text')
    print(f"✅ Text processor retrieved: {type(text_proc).__name__}")
    
except Exception as e:
    print(f"❌ ProcessorFactory test failed: {e}")

print("\n🎉 All tests completed!")
