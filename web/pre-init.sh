sudo pip3 install --upgrade gunicorn
sudo pip3 install --upgrade django
g_ver=$(python3 -c "import gunicorn; print(gunicorn.__version__)")
sudo grep -rl "17.5" /usr/bin/gunicorn | sudo xargs sed -i "s/17.5/$a/g"
