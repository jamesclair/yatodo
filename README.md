## Yet Another Todo App (YaTodo)

An experimental todo app for my own personal use.  Who knows maybe it will be usable by others in the future.

## Foundational Dependencies
- Poetry (version 1.5.1) (asdf)
- Python 3.12.1 (asdf)
- Docker version 25.0.2, build 29cf629 (brew cask)
- kind 0.17.0 (asdf, depends on docker)

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

## Running in Kind

`./create_kind_with_populated_registry.sh`

This script does the following:
- creates a `kind-registry` container
- 

cleanup: `kind delete cluster --name yatodo`

## Usage

See `https://localhost:8081/docs`

## VSCode Debugging

`.vscode/launch.json` and `settings.json` are available.


## TODO:

- automate database setup
- Setup automatic migrations through alembic
- Add Tests for API, Models, Schema, Crud and Config
- Remove initial secrets from files (only ran in isolated local envs, so this can wait for now)
- update kustomize files to point to each dir
- update postgres to be HA within a k8s cluster
- expose ports declaratively in kind
- update k8s cluster to have a gateway w/ loadbalancer using new gateway api
- add ability to delete tasks
- make kind script idempotent