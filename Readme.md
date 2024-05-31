# Cienfuegos Exotics Website

Website for the gardening hobby. A place to show off the garden and advertise plants and mantises in case anyone wants to pick these up locally from me.

## Deploy instructions
We need to set two environment variables `DJANGO_SECRET_KEY` and `DEBUG_MODE`.

To build the docker container

```
docker build -t cienfuegos_exotics -f Dockerfile .
```

To run the container

```
docker run \
    -e DJANGO_SECRET_KEY=somesupersecretstringhexadecimalalphanumericwhatever \
    -e DEBUG_MODE=false \
    -it
    -p 9000:80
    cienfuegos_exotics
```

# Development instructions

```
python manage.py runserver
```
