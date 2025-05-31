@echo off
echo Testing Travel Advisory Bot...
python test_final_complete.py
if %ERRORLEVEL% == 0 (
    echo.
    echo SUCCESS! Now starting Streamlit app...
    echo Opening in browser at http://localhost:8501
    streamlit run src/travel_bot/ui/streamlit_app.py
) else (
    echo.
    echo FAILED! Check errors above.
    pause
)
