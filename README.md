Smart Market
============

## Installation

1. Clone this repository

2. Install python3

`sudo apt-get install python3.5`

3. Initialise [`virtualenv`](http://pypi.python.org/pypi/virtualenv)

    `sudo apt-get install python3-venv`

    `python3 -m venv ENV_NAME`

    and enter it

    `. ENV_NAME/bin/activate`

4. `pip install -r requirements.txt` there

5. Create a Database and Database User

6. Set db settings in django project:

    ```DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'project_name',
            'USER': 'username',
            'PASSWORD': 'password',
            'HOST': 'localhost',
            'PORT': '',
        },
    }

7. Collect staticfiles:

    `python manage.py collectstatic`

8. Init db:

    `python manage.py migrate`

9. Create superuser

    `python manage.py createsuperuser`

10. Run `python manage.py runserver` and browse to [http://localhost:8000](http://localhost:8000)


## Create a Database and Database User

1. Change to this user to perform administrative tasks:

    `sudo su - postgres`

2. Log into a Postgres session:

    `psql`

3. Create a database:

    `CREATE DATABASE myproject;`

4. Create a database user:

    `CREATE USER myprojectuser WITH PASSWORD 'password';`

5. Setting the default encoding:

    `ALTER ROLE myprojectuser SET client_encoding TO 'utf8';`

6. Setting the default transaction isolation scheme:

    `ALTER ROLE myprojectuser SET default_transaction_isolation TO 'read committed';`

7. Setting the timezone:

    `ALTER ROLE myprojectuser SET timezone TO 'UTC';`

8. Setting user access rights to the database:

    `GRANT ALL PRIVILEGES ON DATABASE myproject TO myprojectuser;`

9. Exit the SQL prompt to get back to the postgres user's shell session:

    `\q`

10. Exit out of the postgres user's shell session to get back to your regular user's shell session:

    `exit`