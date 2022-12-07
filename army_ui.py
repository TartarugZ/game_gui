import pygame
import navigation_bar
import pygame_gui


class Army:
    def __init__(self, manager, background):
        self.manager = manager
        self.background = background
        self.troops = 0
        self.fleet = 0
        self.max_troops = 0
        self.max_fleet = 0
        self.distance_number = 0
        self.melee_number = 0
        self.heal_number = 0
        self.schrooner_number = 0
        self.drakkar_number = 0
        self.caravelle_number = 0
        self.max_distance_number = 0
        self.max_melee_number = 0
        self.max_heal_number = 0
        self.max_schrooner_number = 0
        self.max_drakkar_number = 0
        self.max_caravelle_number = 0
        self.all_army = []
        self.text_needed = True

        self.distance = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((250, 150), (100, 50)),
                                                     text='Archer',
                                                     manager=self.manager)
        self.melee = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((250, 200), (100, 50)),
                                                  text='Swordsman',
                                                  manager=self.manager)
        self.heal = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((250, 250), (100, 50)),
                                                 text='Priest',
                                                 manager=self.manager)
        self.schrooner = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((450, 150), (100, 50)),
                                                      text='Schrooner',
                                                      manager=self.manager)
        self.drakkar = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((450, 200), (100, 50)),
                                                    text='Drakkar',
                                                    manager=self.manager)
        self.caravelle = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((450, 250), (100, 50)),
                                                      text='Caravelle',
                                                      manager=self.manager)
        self.all_army.append(self.distance)
        self.all_army.append(self.melee)
        self.all_army.append(self.heal)
        self.all_army.append(self.schrooner)
        self.all_army.append(self.drakkar)
        self.all_army.append(self.caravelle)

    def start(self):
        self.background.fill(pygame.Color(43, 43, 43))
        if self.text_needed:
            navigation_bar.draw_text(self.background,
                                     f'Army:{self.troops}/{self.max_troops}  Fleet:{self.fleet}/{self.max_fleet}',
                                     40, 400, 30)
            navigation_bar.draw_text(self.background,
                                     f'{self.distance_number}/{self.max_distance_number}', 30, 150, 165)
            navigation_bar.draw_text(self.background,
                                     f'{self.melee_number}/{self.max_melee_number}', 30, 150, 215)
            navigation_bar.draw_text(self.background,
                                     f'{self.heal_number}/{self.max_heal_number}', 30, 150, 265)
            navigation_bar.draw_text(self.background,
                                     f'{self.schrooner_number}/{self.max_schrooner_number}', 30, 600, 165)
            navigation_bar.draw_text(self.background,
                                     f'{self.drakkar_number}/{self.max_drakkar_number}', 30, 600, 215)
            navigation_bar.draw_text(self.background,
                                     f'{self.caravelle_number}/{self.max_caravelle_number}', 30, 600, 265)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            self.manager.process_events(event)
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == self.distance:
                    pass  # To game code
                elif event.ui_element == self.melee:
                    pass  # To game code
                elif event.ui_element == self.heal:
                    pass  # To game code
                elif event.ui_element == self.schrooner:
                    pass  # To game code
                elif event.ui_element == self.drakkar:
                    pass  # To game code
                elif event.ui_element == self.caravelle:
                    pass  # To game code

    def hide_all_army(self):
        self.background.fill(pygame.Color(43, 43, 43))
        self.text_needed = False
        for element in self.all_army:
            element.hide()

    def show_all_army(self):
        self.text_needed = True
        for element in self.all_army:
            element.show()
