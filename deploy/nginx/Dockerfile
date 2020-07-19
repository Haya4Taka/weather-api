FROM nginx

COPY deploy/nginx/nginx_default.conf.template /etc/nginx/conf.d/default.conf.template
COPY deploy/nginx/create_conf.sh /etc/nginx/conf.d/create_conf.sh

RUN ["chmod", "+x", "/etc/nginx/conf.d/create_conf.sh"]
CMD ["/etc/nginx/conf.d/create_conf.sh"]