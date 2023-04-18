import pygame
import pygame_gui
from gui import navigation_bar


class Save:
    def __init__(self, manager, background, back):
        self.manager = manager
        self.background = background
        self.back = back

        self.text_needed = True

        self.cloud_save_1 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((170, 100), (200, 50)),
                                                         text='1',
                                                         manager=self.manager)
        self.cloud_save_2 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((170, 200), (200, 50)),
                                                         text='2',
                                                         manager=self.manager)
        self.cloud_save_3 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((170, 300), (200, 50)),
                                                         text='3',
                                                         manager=self.manager)
        self.local_save_1 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((430, 100), (200, 50)),
                                                         text='1',
                                                         manager=self.manager)
        self.local_save_2 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((430, 200), (200, 50)),
                                                         text='2',
                                                         manager=self.manager)
        self.local_save_3 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((430, 300), (200, 50)),
                                                         text='3',
                                                         manager=self.manager)

        self.back_btn = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 0), (100, 50)),
                                                     text='Back',
                                                     manager=self.manager)

    def start(self):
        self.background.fill(pygame.Color(43, 43, 43))
        if not self.back:
            self.back_btn.hide()

        if self.text_needed:
            navigation_bar.draw_text(self.background, "Server saves", 30, 270, 50)
            navigation_bar.draw_text(self.background, "Local saves", 30, 530, 50)

    def hide_all_save(self):
        self.background.fill(pygame.Color(43, 43, 43))
        self.cloud_save_1.hide()
        self.cloud_save_2.hide()
        self.cloud_save_3.hide()
        self.local_save_1.hide()
        self.local_save_2.hide()
        self.local_save_3.hide()
        self.back_btn.hide()

    def show_all_save(self):
        self.cloud_save_1.show()
        self.cloud_save_2.show()
        self.cloud_save_3.show()
        self.local_save_1.show()
        self.local_save_2.show()
        self.local_save_3.show()
        self.back_btn.show()
