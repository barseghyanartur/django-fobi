pip install -r examples/requirements_django_1_7.txt
pip install -r examples/requirements_feincms.txt
python setup.py install
mkdir -p examples/logs examples/db examples/media examples/media/static examples/media/fobi_plugins/content_image
mkdir -p examples/media/fobi_plugins/file
python examples/simple/manage.py collectstatic --noinput --settings=settings_bootstrap3_theme_django_1_7_feincms --traceback -v 3
python examples/simple/manage.py syncdb --noinput --settings=settings_bootstrap3_theme_django_1_7_feincms --traceback -v 3
python examples/simple/manage.py migrate --noinput --settings=settings_bootstrap3_theme_django_1_7_feincms --traceback -v 3
python examples/simple/manage.py fobi_create_test_data --settings=settings_bootstrap3_theme_django_1_7_feincms --traceback -v 3