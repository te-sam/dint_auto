@echo off

echo install environment variable
:: Проверяем, существует ли переменная ALLURE_HOME
if not defined ALLURE_HOME (
    setx ALLURE_HOME "C:\allure" /M
)

:: Проверяем, существует ли нужный путь в PATH
echo %PATH% | findstr /I "%ALLURE_HOME%\bin" > nul
if %errorlevel% neq 0 (
    setx PATH "%PATH%;%ALLURE_HOME%\bin" /M
)

echo install environment
call python -m venv venv
call venv\Scripts\activate

echo install requiremets
call pip install -r requirements.txt