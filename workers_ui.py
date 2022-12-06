import time
import navigation_bar
import pygame
import pygame_gui
import army_ui
import journal_ui
import storage_ui
import settings_ui
import world_ui
import town_ui


class Workers:
    def __init__(self, manager, background):
        self.manager = manager
        self.background = background
        self.text_needed = True
        self.population = 100
        self.buttons = []
        self.count = 0

        self.field_b = 100
        self.iron_mine_b = 15
        self.gold_mine_b = 0
        self.stone_mine_b = 0
        self.sawmill_b = 0
        self.fish_b = 0
        self.blacksmith_b = 50
        self.gunsmith_b = 0
        self.mill_b = 0
        self.bakery_b = 0
        self.gold_melt_b = 0
        self.iron_melt_b = 0
        self.tailor_b = 0
        self.shipyard_b = 0
        self.hunt_b = 0

        self.field = 0
        self.iron_mine = 0
        self.gold_mine = 0
        self.stone_mine = 0
        self.sawmill = 0
        self.fish = 0
        self.blacksmith = 0
        self.gunsmith = 0
        self.mill = 0
        self.bakery = 0
        self.gold_melt = 0
        self.iron_melt = 0
        self.tailor = 0
        self.shipyard = 0
        self.hunt = 0

        self.field_max = self.field_b
        self.iron_mine_max = self.iron_mine_b * 4
        self.gold_mine_max = self.gold_mine_b * 4
        self.stone_mine_max = self.stone_mine_b * 4
        self.sawmill_max = self.sawmill_b
        self.fish_max = self.fish_b
        self.blacksmith_max = self.blacksmith_b
        self.gunsmith_max = self.gunsmith_b
        self.mill_max = self.mill_b
        self.bakery_max = self.bakery_b
        self.gold_melt_max = self.gold_melt_b * 2
        self.iron_melt_max = self.iron_melt_b * 2
        self.tailor_max = self.tailor_b
        self.shipyard_max = self.shipyard_b * 4
        self.hunt_max = self.hunt_b

        self.field_minus = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 0), (150, 25)),
                                                        text='-',
                                                        manager=self.manager)
        self.field_plus = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((270, 0), (150, 25)),
                                                       text='+',
                                                       manager=self.manager)
        self.buttons.append(self.field_minus)
        self.buttons.append(self.field_plus)

        self.gold_mine_minus = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 25), (150, 25)),
                                                            text='-',
                                                            manager=self.manager)
        self.gold_mine_plus = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((270, 25), (150, 25)),
                                                           text='+',
                                                           manager=self.manager)
        self.buttons.append(self.gold_mine_plus)
        self.buttons.append(self.gold_mine_minus)

        self.stone_mine_minus = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 50), (150, 25)),
                                                             text='-',
                                                             manager=self.manager)
        self.stone_mine_plus = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((270, 50), (150, 25)),
                                                            text='+',
                                                            manager=self.manager)
        self.buttons.append(self.stone_mine_plus)
        self.buttons.append(self.stone_mine_minus)

        self.iron_mine_minus = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 75), (150, 25)),
                                                            text='-',
                                                            manager=self.manager)
        self.iron_mine_plus = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((270, 75), (150, 25)),
                                                           text='+',
                                                           manager=self.manager)
        self.buttons.append(self.iron_mine_plus)
        self.buttons.append(self.iron_mine_minus)

        self.sawmill_minus = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 100), (150, 25)),
                                                          text='-',
                                                          manager=self.manager)
        self.sawmill_plus = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((270, 100), (150, 25)),
                                                         text='+',
                                                         manager=self.manager)
        self.buttons.append(self.sawmill_plus)
        self.buttons.append(self.sawmill_minus)

        self.fishing_minus = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 125), (150, 25)),
                                                          text='-',
                                                          manager=self.manager)
        self.fishing_plus = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((270, 125), (150, 25)),
                                                         text='+',
                                                         manager=self.manager)
        self.buttons.append(self.fishing_plus)
        self.buttons.append(self.fishing_minus)

        self.gunsmith_minus = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 150), (150, 25)),
                                                           text='-',
                                                           manager=self.manager)
        self.gunsmith_plus = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((270, 150), (150, 25)),
                                                          text='+',
                                                          manager=self.manager)
        self.buttons.append(self.gunsmith_plus)
        self.buttons.append(self.gunsmith_minus)

        self.mill_minus = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 175), (150, 25)),
                                                       text='-',
                                                       manager=self.manager)
        self.mill_plus = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((270, 175), (150, 25)),
                                                      text='+',
                                                      manager=self.manager)
        self.buttons.append(self.mill_plus)
        self.buttons.append(self.mill_minus)

        self.bakery_minus = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 200), (150, 25)),
                                                         text='-',
                                                         manager=self.manager)
        self.bakery_plus = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((270, 200), (150, 25)),
                                                        text='+',
                                                        manager=self.manager)
        self.buttons.append(self.bakery_plus)
        self.buttons.append(self.bakery_minus)

        self.gold_melt_minus = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 225), (150, 25)),
                                                            text='-',
                                                            manager=self.manager)
        self.gold_melt_plus = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((270, 225), (150, 25)),
                                                           text='+',
                                                           manager=self.manager)
        self.buttons.append(self.gold_melt_plus)
        self.buttons.append(self.gold_melt_minus)

        self.blacksmith_minus = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 250), (150, 25)),
                                                             text='-',
                                                             manager=self.manager)
        self.blacksmith_plus = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((270, 250), (150, 25)),
                                                            text='+',
                                                            manager=self.manager)
        self.buttons.append(self.blacksmith_plus)
        self.buttons.append(self.blacksmith_minus)

        self.iron_melt_minus = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 275), (150, 25)),
                                                            text='-',
                                                            manager=self.manager)
        self.iron_melt_plus = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((270, 275), (150, 25)),
                                                           text='+',
                                                           manager=self.manager)
        self.buttons.append(self.iron_melt_plus)
        self.buttons.append(self.iron_melt_minus)

        self.tailor_minus = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 300), (150, 25)),
                                                         text='-',
                                                         manager=self.manager)
        self.tailor_plus = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((270, 300), (150, 25)),
                                                        text='+',
                                                        manager=self.manager)
        self.buttons.append(self.tailor_plus)
        self.buttons.append(self.tailor_minus)

        self.hunting_minus = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 325), (150, 25)),
                                                          text='-',
                                                          manager=self.manager)
        self.hunting_plus = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((270, 325), (150, 25)),
                                                         text='+',
                                                         manager=self.manager)
        self.buttons.append(self.hunting_plus)
        self.buttons.append(self.hunting_minus)

        self.shipyard_minus = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 350), (150, 25)),
                                                           text='-',
                                                           manager=self.manager)
        self.shipyard_plus = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((270, 350), (150, 25)),
                                                          text='+',
                                                          manager=self.manager)
        self.buttons.append(self.shipyard_plus)
        self.buttons.append(self.shipyard_minus)

    def start(self):
        a = 0
        for button in self.buttons:
            if button.held:
                self.count = self.count + 1
                a = 0
            else:
                a += 1
                if a == 30:
                    self.count = 0
        unemployed_people = self.population - self.count_workers()

        self.background.fill(pygame.Color(43, 43, 43))
        if self.text_needed:
            navigation_bar.draw_text(self.background, f'Unemployed people {unemployed_people}',
                                     15, 700, 10)

            navigation_bar.draw_text(self.background, f'Field {self.field}/{self.field_max}',
                                     15, 210, 5)
            navigation_bar.draw_text(self.background, f'Gold mine {self.gold_mine}/{self.gold_mine_max}',
                                     15, 210, 30)
            navigation_bar.draw_text(self.background, f'Stone mine {self.stone_mine}/{self.stone_mine_max}',
                                     15, 210, 55)
            navigation_bar.draw_text(self.background, f'Iron mine {self.iron_mine}/{self.iron_mine_max}',
                                     15, 210, 80)
            navigation_bar.draw_text(self.background, f'Sawmill {self.sawmill}/{self.sawmill_max}',
                                     15, 210, 105)
            navigation_bar.draw_text(self.background, f'Fishing {self.fish}/{self.fish_max}',
                                     15, 210, 130)
            navigation_bar.draw_text(self.background, f'Gunsmith {self.gunsmith}/{self.gunsmith_max}',
                                     15, 210, 155)
            navigation_bar.draw_text(self.background, f'Mill {self.mill}/{self.mill_max}',
                                     15, 210, 180)
            navigation_bar.draw_text(self.background, f'Bakery {self.bakery}/{self.bakery_max}',
                                     15, 210, 205)
            navigation_bar.draw_text(self.background, f'Gold melt {self.gold_melt}/{self.gold_melt_max}',
                                     15, 210, 230)
            navigation_bar.draw_text(self.background, f'Blacksmith {self.blacksmith}/{self.blacksmith_max}',
                                     15, 210, 255)
            navigation_bar.draw_text(self.background, f'Iron melt {self.iron_melt}/{self.iron_melt_max}',
                                     15, 210, 280)
            navigation_bar.draw_text(self.background, f'Tailor {self.tailor}/{self.tailor_max}',
                                     15, 210, 305)
            navigation_bar.draw_text(self.background, f'Hunting {self.hunt}/{self.hunt_max}',
                                     15, 210, 330)
            navigation_bar.draw_text(self.background, f'Shipyard {self.shipyard}/{self.shipyard_max}',
                                     15, 210, 355)

        if self.field_minus.pressed or (self.field_minus.held and self.count > 20):
            if self.field > 0:
                self.field = self.field - 1

        elif self.field_plus.pressed or (self.field_plus.held and self.count > 20):
            if unemployed_people > 0 and self.field < self.field_max:
                self.field = self.field + 1

        elif self.gold_mine_minus.pressed or (self.gold_mine_minus.held and self.count > 20):
            if self.gold_mine > 0:
                self.gold_mine = self.gold_mine - 1

        elif self.gold_mine_plus.pressed or (self.gold_mine_plus.held and self.count > 20):
            if unemployed_people > 0 and self.gold_mine < self.gold_mine_max:
                self.gold_mine = self.gold_mine + 1

        elif self.stone_mine_minus.pressed or (self.stone_mine_minus.held and self.count > 20):
            if self.stone_mine > 0:
                self.stone_mine = self.stone_mine - 1

        elif self.stone_mine_plus.pressed or (self.stone_mine_plus.held and self.count > 20):
            if unemployed_people > 0 and self.stone_mine < self.stone_mine_max:
                self.stone_mine = self.stone_mine + 1

        elif self.iron_mine_minus.pressed or (self.iron_mine_minus.held and self.count > 20):
            if self.iron_mine > 0:
                self.iron_mine = self.iron_mine - 1

        elif self.iron_mine_plus.pressed or (self.iron_mine_plus.held and self.count > 20):
            if unemployed_people > 0 and self.iron_mine < self.iron_mine_max:
                self.iron_mine = self.iron_mine + 1

        elif self.sawmill_minus.pressed or (self.sawmill_minus.held and self.count > 20):
            if self.sawmill > 0:
                self.sawmill = self.sawmill - 1

        elif self.sawmill_plus.pressed or (self.sawmill_plus.held and self.count > 20):
            if unemployed_people > 0 and self.sawmill < self.sawmill_max:
                self.sawmill = self.sawmill + 1

        elif self.fishing_minus.pressed or (self.field_minus.held and self.count > 20):
            if self.fish > 0:
                self.fish = self.fish - 1

        elif self.fishing_plus.pressed or (self.field_plus.held and self.count > 20):
            if unemployed_people > 0 and self.fish < self.fish_max:
                self.fish = self.fish + 1

        elif self.gunsmith_minus.pressed or (self.gunsmith_minus.held and self.count > 20):
            if self.gunsmith > 0:
                self.gunsmith = self.gunsmith - 1

        elif self.gunsmith_plus.pressed or (self.gunsmith_plus.held and self.count > 20):
            if unemployed_people > 0 and self.gunsmith < self.gunsmith_max:
                self.gunsmith = self.gunsmith + 1

        elif self.mill_minus.pressed or (self.mill_minus.held and self.count > 20):
            if self.mill > 0:
                self.mill = self.mill - 1

        elif self.mill_plus.pressed or (self.mill_plus.held and self.count > 20):
            if unemployed_people > 0 and self.mill < self.mill_max:
                self.mill = self.mill + 1

        elif self.bakery_minus.pressed or (self.bakery_minus.held and self.count > 20):
            if self.bakery > 0:
                self.bakery = self.bakery - 1

        elif self.bakery_plus.pressed or (self.bakery_plus.held and self.count > 20):
            if unemployed_people > 0 and self.bakery < self.bakery_max:
                self.bakery = self.bakery + 1

        elif self.gold_melt_minus.pressed or (self.gold_melt_minus.held and self.count > 20):
            if self.gold_melt > 0:
                self.gold_melt = self.gold_melt - 1

        elif self.gold_melt_plus.pressed or (self.gold_melt_plus.held and self.count > 20):
            if unemployed_people > 0 and self.gold_melt < self.gold_melt_max:
                self.gold_melt = self.gold_melt + 1

        elif self.blacksmith_minus.pressed or (self.blacksmith_minus.held and self.count > 20):
            if self.blacksmith > 0:
                self.blacksmith = self.blacksmith - 1

        elif self.blacksmith_plus.pressed or (self.blacksmith_plus.held and self.count > 20):
            if unemployed_people > 0 and self.blacksmith < self.blacksmith_max:
                self.blacksmith = self.blacksmith + 1

        elif self.iron_melt_minus.pressed or (self.iron_melt_minus.held and self.count > 20):
            if self.iron_melt > 0:
                self.iron_melt = self.iron_melt - 1

        elif self.iron_melt_plus.pressed or (self.iron_melt_plus.held and self.count > 20):
            if unemployed_people > 0 and self.iron_melt < self.iron_melt_max:
                self.iron_melt = self.iron_melt + 1

        elif self.tailor_minus.pressed or (self.tailor_minus.held and self.count > 20):
            if self.tailor > 0:
                self.tailor = self.tailor - 1

        elif self.tailor_plus.pressed or (self.tailor_plus.held and self.count > 20):
            if unemployed_people > 0 and self.tailor < self.tailor_max:
                self.tailor = self.tailor + 1

        elif self.hunting_minus.pressed or (self.hunting_minus.held and self.count > 20):
            if self.hunt > 0:
                self.hunt = self.hunt - 1

        elif self.hunting_plus.pressed or (self.hunting_plus.held and self.count > 20):
            if unemployed_people > 0 and self.hunt < self.hunt_max:
                self.hunt = self.hunt + 1

        elif self.shipyard_minus.pressed or (self.shipyard_minus.held and self.count > 20):
            if self.shipyard > 0:
                self.shipyard = self.shipyard - 1

        elif self.shipyard_plus.pressed or (self.shipyard_plus.held and self.count > 20):
            if unemployed_people > 0 and self.shipyard < self.shipyard_max:
                self.shipyard = self.shipyard + 1

        if unemployed_people > 0:
            for button in self.buttons:
                button.enable()
        else:
            self.field_plus.disable()
            self.gold_mine_plus.disable()
            self.stone_mine_plus.disable()
            self.iron_mine_plus.disable()
            self.sawmill_plus.disable()
            self.fishing_plus.disable()
            self.mill_plus.disable()
            self.bakery_plus.disable()
            self.gold_melt_plus.disable()
            self.blacksmith_plus.disable()
            self.gunsmith_plus.disable()
            self.iron_melt_plus.disable()
            self.tailor_plus.disable()
            self.hunting_plus.disable()
            self.shipyard_plus.disable()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            self.manager.process_events(event)

    def count_workers(self):
        return (self.field + self.iron_mine + self.gold_mine + self.stone_mine
                + self.sawmill + self.fish +
                self.blacksmith + self.gunsmith + self.mill
                + self.bakery + self.gold_melt + self.iron_melt +
                + self.tailor + self.shipyard + self.hunt)

    def hide_all_workers(self):
        self.background.fill(pygame.Color(43, 43, 43))
        self.text_needed = False
        for element in self.buttons:
            element.hide()

    def show_all_workers(self):
        self.text_needed = True
        for element in self.buttons:
            element.show()
