@echo off
set LOG_FILE=%cd%\execution_log.txt

REM Очищаем лог файл перед началом
if exist %LOG_FILE% del %LOG_FILE%

REM Запись в лог файл начала выполнения
echo %date% %time% - Activating virtual environment... >> %LOG_FILE%
echo Activating virtual environment...
call venv\Scripts\activate >> %LOG_FILE% 2>&1

REM Установка переменной окружения для папки с отчетами allure
set ALLURE_RESULTS_DIRECTORY=%cd%\allure-results
set ALLURE_REPORT_DIRECTORY=%cd%\allure-report
echo %date% %time% - Report directories set to %ALLURE_RESULTS_DIRECTORY% and %ALLURE_REPORT_DIRECTORY% >> %LOG_FILE%
echo Report directories set to %ALLURE_RESULTS_DIRECTORY% and %ALLURE_REPORT_DIRECTORY%

REM Удаление предыдущих результатов
:: echo %date% %time% - Removing old results... >> %LOG_FILE%
:: echo Removing old results...
:: if exist %ALLURE_RESULTS_DIRECTORY% rmdir /s /q %ALLURE_RESULTS_DIRECTORY% >> %LOG_FILE% 2>&1
:: if exist %ALLURE_REPORT_DIRECTORY% rmdir /s /q %ALLURE_REPORT_DIRECTORY% >> %LOG_FILE% 2>&1

REM Запуск pytest с плагином allure и выводом в файл и консоль
echo %date% %time% - Running pytest... >> %LOG_FILE%
echo Running pytest...
pytest --alluredir=%ALLURE_RESULTS_DIRECTORY% 
:: >> %LOG_FILE% 2>&1

REM Генерация отчета allure, если pytest завершился
echo %date% %time% - Generating Allure report... >> %LOG_FILE%
echo Generating Allure report...
allure generate %ALLURE_RESULTS_DIRECTORY% -o %ALLURE_REPORT_DIRECTORY% --clean >> %LOG_FILE% 2>&1

REM Ожидание завершения
echo %date% %time% - Allure report generation completed. >> %LOG_FILE%
echo Allure report generation completed.

pause