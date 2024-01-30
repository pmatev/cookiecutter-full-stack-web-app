# Personal Finance App

## Backend

The backend is a REST API written in Python using the FastAPI framework. It requires access to the postgres database.

### Setup

Setup python environment (with pyenv)
```sh
cd api/

pyenv activate personal-finance
```

Setup python environment (with virtualenv)
```sh
cd api/

python -m venv venv
source venv/bin/activate
```

Install dependencies
```sh
pip install -r requirements.txt
```

Seed and migrate the database

```sh
make migrate-up
```


## Frontend (Web)

The web app is built using Typescript / React on Vite.

### Setup
```
cd web/
npm install
```

Run locally:

```
npm run dev
```
