import pygame
import pygame_gui
from pygame_gui.core import ObjectID
from game.config import *


class Town:
    def __init__(self, manager, background, g):
        self.manager = manager
        self.background = background
        self.population = []
        self.materials = []
        self.industries = []
        self.armies = []
        self.happiness_b = []
        self.game = g

        self.houses = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((700, 0), (100, 50)),
                                                   text='Houses',
                                                   manager=self.manager, tool_tip_text="10 wood, 10 stones")
        self.house = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 450), (100, 50)),
                                                  text='House',
                                                  manager=self.manager, tool_tip_text="10 wood, 10 stones",
                                                  object_id=ObjectID(object_id='#build', class_id='@special'))
        self.population.append(self.house)

        self.material = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((700, 50), (100, 50)),
                                                     text='Materials',
                                                     manager=self.manager)
        self.gold_mine = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 450), (100, 50)),
                                                      text='Gold mine',
                                                      manager=self.manager,
                                                      object_id=ObjectID(object_id='#build', class_id='@special'))
        self.stone_mine = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((100, 450), (100, 50)),
                                                       text='Stone mine',
                                                       manager=self.manager,
                                                       object_id=ObjectID(object_id='#build', class_id='@special'))
        self.iron_mine = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((200, 450), (100, 50)),
                                                      text='Iron mine',
                                                      manager=self.manager,
                                                      object_id=ObjectID(object_id='#build', class_id='@special'))
        self.sawmill = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((300, 450), (100, 50)),
                                                    text='Sawmill',
                                                    manager=self.manager,
                                                    object_id=ObjectID(object_id='#build', class_id='@special'))
        self.hunting = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((400, 450), (100, 50)),
                                                    text='Hunter',
                                                    manager=self.manager,
                                                    object_id=ObjectID(object_id='#build', class_id='@special'))
        self.materials.append(self.gold_mine)
        self.materials.append(self.stone_mine)
        self.materials.append(self.iron_mine)
        self.materials.append(self.sawmill)
        self.materials.append(self.hunting)

        self.industry = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((700, 100), (100, 50)),
                                                     text='Industry',
                                                     manager=self.manager)
        self.storage = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 450), (100, 50)),
                                                    text='Storage',
                                                    manager=self.manager,
                                                    object_id=ObjectID(object_id='#build', class_id='@special'))
        self.gold_melt = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((100, 450), (100, 50)),
                                                      text='Melt gold',
                                                      manager=self.manager,
                                                      object_id=ObjectID(object_id='#build', class_id='@special'))
        self.iron_melt = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((200, 450), (100, 50)),
                                                      text='Melt iron',
                                                      manager=self.manager,
                                                      object_id=ObjectID(object_id='#build', class_id='@special'))
        self.industries.append(self.storage)
        self.industries.append(self.gold_melt)
        self.industries.append(self.iron_melt)

        self.army = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((700, 150), (100, 50)),
                                                 text='Army',
                                                 manager=self.manager)
        self.gunsmith = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 450), (100, 50)),
                                                     text='Gunsmith',
                                                     manager=self.manager,
                                                     object_id=ObjectID(object_id='#build', class_id='@special'))
        self.blacksmith = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((100, 450), (100, 50)),
                                                       text='Blacksmith',
                                                       manager=self.manager,
                                                       object_id=ObjectID(object_id='#build', class_id='@special'))
        self.barracks = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((200, 450), (100, 50)),
                                                     text='Barracks',
                                                     manager=self.manager,
                                                     object_id=ObjectID(object_id='#build', class_id='@special'))
        self.shipyard = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((300, 450), (100, 50)),
                                                     text='Shipyard',
                                                     manager=self.manager,
                                                     object_id=ObjectID(object_id='#build', class_id='@special'))
        self.armies.append(self.gunsmith)
        self.armies.append(self.blacksmith)
        self.armies.append(self.barracks)
        self.armies.append(self.shipyard)

        self.happiness = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((700, 200), (100, 50)),
                                                      text='Happiness',
                                                      manager=self.manager)
        self.wheat_field = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 450), (100, 50)),
                                                        text='Wheat field',
                                                        manager=self.manager,
                                                        object_id=ObjectID(object_id='#build', class_id='@special'))
        self.mill = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((100, 450), (100, 50)),
                                                 text='Mill',
                                                 manager=self.manager,
                                                 object_id=ObjectID(object_id='#build', class_id='@special'))
        self.bakery = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((200, 450), (100, 50)),
                                                   text='Bakery',
                                                   manager=self.manager,
                                                   object_id=ObjectID(object_id='#build', class_id='@special'))
        self.tailor = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((300, 450), (100, 50)),
                                                   text='Tailor',
                                                   manager=self.manager,
                                                   object_id=ObjectID(object_id='#build', class_id='@special'))
        self.fishing = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((400, 450), (100, 50)),
                                                    text='Fisherman',
                                                    manager=self.manager,
                                                    object_id=ObjectID(object_id='#build', class_id='@special'))
        self.happiness_b.append(self.wheat_field)
        self.happiness_b.append(self.mill)
        self.happiness_b.append(self.bakery)
        self.happiness_b.append(self.tailor)
        self.happiness_b.append(self.fishing)

        self.stop = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((600, 450), (100, 50)),
                                                 text='Stop',
                                                 manager=self.manager,
                                                 object_id=ObjectID(class_id=None, object_id='#stop'))
        self.details = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((700, 450), (100, 50)),
                                                    text='Details',
                                                    manager=self.manager,
                                                    object_id=ObjectID(class_id=None, object_id='#details'))
        self.hide_all()


    def start(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            self.manager.process_events(event)

        if self.houses.pressed:
            self.hide_all()
            self.enable_side_buttons()
            self.houses.disable()
            for building in self.population:
                building.show()
        if self.material.pressed or not self.material.is_enabled:
            self.hide_all()
            self.enable_side_buttons()
            self.material.disable()
            for building in self.materials:
                building.show()
        if self.industry.pressed or not self.industry.is_enabled:
            self.hide_all()
            self.enable_side_buttons()
            self.industry.disable()
            for building in self.industries:
                building.show()
        if self.army.pressed or not self.army.is_enabled:
            self.hide_all()
            self.enable_side_buttons()
            self.army.disable()
            for building in self.armies:
                building.show()
        if self.happiness.pressed or not self.happiness.is_enabled:
            self.hide_all()
            self.enable_side_buttons()
            self.happiness.disable()
            for building in self.happiness_b:
                building.show()

        if self.house.pressed:
            self.enable_all()
            self.house.disable()
            self.game.show_place(BUILDINGS[HOUSE])
        elif self.gold_mine.pressed:
            self.enable_all()
            self.gold_mine.disable()
            self.game.show_place(BUILDINGS[GOLD_MINE])
        elif self.stone_mine.pressed:
            self.enable_all()
            self.stone_mine.disable()
            self.game.show_place(BUILDINGS[STONE_MINE])
        elif self.iron_mine.pressed:
            self.enable_all()
            self.iron_mine.disable()
            self.game.show_place(BUILDINGS[IRON_MINE])
        elif self.sawmill.pressed:
            self.enable_all()
            self.sawmill.disable()
            self.game.show_place(BUILDINGS[SAWMILL])
        elif self.storage.pressed:
            self.enable_all()
            self.storage.disable()
            self.game.show_place(BUILDINGS[STORAGE])
        elif self.fishing.pressed:
            self.enable_all()
            self.fishing.disable()
            self.game.show_place(BUILDINGS[FISHERMAN])
        elif self.wheat_field.pressed:
            self.enable_all()
            self.wheat_field.disable()
            self.game.show_place(BUILDINGS[WHEAT_FIELD])
        elif self.mill.pressed:
            self.enable_all()
            self.mill.disable()
            self.game.show_place(BUILDINGS[MILL])
        elif self.bakery.pressed:
            self.enable_all()
            self.bakery.disable()
            self.game.show_place(BUILDINGS[BAKERY])
        elif self.hunting.pressed:
            self.enable_all()
            self.hunting.disable()
            self.game.show_place(BUILDINGS[HUNTER])
        elif self.blacksmith.pressed:
            self.enable_all()
            self.blacksmith.disable()
            self.game.show_place(BUILDINGS[BLACKSMITH])
        elif self.gunsmith.pressed:
            self.enable_all()
            self.gunsmith.disable()
            self.game.show_place(BUILDINGS[GUNSMITH])
        elif self.barracks.pressed:
            self.enable_all()
            self.barracks.disable()
            self.game.show_place(BUILDINGS[BARRACKS])
        elif self.shipyard.pressed:
            self.enable_all()
            self.shipyard.disable()
            self.game.show_place(BUILDINGS[SHIPYARD])
        elif self.tailor.pressed:
            self.enable_all()
            self.tailor.disable()
            self.game.show_place(BUILDINGS[TAILOR])
        elif self.iron_melt.pressed:
            self.enable_all()
            self.iron_melt.disable()
            self.game.show_place(BUILDINGS[IRON_MELT])
        elif self.gold_melt.pressed:
            self.enable_all()
            self.gold_melt.disable()
            self.game.show_place(BUILDINGS[GOLD_MELT])
        elif self.stop.pressed:
            self.enable_side_buttons()
            self.enable_all()
            self.hide_all()
            self.game.delete_places()
        elif self.details.pressed:
            pass  # To game code


    def hide_all_town(self):
        self.hide_all()
        self.houses.hide()
        self.material.hide()
        self.industry.hide()
        self.army.hide()
        self.happiness.hide()
        self.details.hide()
        self.stop.hide()

    def show_side_buttons(self):
        self.houses.show()
        self.material.show()
        self.industry.show()
        self.army.show()
        self.happiness.show()
        self.details.show()
        self.stop.show()

    def hide_all(self):
        for building in self.population:
            building.hide()
        for building in self.materials:
            building.hide()
        for building in self.industries:
            building.hide()
        for building in self.armies:
            building.hide()
        for building in self.happiness_b:
            building.hide()

    def enable_all(self):
        self.game.delete_places()
        for building in self.population:
            building.enable()
        for building in self.materials:
            building.enable()
        for building in self.industries:
            building.enable()
        for building in self.armies:
            building.enable()
        for building in self.happiness_b:
            building.enable()

    def enable_side_buttons(self):
        self.houses.enable()
        self.material.enable()
        self.industry.enable()
        self.army.enable()
        self.happiness.enable()
        self.details.enable()
        self.stop.enable()
