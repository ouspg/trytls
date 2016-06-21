FROM nginx:1.9.7
ADD default.conf /etc/nginx/conf.d/
ADD server/server.key /etc/nginx/server/server.key

# ok 
ADD server/ok/index.html /usr/share/nginx/server/ok/html/index.html
ADD server/ok/ssl/server.crt /etc/nginx/server/ok/ssl/server.crt

# wrong_cn 
ADD server/wrong_cn/index.html /usr/share/nginx/server/wrong_cn/html/index.html
ADD server/wrong_cn/ssl/server.crt /etc/nginx/server/wrong_cn/ssl/server.crt

# small_ending_day 
ADD server/small_ending_day/index.html /usr/share/nginx/server/small_ending_day/html/index.html
ADD server/small_ending_day/ssl/server.crt /etc/nginx/server/small_ending_day/ssl/server.crt
