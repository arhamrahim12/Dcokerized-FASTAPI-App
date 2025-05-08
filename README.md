# Tic-Tac-Toe (Dockerized FastAPI Game)

A simple, interactive Tic-Tac-Toe game built using FastAPI (backend) and HTML/CSS/JavaScript (frontend), all containerized using Docker.

## Features

* Interactive Tic-Tac-Toe game playable directly in the browser.
* Choose X or O and play against another player.
* Simple, clean UI.
* FastAPI backend with stateful game logic.
* Fully containerized with Docker.

## How to Use

### 1. Clone this repository:

```bash
git clone <your-repository-link>
cd dockerize-app
```

### 2. Build the Docker image:

```bash
docker build -t tic-tac-toe-app .
```

### 3. Run the Docker container:

```bash
docker run -d -p 8001:8000 tic-tac-toe-app
```

### 4. Play the game:

* Open your browser and go to: `http://localhost:8001`
* Click the cells to make your moves.
* Reset the game using the "Reset" button.

## Project Structure

```
DOCKERIZE APP/
├── app/
│   └── main.py          # FastAPI backend
│   └── static/
│       └── style.css    # Game styles
│   └── templates/
│       └── index.html   # Game HTML
├── requirements.txt     # Dependencies
├── Dockerfile           # Docker instructions
└── .dockerignore        # Ignored files for Docker
```

## Requirements

* Docker
* FastAPI
* Uvicorn

