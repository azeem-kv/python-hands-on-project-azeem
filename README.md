# Order Management System (OMS) - Backend API

A simple Order Management System backend built with **Python + FastAPI** for learning backend fundamentals.

## Tech Stack

- **Framework**: FastAPI (Python 3.11+)
- **Database**: PostgreSQL 15
- **ORM**: SQLAlchemy 2.0
- **Authentication**: JWT (python-jose)
- **Validation**: Pydantic
- **Testing**: pytest
- **Containerization**: Docker + Docker Compose

## Project Structure

```
.
├── app/
│   ├── core/           # Configuration, database, security
│   │   ├── config.py   # Environment settings
│   │   └── database.py # Database connection
│   ├── models/         # SQLAlchemy ORM models
│   ├── schemas/        # Pydantic request/response schemas
│   ├── routes/         # API endpoints (controllers)
│   │   └── health.py   # Health check endpoint
│   ├── services/       # Business logic layer
│   └── main.py         # Application entry point
├── tests/              # Test files
├── docker-compose.yml  # Docker services configuration
├── Dockerfile          # Application container
├── requirements.txt    # Python dependencies
├── .env.example        # Environment template
└── ARCHITECTURE.md     # Architecture decisions
```

## Quick Start

### Option 1: Docker (Recommended)

```bash
# Start all services (API + PostgreSQL)
docker-compose up --build

# API will be available at http://localhost:8000
# Swagger docs at http://localhost:8000/docs
```

### Option 2: Local Development

```bash
# 1. Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Set up environment
cp .env.example .env
# Edit .env with your database credentials

# 4. Start PostgreSQL (via Docker or local install)
docker run -d --name oms_postgres \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_PASSWORD=postgres \
  -e POSTGRES_DB=oms_db \
  -p 5432:5432 \
  postgres:15-alpine

# 5. Run the application
uvicorn app.main:app --reload

# API will be available at http://localhost:8000
```

## Running Tests

```bash
# With virtual environment activated
pytest

# With coverage
pytest --cov=app

# Verbose output
pytest -v
```

## API Endpoints

| Method | Endpoint  | Description          |
|--------|-----------|----------------------|
| GET    | `/`       | API information      |
| GET    | `/health` | Health check         |
| GET    | `/docs`   | Swagger UI           |
| GET    | `/redoc`  | ReDoc documentation  |

## Environment Variables

| Variable                    | Description              | Default                                    |
|-----------------------------|--------------------------|--------------------------------------------|
| `DATABASE_URL`              | PostgreSQL connection    | `postgresql://postgres:postgres@localhost:5432/oms_db` |
| `JWT_SECRET_KEY`            | Secret for JWT tokens    | (required for production)                  |
| `JWT_ALGORITHM`             | JWT signing algorithm    | `HS256`                                    |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | Token expiration time  | `30`                                       |
| `DEBUG`                     | Enable debug mode        | `false`                                    |

## Development

```bash
# Stop containers
docker-compose down

# Stop and remove volumes (reset database)
docker-compose down -v

# View logs
docker-compose logs -f app

# Rebuild after code changes
docker-compose up --build
```
