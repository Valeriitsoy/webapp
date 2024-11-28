# Use lightweight Python image
FROM python:3.12-alpine

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && python -m pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . /app

# Expose the port and run the app
EXPOSE 5000
CMD ["python", "./app.py"]