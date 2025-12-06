@echo off
TITLE ARW2JPG Launcher
CLS

:: ---------------------------------------------------------
:: 1. Check for Drag-and-Drop Input
:: ---------------------------------------------------------
set TARGET=%1

:: If TARGET is empty, go to manual input
if "%TARGET%"=="" goto MANUAL_INPUT

:: If TARGET exists, proceed to Dependency Check
goto CHECK_DEPS

:: ---------------------------------------------------------
:: 2. Manual Input Section
:: ---------------------------------------------------------
:MANUAL_INPUT
echo ========================================================
echo   ARW2JPG Converter
echo ========================================================
echo.
echo Please drag and drop a folder/file onto this icon,
echo OR paste the full path below.
echo.
set /p TARGET="> Enter Path: "

:: ---------------------------------------------------------
:: 3. Dependency Check Algorithm (The Guardrail)
:: ---------------------------------------------------------
:CHECK_DEPS
echo.
echo [System] Checking dependencies...

:: Try to import the required libs silently.
:: 2>NUL hides error messages if they are missing.
python -c "import rawpy, imageio, tqdm" 2>NUL

:: If the previous command failed (ErrorLevel is not 0), we install.
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo [Alert] First time setup detected or libraries missing.
    echo [System] Installing requirements from requirements.txt...
    echo --------------------------------------------------------
    
    :: Install using the requirements.txt located in the same folder as this .bat
    pip install -r "%~dp0requirements.txt"
    
    :: Check if install was successful
    if %ERRORLEVEL% NEQ 0 (
        echo.
        echo [Error] Failed to install dependencies. 
        echo Please ensure Python and Pip are installed correctly.
        pause
        exit /b
    )
    echo.
    echo [Success] Installation complete. Ready to process.
    echo --------------------------------------------------------
) else (
    echo [System] All dependencies look good.
)

:: ---------------------------------------------------------
:: 4. Run the Python Script
:: ---------------------------------------------------------
:PROCESS

echo.
echo Starting Conversion...
echo Target: %TARGET%
echo.

:: Run main.py
python "%~dp0src\main.py" %TARGET%

:: ---------------------------------------------------------
:: 5. Finish
:: ---------------------------------------------------------
echo.
echo Done.
pause