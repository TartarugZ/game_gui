import pygame
import pygame_gui

from pygame_widgets.progressbar import ProgressBar
from gamelogic.config import *


class Storage:
    def __init__(self, manager, background, game):
        self.manager = manager
        self.background = background

        self.resources = game.resources

        self.check_resource = {}
        for r in self.resources:
            self.check_resource[r] = 0

        self.text_needed = True

        self.last_tick = pygame.time.get_ticks()
        self.cooldown = 1000

        self.wood_bar = ProgressBar(self.background,
                                    200, 20, 100, 20,
                                    lambda: self.resources[PLANK][COUNT] / self.resources[PLANK][MAX])
        self.gold_ore_bar = ProgressBar(self.background,
                                        200, 45, 100, 20,
                                        lambda: self.resources[GOLD_ORE][COUNT] / self.resources[GOLD_ORE][MAX])
        self.stone_bar = ProgressBar(self.background,
                                     200, 70, 100, 20,
                                     lambda: self.resources[STONE][COUNT] / self.resources[STONE][MAX])
        self.iron_ore_bar = ProgressBar(self.background,
                                        200, 95, 100, 20,
                                        lambda: self.resources[IRON_ORE][COUNT] / self.resources[IRON_ORE][MAX])
        self.fish_bar = ProgressBar(self.background,
                                    200, 120, 100, 20,
                                    lambda: self.resources[FISH][COUNT] / self.resources[FISH][MAX])
        self.wheat_bar = ProgressBar(self.background,
                                     200, 145, 100, 20,
                                     lambda: self.resources[WHEAT][COUNT] / self.resources[WHEAT][MAX])
        self.flour_bar = ProgressBar(self.background,
                                     200, 170, 100, 20,
                                     lambda: self.resources[FLOUR][COUNT] / self.resources[FLOUR][MAX])
        self.skin_bar = ProgressBar(self.background,
                                    200, 195, 100, 20,
                                    lambda: self.resources[SKIN][COUNT] / self.resources[SKIN][MAX])
        self.armor_bar = ProgressBar(self.background,
                                     200, 220, 100, 20,
                                     lambda: self.resources[ARMOR][COUNT] / self.resources[ARMOR][MAX])
        self.weapon_bar = ProgressBar(self.background,
                                      200, 245, 100, 20,
                                      lambda: self.resources[WEAPON][COUNT] / self.resources[WEAPON][MAX])
        self.clothes_bar = ProgressBar(self.background,
                                       200, 270, 100, 20,
                                       lambda: self.resources[CLOTHES][COUNT] / self.resources[CLOTHES][MAX])
        self.bread_bar = ProgressBar(self.background,
                                     200, 295, 100, 20,
                                     lambda: self.resources[BREAD][COUNT] / self.resources[BREAD][MAX])
        self.gold_bar = ProgressBar(self.background,
                                    200, 320, 100, 20,
                                    lambda: self.resources[GOLD][COUNT] / self.resources[GOLD][MAX])
        self.iron_bar = ProgressBar(self.background,
                                    200, 345, 100, 20,
                                    lambda: self.resources[IRON][COUNT] / self.resources[IRON][MAX])

        self.all_storage = {IRON: self.iron_bar, GOLD: self.gold_bar, BREAD: self.bread_bar, CLOTHES: self.clothes_bar,
                            WEAPON: self.weapon_bar, ARMOR: self.armor_bar, SKIN: self.skin_bar, FLOUR: self.flour_bar,
                            WHEAT: self.wheat_bar, FISH: self.fish_bar, IRON_ORE: self.iron_ore_bar,
                            GOLD_ORE: self.gold_ore_bar, STONE: self.stone_bar, PLANK: self.wood_bar}

        self.wood = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((0, 20), (200, 25)),
                                                text=f'Wood:: {self.resources[PLANK][COUNT]} / '
                                                     f'{self.resources[PLANK][MAX]}',
                                                manager=self.manager)
        self.gold_ore = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((0, 45), (200, 25)),
                                                    text=f'Gold ore:: {self.resources[GOLD_ORE][COUNT]} / '
                                                         f'{self.resources[GOLD_ORE][MAX]}',
                                                    manager=self.manager)
        self.stone = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((0, 70), (200, 25)),
                                                 text=f'Stone:: {self.resources[STONE][COUNT]} / '
                                                      f'{self.resources[STONE][MAX]}',
                                                 manager=self.manager)
        self.iron_ore = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((0, 95), (200, 25)),
                                                    text=f'Iron ore:: {self.resources[IRON_ORE][COUNT]} / '
                                                         f'{self.resources[IRON_ORE][MAX]}',
                                                    manager=self.manager)
        self.fish = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((0, 120), (200, 25)),
                                                text=f'Fish:: {self.resources[FISH][COUNT]} / '
                                                     f'{self.resources[FISH][MAX]}',
                                                manager=self.manager)
        self.wheat = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((0, 145), (200, 25)),
                                                 text=f'Wheat:: {self.resources[WHEAT][COUNT]} / '
                                                      f'{self.resources[WHEAT][MAX]}',
                                                 manager=self.manager)
        self.flour = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((0, 170), (200, 25)),
                                                 text=f'Flour:: {self.resources[FLOUR][COUNT]} / '
                                                      f'{self.resources[FLOUR][MAX]}',
                                                 manager=self.manager)
        self.bread = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((0, 195), (200, 25)),
                                                 text=f'Bread:: {self.resources[BREAD][COUNT]} / '
                                                      f'{self.resources[BREAD][MAX]}',
                                                 manager=self.manager)
        self.skin = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((0, 220), (200, 25)),
                                                text=f'Skin:: {self.resources[SKIN][COUNT]} / '
                                                     f'{self.resources[SKIN][MAX]}',
                                                manager=self.manager)
        self.armor = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((0, 245), (200, 25)),
                                                 text=f'Armor:: {self.resources[ARMOR][COUNT]} / '
                                                      f'{self.resources[ARMOR][MAX]}',
                                                 manager=self.manager)
        self.weapon = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((0, 270), (200, 25)),
                                                  text=f'Weapon:: {self.resources[WEAPON][COUNT]} / '
                                                       f'{self.resources[WEAPON][MAX]}',
                                                  manager=self.manager)
        self.clothes = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((0, 295), (200, 25)),
                                                   text=f'Clothes:: {self.resources[CLOTHES][COUNT]} / '
                                                        f'{self.resources[CLOTHES][MAX]}',
                                                   manager=self.manager)
        self.gold = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((0, 320), (200, 25)),
                                                text=f'Gold:: {self.resources[GOLD][COUNT]} / '
                                                     f'{self.resources[GOLD][MAX]}',
                                                manager=self.manager)
        self.iron = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((0, 345), (200, 25)),
                                                text=f'Iron:: {self.resources[IRON][COUNT]} / '
                                                     f'{self.resources[IRON][MAX]}',
                                                manager=self.manager)

        self.all_labels = []
        self.all_labels.append(self.wood)
        self.all_labels.append(self.gold_ore)
        self.all_labels.append(self.stone)
        self.all_labels.append(self.iron_ore)
        self.all_labels.append(self.fish)
        self.all_labels.append(self.wheat)
        self.all_labels.append(self.flour)
        self.all_labels.append(self.bread)
        self.all_labels.append(self.skin)
        self.all_labels.append(self.armor)
        self.all_labels.append(self.weapon)
        self.all_labels.append(self.clothes)
        self.all_labels.append(self.gold)
        self.all_labels.append(self.iron)

        # button holding timer
        # start_time = time.time()
        # a = (time.time() - start_time) / 20
        # test = ProgressBar(self.background,
        #                    380, 450, 100, 40,
        #                    lambda: 0 + (time.time() - start_time) / 20)

    def start(self):

        now = pygame.time.get_ticks()
        if now - self.last_tick >= self.cooldown:
            self.last_tick = now
            for res in self.resources:

                try:
                    if self.resources[res][COUNT] < self.check_resource[res]:
                        self.all_storage[res].completedColour = "#e61919"
                    elif self.resources[res][COUNT] > self.check_resource[res]:
                        self.all_storage[res].completedColour = "#0d730d"
                    else:
                        self.all_storage[res].completedColour = "#e5e619"
                    self.check_resource[res] = self.resources[res][COUNT]
                except KeyError:
                    pass

            self.background.fill(pygame.Color(43, 43, 43))
            if self.text_needed:
                self.wood.set_text(f'Wood:: {self.resources[PLANK][COUNT]} / {self.resources[PLANK][MAX]}')
                self.gold_ore.set_text(
                    f'Gold ore:: {self.resources[GOLD_ORE][COUNT]} / {self.resources[GOLD_ORE][MAX]}')
                self.stone.set_text(f'Stone:: {self.resources[STONE][COUNT]} / {self.resources[STONE][MAX]}')
                self.iron_ore.set_text(
                    f'Iron ore:: {self.resources[IRON_ORE][COUNT]} / {self.resources[IRON_ORE][MAX]}')
                self.fish.set_text(f'Fish:: {self.resources[FISH][COUNT]} / {self.resources[FISH][MAX]}')
                self.wheat.set_text(f'Wheat:: {self.resources[WHEAT][COUNT]} / {self.resources[WHEAT][MAX]}')
                self.flour.set_text(f'Flour:: {self.resources[FLOUR][COUNT]} / {self.resources[FLOUR][MAX]}')
                self.bread.set_text(f'Bread:: {self.resources[BREAD][COUNT]} / {self.resources[BREAD][MAX]}')
                self.skin.set_text(f'Skin:: {self.resources[SKIN][COUNT]} / {self.resources[SKIN][MAX]}')
                self.armor.set_text(f'Armor:: {self.resources[ARMOR][COUNT]} / {self.resources[ARMOR][MAX]}')
                self.weapon.set_text(f'Weapon:: {self.resources[WEAPON][COUNT]} / {self.resources[WEAPON][MAX]}')
                self.clothes.set_text(f'Clothes:: {self.resources[CLOTHES][COUNT]} / {self.resources[CLOTHES][MAX]}')
                self.gold.set_text(f'Gold:: {self.resources[GOLD][COUNT]} / {self.resources[GOLD][MAX]}')
                self.iron.set_text(f'Iron:: {self.resources[IRON][COUNT]} / {self.resources[IRON][MAX]}')

    def hide_all_storage(self):
        self.background.fill(pygame.Color(43, 43, 43))
        self.text_needed = False
        for element in self.all_labels:
            element.hide()
        for element in self.all_storage:
            self.all_storage[element].hide()

    def show_all_storage(self):
        self.text_needed = True
        for element in self.all_labels:
            element.show()
        for element in self.all_storage:
            self.all_storage[element].show()
