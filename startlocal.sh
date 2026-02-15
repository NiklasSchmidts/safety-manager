#!/bin/bash
set -e

start_server() {
    echo "Starting the server..."
    export PYTHONPATH=$PYTHONPATH:$(pwd)/app
    uvicorn app.main:app --host 0.0.0.0 --port 8080 --reload
}

start_db() {
    echo "Starting the database..."
    docker compose up -d db
    echo "Waiting for the database to be ready..."
    until docker compose exec db pg_isready -U postgres; do
        sleep 1
    done
    echo "Database is ready."
}

cleanup() {
    echo "Cleaning up..."
    docker compose down db
    echo "Cleanup complete."
}

trap cleanup EXIT

start_all() {
    start_db
    start_server
}

start_all