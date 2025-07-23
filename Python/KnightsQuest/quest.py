
import pgzrun

GRID_WIDTH = 16 
GRID_HEIGHT = 12
GRID_SIZE = 50

WIDTH = GRID_WIDTH * GRID_SIZE
HEIGHT = GRID_HEIGHT * GRID_SIZE

# Define the map as a list of strings (1 character per tile)
MAP = [
    "WWWWWWWWWWWWWWWW",
    "W              W",
    "W              W",
    "W   W  KG      W",
    "W              W",
    "W              W",
    "W              W",
    "W              W",
    "W              W",
    "W              W",
    "W              W",
    "WWWWWWWWWWWWWWWW"
]

def get_screen_coords(x, y):
    return (x * GRID_SIZE, y * GRID_SIZE)

def draw_background():
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            tile = MAP[y][x]
            if tile == "W":
                screen.blit("floor1", get_screen_coords(x, y))
            else:
                screen.blit("floor1", get_screen_coords(x, y))

def draw():
    draw_background()

pgzrun.go()