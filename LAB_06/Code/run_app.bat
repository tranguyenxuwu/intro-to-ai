@echo off
echo Installing required packages...
pip install -r requirements.txt

echo.
echo Starting Streamlit app...
streamlit run streamlit_app.py

pause
