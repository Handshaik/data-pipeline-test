# Data Pipeline Test Project

This is a Python project to evaluate basic ETL pipeline skills using a PostgreSQL backend via Docker.

---

## 🔧 Setup Instructions

### 🐍 Python Setup (using `uv`)

```bash
uv venv
source .venv/bin/activate
uv pip install pandas sqlalchemy psycopg2-binary python-dotenv
```

Ensure you have a .env file in the project with the connection string 
```
DB_URL=postgresql://postgres:password@127.0.0.1:55432/test_db
```

### 🐘 Start PostgreSQL via Docker

```bash
make db-start
```

> If you've run this project before and the database volume persists, run:

```bash
make db-stop
docker volume rm data-pipeline-test_pgdata
make db-start
```

## 🚀 Run the Pipeline

```bash
make run
```

You should see output like:

```
✅ Database connection successful.
Transforming data...
```

---

## 🧹 Other Make Commands

| Command       | What it does                      |
|---------------|-----------------------------------|
| `make setup`  | Create virtualenv and install deps |
| `make run`    | Run the ETL pipeline               |
| `make db-start` | Start Postgres via Docker        |
| `make db-stop` | Stop the Docker container         |
| `make clean`  | Remove venv, pycache, etc.         |

---

## ✅ What It Tests

- Reading CSVs (extract)
- Data transformation using Pandas
- Loading into a real PostgreSQL DB
- Creating summary data in the database
- Adding error handling


