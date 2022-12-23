import random

import pygame
from gamelogic.config import *


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
            return self.game.ground_spritesheet.get_sprite(0, 96, self.width, self.height)

        list_str = list(town_map[y - FIELD[Y]])
        list_str[x - FIELD[X]] = 'R'
        town_map[y - FIELD[Y]] = ''.join(list_str)
        if town_map[y - FIELD[Y]][x - FIELD[X] - 1] == 'w' and \
                town_map[y - FIELD[Y] - 1][x - FIELD[X] - 1] == 'w' and \
                town_map[y - FIELD[Y] - 1][x - FIELD[X]] == 'w':
            return self.game.ground_spritesheet.get_sprite(96, 0, self.width, self.height)

        if town_map[y - FIELD[Y] - 1][x - FIELD[X]] == 'w' and \
                town_map[y - FIELD[Y] - 1][x - FIELD[X] + 1] == 'w' and \
                town_map[y - FIELD[Y]][x - FIELD[X] + 1] == 'w':
            return self.game.ground_spritesheet.get_sprite(160, 0, self.width, self.height)

        if town_map[y - FIELD[Y]][x - FIELD[X] - 1] == 'w' and \
                town_map[y - FIELD[Y] + 1][x - FIELD[X] - 1] == 'w' and \
                town_map[y - FIELD[Y] + 1][x - FIELD[X]] == 'w':
            return self.game.ground_spritesheet.get_sprite(96, 64, self.width, self.height)

        if town_map[y - FIELD[Y]][x - FIELD[X] + 1] == 'w' and \
                town_map[y - FIELD[Y] + 1][x - FIELD[X] + 1] == 'w' and \
                town_map[y - FIELD[Y] + 1][x - FIELD[X]] == 'w':
            return self.game.ground_spritesheet.get_sprite(160, 64, self.width, self.height)

        if town_map[y - FIELD[Y] + 1][x - FIELD[X] + 1] == 'w' and \
                not town_map[y - FIELD[Y] + 1][x - FIELD[X]] == 'w' and \
                not town_map[y - FIELD[Y]][x - FIELD[X] + 1] == 'w':
            return self.game.ground_spritesheet.get_sprite(0, 0, self.width, self.height)
        if town_map[y - FIELD[Y] + 1][x - FIELD[X]] == 'w':
            return self.game.ground_spritesheet.get_sprite(32, 0, self.width, self.height)
        if town_map[y - FIELD[Y] + 1][x - FIELD[X] - 1] == 'w' and \
                not town_map[y - FIELD[Y] + 1][x - FIELD[X]] == 'w' and \
                not town_map[y - FIELD[Y]][x - FIELD[X] - 1] == 'w':
            return self.game.ground_spritesheet.get_sprite(64, 0, self.width, self.height)

        if town_map[y - FIELD[Y]][x - FIELD[X] + 1] == 'w':
            return self.game.ground_spritesheet.get_sprite(0, 32, self.width, self.height)

        if town_map[y - FIELD[Y]][x - FIELD[X] - 1] == 'w':
            return self.game.ground_spritesheet.get_sprite(64, 32, self.width, self.height)

        if town_map[y - FIELD[Y] - 1][x - FIELD[X] + 1] == 'w' and \
                not town_map[y - FIELD[Y] - 1][x - FIELD[X]] == 'w' and \
                not town_map[y - FIELD[Y]][x - FIELD[X] + 1] == 'w':
            return self.game.ground_spritesheet.get_sprite(0, 64, self.width, self.height)

        if town_map[y - FIELD[Y] - 1][x - FIELD[X]] == 'w':
            return self.game.ground_spritesheet.get_sprite(32, 64, self.width, self.height)

        if town_map[y - FIELD[Y] - 1][x - FIELD[X] - 1] == 'w' and \
                not town_map[y - FIELD[Y] - 1][x - FIELD[X]] == 'w' and \
                not town_map[y - FIELD[Y]][x - FIELD[X] - 1] == 'w':
            return self.game.ground_spritesheet.get_sprite(64, 64, self.width, self.height)

        else:
            list_str[x - FIELD[X]] = '.'
            town_map[y - FIELD[Y]] = ''.join(list_str)
            return self.game.ground_spritesheet.get_sprite(224, 32, self.width, self.height)


class Water(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = TERRA_LAYER
        pygame.sprite.Sprite.__init__(self)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.image = self.game.ground_spritesheet.get_sprite(32, 32, self.width, self.height)

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
            self.image = self.game.ground_spritesheet.get_sprite(64, 96, self.width,
                                                              self.height)
        elif resource_type == 'S':
            self.image = self.game.ground_spritesheet.get_sprite(96, 96, self.width,
                                                              self.height)
        elif resource_type == 'I':
            self.image = self.game.ground_spritesheet.get_sprite(32, 96, self.width,
                                                              self.height)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
