FROM python:3.8.5
WORKDIR /code
COPY requirements.txt .
RUN python3 -m pip install --upgrade pip \
    && pip3 install -r /code/requirements.txt --no-cache-dir
COPY . .
CMD gunicorn backend.wsgi:application --bind 0.0.0.0:8000
