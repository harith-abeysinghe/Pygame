import pygame

WIDTH, HEIGHT = 900,500
WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("First Game")
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55,40

#Colors
RED = (255,0,0)
GREEN = (0, 255, 0)
BLUE =  (0,0,255)
#Frame Rate
FPS = 60

#Players
YELLOW_SPACESHIP_IMAGE = pygame.image.load("D:\Python\Pygame\Assets\spaceship_yellow.png")
YELLOW_SPACESHIP = pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH,SPACESHIP_HEIGHT))
RED_SPACESHIP_IMAGE = pygame.image.load("D:\Python\Pygame\Assets\spaceship_red.png")
RED_SPACESHIP = pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH,SPACESHIP_HEIGHT))
def draw_window():
    WINDOW.fill(BLUE)
    WINDOW.blit(YELLOW_SPACESHIP, (300,250))
    WINDOW.blit(RED_SPACESHIP, (600, 250))
    pygame.display.update()
def main():
    clock = pygame.time.Clock()
    run = True

    # Game Loop
    while run:
        clock.tick(FPS) #Adding Frame Rate
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw_window()
    pygame.quit()

if __name__ == "__main__":
    main()