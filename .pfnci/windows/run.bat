PowerShell -NoProfile -ExecutionPolicy Bypass -File .pfnci\windows\test.ps1 %*
exit /b %ERRORLEVEL%
