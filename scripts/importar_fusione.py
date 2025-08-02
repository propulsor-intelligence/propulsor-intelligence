"""Importa arquivos SQL do Fusione no MySQL definido no .env."""
from __future__ import annotations

import os
import mysql.connector
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

SQL_DIR = Path(os.getenv("SQL_DIR", "C:/xampp/fusione/sql"))
DB_CONFIG = {
    "host": os.getenv("MYSQL_HOST", "localhost"),
    "user": os.getenv("MYSQL_USER", "root"),
    "password": os.getenv("MYSQL_PASSWORD", ""),
    "database": os.getenv("MYSQL_DB", "fusione"),
}


def run_sql_file(cursor: mysql.connector.cursor.MySQLCursor, path: Path) -> None:
    with path.open("r", encoding="utf-8", errors="ignore") as file:
        sql_statements = file.read()
    for _ in cursor.execute(sql_statements, multi=True):
        pass


def main() -> None:
    files = sorted(SQL_DIR.glob("*.sql"))
    if not files:
        print(f"Nenhum arquivo .sql encontrado em {SQL_DIR}")
        return

    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()
    for sql_file in files:
        print(f"Importando {sql_file.name}...")
        run_sql_file(cursor, sql_file)
        conn.commit()
    cursor.close()
    conn.close()
    print("Importação concluída.")


if __name__ == "__main__":
    main()
