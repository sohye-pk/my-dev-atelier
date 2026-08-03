import os
from flask import Flask

app = Flask(__name__)

# 환경 변수 읽기 (기본값 설정 가능)
# os.getenv('변수명', '기본값')
port = int(os.getenv('APP_PORT', 5000))
mode = os.getenv('APP_MODE', 'Development')

@app.route("/")
def hello():
    return f"현재 모드: {mode} / 포트: {port}에서 실행 중입니다!"

if __name__ == '__main__':
    # 서버 실행
    app.run(host='0.0.0.0', port=port)