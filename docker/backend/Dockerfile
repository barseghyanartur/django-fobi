FROM docker.io/python:3.11-slim
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    software-properties-common \
    cmake \
    mc \
    gettext \
    nano \
    chromium \
    graphviz \
    libpq-dev

RUN pip install pip --upgrade
RUN pip install virtualenv
RUN pip install pip-tools

RUN mkdir /backend
WORKDIR /backend
ADD examples/requirements/ /backend/requirements/
RUN pip install -r /backend/requirements/django_4_2.in
#RUN python -c "import geckodriver_autoinstaller; print(geckodriver_autoinstaller.install())"
RUN python -c "from chromedriver_py import binary_path; print(binary_path)"
COPY . /backend/
RUN python /backend/setup.py develop
