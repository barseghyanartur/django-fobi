#pip install -r examples\requirements.txt --allow-all-external --allow-unverified django-admin-tools
pip install -r examples\django_1_6.txt
python setup.py install
mkdir examples\logs
mkdir examples\db
mkdir examples\media
mkdir examples\media\static
mkdir examples\media\fobi_plugins\content_image
mkdir examples\media\fobi_plugins\file
python examples\simple\manage.py collectstatic --noinput --traceback -v 3
python examples\simple\manage.py syncdb --noinput --traceback -v 3
python examples\simple\manage.py migrate --noinput --traceback -v 3
python examples\simple\manage.py fobi_create_test_data --traceback -v 3
