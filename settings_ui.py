import json

import pygame
import pygame_gui
from pygame_gui.core import ObjectID
import navigation_bar
import webbrowser
import gamelogic.config


class Settings:
    def __init__(self, manager, background, back):
        self.back = back
        self.manager = manager
        self.background = background
        self.text_needed = True
        self.current_volume = gamelogic.config.VOLUME
        self.current_autosave = gamelogic.config.AUTOSAVE
        self.back_btn = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 0), (100, 50)),
                                                     text='Back',
                                                     manager=self.manager)
        self.donate = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((200, 280), (400, 200)),
                                                   text='Donate',
                                                   manager=self.manager,
                                                   object_id=ObjectID(class_id="@special_donate", object_id="#donate"))
        self.volume_slider = pygame_gui.elements.UIHorizontalSlider(relative_rect=pygame.Rect((200, 50), (200, 20)),
                                                                    start_value=self.current_volume * 100,
                                                                    value_range=(0, 100), manager=self.manager)
        self.autosave_slider = pygame_gui.elements.UIHorizontalSlider(relative_rect=pygame.Rect((450, 50), (200, 20)),
                                                                      start_value=self.current_autosave / 60000,
                                                                      value_range=(5, 60), manager=self.manager)
        self.volume_value = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((200, 80), (200, 50)),
                                                        text=f"Current volume:{int(self.current_volume * 100)}",
                                                        manager=self.manager)
        self.autosave_value = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((450, 80), (200, 50)),
                                                          text=f"Autosave timing:{int(self.current_autosave / 60000)}",
                                                          manager=self.manager)

    def start(self):
        if self.volume_slider.has_moved_recently:
            gamelogic.config.VOLUME = self.volume_slider.get_current_value() / 100
            self.volume_value.set_text(f"Current volume:{int(self.volume_slider.get_current_value())}")
            with open("save/locals.json", "r") as file:
                save = json.load(file)
                save['volume'] = self.volume_slider.get_current_value() / 100
            with open("save/locals.json", "w+") as file:
                json.dump(save, file)

        if self.autosave_slider.has_moved_recently:
            gamelogic.config.AUTOSAVE = self.autosave_slider.get_current_value() * 60000
            self.autosave_value.set_text(f"Autosave timing:{int(self.autosave_slider.get_current_value())}")
            with open("save/locals.json", "r") as file:
                save = json.load(file)
                save['autosave'] = self.autosave_slider.get_current_value() * 60000
            with open("save/locals.json", "w+") as file:
                json.dump(save, file)
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
        self.volume_slider.hide()
        self.volume_value.hide()
        self.autosave_slider.hide()
        self.autosave_value.hide()

    def show_all_settings(self):
        self.back_btn.show()
        self.donate.show()
        self.volume_slider.show()
        self.volume_value.show()
        self.autosave_slider.show()
        self.autosave_value.show()
