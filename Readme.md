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
docker run -d \
    -e DJANGO_SECRET_KEY=aogolijkhgokljhalkjhjglkgjhglkj \
    -e DEBUG_MODE=false \
    -p 9000:80 \
    --name cienfuegos_exotics_website \
    --rm \
    cienfuegos_exotics
```


To attach to the container for maintenance

```
docker exec -ti cienfuegos_exotics_website bash

```

# Development instructions

```
python manage.py runserver
```
