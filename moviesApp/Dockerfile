FROM python:latest

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

# EXPOSE 8000

CMD gunicorn --timeout 100 --workers 5 --bind 0.0.0.0:8000 --log-level debug --access-logformat '%(t)s %(h)s "%(r)s" %(s)s' --access-logfile - moviesApp.wsgi:application