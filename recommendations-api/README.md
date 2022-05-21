# Another Django Template

A simple django 3.2 (LTS) project to use as a basis for other projects.

## What's better at it?

I used [poetry](https://python-poetry.org/docs/cli/#new) with the `--src` option to create the base for simplicity, so I don’t need to change anything, just clone the project and use it. I added a `.pre-commit-config.yaml` with some linters to ensure code quality. I used the `django-configuration` to split the `dev` and `prod` configurations following the guidelines of [The Twelve Factor App](https://www.12factor.net).

## How to use?

> Assuming you docker and pre-commit (optional but recommended)

Clone the project: 

    git clone https://github.com/hugobrilhante/another-django-template.git my-project

Enter the project folder and create a `.env` use` .env.example`

    cd my-project
    cp .env.example .env

Build image 
    
    docker compose build

Start project 
    
    docker compose up

> Now he performs the migrations, create a super user with login `admin` and password `qwerty` and starts the project in [localhost](http://127.0.0.1:8000)

## To guarantee a quality code, install the [pre-commit](https://pre-commit.com/#install). 

Update hooks (optional)

    pre-commit autoupdate

Install the hooks

    pre-commit install

> Now the linters will be executed at each commit

To check if everything is in order before the commit run

    pre-commit run -a 



## Installed packages


[django-configurations](https://github.com/jazzband/django-configurations) - A helper for organizing Django settings.

- [django-cache-url](https://github.com/epicserve/django-cache-url) - Use Cache URLs in your Django application.
  
- [dj-database-url](https://github.com/kennethreitz/dj-database-url) - Use Database URLs in your Django Application.
     
- [dj-email-url](https://github.com/migonzalvar/dj-email-url) - Use an URL to configure email backend settings in your Django Application.

[gunicorn](https://gunicorn.org/) - WSGI HTTP Server for UNIX

[psycopg2](https://www.psycopg.org/) - Python-PostgreSQL Database Adapter

[whitenoise](https://github.com/evansd/whitenoise) - Radically simplified static file serving for WSGI applications

