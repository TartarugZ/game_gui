import pygame
import pygame_gui
import navigation_bar


class World:
    def __init__(self, manager, background):
        self.manager = manager
        self.background = background
        self.text_nedeed = True

    def start(self):
        if self.text_nedeed:
            navigation_bar.draw_text(self.background, "World Map", 30, 400, 20)
                
    def hide_all_world(self):
        self.background.fill(pygame.Color(43, 43, 43))
        pass
    
    def show_all_world(self):
        pass
    