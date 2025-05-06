# Use a lightweight official Python base image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app/app

# Set working directory inside the container
WORKDIR /app

# Install dependencies (optimize caching)
COPY requirements.txt .
COPY .flake8 /app/.flake8
RUN pip install --no-cache-dir -r requirements.txt

# Copy application source code
COPY app/ /app
COPY tests/ /app/tests
COPY app/main.py /app/main.py

# Set the default command to run the application
# CMD ["python", "main.py"]
CMD ["tail", "-f", "/dev/null"]