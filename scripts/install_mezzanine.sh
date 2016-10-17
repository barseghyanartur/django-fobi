#pip install -r examples/requirements.txt --allow-all-external --allow-unverified django-admin-tools
pip install -r examples/requirements/django_1_7.txt
pip install -r examples/mezzanine_example/requirements.txt
python setup.py install
mkdir -p examples/logs examples/db examples/media examples/media/static examples/media/fobi_plugins/content_image
mkdir -p examples/media/fobi_plugins/file
python examples/mezzanine_example/manage.py collectstatic --noinput --settings=settings.bootstrap3_theme_mezzanine --traceback -v 3
python examples/mezzanine_example/manage.py syncdb --noinput --settings=settings.bootstrap3_theme_mezzanine --traceback -v 3
python examples/mezzanine_example/manage.py migrate --delete-ghost-migrations --noinput --settings=settings.bootstrap3_theme_mezzanine --traceback -v 3
python examples/mezzanine_example/manage.py fobi_create_test_data --settings=settings.bootstrap3_theme_mezzanine --traceback -v 3
