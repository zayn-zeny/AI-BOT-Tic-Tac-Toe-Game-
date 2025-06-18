# AI-BOT-Tic-Tac-Toe-Game- by ZAYN
Overview
This is a single-player Tic Tac Toe game implemented in Python using the Pygame library. The player competes against an AI opponent that uses the Minimax algorithm to make optimal moves. The game features a graphical interface with a 3x3 grid, where the player places "X" marks by clicking, and the AI places "O" marks automatically.
Features

Graphical Interface: A 500x500 pixel window displays the Tic Tac Toe grid, with "X" marks in red and "O" marks in blue.
Player vs. AI: The player (X) makes moves by clicking on empty cells, while the AI (O) responds with optimal moves.
Minimax Algorithm: Ensures the AI plays perfectly, either winning or forcing a draw when possible.
Console Output: A terminal-based representation of the board updates alongside the graphical interface.
Game Status Checks: Detects wins (horizontal, vertical, diagonal) and draws, ending the game appropriately.

Requirements

Python 3.x
Pygame library (pip install pygame)

Installation

Clone or download the repository to your local machine.
Ensure Python is installed.
Install Pygame by running:pip install pygame


Save the provided Python code as tictactoe.py.

How to Run

Open a terminal or command prompt.
Navigate to the directory containing tictactoe.py.
Run the game with:python tictactoe.py


The game window will open, and the console will display the initial board.

How to Play

The game starts with an empty 3x3 grid.
Click on an empty cell to place an "X".
The AI will automatically place an "O" in response.
The game continues until there is a winner (three "X" or "O" marks in a row, column, or diagonal) or a draw (all cells filled with no winner).
To exit, close the game window.

Code Structure

Initialization: Sets up Pygame, window dimensions, colors, and the game board.
Drawing Functions: draw_board() renders the grid and symbols; printBoard() displays the board in the console.
Input Handling: takeInput() captures mouse clicks to place "X" marks.
Game Logic: checkHorizontal(), checkVertical(), checkDiagonal(), and checkDraw() detect game outcomes.
AI Logic: computerPlayer() uses minimax() to determine the AI's optimal move.
Main Loop: Alternates between player and AI turns until the game ends.

Notes

The AI uses the Minimax algorithm, making it unbeatable (it will win or draw).
The console board updates with a slight delay (0.5 seconds) for visibility.
The game clears the console screen for each board update (compatible with Windows and Unix-based systems).

Author
ZAYN
License
This project is open-source and available for personal use and modification. No formal license is specified.

