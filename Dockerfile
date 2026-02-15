# Stage 1: Build (install dependencies)
FROM python:3.12-slim AS builder

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

ENV UV_LINK_MODE=copy
ENV UV_COMPILE_BYTECODE=1
ENV UV_PYTHON_PREFERENCE=only-system

# Copy pyproject.toml and uv.lock to the builder stage
COPY pyproject.toml uv.lock ./

# Disable development dependencies
ENV UV_NO_DEV=1

# Install dependencies using uv
RUN uv sync --frozen --no-install-project --no-dev

# Stage 2: Final image
FROM python:3.12-slim AS final

# Add User for running the application without root privileges
RUN useradd --create-home appuser

# Set the working directory and permissions
RUN mkdir -p /app && chown appuser:appuser /app

WORKDIR /app

# Copy the installed dependencies from the builder stage
COPY --chown=appuser:appuser --from=builder /app/.venv /app/.venv

# Add the virtual environment's bin directory to the PATH
ENV VIRTUAL_ENV=/app/.venv
ENV PATH="${VIRTUAL_ENV}/bin:$PATH"

# Set the PYTHONPATH to the application directory
ENV PYTHONPATH=/app

# Copy the application code to the final image
COPY --chown=appuser:appuser . .

# Switch to the non-root user
USER appuser

# Run the application using uvicorn from the virtual environment
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]

