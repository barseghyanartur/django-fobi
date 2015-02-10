reset
./scripts/uninstall.sh
./scripts/install3.sh
#cd ..
python examples/simple/manage.py test fobi --traceback
#cd scripts