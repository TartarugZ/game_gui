import pygame
import navigation_bar
import pygame_gui
from gamelogic.config import *
import pyautogui as pg


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
        self.all_army = []
        self.text_needed = True

        self.distance = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((250, 150), (100, 50)),
                                                     text='Archer',
                                                     manager=self.manager)
        self.melee = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((250, 200), (100, 50)),
                                                  text='Swordsman',
                                                  manager=self.manager)
        self.heal = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((250, 250), (100, 50)),
                                                 text='Priest',
                                                 manager=self.manager)
        self.ship_1 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((450, 150), (100, 50)),
                                                   text='Schrooner',
                                                   manager=self.manager)
        self.ship_2 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((450, 200), (100, 50)),
                                                   text='Drakkar',
                                                   manager=self.manager)
        self.ship_3 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((450, 250), (100, 50)),
                                                   text='Caravelle',
                                                   manager=self.manager)
        self.all_army.append(self.distance)
        self.all_army.append(self.melee)
        self.all_army.append(self.heal)
        self.all_army.append(self.ship_1)
        self.all_army.append(self.ship_2)
        self.all_army.append(self.ship_3)

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
                                     f'Army:{self.troops}/{self.max_troops}  Fleet:{self.fleet}/{self.max_fleet}',
                                     40, 400, 30)
            navigation_bar.draw_text(self.background,
                                     f'{self.archer_number}', 30, 150, 160)
            navigation_bar.draw_text(self.background,
                                     f'{self.swordsman_number}', 30, 150, 210)
            navigation_bar.draw_text(self.background,
                                     f'{self.priest_number}', 30, 150, 260)
            navigation_bar.draw_text(self.background,
                                     f'{self.schrooner_number}', 30, 600, 160)
            navigation_bar.draw_text(self.background,
                                     f'{self.drakkar_number}', 30, 600, 210)
            navigation_bar.draw_text(self.background,
                                     f'{self.caravelle_number}', 30, 600, 260)
        if self.troops < self.max_troops:
            for element in range(len(self.all_army)):
                if element < 3:
                    self.all_army[element].enable()
            if self.distance.pressed:
                a = self.game.train_soldiers(1, SOLDIERS[self.distance.text.lower()])
                if not a:
                    pg.alert('You do not have enough resources!', 'Bad news')
            if self.melee.pressed:
                a = self.game.train_soldiers(1, SOLDIERS[self.melee.text.lower()])
                if not a:
                    pg.alert('You do not have enough resources!', 'Bad news')
            if self.heal.pressed:
                a = self.game.train_soldiers(1, SOLDIERS[self.heal.text.lower()])
                if not a:
                    pg.alert('You do not have enough resources!', 'Bad news')
        else:
            for element in range(len(self.all_army)):
                if element < 3:
                    self.all_army[element].disable()

        if self.fleet < self.max_fleet:
            for element in range(len(self.all_army)):
                if element >= 3:
                    self.all_army[element].enable()
            if self.ship_1.pressed:
                a = self.game.train_soldiers(1, SOLDIERS[self.ship_1.text.lower()])
                if not a:
                    pg.alert('You do not have enough resources!', 'Bad news')
            if self.ship_2.pressed:
                a = self.game.train_soldiers(1, SOLDIERS[self.ship_2.text.lower()])
                if not a:
                    pg.alert('You do not have enough resources!', 'Bad news')
            if self.ship_3.pressed:
                a = self.game.train_soldiers(1, SOLDIERS[self.ship_3.text.lower()])
                if not a:
                    pg.alert('You do not have enough resources!', 'Bad news')
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
