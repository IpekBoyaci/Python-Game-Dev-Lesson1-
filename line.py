import pgzrun
from random import randint

# WIDTH and HEIGHT - system variables - output screen
WIDTH = 300
HEIGHT = 300

TITLE = "Rectangle and Line Pattern"

# draw() - inbuilt function gets called automatically. Helps render animations/shapes/texts.
def draw():
    screen.fill(color="black")

    # Rectangle width and height
    width = WIDTH - 200  # 300 - 200 = 100
    height = HEIGHT
    start = (0, 0)
    end = (300, 300)

    start1=(300,300)
    end1=(0,0)

    r, g, b = 255, 0, 88

    for i in range(20):
        # Draw the rectangle
        myRect = Rect((0, 0), (width, height))
        myRect.center = 150, 150
        screen.draw.rect(myRect, (r, g, b))

        # Update rectangle dimensions and colors
        width += 10
        height -= 10
        r = max(r - 10, 0)  # Ensure r doesn't go below 0
        g = min(g + 10, 255)  # Ensure g doesn't exceed 255

        # Draw the line
        screen.draw.line(start, end, (r, g, b))

        # Update line start and end points
        start = (start[0], start[1] + 10)  # Move start down
        end = (end[0], end[1] + 10)  # Move end down

pgzrun.go()
