import pygame
import pygame_gui


def write_story(text):
    with open('story.txt', 'a') as f:
        f.write(text + "/n")


class Journal:
    def __init__(self, manager, background):
        self.manager = manager
        self.background = background

        self.story_tb = pygame_gui.elements.UITextBox(relative_rect=pygame.Rect((0, 0), (800, 500)),
                                                      manager=self.manager, html_text="")
        with open('story.txt', encoding='utf-8', mode='r') as f:
            self.story_tb.set_text(f.read())

    def start(self):
        pass
               
    def hide_all_journal(self):
        self.story_tb.hide()
        
    def show_all_journal(self):
        self.story_tb.show()    
