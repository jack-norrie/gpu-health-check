FROM python:3.12-slim

WORKDIR /app

# Copy application code
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Correct JSON format for ENTRYPOINT
ENTRYPOINT ["python", "main.py"]
