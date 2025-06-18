# import pygame
# import os
# import time
# import random


# pygame.init()


# WIDTH = 500
# HEIGHT = 500
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Tic Tac Toe by ZAYN")

# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# RED = (255, 0, 0)
# BLUE = (0, 0, 255)

# winner = ""
# gameOver = False
# currentPlayer = "X"
# board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]

# def clear_screen():
#     os.system('cls' if os.name == 'nt' else 'clear')

# def print_with_refresh():
#     clear_screen()  
#     printBoard()    
#     time.sleep(0.5)  

# def printBoard():
#     print(board[0], "|", board[1], "|", board[2])
#     print("---------")
#     print(board[3], "|", board[4], "|", board[5])
#     print("---------")
#     print(board[6], "|", board[7], "|", board[8])
#     return 

# def draw_board():
#     screen.fill(BLACK)
#     for i in range(1, 3):
       
#         pygame.draw.line(screen, WHITE, (i * (WIDTH // 3), 0), (i * (WIDTH // 3), HEIGHT), 2)
        
#         pygame.draw.line(screen, WHITE, (0, i * (HEIGHT // 3)), (WIDTH, i * (HEIGHT // 3)), 2)
#     for i in range(9):
#         row, col = divmod(i, 3)
#         if board[i] == "X":
#             pygame.draw.line(screen, RED, (col * (WIDTH // 3) + 10, row * (HEIGHT // 3) + 10), (col * (WIDTH // 3) + (WIDTH // 3) - 10, row * (HEIGHT // 3) + (HEIGHT // 3) - 10), 2)
#             pygame.draw.line(screen, RED, (col * (WIDTH // 3) + (WIDTH // 3) - 10, row * (HEIGHT // 3) + 10), (col * (WIDTH // 3) + 10, row * (HEIGHT // 3) + (HEIGHT // 3) - 10), 2)
#         elif board[i] == "O":
#             pygame.draw.circle(screen, BLUE, (col * (WIDTH // 3) + (WIDTH // 6), row * (HEIGHT // 3) + (HEIGHT // 6)), (WIDTH // 6) - 10, 2)
#     pygame.display.flip()

# def takeInput(board):
#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 return
#             if event.type == pygame.MOUSEBUTTONDOWN and not gameOver:
#                 x, y = event.pos
#                 col = x // (WIDTH // 3)
#                 row = y // (HEIGHT // 3)
#                 index = row * 3 + col
#                 if 0 <= index < 9 and board[index] == "-":
#                     board[index] = "X"
#                     draw_board()
#                     print_with_refresh()
#                     return

# def checkHorizontal():
#     global winner
#     if board[0] == board[1] == board[2] and board[0] != "-":
#         print(board[0] + " won the game!")
#         winner = board[0]
#         return True
#     elif board[3] == board[4] == board[5] and board[3] != "-":
#         print(board[3] + " won the game!")
#         winner = board[3]
#         return True
#     elif board[6] == board[7] == board[8] and board[6] != "-":
#         print(board[6] + " won the game!")
#         winner = board[6]
#         return True
#     else:
#         return False    

# def checkVertical():
#     if board[0] == board[3] == board[6] and board[0] != "-":
#         print(board[0] + " won the game!")
#         winner = board[0]
#         return True
#     elif board[1] == board[4] == board[7] and board[1] != "-":
#         print(board[1] + " won the game!")
#         winner = board[1]
#         return True
#     elif board[2] == board[5] == board[8] and board[2] != "-":
#         print(board[2] + " won the game!")
#         winner = board[2]
#         return True
#     else:
#         return False         

# def checkDiagonal():
#     if board[0] == board[4] == board[8] and board[0] != "-":
#         print(board[0] + " won the game!")
#         winner = board[0]
#         return True
#     elif board[2] == board[4] == board[6] and board[2] != "-":
#         print(board[2] + " won the game!")
#         winner = board[2]
#         return True
#     else:
#         return False 

# def checkWin():
#     global gameOver    
#     if checkHorizontal() == True:
#         gameOver = True
#         return True
#     if checkVertical() == True:
#         gameOver = True
#         return True
#     if checkDiagonal() == True:
#         gameOver = True
#         return True
#     return False

# def checkDraw():
#     global gameOver
#     for i in range(len(board)):
#         if board[i] == "-":
#             return False
#     if winner != "":
#         print("Game is a Draw!")
#         gameOver = True
#         return True        
#     else:    
#         return False

# def switchUser():
#     global currentPlayer
#     if currentPlayer == "X":
#         currentPlayer = "O"
#     elif currentPlayer == "O":
#         currentPlayer = "X"
#     return    

# def computerPlayer():
#     global board
#     global currentPlayer
#     if currentPlayer == "O" and gameOver != True:
#         currentPlayer = "X"
#         while True:
#             cturn = random.randint(0, 8)
#             if board[cturn] == "-":
#                 board[cturn] = "O"
#                 print_with_refresh()
#                 draw_board()
#                 break

# clear_screen()
# printBoard()
# draw_board()

# while not gameOver:
#     takeInput(board)
#     if checkWin() == True:
#         break
#     if checkDraw() == True:
#         break
#     switchUser()
#     computerPlayer()
#     if checkWin() == True:
#         break
#     if checkDraw() == True:
#         break


