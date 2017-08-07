sudo pip3 install --upgrade gunicorn
sudo pip3 install --upgrade django
g_ver=$(python3 -c "import gunicorn; print(gunicorn.__version__)")
sudo grep -rl "17.5" /usr/bin/gunicorn | sudo xargs sed -i "s/17.5/$g_ver/g"
sudo unlink /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
sudo ln -sf /home/box/web/etc/gunicorn.conf /etc/gunicorn.d/hello
sudo ln -sf /home/box/web/etc/gunicorn-django.conf /etc/gunicorn.d/django
sudo /etc/init.d/gunicorn restart
sudo /etc/init.d/mysql start
mysql -uroot -e "CREATE DATABASE qa_db;"
mysql -uroot -e "CREATE USER 'django'@'localhost' IDENTIFIED BY 'admin';"
mysql -uroot -e "GRANT ALL PRIVILEGES ON qa_db.* TO 'django'@'localhost';"
mysql -uroot -e "FLUSH PRIVILEGES;"
