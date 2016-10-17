pip install -r examples/requirements.txt
pip install -r examples/requirements/mptt.txt
python setup.py install
mkdir -p examples/logs examples/db examples/media examples/media/static examples/media/fobi_plugins/content_image
mkdir -p examples/media/fobi_plugins/file
python examples/simple/manage.py collectstatic --noinput --settings=settings.bootstrap3_theme_mptt --traceback -v 3
python examples/simple/manage.py syncdb --noinput --settings=settings.bootstrap3_theme_mptt --traceback -v 3
python examples/simple/manage.py migrate --noinput --settings=settings.bootstrap3_theme_mptt --traceback -v 3
python examples/simple/manage.py fobi_create_test_data --settings=settings.bootstrap3_theme_mptt --traceback -v 3
