#pip install -r examples/requirements.txt --allow-all-external --allow-unverified django-admin-tools
pip install -r examples/requirements/django_1_6.txt
python setup.py install
mkdir -p examples/logs examples/db examples/media examples/media/static examples/media/fobi_plugins/content_image
mkdir -p examples/media/fobi_plugins/file
python examples/simple/manage.py collectstatic --noinput --traceback -v 3 --settings=settings.bootstrap3_theme_django_1_6 --traceback -v 3
python examples/simple/manage.py syncdb --noinput --traceback -v 3 --settings=settings.bootstrap3_theme_django_1_6 --traceback -v 3
python examples/simple/manage.py migrate --noinput --traceback -v 3 --settings=settings.bootstrap3_theme_django_1_6 --traceback -v 3
python examples/simple/manage.py fobi_create_test_data --traceback -v 3 --settings=settings.bootstrap3_theme_django_1_6 --traceback -v 3
