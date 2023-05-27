import pygame
import os

WIDTH, HEIGHT = 900, 500
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("New Game")
background_color = (25, 0, 100)
FPS = 60
SpaceShip = (50,40)

Yellow_Spaceship_Image = pygame.image.load(os.path.join('Images','spaceship_yellow.png'))
Yellow_Spaceship = pygame.transform.rotate(pygame.transform.scale(Yellow_Spaceship_Image, SpaceShip), 90)
Red_Spaceship_Image = pygame.image.load(os.path.join('Images','spaceship_red.png'))
Red_Spaceship = pygame.transform.rotate(pygame.transform.scale(Red_Spaceship_Image, SpaceShip),-90)

def draw_window():
    WINDOW.fill(background_color)
    WINDOW.blit(Yellow_Spaceship, (100,250))
    WINDOW.blit(Red_Spaceship, (700,250))
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw_window()
    pygame.quit()


if __name__ == "__main__":
    main()
