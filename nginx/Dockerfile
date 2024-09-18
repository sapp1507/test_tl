FROM nginx:alpine

COPY nginx.conf /etc/nginx
COPY default.conf /etc/nginx/conf.d/default.conf
COPY upstream.conf /etc/nginx/conf.d/upstream.conf
COPY proxy_params /etc/nginx/proxy_params

RUN echo http://dl-2.alpinelinux.org/alpine/edge/community >> /etc/apk/repositories
RUN apk --no-cache add bash shadow nano && \
    adduser -u 1000 -G www-data -s /bin/sh -D www-data && \
    usermod -u 1000 www-data

EXPOSE 80

CMD ["nginx"]