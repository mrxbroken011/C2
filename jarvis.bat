@echo off
title JARVIS TERMINAL
color 0A
echo Requesting Administrator Privileges...
:: Check for Admin rights
net session >nul 2>&1
if %errorLevel% == 0 (
    echo [SUCCESS] Running as Admin.
    python jarvis.py
) else (
    echo [ERROR] Please right-click this file and select 'Run as Administrator'.
    pause
)
