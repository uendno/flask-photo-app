# Photo App API

## Documentation

For API design, please vist [https://flaskphotoapi.docs.apiary.io/#](https://flaskphotoapi.docs.apiary.io/#)

## Prerequisites

- Docker and docker-compose

## Quick start guide

1. Clone the repo

```
$ git clone git@github.com:duong-le/flask-photo-app.git
$ cd flask-photo-app
```

2. Start the server:

```
$ docker compose up
```

3. Navigate to [http://localhost:5001](http://localhost:5001)

## Testing

```
$ export ENV="test"
$ pytest
```
