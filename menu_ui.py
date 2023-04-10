import random
from os import listdir
from os.path import isfile, join

import pygame
import pygame_gui

import gamelogic.config
import navigation_bar
import settings_ui
from gamelogic.config import *


class Menu:
    def __init__(self, manager, background, window_surface):
        pygame.init()
        music = ['music/menu/' + g for g in listdir("music/menu") if
                 isfile(join("music/menu", g)) and g.endswith('.mp3' or '.wav')]
        self.window_surface = window_surface
        self.text_needed = True
        self.is_running = True
        self.manager = manager
        self.playlist = music
        self.playlist_original = music.copy()
        self.background = background
        self.buttons = []
        self.settings = settings_ui.Settings(self.manager, self.background, True)
        self.settings.hide_all_settings()
        self.sh_settings = False
        self.code_sent_1 = False
        self.forgot_send = False
        self.code_sent_2 = False
        self.pg_elem = []
        self.username = 'Not logged in'
        self.image = pygame.image.load('img/menu.png')

        pygame.mixer.pre_init(44100, -16, 2, 2048)
        pygame.mixer.music.load(self.playlist[0])
        self.playlist.pop(0)
        pygame.mixer.music.play()
        pygame.mixer.music.queue(self.playlist[0])
        self.playlist.pop(0)
        pygame.mixer.music.set_volume(VOLUME)
        pygame.mixer.music.set_endevent(pygame.KEYUP)

        self.new_game_btn = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((100, 130), (200, 70)),
                                                         text='New game',
                                                         manager=self.manager)
        self.load_game_btn = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((100, 230), (200, 70)),
                                                          text='Load game',
                                                          manager=self.manager)
        self.settings_btn = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((100, 330), (200, 70)),
                                                         text='Settings',
                                                         manager=self.manager)
        self.exit_btn = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((100, 430), (200, 70)),
                                                     text='Exit',
                                                     manager=self.manager)
        self.menu_png = pygame_gui.elements.UIImage(relative_rect=pygame.Rect((270, 50), (660, 512)),
                                                    manager=self.manager, image_surface=self.image)
        self.login = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((600, 550), (90, 50)),
                                                  text='Login',
                                                  manager=self.manager)
        self.register = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((700, 550), (90, 50)),
                                                     text='Register',
                                                     manager=self.manager)
        self.forgot_password = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((125, 410), (150, 30)),
                                                            text='Forgot password?',
                                                            manager=self.manager)
        self.back_to_menu = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((200, 550), (90, 50)),
                                                         text='Back',
                                                         manager=self.manager)
        self.email_field = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((100, 180), (200, 40)),
                                                               placeholder_text='Enter email',
                                                               manager=self.manager)
        self.password_field = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((100, 250), (200, 40)),
                                                                  placeholder_text='Enter password',
                                                                  manager=self.manager)
        self.code = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((100, 300), (200, 40)),
                                                        placeholder_text='Enter code',
                                                        manager=self.manager)
        self.login_final = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((150, 350), (120, 50)),
                                                        text='Login',
                                                        manager=self.manager)
        self.save_1 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((150, 180), (100, 50)),
                                                   text='',
                                                   manager=self.manager)
        self.save_2 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((150, 280), (100, 50)),
                                                   text='',
                                                   manager=self.manager)
        self.save_3 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((150, 380), (100, 50)),
                                                   text='',
                                                   manager=self.manager)

        self.password_field.set_text_hidden(True)
        self.hide_login()
        self.hide_saves()
        self.code.hide()
        self.forgot_password.hide()
        self.pg_elem.append(self.new_game_btn)
        self.pg_elem.append(self.settings_btn)
        self.pg_elem.append(self.load_game_btn)
        self.pg_elem.append(self.exit_btn)
        self.pg_elem.append(self.menu_png)
        self.pg_elem.append(self.login)
        self.pg_elem.append(self.register)
        clock = pygame.time.Clock()
        while self.is_running:
            pygame.mixer.music.set_volume(gamelogic.config.VOLUME)
            time_delta = clock.tick(60) / 1000.0
            self.background.fill(pygame.Color(43, 43, 43))

            self.background.fill(pygame.Color(43, 43, 43))
            if self.login.pressed:
                self.code_sent_1 = False
                self.code.hide()
                self.forgot_password.show()
                self.login.disable()
                self.register.enable()
                self.login_final.set_text('Login')
                self.show_registration_fields()
            if self.register.pressed:
                self.register.disable()
                self.forgot_password.hide()
                self.code.hide()
                self.forgot_send = False
                self.code_sent_2 = False
                self.login.enable()
                self.login_final.set_text('Register')
                self.show_registration_fields()
            if self.back_to_menu.pressed:
                self.code_sent_1 = False
                self.forgot_send = False
                self.code_sent_2 = False
                self.code.hide()
                self.hide_saves()
                self.forgot_password.hide()
                self.login.enable()
                self.register.enable()
                self.hide_login()
                self.show_all_menu()
            if self.load_game_btn.pressed:
                self.show_saves()
            if self.save_1.pressed:
                pass
            if self.save_2.pressed:
                pass
            if self.save_3.pressed:
                pass

            if self.login_final.pressed:
                if not self.login.is_enabled and not self.forgot_send and not self.code_sent_2:
                    print("login")
                    self.username = 'gg'
                    pass
                elif not self.register.is_enabled and not self.code_sent_1:
                    print("Register")
                    self.code.show()
                    self.login_final.set_text('Send code')
                    self.code_sent_1 = True
                    pass
                elif self.code_sent_1:
                    print("enter reg code")
                    pass
                elif self.forgot_send and not self.code_sent_2:
                    print('send email')
                    self.login_final.set_text('Send code')
                    self.code_sent_2 = True
                    self.code.show()
                    pass
                elif self.code_sent_2:
                    print("enter forgot code")
                    pass
            if self.forgot_password.pressed:
                self.password_field.hide()
                self.forgot_password.hide()
                self.login_final.set_text('Receive code')
                self.forgot_send = True

            if self.text_needed:
                navigation_bar.draw_text(self.background, "Welcome to the <BUILD ON FIELD>", 40, 400, 30)
                navigation_bar.draw_text(self.background, f'{self.username}', 20, 500, 565)
            if not pygame.mixer.music.get_busy():
                self.playlist = self.playlist_original.copy()
                pygame.mixer.music.load(self.playlist[0])
                self.playlist.pop(0)
                pygame.mixer.music.play()
                pygame.mixer.music.queue(self.playlist[0])
                self.playlist.pop(0)
            for event in pygame.event.get():
                if event.type == pygame.KEYUP:
                    print(self.playlist)
                    if len(self.playlist) > 0:
                        pygame.mixer.music.queue(self.playlist[0])
                        self.playlist.pop(0)
                    else:
                        self.playlist = self.playlist_original.copy()
                        pygame.mixer.music.queue(self.playlist[0])
                        self.playlist.pop(0)
                if event.type == pygame.QUIT:
                    exit()
                self.manager.process_events(event)

            if self.new_game_btn.pressed:
                pygame.mixer.music.stop()
                self.is_running = False
            if self.settings_btn.pressed:
                self.hide_all_menu()
                self.settings.show_all_settings()
                self.sh_settings = True
            if self.exit_btn.pressed:
                exit()
            if self.settings.back_btn.pressed:
                self.sh_settings = False
                self.settings.hide_all_settings()
                self.show_all_menu()
            if self.sh_settings:
                self.settings.start()

            self.manager.update(time_delta)
            self.window_surface.blit(self.background, (0, 0))
            self.manager.draw_ui(self.window_surface)
            pygame.display.update()

    def hide_all_menu(self):
        self.background.fill(pygame.Color(43, 43, 43))
        self.text_needed = False
        self.hide_login()
        for element in self.pg_elem:
            element.hide()

    def show_all_menu(self):
        self.text_needed = True
        for element in self.pg_elem:
            element.show()

    def hide_login(self):
        self.email_field.hide()
        self.password_field.hide()
        self.back_to_menu.hide()
        self.login_final.hide()

    def show_registration_fields(self):
        self.new_game_btn.hide()
        self.settings_btn.hide()
        self.load_game_btn.hide()
        self.exit_btn.hide()
        self.back_to_menu.show()
        self.email_field.show()
        self.password_field.show()
        self.back_to_menu.show()
        self.login_final.show()

    def show_saves(self):
        self.new_game_btn.hide()
        self.settings_btn.hide()
        self.load_game_btn.hide()
        self.exit_btn.hide()
        self.back_to_menu.show()
        self.save_1.show()
        self.save_2.show()
        self.save_3.show()

    def hide_saves(self):
        self.save_1.hide()
        self.save_2.hide()
        self.save_3.hide()
