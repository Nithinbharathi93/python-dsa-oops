@echo off
setlocal

REM Ask for commit message
set /p commitMessage=Enter commit message: 

REM Run git commands
git add .
git commit -m "%commitMessage%"
git push origin main

pause
