## 터미널 조작 로그

### 현재 위치 확인
```
user /Users/Shared/user/my-dev-atelier & pwd
/Users/Shared/user/my-dev-atelier
```

### 목록 확인(숨김 파일 포함)
```
user /Users/Shared/user/my-dev-atelier & ls -a
.	..
```
### 이동
```
user /Users/Shared/user/my-dev-atelier & cd ..
user /Users/Shared/user & 
```

### 생성
```
user /Users/Shared/user/my-dev-atelier & mkdir test
user /Users/Shared/user/my-dev-atelier & ls -a
.	..	test
user /Users/Shared/user/my-dev-atelier & touch test.txt
user /Users/Shared/user/my-dev-atelier & ls -a
.		..		test		test.txt
```

### 복사
```
user /Users/Shared/user/my-dev-atelier & cp test.txt test2.txt
user /Users/Shared/user/my-dev-atelier & ls -a
.		..		test		test.txt	test2.txt
```

### 이동/이름변경
```
user /Users/Shared/user/my-dev-atelier & mv test.txt ../test2.txt
user /Users/Shared/user/my-dev-atelier & ls
README.md
user /Users/Shared/user/my-dev-atelier & ls ../
my-dev-atelier	test2.txt
```

### 삭제
```
user /Users/Shared/user/my-dev-atelier & ls
README.md	test.txt
user /Users/Shared/user/my-dev-atelier & rm test.txt
user /Users/Shared/user/my-dev-atelier & ls
README.md
```

### 파일 내용 확인
```
user /Users/Shared/user/my-dev-atelier & cat test.txt
hello, world
```

### 빈 파일 생성 
```
user /Users/Shared/user/my-dev-atelier & touch test.txt
user /Users/Shared/user/my-dev-atelier & ls -a
.		..		test		test.txt
```
