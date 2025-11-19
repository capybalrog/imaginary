# Используем официальный образ Python 3.13
FROM python:3.13-slim

# Установка переменных окружения
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app

# Установка рабочей директории
WORKDIR /app

# Зависимости для psycopg2 и других библиотек
RUN apt-get update && apt-get install -y \
    gcc \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Копируем requirements и устанавливаем зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Создаём папку static, если её нет
RUN mkdir -p static

# Копируем весь проект
COPY . .

# Открываем порт
EXPOSE 8000

# По умолчанию запускаем API
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
