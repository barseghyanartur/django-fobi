reset
./scripts/uninstall.sh
./scripts/install_django_1_9.sh
python examples/simple/manage.py test fobi --settings=settings.bootstrap3_theme_django_1_9 --traceback -v 3
