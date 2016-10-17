pip uninstall south -y
pip install -r examples/requirements/django_1_10.txt
python setup.py install
mkdir -p examples/logs examples/db examples/media examples/media/static examples/media/fobi_plugins/content_image
mkdir -p examples/media/fobi_plugins/file
python examples/simple/manage.py collectstatic --noinput --settings=settings.bootstrap3_theme_django_1_10 --traceback -v 3
python examples/simple/manage.py migrate --noinput --settings=settings.bootstrap3_theme_django_1_10 --traceback -v 3
python examples/simple/manage.py fobi_create_test_data --settings=settings.bootstrap3_theme_django_1_10 --traceback -v 3
