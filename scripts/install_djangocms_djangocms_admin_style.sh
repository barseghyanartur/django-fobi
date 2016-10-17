#pip install -r examples/requirements.txt --allow-all-external --allow-unverified django-admin-tools
#pip install -r examples/requirements.txt
pip install -r examples/requirements/djangocms.txt
python setup.py install
mkdir -p examples/logs examples/db examples/media examples/media/static examples/media/fobi_plugins/content_image
mkdir -p examples/media/fobi_plugins/file
python examples/simple/manage.py collectstatic --noinput --settings=settings.djangocms_admin_style_theme_djangocms --traceback -v 3
python examples/simple/manage.py syncdb --noinput --settings=settings.djangocms_admin_style_theme_djangocms --traceback -v 3
python examples/simple/manage.py migrate --noinput --settings=settings.djangocms_admin_style_theme_djangocms --traceback -v 3
python examples/simple/manage.py fobi_create_test_data --settings=settings.djangocms_admin_style_theme_djangocms --traceback -v 3
