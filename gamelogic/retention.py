import shelve

import pygame

from gamelogic.config import *

MAP_INDEX = 'index'
WORKER = 'workers'
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
        for r in game.resources:
            if not r == PEOPLE:
                self.file[RES + r] = game.resources[r][COUNT]
        self.file[MAP_INDEX] = len(game.houses)
        j = 0
        for h in game.houses:
            self.file[MAP_INDEX + str(j)] = h.__dict__()
            # print(h.__dict__())
            # if BUILDINGS[h.name][TYPE] == DYNAMIC:
            #     self.file[MAP_INDEX + str(j)] = {
            #         X: h.x // TILESIZE,
            #         Y: h.y // TILESIZE,
            #         NAME: h.name,
            #         WORKER: h.workers,
            #     }
            # else:
            #     self.file[MAP_INDEX + str(j)] = {
            #         X: h.x // TILESIZE,
            #         Y: h.y // TILESIZE,
            #         NAME: h.name,
            #     }
            j += 1
        for a in game.army:
            self.file[game.army[a][NAME]] = {
                COUNT: game.army[a][COUNT],
                ORDER: game.army[a][ORDER]
            }

    def load(self, game):
        for i in game.resources:
            try:
                game.resources[i][COUNT] = self.file[RES + i]
            except FileNotFoundError and KeyError:
                pass
        try:
            index = self.file[MAP_INDEX]
        except FileNotFoundError and KeyError:
            return

        for i in range(index):
            try:
                x = self.file[MAP_INDEX + str(i)][X]
                y = self.file[MAP_INDEX + str(i)][Y]
                building = BUILDINGS[self.file[MAP_INDEX + str(i)][NAME]]
                
                if building[TYPE] == DYNAMIC:
                    worker = self.file[MAP_INDEX + str(i)][WORKER]
                    tick = self.file[MAP_INDEX + str(i)]['tick']
                    game.put_building(x, y, building, worker, tick)
                
                elif building[TYPE] == WAR:
                    tick = self.file[MAP_INDEX + str(i)]['tick']
                    game.put_building(x, y, building, worker, tick)
                
                else:
                    game.put_building(x, y, building)
            except FileNotFoundError and KeyError:
                pass
        for a in game.army:
            try:
                game.army[a][COUNT] = self.file[a][COUNT]
                game.army[a][ORDER] = self.file[a][ORDER]
            except FileNotFoundError and KeyError:
                pass


def __del__(self):
    self.file.close()
