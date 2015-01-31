# jonahnator
The Jonah Peretti Quote Generator

> “It is possible to build a tech company in New York that has really good snacks.”

## Setup (from package root):

1. Install python packages:

  ```
  $ pip install -r requirements.txt
  ```

2. Initialize Django apps:

  ```
  $ ./manage.py syncdb
  ```

4. Install npm packages:

  ```
  $ cd frontend
  $ npm install
  ```

## Running the server:

1. Build the front-end and run the server:

  ```
  $ ./manage.py build_and_run
  ```

2. Navigate to localhost:8000 and enjoy!
