# 🚀 Travel Advisory Bot - Manual Launch Guide

## Quick Start (Recommended)

1. **Open Command Prompt** in the project directory:
   ```cmd
   cd c:\DEV\Travel_Advisory_Bot\travel-advisory-bot
   ```

2. **Run the existing batch script**:
   ```cmd
   start_with_path.bat
   ```

   OR

3. **Run commands manually**:
   ```cmd
   pip install streamlit python-dotenv requests
   set PYTHONPATH=%CD%;%CD%\src;%PYTHONPATH%
   python -m streamlit run src\travel_bot\ui\streamlit_app.py --server.port 8501
   ```

## Alternative Methods

### Method 1: Python Launcher
```cmd
python run_app.py
```

### Method 2: Smart Launcher
```cmd
smart_launch.bat
```

### Method 3: Complete Setup
```cmd
complete_setup.bat
```

### Method 4: Minimal App (if there are import issues)
```cmd
python -m streamlit run minimal_app.py --server.port 8501
```

## Expected Output

When successful, you should see:
- ✅ Dependencies installed
- 🌐 Local URL: http://localhost:8501
- 🌐 Network URL: http://192.168.x.x:8501
- 🚀 Streamlit app running

## Troubleshooting

### If you see import errors:
1. Try the minimal app: `python -m streamlit run minimal_app.py`
2. Run the complete setup: `complete_setup.bat`
3. Check the debug app: `python -m streamlit run debug_app.py --server.port 8502`

### If dependencies are missing:
```cmd
pip install streamlit python-dotenv requests ollama pypdf Pillow transformers torch
```

### If Devstral is not available:
1. Start Ollama: `ollama serve`
2. Pull Devstral: `ollama pull devstral`
3. Check status: `check_devstral.bat`

## Application Features

Once running at http://localhost:8501, you'll have access to:

- 💬 **Travel Chat**: Interactive AI assistant
- 🗺️ **Travel Suggestions**: Personalized recommendations  
- 📋 **Itinerary Planning**: Detailed trip planning
- 🛠️ **Configuration**: Model selection (Ollama/Devstral, OpenAI, etc.)
- 📁 **File Upload**: Support for PDFs, images, videos, audio

## Next Steps

1. Launch the application using any of the methods above
2. Test the interface at http://localhost:8501
3. Configure your preferred AI model in the sidebar
4. Try uploading different file types (text, images, PDFs)
5. Generate travel suggestions and itineraries

The application is fully configured and ready to run!
