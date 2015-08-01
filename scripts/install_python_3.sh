pip install -r examples/requirements.txt
pip install -r examples/requirements_python_3.txt
python setup.py install
mkdir -p examples/logs examples/db examples/media examples/media/static examples/media/fobi_plugins/content_image
python examples/simple/manage.py collectstatic --noinput --settings=settings_bootstrap3_theme_python_3_django_1_8 --traceback -v 3
python examples/simple/manage.py syncdb --noinput --settings=settings_bootstrap3_theme_python_3_django_1_8 --traceback -v 3
python examples/simple/manage.py migrate --noinput --settings=settings_bootstrap3_theme_python_3_django_1_8 --traceback -v 3
python examples/simple/manage.py fobi_create_test_data --settings=settings_bootstrap3_theme_python_3_django_1_8 --traceback -v 3
