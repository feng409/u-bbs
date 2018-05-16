# 换源
ln -f -s /var/www/u-bbs/tuna/sources.list /etc/apt/sources.list
mkdir -p /root/.pip
ln -f -s /var/www/u-bbs/tuna/pip.conf /root/.pip/pip.conf


# 装依赖
apt-get update  # 先更新

# 装 mysql 从配置文件读取密码
# apt-get -y install debconf-utils
debconf-set-selections /var/www/u-bbs/mysql_pass
apt-get -y install mysql-server


# 装软件
apt-get install -y supervisor nginx zsh curl ufw
sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"

# 装python 3.6
# http://docs.python-guide.org/en/latest/starting/install3/linux/
add-apt-repository -y ppa:deadsnakes/ppa
apt-get update
apt-get install -y python3.6
apt-get install -y python3-pip

# 装依赖包
python3.6 -m pip install gunicorn gevent flask flask-migrate pymysql flask-sqlalchemy


# 配置防火墙
ufw allow 22
ufw allow 80
ufw allow 443
ufw default deny incoming
ufw default allow outgoing
ufw status verbose
ufw -f enable

# 删掉 nginx default 设置
rm -f /etc/nginx/sites-enabled/default
rm -f /etc/nginx/sites-available/default

# 建立一个软连接
ln -s -f /var/www/u-bbs/u-bbs.conf /etc/supervisor/conf.d/u-bbs.conf
# 不要再 sites-available 里面放任何东西
ln -s -f /var/www/u-bbs/u-bbs.nginx /etc/nginx/sites-enabled/u-bbs


# 重启服务器
service mysql restart
service supervisor restart
service nginx restart


echo 'succsss'
echo 'ip'
hostname -I

# 下面是其他尝试

# dpkg-reconfigure: unable to re-open stdin: No file or directory
# https://serverfault.com/questions/500764/dpkg-reconfigure-unable-to-re-open-stdin-no-file-or-directory
# export DEBIAN_FRONTEND=noninteractive # 禁止交互(不可取)


# 安装mysql时，解决输入密码问题
#（如果之前有安装失败，记得vagrant ssh登录后卸载掉）
# sudo apt-get --purge remove mysql-server
# sudo apt autoremove
# https://stackoverflow.com/questions/7739645/install-mysql-on-ubuntu-without-a-password-prompt
# apt-get -y install debconf-utils
# debconf-set-selections <<< 'mysql-server mysql-server/root_password password admin'
# debconf-set-selections <<< 'mysql-server mysql-server/root_password_again password admin'
# apt-get -y install mysql-server