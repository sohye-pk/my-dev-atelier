# 🎨 My Dev Atelier: 개발 환경 구축 기록<!-- omit in toc -->

개발 환경 구축 과정과 Git/GitHub 연동, 권한 관리 및 컨테이너 환경 설정을 기록한 기술 문서입니다.

---

# 1. 프로젝트 준비 및 환경 설정

## 1.1. 프로젝트 개요
본 프로젝트는 개발자의 핵심 도구인 터미널(CLI), Docker, Git을 활용하여 효율적이고 재현 가능한 개발 워크스테이션을 구축하는 것을 목표로 합니다. 
단순한 도구 설치를 넘어, 컨테이너 기술을 이용해 환경에 구애받지 않는 웹 서버를 배포하고 데이터 영속성을 직접 검증합니다. 
또한, Git과 GitHub을 연동하여 코드의 이력을 관리하고 협업의 기반을 마련하는 과정을 포함합니다. 
이 과정을 통해 '내 컴퓨터에서만 안 되는' 문제를 해결하고, 어떤 환경에서도 동일하게 동작하는 시스템 설계 사고방식을 학습합니다.

## 1.2. 실행 환경
- OS: macOS Sequoia (v15.7.4)
- Shell: /bin/zsh 
- Docker: 28.5.2
- Git: 2.53.0

## 1.3. 검증 방법


## 1.4. 체크리스트


