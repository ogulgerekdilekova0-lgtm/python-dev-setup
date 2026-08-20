# python-dev-setup
  Учебный проект: настройка среды, PostgreSQL и FastAPI.
  ## Запуск FastAPI
  ```bash
  source venv/bin/activate
  sudo service postgresql start
  uvicorn app.main:app --reload
  ```
  - Документация: http://127.0.0.1:8000/docs
  - Проверка: http://127.0.0.1:8000/health
  ## Скрины
  В папке `examples/` есть скрины работы API и PostgreSQL.