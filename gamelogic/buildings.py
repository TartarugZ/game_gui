import pygame
from gamelogic.config import *


class Building(pygame.sprite.Sprite):
    def __init__(self, game, x, y, building_type):
        self.game = game
        self._layer = HOUSE_LAYER
        pygame.sprite.Sprite.__init__(self)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.name = building_type[NAME]

        self.image_x, self.image_y = building_type[IMAGE]
        self.image = self.game.buildings_spritesheet.get_sprite(self.image_x, self.image_y, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        self.resource_create = building_type[RESOURCES_CREATE]
        self.game.buildings_by_name[building_type[NAME]].add(self)
        
    def __dict__(self):
        return {
            X: self.x // TILESIZE,
            Y: self.y // TILESIZE,
            NAME: self.name,
        }


class DynamicBuilding(Building):
    def __init__(self, game, x, y, building_type, workers=0, tick=pygame.time.get_ticks()):
        super().__init__(game, x, y, building_type)

        self.remove_extra_sprite(building_type)

        self.resource_use = building_type[RESOURCES_USE]
        self.workers = workers
        self.max_workers = building_type[MAX_WORKERS]

        self.last_tick = tick
        self.cooldown = 1000
        
    def __dict__(self):
        sup = super().__dict__()
        sup.update({
            'workers': self.workers,
            'tick': self.last_tick // self.cooldown
        })
        return sup
    
    
    # def download(self, w):
    #     self.workers = w
    #     self.game.resources[PEOPLE][COUNT] -= w

    def add_worker(self):
        if self.workers < self.max_workers and self.game.resources[PEOPLE][COUNT] > 0:
            self.game.resources[PEOPLE][COUNT] -= 1
            self.workers += 1
            return True
        else:
            return False

    def remove_worker(self):
        if self.workers > 0:
            self.game.resources[PEOPLE][COUNT] += 1
            self.workers -= 1
            return True
        else:
            return False

    def remove_extra_sprite(self, building_info):
        if building_info[PLACE] == 'G' or building_info[PLACE] == 'I' or building_info[PLACE] == 'S':
            for spr in self.game.sprites_for_delete:
                if spr.x == self.x and spr.y == self.y:
                    spr.kill()
                    return

    def can_do(self):
        for r in self.resource_create:
            if self.game.resources[r][COUNT] + self.resource_create[r] * self.workers > self.game.resources[r][MAX]:
                return False
        if self.resource_use is not None:
            for r in self.resource_use:
                if self.game.resources[r][COUNT] - self.resource_use[r] * self.workers < 0:
                    return False
        return True

    def update(self):
        if self.can_do():
            now = pygame.time.get_ticks()
            if now - self.last_tick >= self.cooldown:
                self.last_tick = now
                if self.resource_use is not None:
                    for res in self.resource_use:
                        self.game.resources[res][COUNT] -= self.resource_use[res] * self.workers
                for res in self.resource_create:
                    self.game.resources[res][COUNT] += self.resource_create[res] * self.workers


class StaticBuilding(Building):
    def __init__(self, game, x, y, building_type):
        super().__init__(game, x, y, building_type)

        for res in self.resource_create:
            self.game.resources[res][MAX] += self.resource_create[res]
            self.game.resources[res][COUNT] += self.resource_create[res]


class StorageBuilding(Building):
    def __init__(self, game, x, y, building_type):
        super().__init__(game, x, y, building_type)

        for res in self.resource_create:
            self.game.resources[res][MAX] += self.resource_create[res]


class WarBuilding(Building):
    def __init__(self, game, x, y, building_type, tick=pygame.time.get_ticks()):
        super().__init__(game, x, y, building_type)

        self.last_tick = tick
        self.cooldown = 1000

        self.needed_soldiers = []
        self.train = 1

        if building_type[NAME] == BARRACKS:
            self.army_type = MILITARY
        elif building_type[NAME] == SHIPYARD:
            self.army_type = FLEET

        for t in self.resource_create:
            self.game.army[t][MAX] += self.resource_create[t]
    
    def __dict__(self):
        sup = super().__dict__()
        sup.update({
            'tick': self.last_tick // self.cooldown,
        })
        return sup

    def update(self):
        if self.game.train:
            now = pygame.time.get_ticks()
            if now - self.last_tick >= self.cooldown:
                self.last_tick = now
                empty_queue = 0
                for solder in self.game.army:
                    if self.game.army[solder][ORDER] == 0:
                        empty_queue += 1
                    elif self.game.army[solder][ORDER] > 0 and self.game.army[solder][TYPE] == self.army_type:
                        if self.game.army[solder][ORDER] - self.train >= 0:
                            self.game.army[solder][ORDER] -= self.train
                            self.game.army[solder][COUNT] += self.train
                        elif self.game.army[solder][ORDER] > 0:
                            self.game.army[solder][COUNT] += self.game.army[solder][ORDER]
                            self.game.army[solder][ORDER] -= self.game.army[solder][ORDER]
                        else:
                            self.needed_soldiers.remove(solder)
                if empty_queue == len(self.game.army):
                    self.game.train = False

    # def add_soldiers_to_train(self, soldier):
    #     self.needed_soldiers.append(soldier)
