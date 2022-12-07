import pygame
import pygame_gui
from pygame_gui.core import ObjectID
import navigation_bar
import webbrowser


class Settings:
    def __init__(self, manager, background, back):
        self.back = back
        self.manager = manager
        self.background = background
        self.text_needed = True

        self.back_btn = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 0), (200, 50)),
                                                     text='Back',
                                                     manager=self.manager)
        self.donate = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((200, 280), (400, 200)),
                                                   text='Donate',
                                                   manager=self.manager,
                                                   object_id=ObjectID(class_id="@special_donate", object_id="#donate"))

    def start(self):
        if not self.back:
            self.back_btn.hide()
        self.background.fill(pygame.Color(43, 43, 43))
        if self.text_needed:
            navigation_bar.draw_text(self.background, "Made by SS BBSO-01-20", 60, 400, 150)

        if self.donate.pressed:
            webbrowser.open("https://vk.com/seregasil", new=2)
            webbrowser.open("https://vk.com/tartarug", new=2)

    def hide_all_settings(self):
        self.background.fill(pygame.Color(43, 43, 43))
        self.back_btn.hide()
        self.donate.hide()

    def show_all_settings(self):
        self.back_btn.show()
        self.donate.show()
