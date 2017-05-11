wget -O django_fobi_example_app_installer.tar.gz https://github.com/barseghyanartur/django-fobi/archive/stable.tar.gz
virtualenv fobi
source fobi/bin/activate
mkdir django_fobi_example_app_installer/
tar -xvf django_fobi_example_app_installer.tar.gz -C django_fobi_example_app_installer
cd django_fobi_example_app_installer/django-fobi-stable/examples/simple/
pip install -r ../requirements/demo.txt
pip install https://github.com/barseghyanartur/django-fobi/archive/stable.tar.gz
mkdir ../media/
mkdir ../media/static/
mkdir ../static/
mkdir ../db/
mkdir ../logs/
mkdir ../tmp/
cp settings/local_settings.example settings/local_settings.py
#./manage.py syncdb --noinput --traceback -v 3
./manage.py migrate --noinput
./manage.py collectstatic --noinput --traceback -v 3
./manage.py fobi_create_test_data --traceback -v 3
./manage.py runserver 0.0.0.0:8001 --traceback -v 3
