FROM node:14

WORKDIR ./myapp

COPY . .

RUN npm install express nodemon

EXPOSE 3000


CMD [ "node", "server.js" ]