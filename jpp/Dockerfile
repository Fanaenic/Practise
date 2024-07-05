# Используем официальный образ Python версии 3.9
FROM python:3.9-slim

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем только файл requirements.txt в рабочую директорию
COPY requirements.txt /app/

# Обновляем pip и устанавливаем зависимости
RUN python -m pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Копируем все файлы из текущей директории в рабочую директорию в контейнере
COPY . /app/

# Устанавливаем команду по умолчанию для выполнения в контейнере
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
