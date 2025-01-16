#!/bin/bash

# Get project root directory (where .git is located)
ROOT_DIR=$(git rev-parse --show-toplevel)

# Change to root directory
cd "$ROOT_DIR"

# Get current git commit hash
COMMIT_HASH=$(git rev-parse HEAD)

# Create backups directory if it doesn't exist
mkdir -p .env_backups

# Copy .env to backup with commit hash
if [ -f .env ]; then
    cp .env ".env_backups/.env_${COMMIT_HASH}"
    echo "Backed up .env for commit ${COMMIT_HASH}"
else
    echo "Error: .env file not found in project root"
    exit 1
fi 