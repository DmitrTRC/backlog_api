# Backlog

> Simple multiplatform desktop app for storing TODOs, ideas or backlog items.
> You can organize them with boards as a plaintext or markdown. No dependencies, no internet connection required,
> no external accounts. Sleek flow.



## Features
- Organize your thoughts with items & boards. Use Markdown or plaintext for adding new items
- user stories
- bugs
- design changes
- technical debt
- customer requests 
- action items from the retrospective
##### **Technologies:**
* Python3
* Django
* Django REST Framework
* Docker
* Docker-compose
## Build
`docker-compose build`.

## Migrate databases
`docker-compose run --rm web code/manage.py migrate`.

## Run
`docker-compose up`.
