FROM python:3.10-slim

WORKDIR /app

# 1. Copy ONLY requirements first
COPY requirements.txt .

# 2. Install dependencies (This layer will be CACHED unless requirements.txt changes)
RUN pip install --no-cache-dir -r requirements.txt

# 3. Copy the rest of the code (This happens in seconds)
COPY . .

EXPOSE 8000
CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "8000"]