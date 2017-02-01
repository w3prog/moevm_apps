#!/usr/bin/env bash
sudo apt-get update
sudo apt-get -y install python
sudo apt-get -y install python-dev
sudo apt-get -y install python-pip

sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 0C49F3730359A14518585931BC711F9BA15703C6
echo "deb [ arch=amd64,arm64 ] http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.4.list

sudo apt-get install -y mongodb-org
sudo pip install setuptools
sudo pip install wheel
sudo apt-get install -y apache2 apache2-dev libapache2-mod-wsgi
git clone https://github.com/w3prog/moevm_apps.git
sudo move moevm_app /var/www/mse.moevm.info
sudo chown -R :www-data /var/www/mse.moevm.info
sudo chown -R devel /var/www/mse.moevm.info
cd /var/www/mse.moevm.info
sudo pip install -r requirents.txt
python manage.py collectstatic
# сделать модификацию шаблона

sudo mv scripts/mse.moevm.info.conf /etc/apache2/sites-available/
# добавить проверку наличия загрузки данного модуля.
cat "LoadModule wsgi_module /usr/lib/apache2/modules/mod_wsgi.so" >> /etc/apache2/apache2.conf
sudo a2ensite mse.moevm.info

sudo service mongod start
sudo service apache2 start