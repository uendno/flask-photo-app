FROM python:3.7-alpine
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN pip install gunicorn
CMD exec gunicorn 'app:create_app()' --workers 1 --threads 8 --timeout 0