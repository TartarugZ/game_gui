import pygame
import pygame_gui
import navigation_bar
from gamelogic.config import *
import pyautogui as pg


class World:
    def __init__(self, manager, background, game):
        self.game = game
        self.manager = manager
        self.background = background
        self.all_world = []
        self.text_needed = True
        self.color_easy = False
        self.color_medium = False
        self.color_hard = False
        self.exp_easy = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((420, 145), (200, 50)),
                                                     text='Start',
                                                     manager=self.manager)
        self.exp_normal = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((420, 285), (200, 50)),
                                                       text='Start',
                                                       manager=self.manager)
        self.exp_hard = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((420, 425), (200, 50)),
                                                     text='Start',
                                                     manager=self.manager)
        self.all_world.append(self.exp_easy)
        self.all_world.append(self.exp_normal)
        self.all_world.append(self.exp_hard)

    def start(self):
        if self.text_needed:
            # 1 vertical
            pygame.draw.line(self.background, (255, 255, 255),
                             [30, 60],
                             [30, 480], 2)
            # 2
            pygame.draw.line(self.background, (255, 255, 255),
                             [770, 60],
                             [770, 480], 2)
            # 1 horizontal
            pygame.draw.line(self.background, (255, 255, 255),
                             [30, 60],
                             [770, 60], 2)
            # 2
            pygame.draw.line(self.background, (255, 255, 255),
                             [30, 200],
                             [770, 200], 2)
            # 3
            pygame.draw.line(self.background, (255, 255, 255),
                             [30, 340],
                             [770, 340], 2)
            # 4
            pygame.draw.line(self.background, (255, 255, 255),
                             [30, 480],
                             [770, 480], 2)
            navigation_bar.draw_text(self.background, "Expeditions", 40, 400, 10)
            navigation_bar.draw_text_left(self.background, "Easy expedition", 22, 77, 110)
            navigation_bar.draw_text_left(self.background, "Medium expedition", 22, 77, 250)
            navigation_bar.draw_text_left(self.background, "Hard expedition", 22, 77, 390)
            a = str(self.game.expedition[1][RESOURCES_CREATE])[1:-1].replace('\'', ' ')
            navigation_bar.draw_text_left(self.background, "You get →{name}".format(name=a), 22, 76, 160)
            a = str(self.game.expedition[2][RESOURCES_CREATE])[1:-1].replace('\'', ' ')
            navigation_bar.draw_text_left(self.background, "You get →{name}".format(name=a), 22, 76, 300)
            a = str(self.game.expedition[3][RESOURCES_CREATE])[1:-1].replace('\'', ' ')
            navigation_bar.draw_text_left(self.background, "You get →{name}".format(name=a), 22, 76, 440)

            a = str(self.game.expedition[1][COST])[1:-1].replace('\'', ' ')
            if self.color_easy:
                navigation_bar.draw_text(self.background, "{name}".format(name=a), 22, 520, 110,
                                              colour=(188, 30, 30))
            else:
                navigation_bar.draw_text(self.background, "{name}".format(name=a), 22, 520, 110)
            a = str(self.game.expedition[2][COST])[1:-1].replace('\'', ' ')
            if self.color_medium:
                navigation_bar.draw_text(self.background, "{name}".format(name=a), 22, 520, 250,
                                              colour=(188, 30, 30))
            else:
                navigation_bar.draw_text(self.background, "{name}".format(name=a), 22, 520, 250)
            a = str(self.game.expedition[3][COST])[1:-1].replace('\'', ' ')
            if self.color_hard:
                navigation_bar.draw_text(self.background, "{name}".format(name=a), 22, 520, 390,
                                              colour=(188, 30, 30))
            else:
                navigation_bar.draw_text(self.background, "{name}".format(name=a), 22, 520, 390)

        if not self.game.check_expedition(1):
            self.color_easy = True
        else:
            self.color_easy = False
        if not self.game.check_expedition(2):
            self.color_medium = True
        else:
            self.color_medium = False
        if not self.game.check_expedition(3):
            self.color_hard = True
        else:
            self.color_hard = False

        if self.exp_easy.pressed:
            self.game.start_expedition(1)

        if self.exp_normal.pressed:
            self.game.start_expedition(2)

        if self.exp_hard.pressed:
            self.game.start_expedition(3)

    def hide_all_world(self):
        self.background.fill(pygame.Color(43, 43, 43))
        self.text_needed = False
        for element in self.all_world:
            element.hide()

    def show_all_world(self):
        self.text_needed = True
        for element in self.all_world:
            element.show()
