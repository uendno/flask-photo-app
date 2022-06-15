FROM python:3.7
ADD ./wait-for-it.sh /wait-for-it.sh
RUN chmod +x /wait-for-it.sh
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ./wait-for-it.sh db:3306 --timeout=30 -- python3 run.py
