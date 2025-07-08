@echo off
REM Importa todos os arquivos SQL limpos para o MariaDB do XAMPP
REM Ajuste o caminho do MySQL se necessário
set MYSQL_PATH=C:\xampp\mysql\bin\mysql.exe
set DB_NAME=fusione
set SQL_FOLDER="C:\xampp\fusione\Uploaded Files_ static"

cd /d %SQL_FOLDER%

python "%~dp0scripts\corrigir_sql.py"

for %%F in (limpo_*.sql) do (
    echo Importando %%F ...
    "%MYSQL_PATH%" -u root %DB_NAME% < "%%F"
)

echo Importacao concluida.
pause
