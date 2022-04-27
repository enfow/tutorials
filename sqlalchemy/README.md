# SQLAlchemy Tutorial

## Postgresql

```bash
docker exec -it postgres-sqlalchemy /bin/sh
# psql -U postgres
psql (14.2 (Debian 14.2-1.pgdg110+1))
Type "help" for help.

postgres=# \l
                                 List of databases
   Name    |  Owner   | Encoding |  Collate   |   Ctype    |   Access privileges
-----------+----------+----------+------------+------------+-----------------------
 postgres  | postgres | UTF8     | en_US.utf8 | en_US.utf8 |
 template0 | postgres | UTF8     | en_US.utf8 | en_US.utf8 | =c/postgres          +
           |          |          |            |            | postgres=CTc/postgres
 template1 | postgres | UTF8     | en_US.utf8 | en_US.utf8 | =c/postgres          +
           |          |          |            |            | postgres=CTc/postgres
(3 rows)

postgres=# \dt
Did not find any relations.
postgres=# CREATE DATABASE sqlalchemy;
CREATE DATABASE
postgres=# \c sqlalchemy
You are now connected to database "sqlalchemy" as user "postgres".
```
