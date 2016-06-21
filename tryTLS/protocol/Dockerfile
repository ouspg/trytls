FROM nginx:1.9.7
ADD default.conf /etc/nginx/conf.d/
ADD server/server.key /etc/nginx/server/server.key

# sslv2 
ADD server/sslv2/index.html /usr/share/nginx/server/sslv2/html/index.html
ADD server/ok/ssl/server.crt /etc/nginx/server/ok/ssl/server.crt

# sslv3 
ADD server/sslv3/index.html /usr/share/nginx/server/sslv3/html/index.html
ADD server/ok/ssl/server.crt /etc/nginx/server/ok/ssl/server.crt

# tlsv1 
ADD server/tlsv1/index.html /usr/share/nginx/server/tlsv1/html/index.html
ADD server/ok/ssl/server.crt /etc/nginx/server/ok/ssl/server.crt

# tlsv1.1 
ADD server/tlsv1.1/index.html /usr/share/nginx/server/tlsv1.1/html/index.html
ADD server/ok/ssl/server.crt /etc/nginx/server/ok/ssl/server.crt

# tlsv1.2 
ADD server/tlsv1.2/index.html /usr/share/nginx/server/tlsv1.2/html/index.html
ADD server/ok/ssl/server.crt /etc/nginx/server/ok/ssl/server.crt
