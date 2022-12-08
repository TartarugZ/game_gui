import pygame
from game.config import *
import game.buildings as buildings
import game.terra as terra
import game.spritesheet as spritesheet
import game.place as place
from game.retention import Retention


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()

        self.running = True
        self.state = STATE_TOWN

        self.resources = RESOURCES
        self.buildings_by_name = {}

        for b in BUILDINGS:
            self.buildings_by_name[b] = pygame.sprite.Group()

        self.ground_spritesheet = spritesheet.SpriteSheet('img/sprites/ground.png')
        self.buildings_spritesheet = spritesheet.SpriteSheet('img/sprites/ground.png')
        self.save_data = Retention()

    def new(self):
        self.town_sprites = pygame.sprite.LayeredUpdates()
        self.playing = True
        self.houses = pygame.sprite.Group()
        self.places = pygame.sprite.Group()
        self.sprites_for_delete = pygame.sprite.Group()

        self.create_town_map()
        self.save_data.load(self)

    def create_town_map(self):
        for i, row in enumerate(town_map):
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
        for i, row in enumerate(town_map):
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
                    self.check_cost(building_type[COST]):
                self.put_building(x, y, building_type)
                self.pay(building_type[COST])
        except IndexError:
            pass

    def put_building(self, x, y, building_type):
        if building_type[TYPE] == DYNAMIC:
            new_house = buildings.DynamicBuilding(self, x, y, building_type)
        elif building_type[TYPE] == STATIC:
            new_house = buildings.StaticBuilding(self, x, y, building_type)
        elif building_type[TYPE] == WAREHOUSE:
            new_house = buildings.StorageBuilding(self, x, y, building_type)
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

    def check_cost(self, cost):
        for res in cost:
            if cost[res] > self.resources[res][COUNT]:
                return False
        return True

    def pay(self, cost):
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
        self.screen.fill(BLACK)
        self.town_sprites.draw(self.screen)
        self.clock.tick(FPS)
        pygame.display.update()

    def game_over(self):
        pass

    def intro_screen(self):
        pass
