# backend/Dockerfile
FROM python:3.9-slim

WORKDIR /app

# requirements.txt 파일을 먼저 복사하고 의존성 설치
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# FastAPI 애플리케이션 복사
COPY . /app/

EXPOSE 8000

# FastAPI 실행
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