## 1.5. 목차<!-- omit in toc -->
- [1. 프로젝트 준비 및 환경 설정](#1-프로젝트-준비-및-환경-설정)
  - [1.1. 프로젝트 개요](#11-프로젝트-개요)
  - [1.2. 실행 환경](#12-실행-환경)
  - [1.3. 검증 방법](#13-검증-방법)
  - [1.4. 체크리스트](#14-체크리스트)
- [2. 실습 과정 및 로그 기록](#2-실습-과정-및-로그-기록)
  - [2.1. 터미널 조작 로그](#21-터미널-조작-로그)
  - [2.2. 권한 관리 로그](#22-권한-관리-로그)
  - [2.3. Docker 설치 및 기본 점검](#23-docker-설치-및-기본-점검)
  - [2.4. Docker 기본 운영 명령 수행](#24-docker-기본-운영-명령-수행)
  - [2.5. 컨테이너 실행](#25-컨테이너-실행)
  - [2.6. 기존 Dockerfile 기반 커스텀 이미지 제작](#26-기존-dockerfile-기반-커스텀-이미지-제작)
  - [2.7. 포트 매핑 및 접속 결과](#27-포트-매핑-및-접속-결과)
  - [2.8. Docker 볼륨 영속성 검증](#28-docker-볼륨-영속성-검증)
  - [2.9. Git 설정 및 GitHub 연동](#29-git-설정-및-github-연동)
  - [2.10. Git 설정 및 GitHub 연동](#210-git-설정-및-github-연동)
- [3. 트러블 슈팅](#3-트러블-슈팅)
  - [3.1. 폴더 이동 후 원본 폴더가 잔존하는 현상 (Ghost Folder)](#31-폴더-이동-후-원본-폴더가-잔존하는-현상-ghost-folder)

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

## 2.3. Docker 설치 및 기본 점검

### 2.3.1. Docker 버전 확인<!-- omit in toc -->
```bash
user ~/my-dev-atelier % docker --version
Docker version 28.5.2, build ecc6942
```

### 2.3.2. Docker 데몬 동작 여부 확인 결과<!-- omit in toc -->

<details>
<summary>결과 보기</summary>

```bash
user ~/my-dev-atelier % docker info
Client:
 Version:    28.5.2
 Context:    orbstack
 Debug Mode: false
 Plugins:
  buildx: Docker Buildx (Docker Inc.)
    Version:  v0.29.1
    Path:     /Users/sohye.pk4010/.docker/cli-plugins/docker-buildx
  compose: Docker Compose (Docker Inc.)
    Version:  v2.40.3
    Path:     /Users/sohye.pk4010/.docker/cli-plugins/docker-compose

Server:
 Containers: 3
  Running: 0
  Paused: 0
  Stopped: 3
 Images: 1
 Server Version: 28.5.2
 Storage Driver: overlay2
  Backing Filesystem: btrfs
  Supports d_type: true
  Using metacopy: false
  Native Overlay Diff: true
  userxattr: false
 Logging Driver: json-file
 Cgroup Driver: cgroupfs
 Cgroup Version: 2
 Plugins:
  Volume: local
  Network: bridge host ipvlan macvlan null overlay
  Log: awslogs fluentd gcplogs gelf journald json-file local splunk syslog
 CDI spec directories:
  /etc/cdi
  /var/run/cdi
 Swarm: inactive
 Runtimes: io.containerd.runc.v2 runc
 Default Runtime: runc
 Init Binary: docker-init
 containerd version: 1c4457e00facac03ce1d75f7b6777a7a851e5c41
 runc version: d842d7719497cc3b774fd71620278ac9e17710e0
 init version: de40ad0
 Security Options:
  seccomp
   Profile: builtin
  cgroupns
 Kernel Version: 6.17.8-orbstack-00308-g8f9c941121b1
 Operating System: OrbStack
 OSType: linux
 Architecture: x86_64
 CPUs: 6
 Total Memory: 15.67GiB
 Name: orbstack
 ID: f9f4f5ba-6b06-47b3-bb76-b2589f771631
 Docker Root Dir: /var/lib/docker
 Debug Mode: false
 Experimental: false
 Insecure Registries:
  ::1/128
  127.0.0.0/8
 Live Restore Enabled: false
 Product License: Community Engine
 Default Address Pools:
   Base: 192.168.97.0/24, Size: 24
   Base: 192.168.107.0/24, Size: 24
   Base: 192.168.117.0/24, Size: 24
   Base: 192.168.147.0/24, Size: 24
   Base: 192.168.148.0/24, Size: 24
   Base: 192.168.155.0/24, Size: 24
   Base: 192.168.156.0/24, Size: 24
   Base: 192.168.158.0/24, Size: 24
   Base: 192.168.163.0/24, Size: 24
   Base: 192.168.164.0/24, Size: 24
   Base: 192.168.165.0/24, Size: 24
   Base: 192.168.166.0/24, Size: 24
   Base: 192.168.167.0/24, Size: 24
   Base: 192.168.171.0/24, Size: 24
   Base: 192.168.172.0/24, Size: 24
   Base: 192.168.181.0/24, Size: 24
   Base: 192.168.183.0/24, Size: 24
   Base: 192.168.186.0/24, Size: 24
   Base: 192.168.207.0/24, Size: 24
   Base: 192.168.214.0/24, Size: 24
   Base: 192.168.215.0/24, Size: 24
   Base: 192.168.216.0/24, Size: 24
   Base: 192.168.223.0/24, Size: 24
   Base: 192.168.227.0/24, Size: 24
   Base: 192.168.228.0/24, Size: 24
   Base: 192.168.229.0/24, Size: 24
   Base: 192.168.237.0/24, Size: 24
   Base: 192.168.239.0/24, Size: 24
   Base: 192.168.242.0/24, Size: 24
   Base: 192.168.247.0/24, Size: 24
   Base: fd07:b51a:cc66:d000::/56, Size: 64

WARNING: DOCKER_INSECURE_NO_IPTABLES_RAW is set
```
</details>

## 2.4. Docker 기본 운영 명령 수행

### 2.4.1. 이미지<!-- omit in toc -->
```bash
user ~/my-dev-atelier % docker images
REPOSITORY    TAG       IMAGE ID       CREATED        SIZE
hello-world   latest    e2ac70e7319a   4 months ago   10.1kB
```

### 2.4.2. 컨테이너<!-- omit in toc -->
```bash
# 현재 실행 중인 컨테이너만 확인
user ~/my-dev-atelier % docker ps
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES

# 모든 컨테이너를 확인
user ~/my-dev-atelier % docker ps -a
CONTAINER ID   IMAGE         COMMAND    CREATED          STATUS                      PORTS     NAMES
7be917bc5027   hello-world   "/hello"   22 minutes ago   Exited (0) 22 minutes ago             gallant_curran
5bdd4696e042   hello-world   "/hello"   22 minutes ago   Exited (0) 22 minutes ago             jolly_gagarin
e183cf82c3b1   hello-world   "/hello"   53 minutes ago   Exited (0) 53 minutes ago             admiring_hellman
```

### 2.4.3. 운영<!-- omit in toc -->
```bash
# docker logs <컨테이너 ID/이름>
# 실행 중이거나 실행되었던 컨테이너가 출력한 내용(로그) 확인
user ~/my-dev-atelier % docker logs 7be917bc5027

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/

# docker stats <컨테이너 ID/이름>
# 실행 중인 컨테이너의 CPU, 메모리, 네트워크, 디스크 I/O 등 리소스 사용량을 실시간으로 확인
user ~/my-dev-atelier % docker logs admiring_hellman

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
CONTAINER ID   NAME               CPU %     MEM USAGE / LIMIT   MEM %     NET I/O   BLOCK I/O   PIDS 
e183cf82c3b1   admiring_hellman   --        -- / --             --        --        --          -- 
```

## 2.5. 컨테이너 실행

### 2.5.1. hello-world수행 결과<!-- omit in toc -->
```bash
user ~/my-dev-atelier % docker run hello-world

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/
```

### 2.5.2. ubuntu 수행 결과<!-- omit in toc -->
```bash
user ~/my-dev-atelier % docker run -it ubuntu bash
root@cc7d24ad97eb:/# ls
bin  boot  dev  etc  home  lib  lib64  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
root@cc7d24ad97eb:/# echo hello, wolrd
hello, wolrd
root@cc7d24ad97eb:/# pwd
/
root@cc7d24ad97eb:/# exit
exit
user ~/my-dev-atelier % 
```

### 2.5.3. 컨테이너 종료/유지<!-- omit in toc -->
```bash
# attach
# 기존 컨테이너의 메인 프로세스와 연동됨
user ~/my-dev-atelier % docker run -itd --name attach-test ubuntu bash
0b0d6b950590970e7e400f768b39bcfbdf2b0420c5c5a0be439b26484850c646

# 1. 실행 중인 컨테이너에 접속
user ~/my-dev-atelier % docker attach attach-test

# 2. 접속된 상태에서 exit 입력
root@0b0d6b950590:/# exit
exit

# 3. 컨테이너 상태 확인(Exited)
user ~/my-dev-atelier % docker ps -a
CONTAINER ID   IMAGE     COMMAND   CREATED          STATUS                     PORTS     NAMES
0b0d6b950590   ubuntu    "bash"    22 seconds ago   Exited (0) 2 seconds ago             attach-test

# exec
# 기존 컨테이너의 실행에 영향을 미치지 않음
user ~/my-dev-atelier % docker run -itd --name exec-test ubuntu bash
1d76145b84d6699371898c42f8b743db44d5a77597c63e470eb06594ee1dc9e5

# 2. 이번엔 exec로 접속
user ~/my-dev-atelier % docker exec -it exec-test bash

# 3. 접속된 상태에서 exit 입력
root@1d76145b84d6:/# exit
exit

# 4. 컨테이너 상태 확인(Up)
user ~/my-dev-atelier % docker ps   
CONTAINER ID   IMAGE     COMMAND   CREATED          STATUS          PORTS     NAMES
1d76145b84d6   ubuntu    "bash"    21 seconds ago   Up 20 seconds             exec-test
```

## 2.6. 기존 Dockerfile 기반 커스텀 이미지 제작

### 2.6.1. 커스텀 이미지 기본 사항<!-- omit in toc -->
- 베이스 이미지: nginx:latest
- 커스텀 포인트 및 목적
  - 정적 콘텐츠(index.html) 교체
    - 목적: 기본 Nginx 초기 화면 대신 사용자 정의 웹 페이지를 노출
  - 설정 파일 (default.conf) 교체
    - 목적: Nginx의 수신 포트를 기본 80번에서 8080번으로 변경하여 설정 파일이 정상적으로 적용되는지 확인

### 2.6.2. 빌드/실행 명령 및 결과<!-- omit in toc -->

```bash
# 이미지 빌드
docker build -t my-custom-nginx .

# 컨테이너 실행
docker run -d -p 1234:8080 --name my-web-container my-custom-nginx
```

<details>
<summary>결과 보기</summary>

```bash
# 빌드 결과
user ~/my-dev-atelier % docker build -t my-custom-nginx .
[+] Building 0.9s (8/8) FINISHED                                                                                                                                                                docker:orbstack
 => [internal] load build definition from Dockerfile                                                                                                                                                       0.1s
 => => transferring dockerfile: 484B                                                                                                                                                                       0.0s
 => [internal] load metadata for docker.io/library/nginx:latest                                                                                                                                            0.0s
 => [internal] load .dockerignore                                                                                                                                                                          0.0s
 => => transferring context: 2B                                                                                                                                                                            0.0s
 => [1/3] FROM docker.io/library/nginx:latest                                                                                                                                                              0.0s
 => [internal] load build context                                                                                                                                                                          0.1s
 => => transferring context: 294B                                                                                                                                                                          0.0s
 => CACHED [2/3] COPY index.html /usr/share/nginx/html/index.html                                                                                                                                          0.0s
 => [3/3] COPY default.conf /etc/nginx/conf.d/default.conf                                                                                                                                                 0.2s
 => exporting to image                                                                                                                                                                                     0.2s
 => => exporting layers                                                                                                                                                                                    0.1s
 => => writing image sha256:ff34eb165cdea3c92032b5cef62287d74a026849a188daa8759a7054cee36196                                                                                                               0.0s
 => => naming to docker.io/library/my-custom-nginx    

# 로그 
user ~/my-dev-atelier % docker logs my-web-container
/docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to perform configuration
/docker-entrypoint.sh: Looking for shell scripts in /docker-entrypoint.d/
/docker-entrypoint.sh: Launching /docker-entrypoint.d/10-listen-on-ipv6-by-default.sh
10-listen-on-ipv6-by-default.sh: info: Getting the checksum of /etc/nginx/conf.d/default.conf
10-listen-on-ipv6-by-default.sh: info: /etc/nginx/conf.d/default.conf differs from the packaged version
/docker-entrypoint.sh: Sourcing /docker-entrypoint.d/15-local-resolvers.envsh
/docker-entrypoint.sh: Launching /docker-entrypoint.d/20-envsubst-on-templates.sh
/docker-entrypoint.sh: Launching /docker-entrypoint.d/30-tune-worker-processes.sh
/docker-entrypoint.sh: Configuration complete; ready for start up
2026/07/29 11:21:55 [notice] 1#1: using the "epoll" event method
2026/07/29 11:21:55 [notice] 1#1: nginx/1.31.3
2026/07/29 11:21:55 [notice] 1#1: built by gcc 14.2.0 (Debian 14.2.0-19) 
2026/07/29 11:21:55 [notice] 1#1: OS: Linux 6.17.8-orbstack-00308-g8f9c941121b1
2026/07/29 11:21:55 [notice] 1#1: getrlimit(RLIMIT_NOFILE): 20480:1048576
2026/07/29 11:21:55 [notice] 1#1: start worker processes
2026/07/29 11:21:55 [notice] 1#1: start worker process 28
2026/07/29 11:21:55 [notice] 1#1: start worker process 29
2026/07/29 11:21:55 [notice] 1#1: start worker process 30
2026/07/29 11:21:55 [notice] 1#1: start worker process 31
2026/07/29 11:21:55 [notice] 1#1: start worker process 32
2026/07/29 11:21:55 [notice] 1#1: start worker process 33
2026/07/29 11:22:05 [error] 28#28: *1 open() "/usr/share/nginx/html/favicon.ico" failed (2: No such file or directory), client: 192.168.215.1, server: localhost, request: "HEAD /favicon.ico HTTP/1.1", host: "192.168.215.2:8080"
192.168.215.1 - - [29/Jul/2026:11:22:05 +0000] "HEAD /favicon.ico HTTP/1.1" 404 0 "-" "OrbStack-Server-Detection/1.0 (https://orb.cx/srvdetect)" "-"
192.168.215.1 - - [29/Jul/2026:11:22:05 +0000] "GET / HTTP/1.1" 200 245 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36" "-"
2026/07/29 11:22:05 [error] 29#29: *2 open() "/usr/share/nginx/html/favicon.ico" failed (2: No such file or directory), client: 192.168.215.1, server: localhost, request: "HEAD /favicon.ico HTTP/1.1", host: "192.168.215.2:8080"
192.168.215.1 - - [29/Jul/2026:11:22:05 +0000] "HEAD /favicon.ico HTTP/1.1" 404 0 "-" "OrbStack-Server-Detection/1.0 (https://orb.cx/srvdetect)" "-"
192.168.215.1 - - [29/Jul/2026:11:22:05 +0000] "GET /favicon.ico HTTP/1.1" 404 555 "http://my-web-container.orb.local/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36" "-"
2026/07/29 11:22:05 [error] 30#30: *3 open() "/usr/share/nginx/html/favicon.ico" failed (2: No such file or directory), client: 192.168.215.1, server: localhost, request: "GET /favicon.ico HTTP/1.1", host: "my-web-container.orb.local", referrer: "http://my-web-container.orb.local/"
192.168.215.1 - - [29/Jul/2026:11:27:09 +0000] "GET / HTTP/1.1" 200 245 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36" "-"
192.168.215.1 - - [29/Jul/2026:11:27:20 +0000] "GET / HTTP/1.1" 200 245 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36" "-"
192.168.215.1 - - [29/Jul/2026:11:27:52 +0000] "GET / HTTP/1.1" 304 0 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36" "-"
192.168.215.1 - - [29/Jul/2026:11:28:14 +0000] "GET / HTTP/1.1" 200 245 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36" "-"
```
</details>

## 2.7. 포트 매핑 및 접속 결과
```bash
# Docker Hub의 이미지를 임의 포트를 설정하여 
user ~/my-dev-atelier % docker run -p 730:80 nginx
```
![포트 매핑 결과1](./assets/port-connect-success.png)

```bash
user ~/my-dev-atelier % docker run -d -p 1234:8080 --name my-web-container my-custom-nginx
```
![포트 매핑 결과2](./assets/custom-page-build-success.png)

## 2.8. Docker 볼륨 영속성 검증

### 2.8.1. 바인드 마인트<!-- omit in toc -->
- 내 컴퓨터의 특정 폴더와 컨테이너 내부의 폴더를 실시간으로 연결
```bash
# 1. 호스트에 파일 생성
user ~/my-dev-atelier % echo "Before Change" > test.txt

# 2. 바인드 마운트로 컨테이너 실행
user ~/my-dev-atelier % docker run -it --name bind-test -v .:/app ubuntu bash

# 3. 기존 파일 내용 확인
root@f0bd5c420396:/# cat /app/test.txt
Before Change

# 4. (다른 터미널에서) 호스트 파일 수정 및 확인
user2 ~/my-dev-atelier % echo "After Change" > test.txt
user2 ~/my-dev-atelier % cat test.txt
After Change

# 5. 기존 터미널에서 수정된 내용 확인
root@f0bd5c420396:/# cat /app/test.txt
After Change
```

### 2.8.2. 볼륨 영속성<!-- omit in toc -->
```bash
# 1. 볼륨 생성 및 확인
user ~/my-dev-atelier % docker volume create vol
vol
user ~/my-dev-atelier % docker volume ls
DRIVER    VOLUME NAME
local     vol

# 2. 컨테이너 실행 및 데이터 쓰기
user ~/my-dev-atelier % docker run -it --name vol-test1 -v vol:/data ubuntu bash
root@eba4c824d7f1:/# echo "Keep this data" > /data/save.txt
root@eba4c824d7f1:/# exit
exit

# 3. 컨테이너 삭제
user ~/my-dev-atelier % docker rm vol-test1
vol-test1

# 4. 새 컨테이너에서 볼륨 연결 후 확인
user ~/my-dev-atelier % docker run -it --name vol-test2 -v vol:/data ubuntu bash
root@32162810be10:/# cat /data/save.txt
Keep this data
```

## 2.9. Git 설정 및 GitHub 연동

### 2.9.1. Git 설정<!-- omit in toc -->
```bash
user ~/my-dev-atelier % git config --list | grep -E "user|init"
user.name=sohye-pk
user.email=sohye.pk@gmail.com
init.defaultbranch=main
```

### 2.9.2. VSCode & GitHub 연동<!-- omit in toc -->
```bash
user ~/my-dev-atelier % git remote -v                              
origin  https://github.com/sohye-pk/my-dev-atelier.git (fetch)
origin  https://github.com/sohye-pk/my-dev-atelier.git (push)
```
![GitHub/VSCode 연동](./assets/github-vscode-connection.png)

## 2.10. Git 설정 및 GitHub 연동

### 2.10.1. 운영 리소스<!-- omit in toc -->
```bash

```


# 3. 트러블 슈팅

## 3.1. 폴더 이동 후 원본 폴더가 잔존하는 현상 (Ghost Folder)

### 3.1.1. 문제<!-- omit in toc -->
폴더 이동 후 잠시 자리를 비우고 돌아오니 원본 위치에도 폴더가 그대로 남아 있는 데이터 중복 현상 발견
<details>
<summary>문제 로그</summary>

```bash
# 기존 파일/폴더 목록
user /Users/Shared % ls
SC Info   my-dev-atelier

# 이동 폴더 생성
user /Users/Shared % mkdir user

# 파일 이동 후 목록 확인
user /Users/Shared % mv my-dev-atelier user/my-dev-atelier
user /Users/Shared % ls
SC Info user
user /Users/Shared % cd user  
user /Users/Shared/user % ls
my-dev-atelier

# 문제 발생
  [Restored Jul 28, 2026 at 2:37:25 PM]
Last login: Tue Jul 28 14:37:22 on console
user my-dev-atelier % ls ../..
SC Info   my-dev-atelier  user
user my-dev-atelier % cd ../.. 
user Shared % ls
SC Info   my-dev-atelier  user
```
</details>

### 3.1.2. 원인 가설<!-- omit in toc -->
1. APFS 파일 시스템의 '원자적 작업' 중단
    - mv 명령어는 내부적으로 복사(Copy) -> 삭제(Delete) 단계를 거침.
데이터 복사는 완료되어 목적지에 기록되었으나, 원본을 삭제하는 '커밋(Commit)' 단계가 디스크에 물리적으로 반영되기 직전에 시스템 지연이나 세션 중단이 발생했을 가능성.
1. macOS 로컬 스냅샷(Snapshot)에 의한 롤백
    - macOS(APFS)는 약 1시간 간격으로 시스템 상태를 스냅샷으로 저장함.
13:20(명령어 실행)과 14:37(세션 복구) 사이의 시간 간격을 고려할 때, 시스템이 예기치 않게 재시작되면서 명령어 실행 직전의 안정적인 스냅샷 상태로 파일 시스템 일부가 복구되었을 가능성.
이 과정에서 이미 디스크에 써진 '새 폴더'는 유지되고, 삭제되었어야 할 '원본 폴더'가 롤백되어 다시 나타남.
### 3.1.3. 확인 및 추론<!-- omit in toc -->
- 로그 분석을 통한 추론

시간대 대조: 사용자가 자리를 비운 13:20 이후부터 세션이 복구된 14:37 사이의 공백은 시스템이 '절전 모드 해제 실패' 또는 '커널 패닉' 등으로 인해 정상적인 디스크 기록 프로세스를 완료하지 못했음을 시사함.

세션 복구 메시지: [Restored...] 메시지는 터미널 앱이 비정상 종료 후 이전 상태를 강제로 불러왔음을 의미하며, 이 과정에서 파일 시스템의 실제 상태와 터미널의 가상 상태 간의 충돌이 가시화됨.위치에 잔존하는 폴더는 시스템 복구 과정에서 생성된 '유령 폴더'이므로 rm -rf 명령어로 안전하게 삭제.

* (참고) 향후 동일 현상 발생 시 검증 방법

inode 번호 비교: ls -id [원본폴더] [목적지폴더]를 입력하여 고유 번호(inode)를 비교.
번호가 같다면: 하드 링크 형태의 오류.
번호가 다르다면: 시스템 복구 과정에서 별개로 생성/복구된 객체임이 확실함.

### 3.1.4. 해결 및 대안<!-- omit in toc -->
- 해결: 데이터 무결성 확인 후 수동 삭제 

목적지(`user/`)로 이동된 폴더 내 파일들이 깨지지 않고 정상적으로 존재하는지 확인.
원본 위치에 잔존하는 폴더는 시스템 복구 과정에서 생성된 '유령 폴더'이므로 `rm -rf` 명령어로 안전하게 삭제.

- 대안 및 예방

대용량/중요 폴더 이동 시: `mv` 대신 `rsync -aP [원본] [목적지]`를 사용하면 전송 과정을 실시간으로 모니터링할 수 있으며, 전송 완료 후 원본을 지우는 방식(`--remove-source-files`)이 더 안전함.

정기적 디스크 검사: 이러한 현상이 잦을 경우 `디스크 유틸리티`의 '검사/복구(First Aid)' 기능을 통해 파일 시스템의 일관성을 점검.