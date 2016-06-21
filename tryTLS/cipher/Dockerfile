FROM nginx:1.9.7
ADD default.conf /etc/nginx/conf.d/
ADD server/server.key /etc/nginx/server/server.key

# all_complementofall 
ADD server/all_complementofall/index.html /usr/share/nginx/server/all_complementofall/html/index.html
ADD server/ok/ssl/server.crt /etc/nginx/server/ok/ssl/server.crt

# high 
ADD server/high/index.html /usr/share/nginx/server/high/html/index.html
ADD server/ok/ssl/server.crt /etc/nginx/server/ok/ssl/server.crt

# medium 
ADD server/medium/index.html /usr/share/nginx/server/medium/html/index.html
ADD server/ok/ssl/server.crt /etc/nginx/server/ok/ssl/server.crt

# insecure 
ADD server/insecure/index.html /usr/share/nginx/server/insecure/html/index.html
ADD server/ok/ssl/server.crt /etc/nginx/server/ok/ssl/server.crt
