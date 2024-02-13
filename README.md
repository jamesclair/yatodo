## Yet Another Todo App (YaTodo)

An experimental todo app for my own personal use.  Who knows maybe it will be usable by others in the future.

## Foundational Dependencies
- Poetry (version 1.5.1) (asdf)
- Python 3.12.1 (asdf)
- Docker version 25.0.2, build 29cf629 (brew cask)

## Python Dependencies

`poetry shell && poetry install`

## Database Setup

Create a new database in psql called `yatodo`

## Database Migrations

`alembic upgrade head`

## Running on MacOS

- `poetry shell`
- `docker-compose up postgres`
- `uvicorn src.main:app --reload`

## Running in Docker

`docker-compose up`

## Usage

See `https://localhost:8081/docs`

## VSCode Debugging

`.vscode/launch.json` and `settings.json` are available.


## TODO:

- automate database setup
- Setup automatic migrations through alembic
- Add Tests for API, Models, Schema, Crud and Config