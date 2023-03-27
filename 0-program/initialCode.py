from PIL import Image

def create_screen(width, height):
    screen = [[(0, 0, 0) for _ in range(width)] for _ in range(height)]
    return screen

def draw_line(screen, x0, y0, x1, y1, color):
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx - dy

    while x0 != x1 or y0 != y1:
        screen[y0][x0] = color
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x0 += sx
        if e2 < dx:
            err += dx
            y0 += sy
    screen[y0][x0] = color


width = 640
height = 480
screen = create_screen(width, height)

def save_ppm(screen, filename):
    height, width = len(screen), len(screen[0])
    with open(filename, 'w') as f:
        # Write the header
        f.write('P3\n')
        f.write(f'{width} {height}\n')
        f.write('255\n')

        # Write the pixel data
        for row in screen:
            for pixel in row:
                r, g, b = pixel
                f.write(f'{r} {g} {b} ')
            f.write('\n')


def display_screen(screen):
    width = len(screen[0])
    height = len(screen)
    image = Image.new("RGB", (width, height))
    pixel_data = []
    for row in screen:
        for pixel in row:
            pixel_data.append(pixel)
    image.putdata(pixel_data)
    image.show()


# Horizontal line with positive slope
draw_line(screen, 0, 50, 90, 50, (255, 255, 255))

# Vertical line with positive slope
draw_line(screen, 50, 0, 50, 90, (255, 0, 0))

# Line with slope < -1
draw_line(screen, 90, 0, 0, 90, (0, 255, 0))

# Line with slope > 1
draw_line(screen, 0, 0, 90, 90, (0, 0, 255))

# Horizontal line with negative slope
draw_line(screen, 90, 50, 0, 50, (255, 255, 0))

# Vertical line with negative slope
draw_line(screen, 50, 90, 50, 0, (255, 0, 255))

# Line with slope between 0 and 1
draw_line(screen, 0, 0, 90, 50, (255, 255, 255))

# Line with slope between -1 and 0
draw_line(screen, 0, 9, 90, 50, (0, 255, 255))

save_ppm(screen, 'screen.ppm')

