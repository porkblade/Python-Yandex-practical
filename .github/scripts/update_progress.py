#!/usr/bin/env python3
"""Скрипт для автоматического обновления прогресса в README."""

import re
from pathlib import Path
from datetime import datetime

# Структура курса: модуль -> подразделы
COURSE_STRUCTURE = {
    "1": {"name": "Введение", "subsections": []},
    "2": {
        "name": "Базовые конструкции Python",
        "subsections": ["2.1", "2.2", "2.3", "2.4"],
    },
    "3": {
        "name": "Коллекции и работа с памятью",
        "subsections": ["3.1", "3.2", "3.3", "3.4", "3.5", "3.6"],
    },
    "4": {
        "name": "Функции и их особенности в Python",
        "subsections": ["4.1", "4.2", "4.3", "4.4"],
    },
    "5": {
        "name": "Объектно-ориентированное программирование",
        "subsections": ["5.1", "5.2", "5.3", "5.4"],
    },
    "6": {
        "name": "Библиотеки для получения и обработки данных",
        "subsections": ["6.1", "6.2", "6.3", "6.4"],
    },
}


def count_solutions():
    """Подсчитывает количество решенных задач по модулям."""
    root = Path(".")
    completed_sections = set()
    total_tasks = 0

    # Ищем все папки с решениями
    for item in root.iterdir():
        if item.is_dir() and not item.name.startswith("."):
            # Проверяем, соответствует ли имя папки формату модуля
            if re.match(r"^\d+\.\d+$", item.name):
                # Считаем количество .py файлов
                py_files = list(item.glob("*.py"))
                if py_files:
                    completed_sections.add(item.name)
                    total_tasks += len(py_files)

    return completed_sections, total_tasks


def calculate_progress(completed_sections):
    """Вычисляет процент прогресса."""
    total_subsections = sum(
        len(module["subsections"]) if module["subsections"] else 1
        for module in COURSE_STRUCTURE.values()
    )

    completed_count = len(completed_sections)
    return (completed_count / total_subsections * 100) if total_subsections > 0 else 0


def generate_progress_section(completed_sections, total_tasks):
    """Генерирует секцию прогресса для README."""
    progress_percent = calculate_progress(completed_sections)

    lines = [
        "## 🎯 Прогресс прохождения\n",
        f"![Progress](https://img.shields.io/badge/Прогресс-{progress_percent:.0f}%25-blue?style=for-the-badge)\n",
        f"![Tasks](https://img.shields.io/badge/Решено_задач-{total_tasks}-green?style=for-the-badge)\n",
        f"![Updated](https://img.shields.io/badge/Обновлено-{datetime.now().strftime('%d.%m.%Y')}-orange?style=for-the-badge)\n",
        "\n",
    ]

    # Генерируем список модулей с прогрессом
    for module_num, module_info in COURSE_STRUCTURE.items():
        module_name = module_info["name"]
        subsections = module_info["subsections"]

        if not subsections:
            # Модуль без подразделов
            is_completed = module_num in completed_sections
            checkbox = "[x]" if is_completed else "[ ]"
            lines.append(f"- {checkbox} {module_num}. {module_name}\n")
        else:
            # Модуль с подразделами
            completed_subsections = [s for s in subsections if s in completed_sections]
            all_completed = len(completed_subsections) == len(subsections)
            checkbox = "[x]" if all_completed else "[ ]"
            lines.append(f"- {checkbox} {module_num}. {module_name}\n")

            # Добавляем подразделы
            for subsection in subsections:
                is_completed = subsection in completed_sections
                sub_checkbox = "[x]" if is_completed else "[ ]"
                lines.append(f"  - {sub_checkbox} {subsection}\n")

    return "".join(lines)


def update_readme():
    """Обновляет секцию прогресса в README."""
    readme_path = Path("README.md")

    if not readme_path.exists():
        print("README.md не найден!")
        return

    # Читаем текущий README
    content = readme_path.read_text(encoding="utf-8")

    # Подсчитываем прогресс
    completed_sections, total_tasks = count_solutions()

    # Генерируем новую секцию прогресса
    new_progress = generate_progress_section(completed_sections, total_tasks)

    # Заменяем секцию прогресса
    pattern = r"## 🎯 Прогресс прохождения\n.*?(?=\n## |\Z)"
    if re.search(pattern, content, re.DOTALL):
        new_content = re.sub(pattern, new_progress, content, flags=re.DOTALL)
    else:
        # Если секции нет, добавляем перед "Полезные ссылки"
        new_content = content.replace(
            "## 🔗 Полезные ссылки", f"{new_progress}\n## 🔗 Полезные ссылки"
        )

    # Записываем обновленный README
    readme_path.write_text(new_content, encoding="utf-8")
    print(f"✅ README обновлен! Решено задач: {total_tasks}")
    print(f"📊 Прогресс: {calculate_progress(completed_sections):.1f}%")


if __name__ == "__main__":
    update_readme()
