@echo off
title Diabetes Risk Prediction Pipeline - SRM IST
echo ======================================================================
echo Running Diabetes Risk Prediction Pipeline (Preprocessing, EDA, ML, XAI)
echo Student: Agarshna R (RA2411026050061) - SRM IST
echo ======================================================================
echo.
set PYTHONPATH=.;src
set MPLCONFIGDIR=.mpl

if exist "C:\Users\Vishnu\AppData\Local\Programs\Python\Python311\python.exe" (
    "C:\Users\Vishnu\AppData\Local\Programs\Python\Python311\python.exe" run_pipeline.py
) else (
    python run_pipeline.py
)
pause