import pygame
import os
import time
import random

pygame.init()

WIDTH = 500
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe by ZAYN")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

winner = ""
gameOver = False
currentPlayer = "X"
board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_with_refresh():
    clear_screen()  
    printBoard()    
    time.sleep(0.5)  

def printBoard():
    print(board[0], "|", board[1], "|", board[2])
    print("---------")
    print(board[3], "|", board[4], "|", board[5])
    print("---------")
    print(board[6], "|", board[7], "|", board[8])
    return 

def draw_board():
    screen.fill(BLACK)
    for i in range(1, 3):
        pygame.draw.line(screen, WHITE, (i * (WIDTH // 3), 0), (i * (WIDTH // 3), HEIGHT), 2)
        pygame.draw.line(screen, WHITE, (0, i * (HEIGHT // 3)), (WIDTH, i * (HEIGHT // 3)), 2)
    for i in range(9):
        row, col = divmod(i, 3)
        if board[i] == "X":
            pygame.draw.line(screen, RED, (col * (WIDTH // 3) + 10, row * (HEIGHT // 3) + 10), (col * (WIDTH // 3) + (WIDTH // 3) - 10, row * (HEIGHT // 3) + (HEIGHT // 3) - 10), 2)
            pygame.draw.line(screen, RED, (col * (WIDTH // 3) + (WIDTH // 3) - 10, row * (HEIGHT // 3) + 10), (col * (WIDTH // 3) + 10, row * (HEIGHT // 3) + (HEIGHT // 3) - 10), 2)
        elif board[i] == "O":
            pygame.draw.circle(screen, BLUE, (col * (WIDTH // 3) + (WIDTH // 6), row * (HEIGHT // 3) + (HEIGHT // 6)), (WIDTH // 6) - 10, 2)
    pygame.display.flip()

def takeInput(board):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.MOUSEBUTTONDOWN and not gameOver:
                x, y = event.pos
                col = x // (WIDTH // 3)
                row = y // (HEIGHT // 3)
                index = row * 3 + col
                if 0 <= index < 9 and board[index] == "-":
                    board[index] = "X"
                    draw_board()
                    print_with_refresh()
                    return

def checkHorizontal():
    global winner
    if board[0] == board[1] == board[2] and board[0] != "-":
        print(board[0] + " won the game!")
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        print(board[3] + " won the game!")
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        print(board[6] + " won the game!")
        winner = board[6]
        return True
    else:
        return False    

def checkVertical():
    if board[0] == board[3] == board[6] and board[0] != "-":
        print(board[0] + " won the game!")
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        print(board[1] + " won the game!")
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        print(board[2] + " won the game!")
        winner = board[2]
        return True
    else:
        return False         

def checkDiagonal():
    if board[0] == board[4] == board[8] and board[0] != "-":
        print(board[0] + " won the game!")
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        print(board[2] + " won the game!")
        winner = board[2]
        return True
    else:
        return False 

def checkWin():
    global gameOver    
    if checkHorizontal() == True:
        gameOver = True
        return True
    if checkVertical() == True:
        gameOver = True
        return True
    if checkDiagonal() == True:
        gameOver = True
        return True
    return False

def checkDraw():
    global gameOver
    for i in range(len(board)):
        if board[i] == "-":
            return False
    if winner is not None:
        print("Game is a Draw!")
        gameOver = True
        return True        
    else:    
        return False

def switchUser():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    elif currentPlayer == "O":
        currentPlayer = "X"
    return    

def check_win_minimax(board):
    # Check horizontal
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] and board[i] != "-":
            return board[i]
    # Check vertical
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] and board[i] != "-":
            return board[i]
    # Check diagonal
    if board[0] == board[4] == board[8] and board[0] != "-":
        return board[0]
    if board[2] == board[4] == board[6] and board[2] != "-":
        return board[2]
    return None

def check_draw_minimax(board):
    return all(cell != "-" for cell in board)

def minimax(board, isMaximizing):
    # Check for terminal states
    result = check_win_minimax(board)
    if result:
        return 10 if result == "O" else -10
    if check_draw_minimax(board):
        return 0

    if isMaximizing:
        best_score = -float('inf')
        for i in range(9):
            if board[i] == "-":
                board[i] = "O"
                score = minimax(board, False)
                board[i] = "-"  # Undo move
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] == "-":
                board[i] = "X"
                score = minimax(board, True)
                board[i] = "-"  # Undo move
                best_score = min(score, best_score)
        return best_score

def computerPlayer():
    global board, currentPlayer
    if currentPlayer == "O" and not gameOver:
        best_score = -float('inf')
        best_move = None
        for i in range(9):
            if board[i] == "-":
                board[i] = "O"
                score = minimax(board, False)
                board[i] = "-"  # Undo move
                if score > best_score:
                    best_score = score
                    best_move = i
        if best_move is not None:
            board[best_move] = "O"
            print_with_refresh()
            draw_board()
            switchUser()  # Move player switch here to align with game loop

clear_screen()
printBoard()
draw_board()

while not gameOver:
    takeInput(board)
    if checkWin() == True:
        break
    if checkDraw() == True:
        break
    switchUser()
    computerPlayer()
    if checkWin() == True:
        break
    if checkDraw() == True:
        break