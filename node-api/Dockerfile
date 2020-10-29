FROM node:14.14.0-slim
WORKDIR /app
COPY package.json .
RUN yarn install
COPY . .
EXPOSE 6104
CMD ["yarn", "serve"]
