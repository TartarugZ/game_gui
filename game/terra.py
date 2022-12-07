import random

import pygame
from game.config import *


class Ground(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = TERRA_LAYER
        pygame.sprite.Sprite.__init__(self)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.image = self.choose_image(x, y)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def choose_image(self, x, y):
        if town_map[y - FIELD[Y]][x - FIELD[X]] == 'G' or \
                town_map[y - FIELD[Y]][x - FIELD[X]] == 'S' or \
                town_map[y - FIELD[Y]][x - FIELD[X]] == 'I':
            return self.game.stone_spritesheet.get_sprite(0, 0, self.width, self.height)

        list_str = list(town_map[y - FIELD['y']])
        list_str[x - FIELD['x']] = 'R'
        town_map[y - FIELD['y']] = ''.join(list_str)
        if town_map[y - FIELD['y']][x - FIELD['x'] - 1] == 'w' and \
                town_map[y - FIELD['y'] - 1][x - FIELD['x'] - 1] == 'w' and \
                town_map[y - FIELD['y'] - 1][x - FIELD['x']] == 'w':
            return self.game.beach_spritesheet.get_sprite(96, 0, self.width, self.height)

        if town_map[y - FIELD['y'] - 1][x - FIELD['x']] == 'w' and \
                town_map[y - FIELD['y'] - 1][x - FIELD['x'] + 1] == 'w' and \
                town_map[y - FIELD['y']][x - FIELD['x'] + 1] == 'w':
            return self.game.beach_spritesheet.get_sprite(160, 0, self.width, self.height)

        if town_map[y - FIELD['y']][x - FIELD['x'] - 1] == 'w' and \
                town_map[y - FIELD['y'] + 1][x - FIELD['x'] - 1] == 'w' and \
                town_map[y - FIELD['y'] + 1][x - FIELD['x']] == 'w':
            return self.game.beach_spritesheet.get_sprite(96, 64, self.width, self.height)

        if town_map[y - FIELD['y']][x - FIELD['x'] + 1] == 'w' and \
                town_map[y - FIELD['y'] + 1][x - FIELD['x'] + 1] == 'w' and \
                town_map[y - FIELD['y'] + 1][x - FIELD['x']] == 'w':
            return self.game.beach_spritesheet.get_sprite(160, 64, self.width, self.height)

        if town_map[y - FIELD['y'] + 1][x - FIELD['x'] + 1] == 'w' and \
                not town_map[y - FIELD['y'] + 1][x - FIELD['x']] == 'w' and \
                not town_map[y - FIELD['y']][x - FIELD['x'] + 1] == 'w':
            return self.game.beach_spritesheet.get_sprite(0, 0, self.width, self.height)
        if town_map[y - FIELD['y'] + 1][x - FIELD['x']] == 'w':
            return self.game.beach_spritesheet.get_sprite(32, 0, self.width, self.height)
        if town_map[y - FIELD['y'] + 1][x - FIELD['x'] - 1] == 'w' and \
                not town_map[y - FIELD['y'] + 1][x - FIELD['x']] == 'w' and \
                not town_map[y - FIELD['y']][x - FIELD['x'] - 1] == 'w':
            return self.game.beach_spritesheet.get_sprite(64, 0, self.width, self.height)

        if town_map[y - FIELD['y']][x - FIELD['x'] + 1] == 'w':
            return self.game.beach_spritesheet.get_sprite(0, 32, self.width, self.height)

        if town_map[y - FIELD['y']][x - FIELD['x'] - 1] == 'w':
            return self.game.beach_spritesheet.get_sprite(64, 32, self.width, self.height)

        if town_map[y - FIELD['y'] - 1][x - FIELD['x'] + 1] == 'w' and \
                not town_map[y - FIELD['y'] - 1][x - FIELD['x']] == 'w' and \
                not town_map[y - FIELD['y']][x - FIELD['x'] + 1] == 'w':
            return self.game.beach_spritesheet.get_sprite(0, 64, self.width, self.height)

        if town_map[y - FIELD['y'] - 1][x - FIELD['x']] == 'w':
            return self.game.beach_spritesheet.get_sprite(32, 64, self.width, self.height)

        if town_map[y - FIELD['y'] - 1][x - FIELD['x'] - 1] == 'w' and \
                not town_map[y - FIELD['y'] - 1][x - FIELD['x']] == 'w' and \
                not town_map[y - FIELD['y']][x - FIELD['x'] - 1] == 'w':
            return self.game.beach_spritesheet.get_sprite(64, 64, self.width, self.height)

        else:
            list_str[x - FIELD['x']] = '.'
            town_map[y - FIELD['y']] = ''.join(list_str)
            return self.game.grass_spritesheet.get_sprite(32, 32, self.width, self.height)


class Water(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = TERRA_LAYER
        pygame.sprite.Sprite.__init__(self)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.image = self.game.water_spritesheet.get_sprite(0, 0, self.width, self.height)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y


class Mountain(pygame.sprite.Sprite):
    def __init__(self, game, x, y, resource_type):
        self.game = game
        self._layer = TERRA_LAYER
        pygame.sprite.Sprite.__init__(self)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        if resource_type == 'G':
            self.image = self.game.ore_spritesheet.get_sprite(32, random.randint(0, 1) * TILESIZE, self.width,
                                                              self.height)
        elif resource_type == 'S':
            self.image = self.game.ore_spritesheet.get_sprite(64, random.randint(0, 1) * TILESIZE, self.width,
                                                              self.height)
        elif resource_type == 'I':
            self.image = self.game.ore_spritesheet.get_sprite(0, random.randint(0, 1) * TILESIZE, self.width,
                                                              self.height)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
