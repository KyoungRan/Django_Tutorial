# Django_ex

* Virtual Environments

  (Windows)
  $ python -m venv myvenv
  $ myvenv\Scripts\activate

  (Linux & Mac)
  $ python3 -m venv myvenv
  $ source myvenv/bin/activate           // or $ . myvenv/bin/activate


* Install Django
  (myvenv) ~$ pip install django==1.10

* Create Django project
  (myvenv) $ django-admin startproject mysite .

* Create app
  (myvenv) $ python manage.py startapp [app name]

* Running Server
  (myvenv) $ python manage.py runserver

* Open browser
  127.0.0.1:8000

* DB
  // After writing the db model on "models.py"
  // mysite\settings.py : add [app name] in INSTALLED_APPS array.
  (myvenv) $ python manage.py makemigrations [app name]
  (myvenv) $ python manage.py migrate

* shell
  (myvenv) $ python manage.py shell
