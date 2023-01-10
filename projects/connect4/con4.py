import numpy as np
import pygame
import sys
import math
 
red_color = (255,0,0)
yellow_color = (255,255,0)
black_color = (0,0,0)
blue_color = (0,0,255)
 
row_count = 6
column_count = 7
 
def board_create():
    board = np.zeros((row_count,column_count))
    return board
 
def dropping_piece(board, row, col, piece):
    board[row][col] = piece
 
def available_location(board, col):
    return board[row_count-1][col] == 0

def get_next_available_row(board, col):
    for r in range(row_count):
        if board[r][col] == 0:
            return r
def print_board(board):
    print(np.flip(board, 0))

def win_move(board, piece):
    # Kijk voor horizontale win lokaties
    for c in range(column_count-3):
        for r in range(row_count):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True
    # Kijk voor verticale win lokaties
    for c in range(column_count):
        for r in range(row_count-3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True
    # Kijk voor diagonale win lokaties "Positively sloped"
    for c in range(column_count-3):
        for r in range(row_count-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True
    # Kijk voor diagonale win lokaties "Negatively sloped"
    for c in range(column_count-3):
        for r in range(3, row_count):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True
def drawing_board(board):
    for c in range(column_count):
        for r in range(row_count):
            pygame.draw.rect(screen, blue_color, (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen, black_color, (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)

    for c in range(column_count):
        for r in range(row_count):      
            if board[r][c] == 1:
                pygame.draw.circle(screen, red_color, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
            elif board[r][c] == 2: 
                pygame.draw.circle(screen, yellow_color, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
    pygame.display.update()
 
 
board = board_create()
print_board(board)
game_over = False
turn = 0
 
#initalize pygame
pygame.init()
 
#define our screen size
SQUARESIZE = 100
 
#define width and height of board
width = column_count * SQUARESIZE
height = (row_count+1) * SQUARESIZE
 
size = (width, height)
 
RADIUS = int(SQUARESIZE/2 - 5)
 
screen = pygame.display.set_mode(size)
#Calling function drawing_board again
drawing_board(board)
pygame.display.update()
 
myfont = pygame.font.SysFont("monospace", 75)
 
while not game_over:
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
 
        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, black_color, (0,0, width, SQUARESIZE))
            posx = event.pos[0]
            if turn == 0:
                pygame.draw.circle(screen, red_color, (posx, int(SQUARESIZE/2)), RADIUS)
            else: 
                pygame.draw.circle(screen, yellow_color, (posx, int(SQUARESIZE/2)), RADIUS)
        pygame.display.update()
 
        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen, black_color, (0,0, width, SQUARESIZE))
            #print(event.pos)
            # Ask for Player 1 Input
            if turn == 0:
                posx = event.pos[0]
                col = int(math.floor(posx/SQUARESIZE))
 
                if available_location(board, col):
                    row = get_next_available_row(board, col)
                    dropping_piece(board, row, col, 1)
 
                    if win_move(board, 1):
                        label = myfont.render("Player 1 wins!!", 1, red_color)
                        screen.blit(label, (40,10))
                        game_over = True
 
 
            # # Ask for Player 2 Input
            else:               
                posx = event.pos[0]
                col = int(math.floor(posx/SQUARESIZE))
 
                if available_location(board, col):
                    row = get_next_available_row(board, col)
                    dropping_piece(board, row, col, 2)
 
                    if win_move(board, 2):
                        label = myfont.render("Player 2 wins!!", 1, yellow_color)
                        screen.blit(label, (40,10))
                        game_over = True
 
            print_board(board)
            drawing_board(board)
 
            turn += 1
            turn = turn % 2
 
            if game_over:
                pygame.time.wait(3000)