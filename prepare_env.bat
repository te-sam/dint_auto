@echo off
:: Проверка, запущен ли скрипт от имени администратора
net session >nul 2>&1
if %errorlevel% neq 0 (
    :: Перезапуск скрипта с правами администратора
    echo Run as an administrator...
    powershell -Command "Start-Process '%~f0' -Verb RunAs"
    exit /b
)

echo install environment variable
:: Проверяем, существует ли переменная ALLURE_HOME
if not defined ALLURE_HOME (
    setx ALLURE_HOME "C:\allure" /M
    setx PATH "%PATH%;C:\allure\bin" /M
)

:: Изменяем рабочий каталог на расположение текущего .bat файла
cd /d "%~dp0"

echo install environment
call python -m venv venv
call venv\Scripts\activate

echo install requiremets
call pip install -r requirements.txt

echo Successful!

pause