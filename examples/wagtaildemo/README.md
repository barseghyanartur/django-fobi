[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/torchbox/wagtaildemo)

Wagtail demo project
=======================

This is a demonstration project for [Wagtail CMS](http://wagtail.io).

*We do __not__ recommend using this project to start your own site*. This project is only to provide some examples of implementing common features, it is not an exemplar of Django or Wagtail best practice.

If you're reasonably new to Python/Django, we suggest you run this project on a Virtual Machine using Vagrant, which helps  resolve common software dependency issues. However for more experienced developers, instructions to start this project without Vagrant follow below.

Once you're familiar with the examples in this project and you want to start a real site, we strongly recommend running the ``wagtail start`` command in a fresh virtual environment, explained in the [Wagtail CMS Documentation](http://wagtail.readthedocs.org/en/latest/getting_started/).

Setup with Vagrant
------------------

### Dependencies
* [VirtualBox](https://www.virtualbox.org/)
* [Vagrant 1.5+](http://www.vagrantup.com)

### Installation
Run the following commands:

    git clone https://github.com/torchbox/wagtaildemo.git
    cd wagtaildemo
    vagrant up
    vagrant ssh
      (then, within the SSH session:)
    ./manage.py runserver 0.0.0.0:8000

The demo site will now be accessible at [http://localhost:8000/](http://localhost:8000/) and the Wagtail admin interface at [http://localhost:8000/admin/](http://localhost:8000/admin/) . Log into the admin with the credentials ``admin / changeme``.

Setup without Vagrant
-----
Don't want to set up a whole VM to try out Wagtail? No problem.

### Dependencies
* [PostgreSQL](http://www.postgresql.org)
* [PIP](https://github.com/pypa/pip)

### Installation

With PostgreSQL running (and configured to allow you to connect as the 'postgres' user - if not, you'll need to adjust the `createdb` line and the database settings in wagtaildemo/settings/base.py accordingly), run the following commands:

    git clone https://github.com/torchbox/wagtaildemo.git
    cd wagtaildemo
    pip install -r requirements.txt
    createdb -Upostgres wagtaildemo
    ./manage.py migrate
    ./manage.py load_initial_data
    ./manage.py createsuperuser
    ./manage.py runserver

### SQLite support

SQLite is supported as an alternative to PostgreSQL. Before running the `pip install -r requirements.txt` step above, delete the `psycopg2` line in requirements.txt; then, in wagtaildemo/settings/base.py, update the `DATABASES` setting to use `'django.db.backends.sqlite3'` and set `NAME` to be the full path of your database file, as you would with a regular Django project.
