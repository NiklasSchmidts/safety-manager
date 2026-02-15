from contextlib import asynccontextmanager
from datetime import datetime, timezone

import models  # noqa: F401
from api.v1.employee import create_employee_router
from core.config import settings
from core.database import Base, engine
from fastapi import FastAPI


@asynccontextmanager
async def lifespan(app: FastAPI):
    if settings.is_local:
        print("Initializing local database...")
        async with engine.begin() as conn:
            try:
                await conn.run_sync(Base.metadata.create_all)
                print("Database tables created successfully.")
            except Exception as e:
                print(f"Error creating database tables: {e}")
    yield
    if engine:
        await engine.dispose()


app = FastAPI(lifespan=lifespan)

app.include_router(
    create_employee_router(), prefix="/api/v1/employees", tags=["Employees"]
)


@app.get("/health")
async def health_check():
    return {
        "status": "ok",
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }
