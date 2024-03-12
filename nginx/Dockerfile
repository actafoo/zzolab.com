# Build step 1(installing node modules and preparing compiled build)
FROM node:lts as build-stage

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .

RUN npm run build


# Build step 2(Deploying build on NGINX)
FROM nginx:alpine as production-stage

COPY nginx/prod.conf /etc/nginx/nginx.conf

COPY --from=build-stage /app/dist /dist/

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]