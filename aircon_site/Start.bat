@echo off
title CoolTech — Air Conditioning Site
color 0B
echo.
echo  ================================
echo   CoolTech — Air Conditioning Site
echo  ================================
echo.
python --version >nul 2>&1
if errorlevel 1 ( set PYTHON=py ) else ( set PYTHON=python )
%PYTHON% -m pip install flask --quiet --disable-pip-version-check
echo  Flask ready. Starting...
echo  Open browser at: http://localhost:5000
echo.
start "" timeout /t 2 /nobreak >nul & start "" "http://localhost:5000"
%PYTHON% app.py
pause
