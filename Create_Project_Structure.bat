@echo off
title EduFormulaAI - Create Project Structure

echo ==========================================
echo      EduFormula AI Project Structure
echo ==========================================
echo.

cd /d "%~dp0"

mkdir 00_Project_Management
mkdir 01_Documents
mkdir 02_Source
mkdir 03_Content
mkdir 04_Assets
mkdir 05_Database
mkdir 06_Tests
mkdir 07_Releases
mkdir 08_Tools
mkdir 09_Temp
mkdir 10_Backup

mkdir 01_Documents\01_Project
mkdir 01_Documents\02_Architecture
mkdir 01_Documents\03_Database
mkdir 01_Documents\04_UI_UX
mkdir 01_Documents\05_Animation
mkdir 01_Documents\06_AI
mkdir 01_Documents\07_Standards
mkdir 01_Documents\08_Testing
mkdir 01_Documents\09_Release
mkdir 01_Documents\10_UserGuide

mkdir 02_Source\Core
mkdir 02_Source\Modules
mkdir 02_Source\UI
mkdir 02_Source\Database
mkdir 02_Source\AI
mkdir 02_Source\Simulation
mkdir 02_Source\Services
mkdir 02_Source\Utils

mkdir 03_Content\Math\Grade10
mkdir 03_Content\Math\Grade11
mkdir 03_Content\Math\Grade12

mkdir 03_Content\Physics\Grade10
mkdir 03_Content\Physics\Grade11
mkdir 03_Content\Physics\Grade12

mkdir 03_Content\Chemistry\Grade10
mkdir 03_Content\Chemistry\Grade11
mkdir 03_Content\Chemistry\Grade12

mkdir 03_Content\Biology\Grade10
mkdir 03_Content\Biology\Grade11
mkdir 03_Content\Biology\Grade12

mkdir 04_Assets\Images
mkdir 04_Assets\Icons
mkdir 04_Assets\SVG
mkdir 04_Assets\Audio
mkdir 04_Assets\Video
mkdir 04_Assets\Animations
mkdir 04_Assets\Fonts

echo.
echo ==========================================
echo      Project Structure Created Successfully
echo ==========================================
pause