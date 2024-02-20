# Python 3.10.13을 포함한 Debian Bullseye 기반 이미지 사용
FROM python:3.10.13-bullseye

# 작업 디렉토리 설정
WORKDIR /app

# 의존성 파일 복사 및 설치
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# 프로젝트 파일 복사
COPY . .

# 포트 열기
EXPOSE 8000

# Django 서버 실행
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]