from os.path import isdir, join
from os import mkdir, listdir
import shelve
import shutil
import pygame

from gamelogic.static_var import *
from gamelogic.config import BUILDINGS, get_autosave

MAP_INDEX = 'index'
WORKER = 'workers'
LAST_TICK = 'last_tick'
RES = 'res'


class Retention:
    def __init__(self):
        self.last_tick = pygame.time.get_ticks()
        
    def check_cooldown(self):
        cooldown = get_autosave()
        now = pygame.time.get_ticks()
        if now - self.last_tick >= cooldown:
            self.last_tick = now
            return True
        return False

    def save(self, game, dir_name):
        if 'autosave' in dir_name:
            saves = ['save' + g for g in listdir("save") if isdir(join("save", g)) and 'autosave' in g]
            for i in saves:
                shutil.rmtree(f'save/{i}')
        
        if not isdir(f'save/{dir_name}'):
            mkdir(f'save/{dir_name}')
            
        file = shelve.open(f'save/{dir_name}/data')
        for r in game.resources:
            if not r == PEOPLE:
                file[RES + r] = game.resources[r][COUNT]
        file[MAP_INDEX] = len(game.houses)
        j = 0
        for h in game.houses:
            file[MAP_INDEX + str(j)] = h.__dict__()
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
            file[game.army[a][NAME]] = {
                COUNT: game.army[a][COUNT],
                ORDER: game.army[a][ORDER]
            }

    def load(self, game, dir_name):
        file = shelve.open(f'save/{dir_name}/data')
        for i in game.resources:
            try:
                game.resources[i][COUNT] = self.file[RES + i]
            except FileNotFoundError and KeyError:
                pass
        try:
            index = file[MAP_INDEX]
        except FileNotFoundError and KeyError:
            return

        for i in range(index):
            try:
                x = file[MAP_INDEX + str(i)][X]
                y = file[MAP_INDEX + str(i)][Y]
                building = BUILDINGS[file[MAP_INDEX + str(i)][NAME]]
                
                if building[TYPE] == DYNAMIC:
                    worker = file[MAP_INDEX + str(i)][WORKER]
                    tick = file[MAP_INDEX + str(i)]['tick']
                    game.put_building(x, y, building, worker, tick)
                
                elif building[TYPE] == WAR:
                    tick = self.file[MAP_INDEX + str(i)]['tick']
                    game.put_building(x, y, building, tick)
                
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
