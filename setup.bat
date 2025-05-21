@echo off
setlocal ENABLEDELAYEDEXPANSION

pip3 install colorama %*

REM Tìm vị trí thực sự của vocab.txt bằng PowerShell
for /f "delims=" %%F in ('powershell -command "Get-ChildItem -Path C:\Users\ -Filter vocab.txt -Recurse -ErrorAction SilentlyContinue | Select-Object -First 1 -ExpandProperty FullName"') do (
    set "VOCAB_PATH=%%F"
)

REM Nếu không tìm thấy thì báo lỗi và dừng
if not defined VOCAB_PATH (
    echo [!] Không tìm thấy file vocab.txt trên máy.
    pause
    exit /b
)

REM Chuyển \ thành /
set "VOCAB_PATH_PY=%VOCAB_PATH:\=/%"
set "NEW_LINE=file_path = '%VOCAB_PATH_PY%'"

REM Tên file Python cần sửa
set "SRC_FILE=eng.py"
set "TMP_FILE=eng_tmp.py"

if not exist "%SRC_FILE%" (
    echo [!] Không tìm thấy file eng.py trong thư mục hiện tại!
    pause
    exit /b
)

REM Sửa dòng có chứa vocab.txt
(
for /f "usebackq delims=" %%A in ("%SRC_FILE%") do (
    set "line=%%A"
    echo !line! | findstr /c:"vocab.txt" >nul
    if !errorlevel! equ 0 (
        echo %NEW_LINE%
    ) else (
        if "!line!"=="" (
            echo.
        ) else (
            echo !line!
        )
    )
)
) > "%TMP_FILE%"

move /y "%TMP_FILE%" "%SRC_FILE%" > nul
echo.
echo [✓] Đã cập nhật dòng chứa vocab.txt trong eng.py thành:
echo     %NEW_LINE%
echo.
pause
exit /b
