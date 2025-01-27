# 1. Node.js 기반 이미지 사용
FROM node:16 AS build

# 2. 애플리케이션 코드 작업 디렉토리 설정
WORKDIR /app

# 3. package.json과 package-lock.json을 복사하고 의존성 설치
COPY package*.json /app/
RUN npm install

# 4. 애플리케이션 소스 코드를 복사
COPY . /app/

# 5. React 앱 빌드
RUN npm run build

# 6. Nginx를 이용해 빌드된 파일을 서빙
FROM nginx:alpine

# 7. Nginx 설정 파일을 복사 (기본 Nginx 설정을 덮어씀)
COPY --from=build /app/build /usr/share/nginx/html

# 8. Nginx의 기본 포트를 개방 (80)
EXPOSE 80

# 9. Nginx로 애플리케이션 실행
CMD ["nginx", "-g", "daemon off;"]
