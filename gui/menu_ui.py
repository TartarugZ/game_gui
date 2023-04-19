import os
from pathlib import Path
import pygame
import pygame_gui

from gui import save_ui
from gui import windows_control
from gui import navigation_bar
from gui import settings_ui
from gui import music_control
from gamelogic.network import Network
from gamelogic.network_error import *
import gamelogic.config
import gamelogic.game


#  TODO ui restrictions when sending information, autosave button load save, show army queue, check server down
class Menu:
    def __init__(self):
        pygame.init()
        self.window_surface = pygame.display.set_mode((800, 600))
        self.background = pygame.Surface((800, 600))
        self.background.fill(pygame.Color(43, 43, 43))
        pygame.display.set_caption("Build on Field")
        self.manager = pygame_gui.UIManager(pygame.display.get_window_size(),
                                            str(Path(Path.cwd(), 'resources', 'theme.json')))
        icon = pygame.image.load(os.path.abspath(os.curdir) + '/resources/img/f5.png')
        pygame.display.set_icon(icon)

        self.is_running = True
        self.text_needed = True
        self.show_settings = False
        self.show_saves = False
        self.code_sent_reg = False
        self.forgot_send = False
        self.code_sent_forgot = False

        self.buttons = []
        self.gui_elements = []
        self.forbidden_characters = [':', '/', '?', '#', '[', ']', '!', '$', '&', '\'', '(', ')', '*', ';', '=']

        self.network = gamelogic.network.Network()
        self.music = music_control.Music()
        self.game = gamelogic.game.Game(self.background)
        self.settings = settings_ui.Settings(self.manager, self.background, True)
        self.save = save_ui.Save(self.manager, self.background, True, self.game, menu=self)

        self.settings.hide_all_settings()
        self.save.hide_all_save()
        self.username = 'Not logged in'
        self.image = pygame.image.load('./resources/img/menu.png')

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
        self.back_to_menu = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((10, 550), (120, 50)),
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
        self.login_final = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((140, 350), (120, 50)),
                                                        text='Login',
                                                        manager=self.manager)
        self.exception_label = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((0, 510), (720, 50)),
                                                           text='',
                                                           manager=self.manager)
        self.exception_label.text_horiz_alignment = 'left'

        self.password_field.set_text_hidden(True)
        self.password_field.set_forbidden_characters(forbidden_characters=self.forbidden_characters)
        self.email_field.set_forbidden_characters(forbidden_characters=self.forbidden_characters)
        self.hide_login()
        self.code.hide()
        self.forgot_password.hide()
        self.gui_elements.append(self.new_game_btn)
        self.gui_elements.append(self.settings_btn)
        self.gui_elements.append(self.load_game_btn)
        self.gui_elements.append(self.exit_btn)
        self.gui_elements.append(self.menu_png)
        self.gui_elements.append(self.login)
        self.gui_elements.append(self.register)
        self.clock = pygame.time.Clock()

    def start(self):
        while self.is_running:
            pygame.mixer.music.set_volume(gamelogic.config.VOLUME)
            time_delta = self.clock.tick(60) / 1000.0
            self.background.fill(pygame.Color(43, 43, 43))
            self.music.music_check()
            self.background.fill(pygame.Color(43, 43, 43))
            if self.login.pressed:
                self.code_sent_reg = False
                self.code.hide()
                self.forgot_password.show()
                self.login.disable()
                self.register.enable()
                self.exception_label.set_text('')
                self.password_field.set_text('')
                self.code.set_text('')
                self.login_final.set_text('Login')
                self.show_registration_fields()
            elif self.register.pressed:
                self.register.disable()
                self.forgot_password.hide()
                self.exception_label.set_text('')
                self.password_field.set_text('')
                self.code.set_text('')
                self.code.hide()
                self.forgot_send = False
                self.code_sent_forgot = False
                self.login.enable()
                self.login_final.set_text('Register')
                self.show_registration_fields()
            elif self.back_to_menu.pressed:
                self.code_sent_reg = False
                self.forgot_send = False
                self.code_sent_forgot = False
                self.password_field.set_text('')
                self.code.set_text('')
                self.code.hide()
                self.exception_label.set_text('')
                self.forgot_password.hide()
                self.login.enable()
                self.register.enable()
                self.hide_login()
                self.show_all_menu()

            if self.login_final.pressed:
                if not self.login.is_enabled and not self.forgot_send and not self.code_sent_forgot:
                    self.sign_in()
                    print("Sign In")
                elif not self.register.is_enabled and not self.code_sent_reg:
                    self.sign_up()
                    print("Sign Up")
                elif self.code_sent_reg:
                    self.send_registration_code()
                    print("Confirm Registration")
                elif self.forgot_send and not self.code_sent_forgot:
                    self.restore_password()
                    print('Restore Password')
                elif self.code_sent_forgot:
                    self.confirm_restoring_password()
                    print("Confirm Restoring Password")
            if self.forgot_password.pressed:
                self.password_field.hide()
                self.forgot_password.hide()
                self.login_final.set_text('Receive Code')
                self.forgot_send = True

            if self.text_needed:
                navigation_bar.draw_text(self.background, "Welcome to the <BUILD ON FIELD>", 40, 400, 30)
                navigation_bar.draw_text(self.background, f'{self.username}', 20, 450, 565)

            for event in pygame.event.get():
                self.music.music_playlist(event=event)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_TAB:
                        if self.email_field.is_focused:
                            self.email_field.unfocus()
                            self.password_field.focus()
                        elif self.password_field.is_focused:
                            self.email_field.focus()
                            self.password_field.unfocus()
                    elif event.key == (pygame.K_RETURN or pygame.K_KP_ENTER):
                        self.login_final.pressed_event = True
                if event.type == pygame.QUIT:
                    exit()
                self.manager.process_events(event)

            if self.new_game_btn.pressed:
                self.game.new()
                self.start_game()
            if self.settings_btn.pressed:
                self.hide_all_menu()
                self.settings.show_all_settings()
                self.show_settings = True
            if self.load_game_btn.pressed:
                self.hide_all_menu()
                self.save.show_all_save()
                self.show_saves = True
            if self.settings.back_btn.pressed:
                self.show_settings = False
                self.settings.hide_all_settings()
                self.show_all_menu()
            if self.save.back_btn.pressed:
                self.show_saves = False
                self.save.hide_all_save()
                self.show_all_menu()
            if self.show_settings:
                self.settings.start()
            if self.show_saves:
                self.save.start()
            if self.exit_btn.pressed:
                exit()

            self.manager.update(time_delta)
            self.window_surface.blit(self.background, (0, 0))
            self.manager.draw_ui(self.window_surface)
            pygame.display.update()

    def hide_all_menu(self):
        self.background.fill(pygame.Color(43, 43, 43))
        self.text_needed = False
        self.hide_login()
        self.exception_label.hide()
        for element in self.gui_elements:
            element.hide()

    def show_all_menu(self):
        self.text_needed = True
        self.exception_label.show()
        self.exception_label.set_text('')
        for element in self.gui_elements:
            element.show()

    def hide_login(self):
        self.email_field.hide()
        self.password_field.hide()
        self.back_to_menu.hide()
        self.login_final.hide()
        self.exception_label.set_text('')

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

    def sign_up(self):
        try:
            self.network.register(self.email_field.get_text(), self.password_field.get_text())
            self.email_field.hide()
            self.password_field.hide()
            self.password_field.set_text('')
            self.code_sent_reg = True
            self.code.show()
            self.login_final.set_text('Send code')
            self.exception_label.set_text('')
        except (RegistrationError, DbUnavailableError, NotEmailError) as e:
            self.exception_label.set_text(e.__str__())
        except Exception:
            self.exception_label.set_text('Oh my God! Server is down!')

    def send_registration_code(self):
        try:
            self.network.confirm_account(self.code.get_text())
            self.username = self.email_field.get_text()
            self.back_to_menu.pressed_event = True
            self.exception_label.set_text('')
        except (WrongCodeError, TokenError) as e:
            self.exception_label.set_text(e.__str__())
        except Exception:
            self.exception_label.set_text('Oh my God! Server is down!')

    def sign_in(self):
        try:
            self.network.login(self.email_field.get_text(), self.password_field.get_text())
            self.username = self.email_field.get_text()
            self.password_field.set_text('')
            self.exception_label.set_text('')
            self.back_to_menu.pressed_event = True
        except (AuthError, WrongEnterError) as e:
            self.exception_label.set_text(e.__str__())
        except Exception:
            self.exception_label.set_text('Oh my God! Server is down!')

    def restore_password(self):
        try:
            self.network.forgot_password(self.email_field.get_text())
            self.exception_label.set_text('')
            self.login_final.set_text('Send code')
            self.code_sent_forgot = True
            self.code.show()
            self.password_field.show()
        except NotEmailError as e:
            self.exception_label.set_text(e.__str__())
        except Exception:
            self.exception_label.set_text('Oh my God! Server is down!')

    def confirm_restoring_password(self):
        try:
            self.network.reset_password(self.email_field.get_text(), self.password_field.get_text(),
                                        self.code.get_text())
            self.exception_label.set_text('')
            self.back_to_menu.pressed_event = True
        except (NotEmailError, WrongCodeError) as e:
            self.exception_label.set_text(e.__str__())
        except Exception:
            self.exception_label.set_text('Oh my God! Server is down!')

    def load_server_saves(self):
        try:
            return self.network.get_all_game_info()
        except Exception:
            pass

    def start_game(self):
        a = windows_control.Start(self.network, self.music, self.game, self)
        self.hide_all_menu()
        a.start()
        del a
        self.show_all_menu()

    def save_server(self, num, name):
        try:
            data = self.game.server_save_data()
            self.network.update_game_save(num, data[0], data[1], data[2], name)
        except Exception:
            pass

    def load_server(self, num):
        try:
            data = self.network.get_game_save(num)
            self.game.server_load(data[0], data[1], data[2])
        except Exception:
            pass

