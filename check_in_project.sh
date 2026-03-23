#!/bin/bash

PROJECT_DIR=$(realpath $(dirname $0))

cd "$PROJECT_DIR"

uv run pyrefly check .
