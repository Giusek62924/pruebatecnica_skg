FROM node:18-alpine as build-step

RUN mkdir -p /skg/app

WORKDIR /skg/app

COPY dist.zip /skg/app

RUN unzip dist.zip

FROM nginx:1.21.6-alpine

COPY --from=build-step /skg/app/dist/front-ptskg /usr/share/nginx/html
