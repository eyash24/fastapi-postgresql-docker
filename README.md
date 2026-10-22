# FastAPI - Postgresql

## AIM
- Learn about connecting FastAPI with postgres on Docker

## Setup
### 1. Docker Setup

Pull the PostgreSQL Alpine image:

```bash
docker pull postgres:alpine
```

Create and start the PostgreSQL container:

```bash
docker run --name fastapi-postgres-docker \
  -e POSTGRES_PASSWORD="Password" \
  -d -p 5432:5432 postgres:alpine
```

Connect to PostgreSQL from your local terminal:

```bash
psql -h localhost -p 5432 -U postgres -d postgres
```

Enter `Password` when prompted.

Alternatively, access PostgreSQL directly inside the Docker container:

```bash
docker exec -it fastapi-postgres-docker psql -U postgres
```

### 2. Database and User Setup

Execute the following SQL commands in the PostgreSQL shell to create the application database and user:

```sql
-- Create the application database
CREATE DATABASE fastapi_postgres_database;

-- Create the application user
CREATE USER myuser WITH ENCRYPTED PASSWORD 'postgres_password';

-- Grant database-level privileges
GRANT ALL PRIVILEGES
ON DATABASE fastapi_postgres_database
TO myuser;
```

Connect to the newly created database:

```sql
\c fastapi_postgres_database
```

Grant the application user permission to access the `public` schema and create tables:

```sql
GRANT USAGE, CREATE ON SCHEMA public TO myuser;
```

To list databases, use:

```sql
\l
```

### 3. Configure the Database Connection

Configure the following SQLAlchemy connection URL in your environment configuration:

```env
DATABASE_URL=postgresql+psycopg://myuser:"Password"@localhost:5432/fastapi_postgres_database
```

Ensure that the database credentials match the user and password configured in PostgreSQL.

**Note:** Replace example passwords with secure values when deploying outside a local development environment. Do not commit real credentials to version control.

### 4. Verify the Setup

Verify that the application user can connect to the database:

```bash
docker exec -it fastapi-postgres-docker \
  psql -U myuser -d fastapi_postgres_database
```

Test table creation:

```sql
CREATE TABLE test_table (
    id SERIAL PRIMARY KEY
);

DROP TABLE test_table;
```

If both statements execute successfully, the database connection and schema permissions are configured correctly.


## Reference
- [Fastapi with Postgresql and docker](https://youtu.be/2X8B_X2c27Q?si=-DK9d-alqjZjvTAm)
