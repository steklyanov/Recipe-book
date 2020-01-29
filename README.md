# Recipe-book
Site for your recipes using Django, DRF, Docker, TDD and PostgreSQL

Backend implementation of the following functionality:

 - User(extend built-in model)
 - Tag model
 - Recipe model
 - Ingredient model

 All necessary permissions, authentication.
All functionality is covered with tests, packed in a Docker container, support Travis-CI integration.

**Usage:**

Clone this repo:

    git clone https://github.com/steklyanov/Recipe-book.git
    cd Recipe-book

Run tests and linter:

     docker-compose run --rm app sh -c "python manage.py test && flake8"