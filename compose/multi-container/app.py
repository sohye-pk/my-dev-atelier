from flask import Flask
from redis import Redis

app = Flask(__name__)
# 'redis-db'라는 서비스 이름으로 접속 (Service Discovery 활용)
cache = Redis(host='redis-db', port=6379)

@app.route('/')
def hello():
    print("Nginx로부터 요청을 받았습니다!") # 로그에 출력됨
    count = cache.incr('hits')
    print(f"Redis에 접속해서 숫자를 {count}로 올렸습니다.") # 로그에 출력됨
    return f'안녕하세요! 이 페이지는 {count}번 조회되었습니다.\n'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
