# Architecture Decision Record

## Framework Choice: Python + FastAPI

### Why Python?
- **Beginner-friendly**: Clean, readable syntax ideal for learning backend
- **Rich ecosystem**: Excellent libraries for ORM (SQLAlchemy), validation (Pydantic), testing (pytest)
- **Strong typing support**: Type hints help catch errors early and improve IDE support

### Why FastAPI?
- **Modern & Fast**: Built on Starlette and Pydantic, one of the fastest Python frameworks
- **Automatic API docs**: Swagger UI and ReDoc generated automatically at `/docs` and `/redoc`
- **Validation built-in**: Pydantic models provide request/response validation out of the box
- **Async support**: Native async/await for better performance
- **Standards-based**: OpenAPI and JSON Schema compliance

### Key Libraries
- **FastAPI**: Web framework
- **SQLAlchemy**: ORM for database operations
- **Pydantic**: Data validation and settings management
- **Alembic**: Database migrations
- **python-jose**: JWT token handling
- **passlib**: Password hashing
- **pytest**: Testing framework
- **uvicorn**: ASGI server

### Project Structure Philosophy
Following a **modular, layered architecture**:
- **Routes/Controllers**: Handle HTTP requests/responses
- **Services**: Business logic layer
- **Models**: Database entities (SQLAlchemy)
- **Schemas**: Request/Response validation (Pydantic)
- **Core**: Configuration, security, dependencies
