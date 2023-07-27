import pygame

WIDTH, HEIGHT = 900, 500
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Game")
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40

# Colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
# Frame Rate
FPS = 60
# Movement Speed
VEL = 5

BORDER = pygame.Rect(WIDTH / 2 - 5, 0, 10, HEIGHT)

# Players
YELLOW_SPACESHIP_IMAGE = pygame.image.load("D:\Python\Pygame\Assets\spaceship_yellow.png")
YELLOW_SPACESHIP = pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))
YELLOW_SPACESHIP = pygame.transform.rotate(YELLOW_SPACESHIP, 90)


def yellow_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_a] and yellow.x - VEL > 0:  # Left
        yellow.x -= VEL
    if keys_pressed[pygame.K_d] and yellow.x + VEL + yellow.width < BORDER.x:  # Right
        yellow.x += VEL
    if keys_pressed[pygame.K_w] and yellow.y - VEL > 0:  # Up
        yellow.y -= VEL
    if keys_pressed[pygame.K_d] and yellow.y + VEL + yellow.height < HEIGHT - 5:  # Down
        yellow.y += VEL


def red_movement(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT] and red.x - VEL > BORDER.x + BORDER.width:  # Left
        red.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and red.x + VEL + red.width < WIDTH:  # Right
        red.x += VEL
    if keys_pressed[pygame.K_UP] and red.y - VEL > 0:  # Up
        red.y -= VEL
    if keys_pressed[pygame.K_DOWN] and red.y + VEL + red.height < HEIGHT - 5:  # Down
        red.y += VEL


RED_SPACESHIP_IMAGE = pygame.image.load("D:\Python\Pygame\Assets\spaceship_red.png")
RED_SPACESHIP = pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))
RED_SPACESHIP = pygame.transform.rotate(RED_SPACESHIP, 270)


def draw_window(red, yellow):
    WINDOW.fill(BLUE)
    pygame.draw.rect(WINDOW, BLACK, BORDER, 10)
    WINDOW.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WINDOW.blit(RED_SPACESHIP, (red.x, red.y))
    pygame.display.update()


def main():
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    clock = pygame.time.Clock()
    run = True

    # Game Loop
    while run:
        clock.tick(FPS)  # Adding Frame Rate
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        # red.y +=1

        keys_pressed = pygame.key.get_pressed()
        yellow_movement(keys_pressed, yellow)
        red_movement(keys_pressed, red)

        draw_window(red, yellow)
    pygame.quit()


if __name__ == "__main__":
    main()
