import pygame
import pygame_gui
import navigation_bar
import settings_ui


class Menu:
    def __init__(self, manager, background, window_surface):
        pygame.init()
        self.window_surface = window_surface
        self.text_needed = True
        self.is_running = True
        self.manager = manager
        self.background = background
        self.buttons = []
        self.settings = settings_ui.Settings(self.manager, self.background, True)
        self.settings.hide_all_settings()
        self.sh_settings = False

        self.start_btn = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((300, 150), (200, 80)),
                                                      text='Game',
                                                      manager=self.manager)
        self.settings_btn = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((300, 250), (200, 80)),
                                                         text='Settings',
                                                         manager=self.manager)
        self.exit_btn = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((300, 350), (200, 80)),
                                                     text='Exit',
                                                     manager=self.manager)
        self.buttons.append(self.start_btn)
        self.buttons.append(self.settings_btn)
        self.buttons.append(self.exit_btn)
        clock = pygame.time.Clock()
        while self.is_running:
            time_delta = clock.tick(60) / 1000.0
            self.background.fill(pygame.Color(43, 43, 43))
            if self.text_needed:
                navigation_bar.draw_text(self.background, "Welcome to the <BUILD ON FIELD>", 40, 400, 50)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                self.manager.process_events(event)
                if event.type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == self.start_btn:
                        self.is_running = False
                    elif event.ui_element == self.settings_btn:
                        self.hide_all_menu()
                        self.settings.show_all_settings()
                        self.sh_settings = True
                    elif event.ui_element == self.exit_btn:
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
        for element in self.buttons:
            element.hide()

    def show_all_menu(self):
        self.text_needed = True
        for element in self.buttons:
            element.show()
