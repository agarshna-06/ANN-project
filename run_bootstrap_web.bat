@echo off
title Diabetes AI Bootstrap Web Dashboard - SRM IST
echo ======================================================================
echo Launching Bootstrap 5.3 Modern Diabetes AI Web Platform
echo Student: Agarshna R (RA2411026050061) - SRM IST
echo ======================================================================
echo.
echo Starting local web server at http://localhost:8000 ...
start "" http://localhost:8000/index.html

if exist "C:\Users\Vishnu\AppData\Local\Programs\Python\Python311\python.exe" (
    "C:\Users\Vishnu\AppData\Local\Programs\Python\Python311\python.exe" -m http.server 8000
) else (
    python -m http.server 8000
)
pause

