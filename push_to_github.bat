@echo off
echo ===================================================
echo   Deploying Ankit Kumar Portfolio to GitHub
echo ===================================================
git add .
git commit -m "Update portfolio website and resumes"
git push -u origin main
echo.
echo Deployment push complete! Check your repository.
pause
