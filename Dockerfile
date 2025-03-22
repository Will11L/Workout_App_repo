# Use official Python runtime as base image
FROM python:3.12.9-slim
 
# Set working directory in container
WORKDIR /app
 
# Install system dependencies (if needed, e.g., for SQLite)
RUN apt-get update && apt-get install -y \
    gcc \
&& rm -rf /var/lib/apt/lists/*
 
# Copy requirements file and install dependencies
COPY update_requirements.py .
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
 
# Copy the directory into the container
COPY core ./core
COPY data ./files
COPY files ./files
COPY  tests ./tests
 
# Copy only necessary application files
COPY app_bootstrap.py .
COPY app_database.py .
COPY common_css.py .
COPY database_page.py .
COPY exec_file.py .
COPY login_page.py .
COPY main_page.py .
COPY database.db .
# TODO : page_1.py, page_2.py will be removed
COPY page_1.py . 
COPY page_2.py .
COPY styles_database_page.py .
COPY styles_login_page.py .
COPY styles_main_page.py .
 
# Expose port 8080
EXPOSE 8080
 
# Set environment variables
ENV PYTHONUNBUFFERED=1
 
# Run the application using exec_file.py
CMD ["python", "exec_file.py"]