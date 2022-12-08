import time

import pygame
import pygame_gui
from pygame_widgets.progressbar import ProgressBar
import navigation_bar
import army_ui
import journal_ui
import settings_ui
import world_ui
import workers_ui
import town_ui
import pygame_widgets
from game.config import *


class Storage:
    def __init__(self, manager, background, game):
        self.manager = manager
        self.background = background

        self.resources = game.resources

        self.check_resource = {}
        for r in self.resources:
            self.check_resource[r] = 0

        self.all_storage = {}
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
        # self.meat_bar = ProgressBar(self.background,
        #                             130, 450, 100, 40,
        #                             lambda: self.resources[MEAT][COUNT] / self.resources[MEAT][MAX])
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
        self.all_storage[IRON] = self.iron_bar
        self.all_storage[GOLD] = self.gold_bar
        self.all_storage[BREAD] = self.bread_bar
        self.all_storage[CLOTHES] = self.clothes_bar
        self.all_storage[WEAPON] = self.weapon_bar
        self.all_storage[ARMOR] = self.armor_bar
        self.all_storage[SKIN] = self.skin_bar
        # self.all_storage.append(self.meat_bar)
        self.all_storage[FLOUR] = self.flour_bar
        self.all_storage[WHEAT] = self.wheat_bar
        self.all_storage[FISH] = self.fish_bar
        self.all_storage[IRON_ORE] = self.iron_ore_bar
        self.all_storage[GOLD_ORE] = self.gold_ore_bar
        self.all_storage[STONE] = self.stone_bar
        self.all_storage[PLANK] = self.wood_bar

        self.all_labels = []

        self.wood = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((0, 20), (200, 25)),
                                                text=f'Wood:: {self.resources[PLANK][COUNT]} / {self.resources[PLANK][MAX]}',
                                                manager=self.manager)
        self.gold_ore = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((0, 45), (200, 25)),
                                                    text=f'Gold ore:: {self.resources[GOLD_ORE][COUNT]} / {self.resources[GOLD_ORE][MAX]}',
                                                    manager=self.manager)
        self.stone = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((0, 70), (200, 25)),
                                                 text=f'Stone:: {self.resources[STONE][COUNT]} / {self.resources[STONE][MAX]}',
                                                 manager=self.manager)
        self.iron_ore = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((0, 95), (200, 25)),
                                                    text=f'Iron ore:: {self.resources[IRON_ORE][COUNT]} / {self.resources[IRON_ORE][MAX]}',
                                                    manager=self.manager)
        self.fish = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((0, 120), (200, 25)),
                                                text=f'Fish:: {self.resources[FISH][COUNT]} / {self.resources[FISH][MAX]}',
                                                manager=self.manager)
        self.wheat = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((0, 145), (200, 25)),
                                                 text=f'Wheat:: {self.resources[WHEAT][COUNT]} / {self.resources[WHEAT][MAX]}',
                                                 manager=self.manager)
        self.flour = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((0, 170), (200, 25)),
                                                 text=f'Flour:: {self.resources[FLOUR][COUNT]} / {self.resources[FLOUR][MAX]}',
                                                 manager=self.manager)
        self.bread = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((0, 195), (200, 25)),
                                                 text=f'Bread:: {self.resources[BREAD][COUNT]} / {self.resources[BREAD][MAX]}',
                                                 manager=self.manager)
        self.skin = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((0, 220), (200, 25)),
                                                text=f'Skin:: {self.resources[SKIN][COUNT]} / {self.resources[SKIN][MAX]}',
                                                manager=self.manager)
        self.armor = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((0, 245), (200, 25)),
                                                 text=f'Armor:: {self.resources[ARMOR][COUNT]} / {self.resources[ARMOR][MAX]}',
                                                 manager=self.manager)
        self.weapon = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((0, 270), (200, 25)),
                                                  text=f'Weapon:: {self.resources[WEAPON][COUNT]} / {self.resources[WEAPON][MAX]}',
                                                  manager=self.manager)
        self.clothes = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((0, 295), (200, 25)),
                                                   text=f'Clothes:: {self.resources[CLOTHES][COUNT]} / {self.resources[CLOTHES][MAX]}',
                                                   manager=self.manager)
        self.gold = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((0, 320), (200, 25)),
                                                text=f'Gold:: {self.resources[GOLD][COUNT]} / {self.resources[GOLD][MAX]}',
                                                manager=self.manager)
        self.iron = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((0, 345), (200, 25)),
                                                text=f'Iron:: {self.resources[IRON][COUNT]} / {self.resources[IRON][MAX]}',
                                                manager=self.manager)
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

        # start_time = time.time()
        # a = (time.time() - start_time) / 20
        # test = ProgressBar(self.background,
        #                    380, 450, 100, 40,
        #                    lambda: 0 + (time.time() - start_time) / 20)

    def start(self):

        # if self.resources[PLANK][COUNT] < self.wood_check:
        #     self.wood_bar.completedColour = "#e61919"
        # elif self.resources[PLANK][COUNT] > self.wood_check:
        #     self.wood_bar.completedColour = "#0d730d"
        # else:
        #     self.wood_bar.completedColour = "#e5e619"
        #
        # if self.resources[PLANK][COUNT] < self.gold_check:
        #     self.gold_bar.completedColour = "#e61919"
        # elif self.wood > self.wood_check:
        #     self.gold_bar.completedColour = "#0d730d"
        # else:
        #     self.gold_bar.completedColour = "#e5e619"
        #
        # if self.stone < self.stone_check:
        #     self.stone_bar.completedColour = "#e61919"
        # elif self.stone > self.stone_check:
        #     self.stone_bar.completedColour = "#0d730d"
        # else:
        #     self.stone_bar.completedColour = "#e5e619"
        #
        # if self.iron < self.iron_check:
        #     self.iron_bar.completedColour = "#e61919"
        # elif self.iron > self.iron_check:
        #     self.iron_bar.completedColour = "#0d730d"
        # else:
        #     self.iron_bar.completedColour = "#e5e619"
        #
        # if self.gold_ore < self.gold_ore_check:
        #     self.gold_ore_bar.completedColour = "#e61919"
        # elif self.gold_ore > self.gold_ore_check:
        #     self.gold_ore_bar.completedColour = "#0d730d"
        # else:
        #     self.gold_ore_bar.completedColour = "#e5e619"
        #
        # if self.iron_ore < self.iron_ore:
        #     self.iron_ore_bar.completedColour = "#e61919"
        # elif self.iron_ore > self.iron_ore:
        #     self.iron_ore_bar.completedColour = "#0d730d"
        # else:
        #     self.iron_ore_bar.completedColour = "#e5e619"
        #
        # if self.fish < self.fish_check:
        #     self.fish_bar.completedColour = "#e61919"
        # elif self.fish > self.fish_check:
        #     self.fish_bar.completedColour = "#0d730d"
        # else:
        #     self.fish_bar.completedColour = "#e5e619"
        #
        # if self.wheat < self.wheat_check:
        #     self.wheat_bar.completedColour = "#e61919"
        # elif self.wheat > self.wheat_check:
        #     self.wheat_bar.completedColour = "#0d730d"
        # else:
        #     self.wheat_bar.completedColour = "#e5e619"
        #
        # if self.flour < self.flour_check:
        #     self.flour_bar.completedColour = "#e61919"
        # elif self.flour > self.flour_check:
        #     self.flour_bar.completedColour = "#0d730d"
        # else:
        #     self.flour_bar.completedColour = "#e5e619"
        #
        # if self.bread < self.bread_check:
        #     self.bread_bar.completedColour = "#e61919"
        # elif self.bread > self.bread_check:
        #     self.bread_bar.completedColour = "#0d730d"
        # else:
        #     self.bread_bar.completedColour = "#e5e619"
        #
        # if self.meat < self.meat_check:
        #     self.meat_bar.completedColour = "#e61919"
        # elif self.meat > self.meat_check:
        #     self.meat_bar.completedColour = "#0d730d"
        # else:
        #     self.meat_bar.completedColour = "#e5e619"
        #
        # if self.skin < self.skin_check:
        #     self.skin_bar.completedColour = "#e61919"
        # elif self.skin > self.skin_check:
        #     self.skin_bar.completedColour = "#0d730d"
        # else:
        #     self.skin_bar.completedColour = "#e5e619"
        #
        # if self.armor < self.armor_check:
        #     self.armor_bar.completedColour = "#e61919"
        # elif self.armor > self.armor_check:
        #     self.armor_bar.completedColour = "#0d730d"
        # else:
        #     self.armor_bar.completedColour = "#e5e619"
        #
        # if self.weapon < self.weapon_check:
        #     self.weapon_bar.completedColour = "#e61919"
        # elif self.weapon > self.weapon_check:
        #     self.weapon_bar.completedColour = "#0d730d"
        # else:
        #     self.weapon_bar.completedColour = "#e5e619"
        #
        # if self.clothes < self.clothes_check:
        #     self.clothes_bar.completedColour = "#e61919"
        # elif self.clothes > self.clothes_check:
        #     self.clothes_bar.completedColour = "#0d730d"
        # else:
        #     self.clothes_bar.completedColour = "#e5e619"
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
