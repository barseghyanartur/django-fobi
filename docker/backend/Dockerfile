FROM docker.io/python:3.9
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

RUN add-apt-repository ppa:deadsnakes/ppa --yes

#RUN apt-get update && \
#    RUN apt-get install -y  --no-install-recommends \
#    python3.6-dev \
#    python3.7-dev \
#    python3.8-dev

    #RUN apt-get install -y firefox

RUN pip install pip --upgrade
RUN pip install virtualenv

RUN mkdir /backend
WORKDIR /backend
ADD examples/requirements/ /backend/requirements/
RUN pip install -r /backend/requirements/django_4_1.in
#RUN python -c "import geckodriver_autoinstaller; print(geckodriver_autoinstaller.install())"
RUN python -c "from chromedriver_py import binary_path; print(binary_path)"
COPY . /backend/
RUN python /backend/setup.py develop
