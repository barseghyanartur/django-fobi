reset
#./scripts/uninstall.sh
./scripts/configure.sh
python examples/simple/manage.py test fobi --settings=settings_test
