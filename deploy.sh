# 建立一个软连接
ln -s -f /var/www/u-bbs/u-bbs.conf /etc/supervisor/conf.d/u-bbs.conf
# 不要再 sites-available 里面放任何东西
ln -s -f /var/www/u-bbs/u-bbs.nginx /etc/nginx/sites-enabled/u-bbs


# 重启服务器
service mysql restart
service supervisor restart
service nginx restart