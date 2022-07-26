FROM python:3.10
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /cic_app

COPY requirements/base.txt /cic_app/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /cic_app