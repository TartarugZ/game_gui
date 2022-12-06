import pygame
import pygame_gui
import town_ui
import army_ui
import storage_ui
import settings_ui
import world_ui
import workers_ui


def write_story(text):
    with open('story.txt', 'a') as f:
        f.write(text + "/n")


class Journal:
    def __init__(self, manager, background):
        self.manager = manager
        self.background = background
        self.story_tb = pygame_gui.elements.UITextBox(relative_rect=pygame.Rect((0, 0), (800, 500)),
                                                      manager=self.manager, html_text="")

    def start(self):
        with open('story.txt', encoding='utf-8', mode='r') as f:
            self.story_tb.set_text(f.read())
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            self.manager.process_events(event)
               
    def hide_all_journal(self):
        self.story_tb.hide()
        
    def show_all_journal(self):
        self.story_tb.show()    
