[app]

# (str) Назва додатка, яку бачитиме користувач
title = МУРЧК

# (str) Назва пакета (без пробілів та спецсимволів)
package.name = calculator

# (str) Домен пакета (разом з назвою пакета утворить org.test.calculator)
package.domain = org.test

# (str) Шлях до головного файлу (зазвичай main.py)
source.dir = .

# (list) Розширення файлів, які будуть включені в збірку
source.include_exts = py,png,jpg,kv,atlas

# (str) Файл іконки (має бути в тій же папці)
icon.filename = icon.png

# (str) Версія додатка
version = 0.1

# (list) Бібліотеки, які потрібні для роботи (додай сюди інші, якщо треба)
requirements = python3,kivy

# (str) Орієнтація екрана
orientation = portrait

# (bool) Чи залишати екран увімкненим під час роботи
android.wakelock = False

# (list) Дозволи (якщо потрібен інтернет, розкоментуй)
# android.permissions = INTERNET

# (int) API рівень (33 зараз стандарт для Google Play)
android.api = 33

# (int) Мінімальний API (Android 5.0+)
android.minapi = 21

# (bool) Копіювати бібліотеки в папку додатка
android.copy_libs = 1

# (str) Тема (можна залишити стандартну)
android.entrypoint = org.kivy.android.PythonActivity

[buildozer]
# (int) Рівень деталізації логів (2 — показувати все)
log_level = 2

# (str) Папка для збереження готових .apk
bin_dir = ./bin
