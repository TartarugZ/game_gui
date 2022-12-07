import shelve

import pygame

from game.config import *

MAP_INDEX = 'index'
WORKER = 'worker'
LAST_TICK = 'last_tick'
RES = 'res'


class Retention:
    def __init__(self):
        self.file = shelve.open('save/data')
        self.last_tick = pygame.time.get_ticks()
        self.cooldown = 300000

    def check_cooldown(self):
        now = pygame.time.get_ticks()
        if now - self.last_tick >= self.cooldown:
            self.last_tick = now
            return True
        return False

    def save(self, game):
        for i in game.resources:
            if not i == PEOPLE:
                self.file[RES + i] = game.resources[i][COUNT]
        self.file[MAP_INDEX] = len(game.houses)
        j = 0
        for i in game.houses:
            if BUILDINGS[i.name][TYPE] == DYNAMIC:
                self.file[MAP_INDEX + str(j)] = {
                    X: i.x // TILESIZE,
                    Y: i.y // TILESIZE,
                    NAME: i.name,
                    WORKER: i.workers,
                    LAST_TICK: i.last_tick
                }
            if BUILDINGS[i.name][TYPE] == STATIC or BUILDINGS[i.name][TYPE] == WAREHOUSE:
                self.file[MAP_INDEX + str(j)] = {
                    X: i.x // TILESIZE,
                    Y: i.y // TILESIZE,
                    NAME: i.name,
                }
            j += 1

    def load(self, game):
        for i in game.resources:
            try:
                game.resources[i][COUNT] = self.file[RES + i]
            except FileNotFoundError and KeyError:
                pass
        try:
            for i in range(self.file[MAP_INDEX]):
                x = self.file[MAP_INDEX + str(i)][X]
                y = self.file[MAP_INDEX + str(i)][Y]
                b = BUILDINGS[self.file[MAP_INDEX + str(i)][NAME]]
                if b[TYPE] == DYNAMIC:
                    house = game.put_building(x, y, b)
                    house.download(
                        self.file[MAP_INDEX + str(i)][WORKER],
                        self.file[MAP_INDEX + str(i)][LAST_TICK]
                    )
                elif b[TYPE] == STATIC or b[TYPE] == WAREHOUSE:
                    game.put_building(x, y, b)
        except FileNotFoundError and KeyError:
            pass


def __del__(self):
    self.file.close()
