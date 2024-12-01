import pgzrun

# WIDTH and HEIGHT - system variables - output screen
WIDTH = 300
HEIGHT = 300

TITLE = "Circle Pattern"

# draw() - inbuilt function gets called automatically. Helps render animations/shapes/texts.
def draw():
    screen.fill(color="black")

    # Circle properties
    radius = HEIGHT
    r=0
    g=255
    b = 8

    for i in range(100):
        # Draw the circle
        screen.draw.circle((150, 150), radius, (r, g, b))

        # Update properties for the next circle
        radius -= 10
        r = min(r + 10, 255)
        g = max(g - 10, 0)

pgzrun.go()
