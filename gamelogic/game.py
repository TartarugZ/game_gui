import pygame
import gamelogic.buildings as buildings
import gamelogic.terra as terra
import gamelogic.spritesheet as spritesheet
import gamelogic.place as place
from gamelogic.retention import Retention
from gamelogic.config import *

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()

        self.buildings_by_name = {}

        for b in BUILDINGS:
            self.buildings_by_name[b] = pygame.sprite.Group()

        self.ground_spritesheet = spritesheet.SpriteSheet('resources/img/sprites/ground.png')
        self.buildings_spritesheet = spritesheet.SpriteSheet('resources/img/sprites/buildings.png')
        self.save_data = Retention()
        
        self.new()

    def new(self):
        self.train = True

        self.running = True
        
        self.resources = START_RESOURCES.copy()
        self.army = START_ARMY.copy()
        self.expedition = EXPEDITION.copy()
        self.map = town_map.copy()
        
        self.town_sprites = pygame.sprite.LayeredUpdates()
        self.houses = pygame.sprite.Group()
        self.places = pygame.sprite.Group()
        self.sprites_for_delete = pygame.sprite.Group()

        self.create_town_map()
        # self.save_data.load(self)
    
    def local_save(self, dir_name):
        self.save_data.save(self, dir_name)
        
    def local_load(self, dir_name):
        self.new()
        self.save_data.load(self, dir_name)
    
    def server_save_data(self):
        save_res = {}
        save_houses = []
        save_army = {}
        for r in self.resources:
            if not r == PEOPLE:
                save_res.update({r: self.resources[r][COUNT]})
        
        for h in self.houses:
            save_houses.append(h.__dict__())
            
        for a in self.army:
            save_army.update({
                a: {
                    COUNT: self.army[a][COUNT],
                    ORDER: self.army[a][ORDER]
                }
            })
        return save_army, save_res, save_houses
    
    def server_load(self, save_army, save_resources, save_houses):
        self.new()
        for res in save_resources:
            self.resources[res][COUNT] = save_resources[res]
            
        for house in save_houses:
            x = house[X]
            y = house[Y]
            building = BUILDINGS[house[NAME]]
            
            if building[TYPE] == DYNAMIC:
                worker = house['workers']
                tick = house['tick']
                self.put_building(x, y, building, worker, tick)
                
            elif building[TYPE] == WAR:
                tick = house['tick']
                self.put_building(x, y, building, tick)
                
            else:
                self.put_building(x, y, building)
        
        for arm in save_army:
            self.army[arm][COUNT] = save_army[arm][COUNT]
            self.army[arm][ORDER] = save_army[arm][ORDER]            
            
    
    # def server_load(self, army, resources, houses):
    #     self.new()
        
        
    def create_town_map(self):
        for i, row in enumerate(self.map):
            for j, column in enumerate(row):
                if column == 'w':
                    self.town_sprites.add(terra.Water(self, j + FIELD[X], i + FIELD[Y]))
                elif column == '.':
                    self.town_sprites.add(terra.Ground(self, j + FIELD[X], i + FIELD[Y]))
                elif column == '0':
                    pass
                else:
                    self.town_sprites.add(terra.Ground(self, j + FIELD[X], i + FIELD[Y]))
                    mount = terra.Mountain(self, j + FIELD[X], i + FIELD[Y], column)
                    self.town_sprites.add(mount)
                    self.sprites_for_delete.add(mount)

    def show_place(self, building):
        for i, row in enumerate(self.map):
            for j, column in enumerate(row):
                if column == building[PLACE]:
                    if self.check_building(j + FIELD[X], i + FIELD[Y]):
                        pl = place.Place(self, j + FIELD[X], i + FIELD[Y])
                        self.town_sprites.add(pl)
                        self.places.add(pl)

    def delete_places(self):
        for s in self.places:
            s.kill()

    def build_building(self, x, y, building_type):
        try:
            if self.check_place(x * TILESIZE, y * TILESIZE) and \
                    self.check_building(x * TILESIZE, y * TILESIZE) and \
                    self.check_cost_resource(building_type[COST]):
                self.put_building(x, y, building_type)
                self.pay_resource(building_type[COST])
        except IndexError:
            pass

    def put_building(self, x, y, building_type, workers=0, tick=pygame.time.get_ticks()):
        if building_type[TYPE] == DYNAMIC:
            self.resources[PEOPLE][COUNT] -= workers
            new_house = buildings.DynamicBuilding(self, x, y, building_type, workers=workers, tick=tick)
        elif building_type[TYPE] == STATIC:
            new_house = buildings.StaticBuilding(self, x, y, building_type)
        elif building_type[TYPE] == WAREHOUSE:
            new_house = buildings.StorageBuilding(self, x, y, building_type)
        elif building_type[TYPE] == WAR:
            new_house = buildings.WarBuilding(self, x, y, building_type, tick=tick)
        else:
            return None
        self.houses.add(new_house)
        self.town_sprites.add(new_house)
        return new_house

    def check_place(self, b_x, b_y):
        for p in self.places:
            if p.x == b_x and p.y == b_y:
                return True
        return False

    def check_building(self, new_x, new_y):
        for h in self.houses:
            if h.x == new_x and h.y == new_y:
                return False
        return True

    def check_cost_resource(self, cost):
        for res in cost:
            if cost[res] > self.resources[res][COUNT]:
                return False
        return True

    def pay_resource(self, cost):
        for res in cost:
            self.resources[res][COUNT] -= cost[res]

    def workers_in_current_type_building(self, build_name):
        workers = 0
        max_workers = 0
        for build in self.buildings_by_name[build_name]:
            workers += build.workers
            max_workers += build.max_workers
        return workers, max_workers

    def add_worker(self, building_name):
        for b in self.buildings_by_name[building_name]:
            if b.add_worker():
                return

    def remove_worker(self, building):
        for b in self.buildings_by_name[building]:
            if b.remove_worker():
                return

    def update(self):
        self.town_sprites.update()

    def draw(self):
        # self.screen.fill(BLACK)
        self.town_sprites.draw(self.screen)
        self.clock.tick(FPS)
        pygame.display.update()

    def train_soldiers(self, count, soldier):
        if self.check_cost_resource(self.army[soldier][COST]):
            self.train = True
            self.pay_resource(self.army[soldier][COST])
            self.army[soldier][ORDER] += count

    def check_cost_army(self, cost):
        for s in cost:
            if cost[s] > self.army[s][COUNT]:
                return False
        return True

    def pay_army(self, cost):
        for s in cost:
            self.army[s][COUNT] -= cost[s]

    def get_resource_from_expedition(self, ex_resources):
        for res in ex_resources:
            self.resources[res][COUNT] += ex_resources[res]

    def start_expedition(self, expedition_type):
        ex = self.expedition[expedition_type]
        if self.check_cost_army(ex[COST]):
            self.pay_army(ex[COST])
            self.get_resource_from_expedition(ex[RESOURCES_CREATE])

    def check_expedition(self, expedition_type):
        ex = self.expedition[expedition_type]
        return self.check_cost_army(ex[COST])

    def check_soldiers(self, soldier):
        return self.check_cost_resource(self.army[soldier][COST])

