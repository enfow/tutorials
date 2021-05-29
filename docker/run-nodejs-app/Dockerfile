FROM node:14

# Working directory 설정
WORKDIR /usr/src/app

# package*.json을 Container의 ./ 에 추가
COPY package*.json ./

# package.json의 dependencies 설치
RUN npm install

COPY index.js ./

EXPOSE 3000

CMD ["node", "index.js"]
