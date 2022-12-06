import pygame
import pygame_gui
import army_ui
import journal_ui
import storage_ui
import settings_ui
import town_ui
import workers_ui


class World:
    def __init__(self, manager, background):
        self.manager = manager
        self.background = background

    def start(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            self.manager.process_events(event)
                
    def hide_all_world(self):
        self.background.fill(pygame.Color(43, 43, 43))
        pass
    
    def show_all_world(self):
        pass
    