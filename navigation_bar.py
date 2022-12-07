import pygame
import pygame_gui


def draw_text(surf, text, size, x, y):
    font = pygame.font.Font('fonts/TimesNewRomanRegular.ttf', size)
    text_surface = font.render(text, True, (187, 187, 187))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


class NavigationBar:
    def __init__(self, manager):
        self.manager = manager
        self.clock = pygame.time.Clock()
 
        self.journal = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 500), (200, 50)),
                                                    text='Journal',
                                                    manager=self.manager)
        self.town = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((200, 500), (200, 50)),
                                                 text='Town',
                                                 manager=self.manager)
        self.storage = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((400, 500), (200, 50)),
                                                    text='Storage',
                                                    manager=self.manager)
        self.workers = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((600, 500), (200, 50)),
                                                    text='Workers',
                                                    manager=self.manager)
        self.army = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 550), (200, 50)),
                                                 text='Army',
                                                 manager=self.manager)
        self.world = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((200, 550), (200, 50)),
                                                  text='World',
                                                  manager=self.manager)
        self.settings = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((400, 550), (200, 50)),
                                                     text='Settings',
                                                     manager=self.manager)
        self.some = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((600, 550), (200, 50)),
                                                 text='some',
                                                 manager=self.manager)
        
    def hide_all_navigation(self):
        self.journal.hide()
        self.town.hide()
        self.storage.hide()
        self.workers.hide()
        self.army.hide()
        self.world.hide()
        self.settings.hide()
        self.some.hide()
        
    def show_all_navigation(self):
        self.journal.show()
        self.town.show()
        self.storage.show()
        self.workers.show()
        self.army.show()
        self.world.show()
        self.settings.show()
        self.some.show()
    
    def enable_all_navigation(self):
        self.journal.enable()
        self.town.enable()
        self.storage.enable()
        self.workers.enable()
        self.army.enable()
        self.world.enable()
        self.settings.enable()
        