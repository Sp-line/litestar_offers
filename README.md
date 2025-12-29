# 🚀 Litestar Offers API

A high-performance, asynchronous REST API built with **Python 3.12**, **Litestar**, and **Granian**. Designed for speed and scalability, fully containerized with **Docker**.

---

## ⚡ Key Features

- **Modern & Fast**: Built on [Litestar](https://litestar.dev/) — a framework known for its top-tier performance and developer ergonomics.
- **ASGI Server**: Powered by [Granian](https://github.com/emmett-framework/granian) (Rust-based ASGI server) for maximum throughput.
- **Async Database**: Uses **SQLAlchemy 2.0** with `asyncpg` for non-blocking PostgreSQL interactions.
- **Clean Architecture**: Structured with clear separation of concerns (Controllers, Services, Repositories).
- **Dockerized**: Production-ready `Dockerfile` with non-root user security and multi-stage caching.
- **OpenAPI**: Automatic, interactive API documentation (Swagger UI & ReDoc).

---

## 📂 Project Structure

```text
litestar_offers/
├── app/
│   ├── models/          # Database Models (SQLAlchemy)
│   ├── repositories/    # Data Access Layer (CRUD)
│   ├── schemas/         # Pydantic DTOs & Validation
│   ├── services/        # Business Logic
│   ├── application.py   # App factory & Configuration
│   ├── config.py        # Settings management
│   ├── db.py            # Database connection & init
│   └── exceptions.py    # Custom error handling
├── .dockerignore        # Build optimization
├── .env                 # Environment variables
├── docker-compose.yml   # Infrastructure orchestration
├── Dockerfile           # Optimized container definition
└── requirements.txt     # Python dependencies
```

---

## 🛠 Tech Stack

| Category | Technology |
| :--- | :--- |
| **Language** | Python 3.12 |
| **Framework** | Litestar |
| **Server (ASGI)** | Granian (Rust) |
| **Database** | PostgreSQL 16 |
| **ORM** | SQLAlchemy 2.0 (Async) |
| **Driver** | AsyncPG |
| **Containerization** | Docker, Docker Compose |

---

## 🚀 Getting Started
The project is designed to run seamlessly with Docker.

1. **Prerequisites**
   - Docker & Docker Compose installed.

2. **Clone the Repository**
   ```bash
    git clone https://github.com/Sp-line/litestar_offers.git
    cd litestar_offers
    ```

3. **Run with Docker**
    ```bash
    docker compose up --build
    ```
   
---

## 🔌 API Documentation
Once the server is running, you can access the interactive API docs:

| Interface | URL | Description |
| :--- | :--- | :--- |
| **Swagger UI** | [http://localhost:5000/schema/swagger](http://localhost:5000/schema/swagger) | Interactive API testing tool |
| **ReDoc** | [http://localhost:5000/schema/redoc](http://localhost:5000/schema/redoc) | Alternative documentation view |
| **OpenAPI JSON** | [http://localhost:5000/schema/openapi.json](http://localhost:5000/schema/openapi.json) | Raw OpenAPI schema |

---

## 🔧 Development & Testing
Health Checks
The docker-compose.yml includes a health check for PostgreSQL using pg_isready. The API service will wait for the database to be fully ready before starting, preventing connection errors on startup.

**Local Development (without Docker)**
If you prefer running it locally:
1. Create a virtual environment:
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # or .venv\Scripts\activate on Windows
    ```
   
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
   
3. Run the server:
    ```bash
    granian --interface asgi --reload app.application:app
    ```

