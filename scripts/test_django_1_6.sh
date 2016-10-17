reset
./scripts/uninstall.sh
./scripts/install_django_1_6.sh
python examples/simple/manage.py test fobi --traceback -v 3 --settings=settings.bootstrap3_theme_django_1_6
