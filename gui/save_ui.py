import datetime
import time
from os.path import isdir, join
from os import listdir
import pygame
import pygame_gui

import gamelogic.config
from gui import navigation_bar


class Save:
    def __init__(self, manager, background, back, game, menu):
        self.manager = manager
        self.background = background
        self.back = back
        self.game = game
        self.menu = menu
        self.server_saves = []
        self.local_saves = [g for g in listdir("save") if isdir(join("save", g)) and 'autosave' not in g]
        self.text_needed = True
        self.last_tick = pygame.time.get_ticks()

        self.cloud_save_1 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((170, 100), (200, 50)),
                                                         text='Empty',
                                                         manager=self.manager)
        self.cloud_save_2 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((170, 200), (200, 50)),
                                                         text='Empty',
                                                         manager=self.manager)
        self.cloud_save_3 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((170, 300), (200, 50)),
                                                         text='Empty',
                                                         manager=self.manager)
        self.local_save_1 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((430, 100), (200, 50)),
                                                         text='Empty',
                                                         manager=self.manager)
        self.local_save_2 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((430, 200), (200, 50)),
                                                         text='Empty',
                                                         manager=self.manager)
        self.local_save_3 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((430, 300), (200, 50)),
                                                         text='Empty',
                                                         manager=self.manager)
        self.autosave = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((250, 400), (300, 50)),
                                                     text='Autosave',
                                                     manager=self.manager)

        self.autosave.set_text(''.join(g for g in listdir("save") if isdir(join("save", g)) and 'autosave' in g))
        if not self.back:
            self.autosave.disable()
        self.back_btn = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 0), (100, 50)),
                                                     text='Back',
                                                     manager=self.manager)

        self.load_but = [self.local_save_1, self.local_save_2, self.local_save_3, self.cloud_save_1, self.cloud_save_2,
                         self.cloud_save_3, self.autosave]

    def start(self):
        cooldown = 5000
        now = pygame.time.get_ticks()
        if now - self.last_tick >= cooldown:
            self.last_tick = now
            self.server_saves = self.menu.load_server_saves()
        self.background.fill(pygame.Color(43, 43, 43))
        if not self.back:
            self.back_btn.hide()

        if self.text_needed:
            navigation_bar.draw_text(self.background, "Server saves", 30, 270, 50)
            navigation_bar.draw_text(self.background, "Local saves", 30, 530, 50)

        self.local_saves = [g for g in listdir("save") if isdir(join("save", g)) and 'autosave' not in g]
        if 'save_1' in ''.join(g for g in listdir("save") if isdir(join("save", g)) and 'save_1' in g):
            self.local_save_1.set_text('save_1')
        if 'save_2' in ''.join(g for g in listdir("save") if isdir(join("save", g)) and 'save_2' in g):
            self.local_save_2.set_text('save_2')
        if 'save_3' in ''.join(g for g in listdir("save") if isdir(join("save", g)) and 'save_3' in g):
            self.local_save_3.set_text('save_3')
        try:
            if len(self.server_saves) > 0:
                for i in self.server_saves:
                    if i['game_id'] == 1:
                        self.cloud_save_1.set_text(i['game_name'])
                    elif i['game_id'] == 2:
                        self.cloud_save_2.set_text(i['game_name'])
                    elif i['game_id'] == 3:
                        self.cloud_save_3.set_text(i['game_name'])
        except Exception:
            pass

        a = ''.join(g for g in listdir("save") if isdir(join("save", g)) and 'autosave' in g)
        if a != '':
            self.autosave.set_text(a)
        else:
            self.autosave.set_text('No Autosave')
        if self.back:  # load
            for i in self.load_but:
                if i.text == 'Empty':
                    i.disable()
                else:
                    i.enable()
            if self.local_save_1.pressed:
                self.game.local_load(self.local_save_1.text)
                self.back_btn.pressed_event = True
                self.menu.start_game()
            elif self.local_save_2.pressed:
                self.game.local_load(self.local_save_2.text)
                self.back_btn.pressed_event = True
                self.menu.start_game()
            elif self.local_save_3.pressed:
                self.game.local_load(self.local_save_3.text)
                self.back_btn.pressed_event = True
                self.menu.start_game()
            elif self.cloud_save_1.pressed:
                self.menu.load_server(1)
                self.back_btn.pressed_event = True
                self.menu.start_game()
            elif self.cloud_save_2.pressed:
                self.menu.load_server(2)
                self.back_btn.pressed_event = True
                self.menu.start_game()
            elif self.cloud_save_3.pressed:
                self.menu.load_server(3)
                self.back_btn.pressed_event = True
                self.menu.start_game()
        else:  # save
            if self.local_save_1.pressed:
                self.game.local_save('save_1')
            elif self.local_save_2.pressed:
                self.game.local_save('save_2')
            elif self.local_save_3.pressed:
                self.game.local_save('save_3')
            elif self.cloud_save_1.pressed:
                self.menu.save_server(1, 'save_1' + str(datetime.datetime.now().strftime("%Y-%m-%d %Hh %Mm")))
            elif self.cloud_save_2.pressed:
                self.menu.save_server(2, 'save_2' + str(datetime.datetime.now().strftime("%Y-%m-%d %Hh %Mm")))
            elif self.cloud_save_3.pressed:
                self.menu.save_server(3, 'save_3' + str(datetime.datetime.now().strftime("%Y-%m-%d %Hh %Mm")))

    def hide_all_save(self):
        self.background.fill(pygame.Color(43, 43, 43))
        self.cloud_save_1.hide()
        self.cloud_save_2.hide()
        self.cloud_save_3.hide()
        self.local_save_1.hide()
        self.local_save_2.hide()
        self.local_save_3.hide()
        self.autosave.hide()
        self.back_btn.hide()

    def show_all_save(self):
        self.cloud_save_1.show()
        self.cloud_save_2.show()
        self.cloud_save_3.show()
        self.local_save_1.show()
        self.local_save_2.show()
        self.local_save_3.show()
        self.autosave.show()
        self.back_btn.show()
