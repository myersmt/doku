'''
Matt Myers
09/16/2021
Sudoku Game and Solver
Sudoku is a classic intellectual game where there is a 3x3
grid with a 3x3 matrix inside making 9 large zones with 81
total squares. The goal of this game is to complete all 81
squares following the set rules. The rules are in each 
large square it must go 1-9 without repeating and in each
column and row it must go 1-9 without repeating.
'''
import pygame as pg
import sys, random

#Initialize the pygame module
pg.init()

#Background color
backg = (50,50,50)

#Game Setup
logo = pg.image.load("waff_logo_1.png")
fps = 600
clock = pg.time.Clock()
w_width = 600
w_height = 800


# Display the window
window = pg.display.set_mode((w_width,w_height))
pg.display.set_icon(logo)
pg.display.set_caption('Sudoku Solver')

# The main function that controls the game
def main () :
  looping = True
  
  # The main game loop
  while looping :
    # Get inputs
    for event in pg.event.get() :
      if event.type == pg.QUIT :
        pg.quit()
        sys.exit()
    
    # Processing
    # This section will be built out later
 
    # Render elements of the game
    window.fill(backg)
    pg.display.update()
    clock.tick(fps)

main()

