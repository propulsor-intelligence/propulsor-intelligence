import os
import re

SQL_DIR = r"C:\\xampp\\fusione\\Uploaded Files_ static"

INVALID_PATTERNS = [
    r"PRAGMA", r"TRANSACTION", r"BEGIN", r"COMMIT"
]

REPLACEMENTS = {
    '├º': 'ç', '├ú': 'ã', '├¡': 'á', '├â': 'â',
    '├Ã©': 'é', 'Ã§': 'ç', 'Ã£': 'ã', 'Ã³': 'ó',
    'Ã¡': 'á', 'Ãª': 'ê', 'Ã©': 'é', 'Ãº': 'ú',
    'Ã­': 'í', 'Ã¢': 'â', 'Ã ': 'à'
}


def clean_line(line: str) -> str:
    for wrong, right in REPLACEMENTS.items():
        if wrong in line:
            line = line.replace(wrong, right)
    return line


def process_file(path: str, output_path: str) -> None:
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()

    cleaned = []
    for line in lines:
        if any(re.search(p, line, re.IGNORECASE) for p in INVALID_PATTERNS):
            continue
        cleaned.append(clean_line(line))

    with open(output_path, 'w', encoding='utf-8') as f:
        f.writelines(cleaned)


def main() -> None:
    for fname in os.listdir(SQL_DIR):
        if fname.lower().endswith('.sql') and not fname.startswith('limpo_'):
            src = os.path.join(SQL_DIR, fname)
            dst = os.path.join(SQL_DIR, f'limpo_{fname}')
            process_file(src, dst)
            print(f'Gerado {dst}')


if __name__ == '__main__':
    main()
