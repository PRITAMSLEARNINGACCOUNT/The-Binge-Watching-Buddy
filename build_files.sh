apt-get update && apt-get install -y default-libmysqlclient-dev
pip install setuptools
pip install -r requirements.txt
python manage.py collectstatic
python manage.py makemigrations
python manage.py migrate