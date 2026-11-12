@echo off
title Diabetes Risk Prediction Web Application - SRM IST
echo ======================================================================
echo Launching Early-Stage Diabetes Prediction System (Streamlit App)
echo Student: Agarshna R (RA2411026050061) - SRM IST
echo ======================================================================
echo.
set PYTHONPATH=.;src
set MPLCONFIGDIR=.mpl

if exist "C:\Users\Vishnu\AppData\Local\Programs\Python\Python311\python.exe" (
    "C:\Users\Vishnu\AppData\Local\Programs\Python\Python311\python.exe" -m streamlit run app.py
) else (
    python -m streamlit run app.py
)
pause


