# 🎨 My Dev Atelier: 개발 환경 구축 기록<!-- omit in toc -->

개발 환경 구축 과정과 Git/GitHub 연동, 권한 관리 및 컨테이너 환경 설정을 기록한 기술 문서입니다.

---

# 1. 프로젝트 준비 및 환경 설정

## 1.1. 프로젝트 개요

## 1.2. 실행 환경

## 1.3. 검증 방법

## 1.4. 체크리스트

## 1.5. 목차
- [1. 프로젝트 준비 및 환경 설정](#1-프로젝트-준비-및-환경-설정)
  - [1.1. 프로젝트 개요](#11-프로젝트-개요)
  - [1.2. 실행 환경](#12-실행-환경)
  - [1.3. 검증 방법](#13-검증-방법)
  - [1.4. 체크리스트](#14-체크리스트)
  - [1.5. 목차](#15-목차)
- [2. 실습 과정 및 로그 기록](#2-실습-과정-및-로그-기록)
  - [2.1. 터미널 조작 로그](#21-터미널-조작-로그)
  - [2.2. 권한 관리 로그](#22-권한-관리-로그)
- [3. 트러블 슈팅](#3-트러블-슈팅)

# 2. 실습 과정 및 로그 기록 

## 2.1. 터미널 조작 로그

### 2.1.1. 현재 위치 확인<!-- omit in toc -->
```bash
user /Users/Shared/user/my-dev-atelier % pwd
/Users/Shared/user/my-dev-atelier
```

### 2.1.2. 목록 확인(숨김 파일 포함)<!-- omit in toc -->
```bash
user /Users/Shared/user/my-dev-atelier % ls -a
.	..
```

### 2.1.3. 이동<!-- omit in toc -->
```bash
user /Users/Shared/user/my-dev-atelier % cd ..
user /Users/Shared/user % 
```

### 2.1.4. 생성<!-- omit in toc -->
```bash
user /Users/Shared/user/my-dev-atelier % mkdir test
user /Users/Shared/user/my-dev-atelier % ls -a
.	..	test
user /Users/Shared/user/my-dev-atelier % touch test.txt
user /Users/Shared/user/my-dev-atelier % ls -a
.		..		test		test.txt
```

### 2.1.5. 복사<!-- omit in toc -->
```bash
user /Users/Shared/user/my-dev-atelier % cp test.txt test2.txt
user /Users/Shared/user/my-dev-atelier % ls -a
.		..		test		test.txt	test2.txt
```

### 2.1.6. 이동/이름변경<!-- omit in toc -->
```bash
user /Users/Shared/user/my-dev-atelier % mv test.txt ../test2.txt
user /Users/Shared/user/my-dev-atelier % ls
README.md
user /Users/Shared/user/my-dev-atelier % ls ../
my-dev-atelier	test2.txt
```

### 2.1.7. 삭제<!-- omit in toc -->
```bash
user /Users/Shared/user/my-dev-atelier % ls
README.md	test.txt
user /Users/Shared/user/my-dev-atelier % rm test.txt
user /Users/Shared/user/my-dev-atelier % ls
README.md
```

### 2.1.8. 파일 내용 확인<!-- omit in toc -->
```bash
user /Users/Shared/user/my-dev-atelier % cat test.txt
hello, world
```

### 2.1.9. 빈 파일 생성<!-- omit in toc -->
```bash
user /Users/Shared/user/my-dev-atelier % touch test.txt
user /Users/Shared/user/my-dev-atelier % ls -a
.		..		test		test.txt
```


## 2.2. 권한 관리 로그

### 2.2.1. 파일 권한 제어<!-- omit in toc -->
```bash
# [1] 초기 내용 작성 및 확인
user /Users/Shared/user/my-dev-atelier % echo "이것은 비밀 문서입니다." > test.txt
user /Users/Shared/user/my-dev-atelier % cat test.txt
이것은 비밀 문서입니다.

# [2] 권한 전체 박탈 (chmod 000)
user /Users/Shared/user/my-dev-atelier % chmod 000 test.txt

# [3] 접근 거부 확인 (Permission Denied)
user /Users/Shared/user/my-dev-atelier % cat test.txt
cat: test.txt: Permission denied
user /Users/Shared/user/my-dev-atelier % echo "내용 수정하기" > test.txt
zsh: permission denied: test.txt

# [4] 권한 복구 및 확인 (chmod 600: 소유자 읽기/쓰기)
user /Users/Shared/user/my-dev-atelier % chmod 600 test.txt
user /Users/Shared/user/my-dev-atelier % echo "내용 수정하기" > test.txt
user /Users/Shared/user/my-dev-atelier % cat test.txt                   
내용 수정하기
```

### 2.2.2. 폴더 권한 제어<!-- omit in toc -->
```bash
# [1] 디렉토리 진입 확인
user /Users/Shared/user/my-dev-atelier % cd test_dir       
user /Users/Shared/user/my-dev-atelier/test_dir cd ../

# [2] 디렉토리 권한 박탈 (chmod 000)
user /Users/Shared/user/my-dev-atelier % chmod 000 test_dir

# [3] 접근 거부 확인 (Permission Denied)
user /Users/Shared/user/my-dev-atelier % cd test_dir
cd: permission denied: test_dir

# [4] 권한 복구 및 진입 확인 (chmod 700: 소유자 모든 권한)
user /Users/Shared/user/my-dev-atelier % chmod 700 test_dir
user /Users/Shared/user/my-dev-atelier % cd test_dir
user /Users/Shared/user/my-dev-atelier/test_dir cd ../
```

### 2.2.3. 권한 최종 확인<!-- omit in toc -->
```bash
# 권한 변경 전
user /Users/Shared/user/my-dev-atelier % ls -l
total 8
-rw-r--r--  1 user  wheel  1424 Jul 28 15:04 README.md
-rw-r--r--  1 user  wheel     0 Jul 28 15:08 test.txt
drwxr-xr-x  2 user  wheel    64 Jul 28 15:08 test_dir

# 권한 변경 후
user /Users/Shared/user/my-dev-atelier % ls -l
total 16
-rw-r--r--  1 user  wheel  1424 Jul 28 15:04 README.md
-rw-------  1 user  wheel    34 Jul 28 15:17 test.txt
drwx------  2 user  wheel    64 Jul 28 15:08 test_dir
```

# 3. 트러블 슈팅