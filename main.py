import sys
import pygame
from map import *


def map_update(adress, scale):
    Map.get_image(adress, scale)
    map.image = pygame.image.load("data/map.png")
    map.rect = map.image.get_rect()
    map.rect.x, map.rect.y = 0, 0


def draw_scene():
    visible_sprites.draw(screen)
    map_update(adress_p, scale_p)


scale_p = 17
adress_p = "Дворцовая площадь, 2"

pygame.init()
pygame.display.set_caption('My map')

visible_sprites = pygame.sprite.Group()
map = pygame.sprite.Sprite()
map_update(adress_p, scale_p)
screen = pygame.display.set_mode(map.rect.size)
visible_sprites.add(map)

while True:
    screen.fill(pygame.Color('black'))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            print("*")
            scale_p += 1
            if scale_p > 17:
                scale_p = 17
        elif keys[pygame.K_s]:
            scale_p -= 1
            if scale_p < 0:
                scale_p = 0

    print(scale_p)
    draw_scene()
    pygame.display.flip()
