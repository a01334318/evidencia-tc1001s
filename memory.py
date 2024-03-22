"""Memory, puzzle game of number pairs.

Exercises:

1. Count and print how many taps occur.
2. Decrease the number of tiles to a 4x4 grid.
3. Detect when all tiles are revealed.
4. Center single-digit tile.
5. Use letters instead of tiles.
"""

import random as r
import turtle as t
from freegames import path


# Load the car image from file
car = path('car.gif')

# Create a list of tile numbers for the game
tiles = list(range(32)) * 2

# Dictionary to keep track of game state
state = {'mark': None}

# List to keep track of whether each tile is hidden or revealed
hide = [True] * 64

# Variable to keep track of the number of tap events
tap_count = 0


# Function to draw a white square with a black outline at (x, y)
def square(x, y):
    """Draw white square with black outline at (x, y)."""
    t.up()
    t.goto(x, y)
    t.down()
    t.color('black', 'white')
    t.begin_fill()
    for count in range(4):
        t.forward(50)
        t.left(90)
    t.end_fill()


# Function to convert (x, y) coordinates to tiles index
def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


# Function to convert tiles count to (x, y) coordinates
def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


# Function to handle a tap (click) event
def tap(x, y):
    """Update mark, hidden tiles, and tap count based on tap."""
    global tap_count
    tap_count += 1  # Increment the tap count
    spot = index(x, y)
    mark = state['mark']

    # If no tile is marked or the clicked tile is different from the marked one
    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        # If the clicked tile matches the marked tile, reveal both
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None


# Function to check if all tiles are revealed
def all_revealed():
    """Check if all tiles are revealed."""
    return all(not h for h in hide)


# Function to draw the game screen
def draw():
    """Draw image and tiles."""
    t.clear()
    t.goto(0, 0)
    t.shape(car)
    t.stamp()

    # Draw the tiles
    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    # If there is a marked tile and it is hidden, display its value
    if mark is not None and hide[mark]:
        x, y = xy(mark)
        t.up()
        t.goto(x + 2, y)
        t.color('black')
        t.write(tiles[mark], font=('Arial', 30, 'normal'))

    # Display the tap count
    t.goto(-180, 180)
    t.write(f'Taps: {tap_count}', font=('Arial', 16, 'normal'))

    # Check if all tiles are revealed
    if all_revealed():
        t.goto(-180, 160)
        t.write("Congratulations! You've revealed all tiles!",
                font=('Arial', 16, 'normal'))

    t.update()
    t.ontimer(draw, 100)


# Shuffle the tile numbers for random arrangement
r.shuffle(tiles)

# Set up the game window
t.setup(420, 420, 370, 0)

# Add the car image as a shape
t.addshape(car)

# Hide the turtle cursor
t.hideturtle()

# Disable animation tracer
t.tracer(False)

# Register the tap function to handle click events
t.onscreenclick(tap)

# Start drawing the game
draw()

# Finish the game window
t.done()
