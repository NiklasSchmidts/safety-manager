# 🛡️ SafetyGear Manager

A modern backend service for managing safety equipment inventory and employee assignments. Built with **FastAPI**, **SQLAlchemy 2.0**, and **PostgreSQL**.

The **SafetyGear Manager** solves the "Who has what?" problem by tracking equipment lifecycle—from checkout to return—ensuring full traceability and availability of critical safety gear.

---

## 🚀 Features

- **Equipment Management**: Create, update, and track safety gear (e.g., helmets, boots) with serial numbers and status.
- **Employee Management**: Manage personnel records and department assignments.
- **Checkout Process**: Assign available equipment to employees with automatic availability checks.
- **Audit Trail**: Full history of assignments and returns (Who had item X at time Y?).
- **Async Architecture**: High-performance API built on Python's `asyncio` stack.

---

## 🛠️ Tech Stack

- **Language**: Python 3.12 (Modern type hints & speed)
- **Framework**: FastAPI (Async)
- **Validation**: Pydantic v2 (Fast data parsing)
- **Configuration**: Pydantic Settings (Type-safe env management)
- **Database**: PostgreSQL 16 (Current stable)
- **ORM**: SQLAlchemy 2.0 (Async)
- **Migrations**: Alembic
- **Package Manager**: uv (Blazing fast pip replacement)
- **Linting/Formatting**: Ruff (Rust-based linter)
- **Containerization**: Docker & Docker Compose Plugin (v2)

---

## 📐 Architecture Overview
The application follows a clean architecture with clear separation of concerns:
- **Models**: SQLAlchemy models representing database tables.
- **Schemas**: Pydantic models for request/response validation.
- **CRUD Operations**: Encapsulated in a dedicated module for database interactions.
- **API Routes**: Organized by resource (e.g., `/equipment`, `/employees`).
- **Configuration**: Centralized settings management using Pydantic.

---

## Folder Structure

safetygear-manager/
├── Dockerfile
├── README.md
├── app
│   ├── __init__.py
│   ├── api
│   │   └── v1
│   │       └── employee.py
│   ├── app_factory.py
│   ├── core
│   │   ├── config.py
│   │   └── database.py
│   ├── crud
│   ├── main.py
│   ├── models
│   │   ├── __init__.py
│   │   ├── employee.py
│   │   └── equipment.py
│   ├── schemas
│   └── server.py
├── docker-compose.yml
├── pyproject.toml
├── setup.sh
├── startlocal.sh
├── tests
└── uv.lock

---

## 📦 Getting Started

### Prerequisites

- **Docker** & **Docker Compose**
- **uv** 

### 1. Setup

# Runs the setup script to setup the development environment (installs uv, docker, docker compose, and other dependencies)
./setup.sh

### 2. Build & Run

```bash
# Build and start the application with Docker Compose
docker compose up --build
```

For development, you can start the server with hot-reloading and the database with:

```bash
startlocal.sh
```

