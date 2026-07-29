# 1. 베이스 이미지 선택 (Nginx 최신 버전)
FROM nginx:latest

# 2. 내가 만든 index.html을 Nginx의 기본 웹 콘텐츠 경로로 복사
# Nginx의 기본 경로: /usr/share/nginx/html/
COPY index.html /usr/share/nginx/html/index.html

# 3. 설정 파일 교체 (Nginx 설정)
# 기본 설정 파일 위치인 /etc/nginx/conf.d/default.conf를 내가 만든 파일로 덮어쓰기
COPY default.conf /etc/nginx/conf.d/default.conf