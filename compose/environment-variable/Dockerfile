# 1. 베이스 이미지 선택
FROM python:3.9-slim

# 2. 작업 디렉토리 설정
WORKDIR /app

# 3. 필요한 라이브러리 설치
RUN pip install flask

# 4. 소스 코드 복사
COPY app.py .

# 5. 환경 변수 기본값 설정
ENV APP_PORT=8080
ENV APP_MODE=Production

# 6. 서버 실행
CMD ["python", "app.py"]