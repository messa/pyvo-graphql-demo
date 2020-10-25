GraphQL demo: Python backend + React frontend
=============================================

Presented on [Pyvo.cz on 2020-10-21](https://pyvo.cz/praha-pyvo/2020-10/).

How to run it
-------------

### Backend

Prerequisites: you need to have recent [Python 3](https://naucse.python.cz/lessons/beginners/install/) installed.

```shell
$ cd backend
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ python web_app.py
```

### Frontend

Prerequisites: you need to have [Node.js](https://nodejs.org/en/) installed.

```shell
$ cd frontend
$ npm install
$ npm run dev
```

Open browser at [127.0.0.1:5000/api/graphql](http://127.0.0.1:5000/api/graphql) for the backend API,
or [127.0.0.1:3000](http://127.0.0.1:3000/) for the frontend.

### Test "hello world" GraphQL query

Open this address: [127.0.0.1:5000/api/graphql?query=%7B%0A%20%20hello%0A%7D](http://127.0.0.1:5000/api/graphql?query=%7B%0A%20%20hello%0A%7D)

It should open the GraphiQL web UI. You should see the query result on the right side of the screen:

```json
{
  "data": {
    "hello": "world"
  }
}
```
