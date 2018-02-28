#!/usr/bin/env bash
reset
#./scripts/uninstall.sh
#./scripts/install.sh
python examples/simple/manage.py test fobi --settings=settings.test
