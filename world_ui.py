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
        self.exp_easy = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((200, 150), (200, 50)),
                                                     text='Easy Expedition',
                                                     manager=self.manager)
        self.exp_normal = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((200, 200), (200, 50)),
                                                       text='Normal Expedition',
                                                       manager=self.manager)
        self.exp_hard = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((200, 250), (200, 50)),
                                                     text='Hard Expedition',
                                                     manager=self.manager)
        self.all_world.append(self.exp_easy)
        self.all_world.append(self.exp_normal)
        self.all_world.append(self.exp_hard)

    def start(self):
        if self.text_needed:
            navigation_bar.draw_text(self.background, "Expeditions", 30, 400, 20)
            navigation_bar.draw_text(self.background, "{name}".format(name=str(self.game.expedition[1][RESOURCES_CREATE])[1:-1].replace('\'','')), 20, 500, 160)
            navigation_bar.draw_text(self.background, "{name}".format(name=str(self.game.expedition[2][RESOURCES_CREATE])[1:-1].replace('\'','')), 20, 500, 210)
            navigation_bar.draw_text(self.background, "{name}".format(name=str(self.game.expedition[3][RESOURCES_CREATE])[1:-1].replace('\'','')), 20, 500, 260)

        if self.exp_easy.pressed:
            a = self.game.start_expedition(1)
            if not a:
                pg.alert('You do not have enough resources!', 'Bad news')
        if self.exp_normal.pressed:
            a = self.game.start_expedition(2)
            if not a:
                pg.alert('You do not have enough resources!', 'Bad news')
        if self.exp_hard.pressed:
            a = self.game.start_expedition(3)
            if not a:
                pg.alert('You do not have enough resources!', 'Bad news')

    def hide_all_world(self):
        self.background.fill(pygame.Color(43, 43, 43))
        self.text_needed = False
        for element in self.all_world:
            element.hide()

    def show_all_world(self):
        self.text_needed = True
        for element in self.all_world:
            element.show()
