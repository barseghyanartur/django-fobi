#./scripts/uninstall.sh
#./scripts/install.sh
rm docs/*.rst
rm -rf builddocs/
sphinx-apidoc src/fobi --full -o docs -H 'django-fobi' -A 'Artur Barseghyan <artur.barseghyan@gmail.com>' -V '0.1' -f -d 20
cp docs/conf.distrib docs/conf.py
