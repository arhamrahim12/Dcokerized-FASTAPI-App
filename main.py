from fastapi import FastAPI, HTTPException, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import os

app = FastAPI()

# Setup templates and static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

# Game state
board = [" " for _ in range(9)]
current_player = "X"

@app.get("/", response_class=HTMLResponse)
async def game_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "board": board})

@app.post("/play/{position}")
def make_move(position: int):
    global current_player

    if position < 0 or position > 8:
        raise HTTPException(status_code=400, detail="Invalid position. Use 0-8.")
    
    if board[position] != " ":
        raise HTTPException(status_code=400, detail="Position already taken.")
    
    board[position] = current_player
    if check_winner():
        winner = current_player
        reset_board()
        return {"message": f"Player {winner} wins!"}
    
    # Switch player
    current_player = "O" if current_player == "X" else "X"
    return {"board": board, "next_player": current_player}

@app.post("/reset")
def reset_board():
    global board, current_player
    board = [" " for _ in range(9)]
    current_player = "X"
    return {"message": "Board reset", "board": board}

def check_winner():
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != " ":
            return True
    return False
