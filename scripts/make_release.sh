#python setup.py register
python setup.py sdist bdist_wheel
twine upload dist/*
