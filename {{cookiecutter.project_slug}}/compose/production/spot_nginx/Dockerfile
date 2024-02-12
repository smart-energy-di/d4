FROM nginx:1.25

RUN rm /etc/nginx/conf.d/default.conf
COPY ./compose/production/spot_nginx/nginx.conf /etc/nginx/conf.d
