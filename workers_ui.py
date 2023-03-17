import navigation_bar
import pygame
import pygame_gui
from gamelogic.config import *


class Workers:
    def __init__(self, manager, background, game):
        self.manager = manager
        self.background = background
        self.game = game
        self.text_needed = True
        self.population = self.game.resources[PEOPLE][COUNT]
        self.buttons = []
        self.count = 0

        self.worker_check()

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


    def worker_check(self):
        self.population = self.game.resources[PEOPLE][COUNT]
        self.field, self.field_max = self.game.workers_in_current_type_building(WHEAT_FIELD)
        self.iron_mine, self.iron_mine_max = self.game.workers_in_current_type_building(IRON_MINE)
        self.gold_mine, self.gold_mine_max = self.game.workers_in_current_type_building(GOLD_MINE)
        self.stone_mine, self.stone_mine_max = self.game.workers_in_current_type_building(STONE_MINE)
        self.sawmill, self.sawmill_max = self.game.workers_in_current_type_building(SAWMILL)
        self.fish, self.fish_max = self.game.workers_in_current_type_building(FISHERMAN)
        self.blacksmith, self.blacksmith_max = self.game.workers_in_current_type_building(BLACKSMITH)
        self.gunsmith, self.gunsmith_max = self.game.workers_in_current_type_building(GUNSMITH)
        self.mill, self.mill_max = self.game.workers_in_current_type_building(MILL)
        self.bakery, self.bakery_max = self.game.workers_in_current_type_building(BAKERY)
        self.gold_melt, self.gold_melt_max = self.game.workers_in_current_type_building(GOLD_MELT)
        self.iron_melt, self.iron_melt_max = self.game.workers_in_current_type_building(IRON_MELT)
        self.tailor, self.tailor_max = self.game.workers_in_current_type_building(TAILOR)
        self.hunt, self.hunt_max = self.game.workers_in_current_type_building(HUNTER)

    def start(self):
        self.worker_check()
        self.population = self.game.resources[PEOPLE][COUNT]
        a = 0
        for button in self.buttons:
            if button.held:
                self.count = self.count + 1
                a = 0
            else:
                a += 1
                if a == 30:
                    self.count = 0
        unemployed_people = self.population

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

        if self.field_minus.pressed or (self.field_minus.held and self.count > 20):
            if self.field > 0:
                self.game.remove_worker(WHEAT_FIELD)

        elif self.field_plus.pressed or (self.field_plus.held and self.count > 20):
            if unemployed_people > 0 and self.field < self.field_max:
                self.game.add_worker(WHEAT_FIELD)

        elif self.gold_mine_minus.pressed or (self.gold_mine_minus.held and self.count > 20):
            if self.gold_mine > 0:
                self.game.remove_worker(GOLD_MINE)

        elif self.gold_mine_plus.pressed or (self.gold_mine_plus.held and self.count > 20):
            if unemployed_people > 0 and self.gold_mine < self.gold_mine_max:
                self.game.add_worker(GOLD_MINE)

        elif self.stone_mine_minus.pressed or (self.stone_mine_minus.held and self.count > 20):
            if self.stone_mine > 0:
                self.game.remove_worker(STONE_MINE)

        elif self.stone_mine_plus.pressed or (self.stone_mine_plus.held and self.count > 20):
            if unemployed_people > 0 and self.stone_mine < self.stone_mine_max:
                self.game.add_worker(STONE_MINE)

        elif self.iron_mine_minus.pressed or (self.iron_mine_minus.held and self.count > 20):
            if self.iron_mine > 0:
                self.game.remove_worker(IRON_MINE)

        elif self.iron_mine_plus.pressed or (self.iron_mine_plus.held and self.count > 20):
            if unemployed_people > 0 and self.iron_mine < self.iron_mine_max:
                self.game.add_worker(IRON_MINE)

        elif self.sawmill_minus.pressed or (self.sawmill_minus.held and self.count > 20):
            if self.sawmill > 0:
                self.game.remove_worker(SAWMILL)

        elif self.sawmill_plus.pressed or (self.sawmill_plus.held and self.count > 20):
            if unemployed_people > 0 and self.sawmill < self.sawmill_max:
                self.game.add_worker(SAWMILL)

        elif self.fishing_minus.pressed or (self.field_minus.held and self.count > 20):
            if self.fish > 0:
                self.game.remove_worker(FISHERMAN)

        elif self.fishing_plus.pressed or (self.field_plus.held and self.count > 20):
            if unemployed_people > 0 and self.fish < self.fish_max:
                self.game.add_worker(FISHERMAN)

        elif self.gunsmith_minus.pressed or (self.gunsmith_minus.held and self.count > 20):
            if self.gunsmith > 0:
                self.game.remove_worker(GUNSMITH)

        elif self.gunsmith_plus.pressed or (self.gunsmith_plus.held and self.count > 20):
            if unemployed_people > 0 and self.gunsmith < self.gunsmith_max:
                self.game.add_worker(GUNSMITH)

        elif self.mill_minus.pressed or (self.mill_minus.held and self.count > 20):
            if self.mill > 0:
                self.game.remove_worker(MILL)

        elif self.mill_plus.pressed or (self.mill_plus.held and self.count > 20):
            if unemployed_people > 0 and self.mill < self.mill_max:
                self.game.add_worker(MILL)

        elif self.bakery_minus.pressed or (self.bakery_minus.held and self.count > 20):
            if self.bakery > 0:
                self.game.remove_worker(BAKERY)

        elif self.bakery_plus.pressed or (self.bakery_plus.held and self.count > 20):
            if unemployed_people > 0 and self.bakery < self.bakery_max:
                self.game.add_worker(BAKERY)

        elif self.gold_melt_minus.pressed or (self.gold_melt_minus.held and self.count > 20):
            if self.gold_melt > 0:
                self.game.remove_worker(GOLD_MELT)

        elif self.gold_melt_plus.pressed or (self.gold_melt_plus.held and self.count > 20):
            if unemployed_people > 0 and self.gold_melt < self.gold_melt_max:
                self.game.add_worker(GOLD_MELT)

        elif self.blacksmith_minus.pressed or (self.blacksmith_minus.held and self.count > 20):
            if self.blacksmith > 0:
                self.game.remove_worker(BLACKSMITH)

        elif self.blacksmith_plus.pressed or (self.blacksmith_plus.held and self.count > 20):
            if unemployed_people > 0 and self.blacksmith < self.blacksmith_max:
                self.game.add_worker(BLACKSMITH)

        elif self.iron_melt_minus.pressed or (self.iron_melt_minus.held and self.count > 20):
            if self.iron_melt > 0:
                self.game.remove_worker(IRON_MELT)

        elif self.iron_melt_plus.pressed or (self.iron_melt_plus.held and self.count > 20):
            if unemployed_people > 0 and self.iron_melt < self.iron_melt_max:
                self.game.add_worker(IRON_MELT)

        elif self.tailor_minus.pressed or (self.tailor_minus.held and self.count > 20):
            if self.tailor > 0:
                self.game.remove_worker(TAILOR)

        elif self.tailor_plus.pressed or (self.tailor_plus.held and self.count > 20):
            if unemployed_people > 0 and self.tailor < self.tailor_max:
                self.game.add_worker(TAILOR)

        elif self.hunting_minus.pressed or (self.hunting_minus.held and self.count > 20):
            if self.hunt > 0:
                self.game.remove_worker(HUNTER)

        elif self.hunting_plus.pressed or (self.hunting_plus.held and self.count > 20):
            if unemployed_people > 0 and self.hunt < self.hunt_max:
                self.game.add_worker(HUNTER)


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

    def hide_all_workers(self):
        self.background.fill(pygame.Color(43, 43, 43))
        self.text_needed = False
        for element in self.buttons:
            element.hide()

    def show_all_workers(self):
        self.text_needed = True
        for element in self.buttons:
            element.show()
