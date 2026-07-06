.PHONY: help dev dev-backend dev-frontend migrate db-shell clean lint

help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

dev: ## Start all services (docker compose)
	docker compose up -d

dev-backend: ## Start the backend server locally
	cd backend && uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

dev-frontend: ## Start the frontend dev server
	cd frontend && npm run dev

migrate: ## Run Alembic migrations
	cd backend && alembic upgrade head

migrate-new: ## Create a new migration
	cd backend && alembic revision --autogenerate -m "$(message)"

db-shell: ## Connect to the database
	psql postgresql://prospectpilot:prospectpilot_dev@localhost:5432/prospectpilot

clean: ## Clean Python cache files
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null
	find . -type f -name "*.pyc" -delete

lint: ## Run linters
	cd backend && ruff check . && ruff format --check .