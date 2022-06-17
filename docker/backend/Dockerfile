FROM docker.io/python:3.9
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED 1

RUN apt-get update
RUN apt-get install -y build-essential
RUN apt-get install -y cmake
RUN apt-get install -y libpq-dev
RUN apt-get install -y mc
RUN apt-get install -y graphviz
RUN apt-get install -y gettext
RUN apt-get install -y nano
RUN apt-get install -y chromium
#RUN apt-get install -y firefox

RUN pip install pip --upgrade
RUN pip install virtualenv

RUN mkdir /backend
WORKDIR /backend
ADD examples/requirements/ /backend/requirements/
RUN pip install -r /backend/requirements/django_3_2.in
#RUN python -c "import geckodriver_autoinstaller; print(geckodriver_autoinstaller.install())"
RUN python -c "from chromedriver_py import binary_path; print(binary_path)"
COPY . /backend/
RUN python /backend/setup.py develop
