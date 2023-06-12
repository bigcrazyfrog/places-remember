# Places Remember

This repository contains the code for Places Remember API backend.

---

## Documentation

This project has been developed using [Django][django] and [Django Ninja][djangoninja], [Postgres][postgres] as relational database.

Code structure implementation follows a [Clean Architecture][cleanarchitecture] approach, emphasizing on code readability, responsibility decoupling and unit testing.

## Setup

Download source code cloning this repository:
```
git clone https://github.com/bigcrazyfrog/places-remember.git
```

## Run the API backend:

If you don't use gitlab-runner for some personal reasons:

Create `.env` file from `.env.example`.

Create docker images and execute the containers for development. Use make:
```
make build
make up
```


[//]: # (Links)

[django]: <https://www.djangoproject.com>
[djangoninja]: <https://django-ninja.rest-framework.com/>
[postgres]: <https://www.postgresql.org>
[cleanarchitecture]: <https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html>
[pipenv]: <https://docs.pipenv.org/>
