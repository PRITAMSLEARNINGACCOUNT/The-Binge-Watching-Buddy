
sudo apt-get update
sudo apt-get install -y mysql-server-8.0
sudo apt-get install -y default-libmysqlclient-dev
apt-get update && apt-get install -y default-libmysqlclient-dev
pip install setuptools
pip install -r requirements.txt
python manage.py collectstatic
python manage.py makemigrations
python manage.py migrate