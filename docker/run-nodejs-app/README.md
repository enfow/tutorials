# Run NodeJS App on Docker

- Docker를 사용하여 NodeJS Application을 실행하는 방법은 다음과 같다.

## 1. Build Docker Image

- 다음과 같은 Dockerfile을 작성한다.
- COPY를 두 번에 나누어 하고 있다.
  - 종속성(package.json)과 관련된 부분과 그외 부분을 나눔으로서 source code만 바꾸기 위한 목적으로 재 build 할 때  npm install을 생략하도록 한다.

```bash
FROM node:14

WORKDIR /usr/src/app

# package*.json을 Container의 ./ 에 추가
COPY package*.json ./

# package.json의 dependencies 설치
RUN npm install

COPY index.js ./

EXPOSE 3000

CMD ["node", "index.js"]
```

- Image를 build 한다.

```bash
$ docker build ./ -t <Image NAME>
```

## 2. Run Docker Container

- Docker Container에 접근하기 위해서는 Port Mapping을 해주어야 한다.

```bash
$ docker run -p 3000:3000 <Image NAME>
```

## 3. Request to Docker Container

- 매핑한 포트로 Request를 보내면 적절한 Response를 받게 된다.

```bash
$ curl -X GET http://localhost:3000

# -> hello world
```

## 4. Update Application without re-Build

- [Docker Run: VOLUME[Shared Filesystems]](<https://docs.docker.com/engine/reference/run/#volume-shared-filesystems>)
- Image Build시 적용되는 COPY가 아니라 Container 생성 시 파일에 접근하도록 하는 방법도 있다.
- 이렇게 하면 Source Code가 바뀔 때마다 매번 Image를 build 할 필요가 없다.

```bash
# -v [host-src:]container-dest

# select directory
docker run -v $(pwd):/usr/src/app <Image NAME>
# or specific file
docker run -v $(pwd)/index.js:/usr/src/app/index.js <Image NAME>
```
