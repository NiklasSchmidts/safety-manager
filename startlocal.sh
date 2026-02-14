#!/bin/bash
set -e

start_server() {
    echo "Starting the server..."
    uvicorn app.main:app --host 0.0.0.0 --port 8080 --reload
}

start_db() {
    echo "Starting the database..."
    docker compose up -d db
}

start_all() {
    start_db
    start_server
}

start_all