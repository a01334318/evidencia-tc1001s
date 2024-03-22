"""Tic Tac Toe

Exercises

1. Give the X and O a different color and width.
2. What happens when someone taps a taken spot?
3. How would you detect when someone has won?
4. How could you create a computer player?
"""
from turtle import *
from freegames import line

# Define the grid size and initialize the grid with empty strings
# so later we can change the empty string to a player.
GRID_SIZE = 3
grid_data = [[''] * GRID_SIZE for _ in range(GRID_SIZE)]

def grid():
    """Draw tic-tac-toe grid."""
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)


# Function to draw X player
def drawx(x, y):
    """Draw X player."""
    #The color function is called to change the color of the player X to blue
    color("blue")
    line(x, y, x + 133, y + 133)
    line(x, y + 133, x + 133, y)

# Function to draw O player
def drawo(x, y):
    """Draw O player."""
    #The color function is called to change the color of the player o to red
    color("red")
    up()
    goto(x + 67, y + 5)
    down()
    circle(62)


def floor(value):
    """Round value down to grid with square size 133."""
    return ((value + 200) // 133) * 133 - 200


state = {'player': 0}
players = [drawx, drawo]


def tap(x, y):
    """Draw X or O in tapped square."""
    x = floor(x)
    y = floor(y)
    player = state['player']
    draw = players[player]
    

    # Convert x and y to indexes
    row = int((y + 200) // 133)
    col = int((x + 200) // 133)
    
    # Check if the box is already used with the indexes from above
    if grid_data[row][col] == '':
        #draws the player inside the box
        draw(x, y) 
        #changes the data for that specific box into the player
        grid_data[row][col] = 'X' if player == 0 else 'O'
        #The player changes
        update()
        state['player'] = not player


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
grid()
update()
onscreenclick(tap)
done()

