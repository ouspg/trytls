FROM nginx:1.9.7

ADD default.conf /etc/nginx/conf.d/

#ok

ADD server/ok/index.html /usr/share/nginx/server/ok/index.html
ADD server/ok/ssl/server.crt /etc/nginx/server/ok/ssl/server.crt
ADD server/ok/ssl/server.key /etc/nginx/server/ok/ssl/server.key

#wrong hostname

ADD server/hostname/index.html /usr/share/nginx/server/hostname/index.html
ADD server/hostname/ssl/server.crt /etc/nginx/server/hostname/ssl/server.crt
ADD server/hostname/ssl/server.key /etc/nginx/server/hostname/ssl/server.key
