# django-course
docker build . - builds an image from Dockerfile
docker-compose up - Builds, (re)creates, starts, and attaches to containers for a service.
docker-compose run app sh -c "django-admin.py startproject app ."

docker-compose run app sh -c "python manage.py test"
docker-compose run app sh -c "python manage.py startapp core"