@echo off
title Push ANN-project to GitHub - agarshna-06
echo ======================================================================
echo Pushing Project to GitHub Repository: agarshna-06/ANN-project (Public)
echo ======================================================================
echo.
echo Step 1: Ensure you have created the empty repository on GitHub:
echo         https://github.com/new -> Name: ANN-project (Public, without README)
echo.
echo Step 2: Choose your authentication method below:
echo   [1] Standard Git Login (Web Browser / Credential Manager popup)
echo   [2] Using GitHub Personal Access Token (PAT)
echo.
set /p choice="Enter choice [1 or 2]: "

if "%choice%"=="2" (
    set /p token="Enter your GitHub Personal Access Token (PAT): "
    echo Setting remote with token...
    git remote set-url origin https://agarshna-06:%token%@github.com/agarshna-06/ANN-project.git
    echo Pushing to GitHub...
    git push -u origin main
    git remote set-url origin https://github.com/agarshna-06/ANN-project.git
) else (
    echo Pushing to GitHub (A browser window may open to authenticate)...
    git push -u origin main
)

echo.
echo ======================================================================
echo If push succeeded, your repo is live at:
echo https://github.com/agarshna-06/ANN-project
echo ======================================================================
pause
