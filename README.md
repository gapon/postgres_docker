# Creating Postgres with Docker and populating it with fake data

1. Создать контейнер с Postgres
```bash
docker run \
--name basic-postgres \
--rm \
-e POSTGRES_USER=postgres \
-e POSTGRES_PASSWORD=password \
-e PGDATA=/var/lib/postgresql/data/pgdata \
-v ~/Downloads/postgresql/data:/var/lib/postgresql/data \
-p 5432:5432 \
-it \
postgres:14.2-alpine
```

2. Зайти в контейнер
```bash
docker exec -it basic-postgres /bin/sh
```

3. Запустить psql
```bash
psql --username postgres
```

4. Создать базу данных
```bash
CREATE DATABASE test_db;
```

5. Выйти из psql
```bash
\q