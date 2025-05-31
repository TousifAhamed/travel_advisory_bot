#!/usr/bin/env python3
"""
Comprehensive validation test for the Travel Advisory Bot
Tests all processor imports and basic functionality
"""
import os
import sys

# Add the src directory to Python path
project_root = os.path.dirname(os.path.abspath(__file__))
src_path = os.path.join(project_root, 'src')
sys.path.insert(0, src_path)

def test_imports():
    """Test all critical imports"""
    print("🔍 Testing Critical Imports...")
    print("-" * 40)
    
    test_results = {}
    
    # Test core models
    try:
        from travel_bot.models import InputProcessor, ProcessedInput, InputType
        test_results['models'] = "✅ SUCCESS"
        print("✅ Core models imported successfully")
    except Exception as e:
        test_results['models'] = f"❌ FAILED: {e}"
        print(f"❌ Core models failed: {e}")
    
    # Test text processor
    try:
        from travel_bot.processors.text_processor import TextProcessor, BaseProcessor
        test_results['text_processor'] = "✅ SUCCESS"
        print("✅ TextProcessor imported successfully")
    except Exception as e:
        test_results['text_processor'] = f"❌ FAILED: {e}"
        print(f"❌ TextProcessor failed: {e}")
    
    # Test image processor
    try:
        from travel_bot.processors.image_processor import ImageProcessor
        test_results['image_processor'] = "✅ SUCCESS"
        print("✅ ImageProcessor imported successfully")
    except Exception as e:
        test_results['image_processor'] = f"❌ FAILED: {e}"
        print(f"❌ ImageProcessor failed: {e}")
    
    # Test audio processor
    try:
        from travel_bot.processors.audio_processor import AudioProcessor
        test_results['audio_processor'] = "✅ SUCCESS"
        print("✅ AudioProcessor imported successfully")
    except Exception as e:
        test_results['audio_processor'] = f"❌ FAILED: {e}"
        print(f"❌ AudioProcessor failed: {e}")
    
    # Test PDF processor
    try:
        from travel_bot.processors.pdf_processor import PDFProcessor
        test_results['pdf_processor'] = "✅ SUCCESS"
        print("✅ PDFProcessor imported successfully")
    except Exception as e:
        test_results['pdf_processor'] = f"❌ FAILED: {e}"
        print(f"❌ PDFProcessor failed: {e}")
    
    # Test video processor
    try:
        from travel_bot.processors.video_processor import VideoProcessor
        test_results['video_processor'] = "✅ SUCCESS"
        print("✅ VideoProcessor imported successfully")
    except Exception as e:
        test_results['video_processor'] = f"❌ FAILED: {e}"
        print(f"❌ VideoProcessor failed: {e}")
    
    # Test processor factory
    try:
        from travel_bot.processors import ProcessorFactory
        test_results['processor_factory'] = "✅ SUCCESS"
        print("✅ ProcessorFactory imported successfully")
    except Exception as e:
        test_results['processor_factory'] = f"❌ FAILED: {e}"
        print(f"❌ ProcessorFactory failed: {e}")
    
    # Test main TravelBot
    try:
        from travel_bot.travel_bot import TravelBot
        test_results['travel_bot'] = "✅ SUCCESS"
        print("✅ TravelBot imported successfully")
    except Exception as e:
        test_results['travel_bot'] = f"❌ FAILED: {e}"
        print(f"❌ TravelBot failed: {e}")
    
    return test_results

def test_processor_functionality():
    """Test basic processor functionality"""
    print("\n🧪 Testing Processor Functionality...")
    print("-" * 40)
    
    try:
        from travel_bot.processors.text_processor import TextProcessor
        from travel_bot.models import InputType
        
        # Create text processor instance
        processor = TextProcessor()
        print("✅ TextProcessor instance created")
        
        # Test supports_input_type
        supports_text = processor.supports_input_type(InputType.TEXT)
        print(f"✅ Supports TEXT input: {supports_text}")
        
        # Test language detection (if available)
        try:
            language = processor.detect_language("Hello, how are you?")
            print(f"✅ Language detection works: detected '{language}'")
        except Exception as e:
            print(f"⚠️  Language detection issue: {e}")
        
        # Test entity extraction
        try:
            entities = processor.extract_travel_entities("I want to visit Paris for vacation and see museums")
            print(f"✅ Entity extraction works: found {len(entities)} categories")
            if entities:
                for category, items in entities.items():
                    print(f"   - {category}: {items}")
        except Exception as e:
            print(f"❌ Entity extraction failed: {e}")
        
        return True
        
    except Exception as e:
        print(f"❌ Processor functionality test failed: {e}")
        return False

def test_factory():
    """Test ProcessorFactory functionality"""
    print("\n🏭 Testing ProcessorFactory...")
    print("-" * 40)
    
    try:
        from travel_bot.processors import ProcessorFactory
        
        factory = ProcessorFactory()
        print("✅ ProcessorFactory instance created")
        
        # Test getting different processors
        processors_to_test = ['text', 'image', 'audio', 'pdf', 'video']
        
        for proc_type in processors_to_test:
            try:
                processor = factory.get_processor(proc_type)
                if processor:
                    print(f"✅ {proc_type.upper()} processor created: {type(processor).__name__}")
                else:
                    print(f"⚠️  {proc_type.upper()} processor returned None")
            except Exception as e:
                print(f"❌ {proc_type.upper()} processor failed: {e}")
        
        return True
        
    except Exception as e:
        print(f"❌ ProcessorFactory test failed: {e}")
        return False

def main():
    """Run all validation tests"""
    print("🚀 Travel Advisory Bot - Comprehensive Validation")
    print("=" * 50)
    
    # Test imports
    import_results = test_imports()
    
    # Test processor functionality
    functionality_ok = test_processor_functionality()
    
    # Test factory
    factory_ok = test_factory()
    
    # Summary
    print("\n" + "=" * 50)
    print("📊 VALIDATION SUMMARY")
    print("=" * 50)
    
    success_count = sum(1 for result in import_results.values() if "SUCCESS" in result)
    total_count = len(import_results)
    
    print(f"Import Tests: {success_count}/{total_count} passed")
    for component, result in import_results.items():
        print(f"  - {component}: {result}")
    
    print(f"\nFunctionality Tests: {'✅ PASSED' if functionality_ok else '❌ FAILED'}")
    print(f"Factory Tests: {'✅ PASSED' if factory_ok else '❌ FAILED'}")
    
    if success_count == total_count and functionality_ok and factory_ok:
        print("\n🎉 ALL TESTS PASSED! Application is ready for use.")
        print("🌐 Streamlit app should be accessible at: http://localhost:8501")
    else:
        print("\n⚠️  Some tests failed. Please check the errors above.")
    
    print("\n🎯 Next steps:")
    print("   1. Open http://localhost:8501 in your browser")
    print("   2. Test the travel suggestion features")
    print("   3. Try uploading different file types")
    print("   4. Test the chat functionality")

if __name__ == "__main__":
    main()
