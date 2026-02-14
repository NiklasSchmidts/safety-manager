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

