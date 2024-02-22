# Python 3.10.13을 포함한 Debian Bullseye 기반 이미지 사용
FROM python:3.10.13-bullseye

# 작업 디렉토리 설정
WORKDIR /app

# 의존성 파일 복사 및 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 비루트 사용자 'django' 추가
RUN adduser --disabled-password --gecos "" django

# 스크립트 디렉토리 권한 설정
COPY ./scripts /scripts
RUN chmod -R +x /scripts && \
    chown -R django:django /scripts

# 프로젝트 파일 복사 및 권한 설정
COPY --chown=django:django . .

# umask 설정
RUN umask 0022

# 포트 열기
EXPOSE 8000

# 컨테이너 실행 사용자 변경
USER django
