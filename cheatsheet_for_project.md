Setup Django Project шт Docker

    docker-compose run app sh -c "django-admin.py startproject app ."

Create new app with name core

    docker-compose run sh -c "python manage.py startapp core"

Run tests and linter

     docker-compose run --rm app sh -c "python manage.py test && flake8"