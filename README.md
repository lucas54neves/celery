# celery

Studies on Celery (Distributed Task Queue)

# Commands

## How to run

```bash
docker-compose up --build
```

## Create tasks

```bash
http://localhost:8000/process?a=3&b=8
```

## Monitor websocket using flower

```bash
ws://localhost:8000/ws/task/a579b493-c977-4cfa-8a28-345eff5bc2d2
```

## Architecture

![Image](/.github/archtecture.webp)
