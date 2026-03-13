# ===================================
# LLM Prompt Router - Makefile
# ===================================

# Default variables
APP=app.main:app
HOST=0.0.0.0
PORT=8000

# ==========================
# Run Development Server
# ==========================

run:
	uvicorn $(APP) --host $(HOST) --port $(PORT) --reload


# ==========================
# Install Dependencies
# ==========================

install:
	pip install -r requirements.txt


# ==========================
# Run Tests
# ==========================

test:
	pytest tests/


# ==========================
# Run Batch Router Tests
# ==========================

router-test:
	python scripts/run_tests.py


# ==========================
# Start Docker Environment
# ==========================

docker-up:
	docker compose -f docker/docker-compose.yml up --build


# ==========================
# Stop Docker Environment
# ==========================

docker-down:
	docker compose -f docker/docker-compose.yml down


# ==========================
# Format Code (optional)
# ==========================

format:
	black app/


# ==========================
# Lint Code (optional)
# ==========================

lint:
	flake8 app/


# ==========================
# Clean Cache Files
# ==========================

clean:
	find . -type d -name "__pycache__" -exec rm -r {} +
	find . -name "*.pyc" -delete