import pygame
import pygame_gui
from pygame_gui.core import ObjectID

import army_ui
import journal_ui
import storage_ui
import settings_ui
import world_ui
import workers_ui


class Town:
    def __init__(self, manager, background):
        self.manager = manager
        self.background = background
        self.population = []
        self.materials = []
        self.industries = []
        self.armies = []
        self.happiness_b = []

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
        if self.houses.pressed or not self.houses.is_enabled:
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
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            self.manager.process_events(event)
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == self.house:
                    self.enable_all()
                    house.disable()
                elif event.ui_element == self.gold_mine:
                    self.enable_all()
                    gold_mine.disable()
                elif event.ui_element == self.stone_mine:
                    self.enable_all()
                    stone_mine.disable()
                elif event.ui_element == self.iron_mine:
                    self.enable_all()
                    iron_mine.disable()
                elif event.ui_element == self.sawmill:
                    self.enable_all()
                    sawmill.disable()
                elif event.ui_element == self.storage:
                    self.enable_all()
                    storage.disable()
                elif event.ui_element == self.fishing:
                    self.enable_all()
                    fishing.disable()
                elif event.ui_element == self.wheat_field:
                    self.enable_all()
                    wheat_field.disable()
                elif event.ui_element == self.mill:
                    self.enable_all()
                    mill.disable()
                elif event.ui_element == self.bakery:
                    self.enable_all()
                    bakery.disable()
                elif event.ui_element == self.hunting:
                    self.enable_all()
                    hunting.disable()
                elif event.ui_element == self.blacksmith:
                    self.enable_all()
                    blacksmith.disable()
                elif event.ui_element == self.gunsmith:
                    self.enable_all()
                    gunsmith.disable()
                elif event.ui_element == self.barracks:
                    self.enable_all()
                    barracks.disable()
                elif event.ui_element == self.shipyard:
                    self.enable_all()
                    shipyard.disable()
                elif event.ui_element == self.tailor:
                    self.enable_all()
                    tailor.disable()
                elif event.ui_element == self.iron_melt:
                    self.enable_all()
                    iron_melt.disable()
                elif event.ui_element == self.gold_melt:
                    self.enable_all()
                    gold_melt.disable()
                elif event.ui_element == self.stop:
                    self.enable_side_buttons()
                    self.enable_all()
                    self.hide_all()
                elif event.ui_element == self.details:
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
