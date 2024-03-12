# Node.js 이미지를 기반으로 함
FROM node:lts

# 작업 디렉토리 설정
WORKDIR /app

# 의존성 파일 복사 및 설치
COPY package*.json ./
RUN npm install --silent

# 프로젝트 파일 복사
COPY . .

# 포트 열기
EXPOSE 5173

# Vite 개발 서버를 실행
CMD ["npm", "run", "dev"]
