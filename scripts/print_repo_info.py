#!/usr/bin/env python3
"""
scripts/print_repo_info.py

Сканирует директорию репозитория и выводит статистику по типам файлов.
Запуск: python3 scripts/print_repo_info.py /path/to/repo
Если путь не указан — по умолчанию текущая директория.
"""
import os
import sys
from collections import Counter


def scan(path):
    counts = Counter()
    for root, _, files in os.walk(path):
        for f in files:
            ext = os.path.splitext(f)[1].lower() or '<noext>'
            counts[ext] += 1
    total = sum(counts.values())
    print(f"Scanned {total} files in: {os.path.abspath(path)}\n")
    for ext, cnt in counts.most_common():
        print(f"{ext:8} {cnt:6}  {cnt/total:.1%}")


if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "."
    scan(path)
