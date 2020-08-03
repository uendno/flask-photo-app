# Quick Start

1. Clone the repo

```
$ git clone
$ cd flask-photo-app
```

2. Initialize and activate a virtualenv:

```
$ python3 -m venv env
$ source env/bin/activate
```

3. Install the dependencies:

```
$ pip3 install -r requirements.txt
```

4. Start up the database:

```
$ docker-compose up
```

5. Run the development server:

```
$ export ENV=dev
$ python3 run.py
```

6. Navigate to [http://localhost:5000](http://localhost:5000)
