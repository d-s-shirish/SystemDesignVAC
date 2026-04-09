# 1. Base image
FROM python:3.11-slim

# 2. Set working directory inside container
WORKDIR /app

# 3. Copy files into container
COPY . .

# 4. Install dependencies
RUN pip install --no-cache-dir -r requirements.txt
    
# 5. Expose port
EXPOSE 5000

# 6. Run application
CMD ["python", "app.py"]