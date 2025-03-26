# import os

# CANVAS_SIZE = 10  # Grid ki size (10x10)
# ERASER = 'E'  # Eraser ko represent karne ke liye
# BLANK = ' '  # Blank (Erased) area
# GRID_CELL = '■'  # Normal Grid Cell


# # Grid initialize karna
# grid = [[GRID_CELL for _ in range(CANVAS_SIZE)] for _ in range(CANVAS_SIZE)]

# # Eraser ka initial position (center)
# eraser_x, eraser_y = CANVAS_SIZE // 2, CANVAS_SIZE // 2

# def display_grid():
#     """Terminal me grid show karne ka function"""
#     os.system('cls' if os.name == 'nt' else 'clear')  # Screen clear 
#     for row in range(CANVAS_SIZE):
#         for col in range(CANVAS_SIZE):
#             if row == eraser_y and col == eraser_x:
#                 print(ERASER, end=' ')
#             else:
#                 print(grid[row][col], end=' ')
#         print()
#     print("\nMove Eraser with W (up), S (down), A (left), D (right). Press Q to quit.")

# def move_eraser(direction):
#     """Eraser ko move karne ka function"""
#     global eraser_x, eraser_y

#     # Pehle wali position ko erase karke dega
#     grid[eraser_y][eraser_x] = BLANK

#     # Movement logic
#     if direction == 'W' and eraser_y > 0:
#         eraser_y -= 1
#     elif direction == 'S' and eraser_y < CANVAS_SIZE - 1:
#         eraser_y += 1
#     elif direction == 'A' and eraser_x > 0:
#         eraser_x -= 1
#     elif direction == 'D' and eraser_x < CANVAS_SIZE - 1:
#         eraser_x += 1

# # Game Loop
# while True:
#     display_grid()
#     move = input("Enter Move: ").strip().upper()
    
#     if move == 'Q':  # Quit 
#         break
#     elif move in ['W', 'A', 'S', 'D']:  # Valid moves
#         move_eraser(move)

import pygame

pygame.init()

# Constants
CANVA_WIDTH = 400
CANVA_HEIGHT = 400
CELL_SIZE = 40
ERASER_SIZE = 20

# Colors
BLUE = (0, 0, 225)
WHITE = (255, 255, 255)
PINK = (255, 182, 193)

# Initialize screen
screen = pygame.display.set_mode((CANVA_WIDTH, CANVA_HEIGHT))
pygame.display.set_caption("Eraser Effect in Python")

# Create grid
grid = []
for row in range(0, CANVA_HEIGHT, CELL_SIZE):
    for col in range(0, CANVA_WIDTH, CELL_SIZE):
        rect = pygame.Rect(col, row, CELL_SIZE, CELL_SIZE)
        grid.append(rect)

# Create eraser
eraser = pygame.Rect(200, 200, ERASER_SIZE, ERASER_SIZE)

# Game loop variables
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(WHITE)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw grid
    new_grid = []
    for rect in grid:
        if not eraser.colliderect(rect):
            new_grid.append(rect)
        else:
            pygame.draw.rect(screen, WHITE, rect)  # Erased area

    grid = new_grid  # Update grid after loop

    for rect in grid:
        pygame.draw.rect(screen, BLUE, rect)

    # Eraser movement with mouse
    mouse_x, mouse_y = pygame.mouse.get_pos()
    eraser.topleft = (mouse_x, mouse_y)
    
    pygame.draw.rect(screen, PINK, eraser)  # Draw eraser

    pygame.display.flip()
    clock.tick(60)  # Maintain smooth frame rate

pygame.quit()

