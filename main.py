import sys
import pygame
from map import *

pygame.init()
pygame.display.set_caption('My map')

visible_sprites = pygame.sprite.Group()
map = pygame.sprite.Sprite()
Map.get_image("Дворцовая площадь, 2")
map.image = pygame.image.load("data/map.png")
map.rect = map.image.get_rect()
map.rect.x, map.rect.y = 0, 0
screen = pygame.display.set_mode(map.rect.size)
visible_sprites.add(map)


def draw_scene():
    visible_sprites.draw(screen)
    # visible_sprites.update()


while True:
    screen.fill(pygame.Color('black'))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    draw_scene()
    pygame.display.flip()

