import pygame
import navigation_bar
import pygame_gui
from gamelogic.config import *


class Army:

    def __init__(self, manager, background, game):
        self.game = game
        self.manager = manager
        self.background = background
        self.troops = self.game.army[SWORDSMAN][COUNT] + self.game.army[ARCHER][COUNT] + self.game.army[PRIEST][COUNT]
        self.fleet = self.game.army[SCHROONER][COUNT] + self.game.army[DRAKKAR][COUNT] + self.game.army[CARAVELLE][
            COUNT]
        self.max_troops = self.game.army[SWORDSMAN][MAX]
        self.max_fleet = self.game.army[SCHROONER][MAX]
        self.archer_number = self.game.army[ARCHER][COUNT]
        self.swordsman_number = self.game.army[SWORDSMAN][COUNT]
        self.priest_number = self.game.army[PRIEST][COUNT]
        self.schrooner_number = self.game.army[SCHROONER][COUNT]
        self.drakkar_number = self.game.army[DRAKKAR][COUNT]
        self.caravelle_number = self.game.army[CARAVELLE][COUNT]
        self.color_distance = False
        self.color_melee = False
        self.color_heal = False
        self.color_ship1 = False
        self.color_ship2 = False
        self.color_ship3 = False
        self.all_army = []
        self.text_needed = True

        self.distance = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((150, 110), (100, 50)),
                                                     text='Archer',
                                                     manager=self.manager)
        self.melee = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((150, 250), (100, 50)),
                                                  text='Swordsman',
                                                  manager=self.manager)
        self.heal = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((150, 390), (100, 50)),
                                                 text='Priest',
                                                 manager=self.manager)
        self.ship_1 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((542, 110), (100, 50)),
                                                   text='Schrooner',
                                                   manager=self.manager)
        self.ship_2 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((542, 250), (100, 50)),
                                                   text='Drakkar',
                                                   manager=self.manager)
        self.ship_3 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((542, 390), (100, 50)),
                                                   text='Caravelle',
                                                   manager=self.manager)
        # self.up_dist = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((300, 110), (50, 50)),
        #                                              text='↑',
        #                                              manager=self.manager)
        # self.up_melee = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((300, 250), (50, 50)),
        #                                           text='↑',
        #                                           manager=self.manager)
        # self.up_heal = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((300, 390), (50, 50)),
        #                                          text='↑',
        #                                          manager=self.manager)
        # self.up_ship1 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((692, 110), (50, 50)),
        #                                            text='↑',
        #                                            manager=self.manager)
        # self.up_ship2 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((692, 250), (50, 50)),
        #                                            text='↑',
        #                                            manager=self.manager)
        # self.up_ship3 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((692, 390), (50, 50)),
        #                                            text='↑',
        #                                            manager=self.manager)
        self.all_army.append(self.distance)
        self.all_army.append(self.melee)
        self.all_army.append(self.heal)
        self.all_army.append(self.ship_1)
        self.all_army.append(self.ship_2)
        self.all_army.append(self.ship_3)
        # self.all_army.append(self.up_dist)
        # self.all_army.append(self.up_melee)
        # self.all_army.append(self.up_heal)
        # self.all_army.append(self.up_ship1)
        # self.all_army.append(self.up_ship2)
        # self.all_army.append(self.up_ship3)

    def start(self):
        self.troops = self.game.army[SWORDSMAN][COUNT] + self.game.army[ARCHER][COUNT] + self.game.army[PRIEST][COUNT]
        self.fleet = self.game.army[SCHROONER][COUNT] + self.game.army[DRAKKAR][COUNT] + self.game.army[CARAVELLE][
            COUNT]
        self.max_troops = self.game.army[SWORDSMAN][MAX]
        self.max_fleet = self.game.army[SCHROONER][MAX]
        self.archer_number = self.game.army[ARCHER][COUNT]
        self.swordsman_number = self.game.army[SWORDSMAN][COUNT]
        self.priest_number = self.game.army[PRIEST][COUNT]
        self.schrooner_number = self.game.army[SCHROONER][COUNT]
        self.drakkar_number = self.game.army[DRAKKAR][COUNT]
        self.caravelle_number = self.game.army[CARAVELLE][COUNT]
        self.background.fill(pygame.Color(43, 43, 43))
        if self.text_needed:
            navigation_bar.draw_text(self.background,
                                     f'Army: {self.troops}/{self.max_troops}',
                                     40, 200, 10)
            navigation_bar.draw_text(self.background,
                                     f'Fleet:{self.fleet}/{self.max_fleet}',
                                     40, 600, 10)
            navigation_bar.draw_text(self.background,
                                     f'You have {self.archer_number}', 22, 200, 80)
            navigation_bar.draw_text(self.background,
                                     f'You have {self.swordsman_number}', 22, 200, 220)
            navigation_bar.draw_text(self.background,
                                     f'You have {self.priest_number}', 22, 200, 360)
            navigation_bar.draw_text(self.background,
                                     f'You have {self.schrooner_number}', 22, 592, 80)
            navigation_bar.draw_text(self.background,
                                     f'You have {self.drakkar_number}', 22, 592, 220)
            navigation_bar.draw_text(self.background,
                                     f'You have {self.caravelle_number}', 22, 592, 360)

            a = str(self.game.army[ARCHER][COST])[1:-1].replace('\'', ' ')
            if self.color_distance:
                navigation_bar.draw_text(self.background,
                                         f'{a}', 22, 200, 165, colour=(188, 30, 30))
            else:
                navigation_bar.draw_text(self.background,
                                         f'{a}', 22, 200, 165)
            a = str(self.game.army[SWORDSMAN][COST])[1:-1].replace('\'', ' ')
            if self.color_melee:
                navigation_bar.draw_text(self.background,
                                         f'{a}', 22, 200, 305, colour=(188, 30, 30))
            else:
                navigation_bar.draw_text(self.background,
                                         f'{a}', 22, 200, 305)
            a = str(self.game.army[PRIEST][COST])[1:-1].replace('\'', ' ')
            if self.color_heal:
                navigation_bar.draw_text(self.background,
                                         f'{a}', 22, 200, 445, colour=(188, 30, 30))
            else:
                navigation_bar.draw_text(self.background,
                                         f'{a}', 22, 200, 445)
            a = str(self.game.army[SCHROONER][COST])[1:-1].replace('\'', ' ')
            if self.color_ship1:
                navigation_bar.draw_text(self.background,
                                         f'{a}', 22, 592, 165, colour=(188, 30, 30))
            else:
                navigation_bar.draw_text(self.background,
                                         f'{a}', 22, 592, 165)
            a = str(self.game.army[DRAKKAR][COST])[1:-1].replace('\'', ' ')
            if self.color_ship2:
                navigation_bar.draw_text(self.background,
                                         f'{a}', 22, 592, 305, colour=(188, 30, 30))
            else:
                navigation_bar.draw_text(self.background,
                                         f'{a}', 22, 592, 305)
            a = str(self.game.army[CARAVELLE][COST])[1:-1].replace('\'', ' ')
            if self.color_ship3:
                navigation_bar.draw_text(self.background,
                                         f'{a}', 22, 592, 445, colour=(188, 30, 30))
            else:
                navigation_bar.draw_text(self.background,
                                         f'{a}', 22, 592, 445)
            # 1 vertical
            pygame.draw.line(self.background, (255, 255, 255),
                             [20, 60],
                             [20, 480], 2)
            # 2
            pygame.draw.line(self.background, (255, 255, 255),
                             [380, 60],
                             [380, 480], 2)
            # 1 horizontal
            pygame.draw.line(self.background, (255, 255, 255),
                             [20, 60],
                             [380, 60], 2)
            # 2
            pygame.draw.line(self.background, (255, 255, 255),
                             [20, 200],
                             [380, 200], 2)
            # 3
            pygame.draw.line(self.background, (255, 255, 255),
                             [20, 340],
                             [380, 340], 2)
            # 4
            pygame.draw.line(self.background, (255, 255, 255),
                             [20, 480],
                             [380, 480], 2)

            # 1 vertical
            pygame.draw.line(self.background, (255, 255, 255),
                             [390, 60],
                             [390, 480], 2)
            # 2
            pygame.draw.line(self.background, (255, 255, 255),
                             [780, 60],
                             [780, 480], 2)
            # 1 horizontal
            pygame.draw.line(self.background, (255, 255, 255),
                             [390, 60],
                             [780, 60], 2)
            # 2
            pygame.draw.line(self.background, (255, 255, 255),
                             [390, 200],
                             [780, 200], 2)
            # 3
            pygame.draw.line(self.background, (255, 255, 255),
                             [390, 340],
                             [780, 340], 2)
            # 4
            pygame.draw.line(self.background, (255, 255, 255),
                             [390, 480],
                             [780, 480], 2)

        if not self.game.check_soldiers(SOLDIERS[self.distance.text.lower()]):
            self.color_distance = True
        else:
            self.color_distance = False
        if not self.game.check_soldiers(SOLDIERS[self.melee.text.lower()]):
            self.color_melee = True
        else:
            self.color_melee = False
        if not self.game.check_soldiers(SOLDIERS[self.heal.text.lower()]):
            self.color_heal = True
        else:
            self.color_heal = False
        if not self.game.check_soldiers(SOLDIERS[self.ship_1.text.lower()]):
            self.color_ship_1 = True
        else:
            self.color_ship_1 = False
        if not self.game.check_soldiers(SOLDIERS[self.ship_2.text.lower()]):
            self.color_ship_2 = True
        else:
            self.color_ship_2 = False
        if not self.game.check_soldiers(SOLDIERS[self.ship_3.text.lower()]):
            self.color_ship_3 = True
        else:
            self.color_ship_3 = False

        if self.troops < self.max_troops:
            for element in range(len(self.all_army)):
                if element < 3:
                    self.all_army[element].enable()
            if self.distance.pressed:
                self.game.train_soldiers(1, SOLDIERS[self.distance.text.lower()])
            if self.melee.pressed:
                self.game.train_soldiers(1, SOLDIERS[self.melee.text.lower()])
            if self.heal.pressed:
                self.game.train_soldiers(1, SOLDIERS[self.heal.text.lower()])

        else:
            for element in range(len(self.all_army)):
                if element < 3:
                    self.all_army[element].disable()

        if self.fleet < self.max_fleet:
            for element in range(len(self.all_army)):
                if element >= 3:
                    self.all_army[element].enable()
            if self.ship_1.pressed:
                self.game.train_soldiers(1, SOLDIERS[self.ship_1.text.lower()])
            if self.ship_2.pressed:
                self.game.train_soldiers(1, SOLDIERS[self.ship_2.text.lower()])
            if self.ship_3.pressed:
                self.game.train_soldiers(1, SOLDIERS[self.ship_3.text.lower()])

        else:
            for element in range(len(self.all_army)):
                if element >= 3:
                    self.all_army[element].disable()

    def hide_all_army(self):
        self.background.fill(pygame.Color(43, 43, 43))
        self.text_needed = False
        for element in self.all_army:
            element.hide()

    def show_all_army(self):
        self.text_needed = True
        for element in self.all_army:
            element.show()
