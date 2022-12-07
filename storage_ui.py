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

        self.all_storage = []
        self.text_needed = True

        self.wood_bar = ProgressBar(self.background,
                                    130, 100, 100, 40,
                                    lambda: self.resources[PLANK][COUNT] / self.resources[PLANK][MAX])
        self.gold_ore_bar = ProgressBar(self.background,
                                        130, 150, 100, 40,
                                        lambda: self.resources[GOLD_ORE][COUNT] / self.resources[GOLD_ORE][MAX])
        self.stone_bar = ProgressBar(self.background,
                                     130, 200, 100, 40,
                                     lambda: self.resources[STONE][COUNT] / self.resources[STONE][MAX])
        self.iron_ore_bar = ProgressBar(self.background,
                                        130, 250, 100, 40,
                                        lambda: self.resources[IRON_ORE][COUNT] / self.resources[IRON_ORE][MAX])
        self.fish_bar = ProgressBar(self.background,
                                    130, 300, 100, 40,
                                    lambda: self.resources[FISH][COUNT] / self.resources[FISH][MAX])
        self.wheat_bar = ProgressBar(self.background,
                                     130, 350, 100, 40,
                                     lambda: self.resources[WHEAT][COUNT] / self.resources[WHEAT][MAX])
        self.flour_bar = ProgressBar(self.background,
                                     130, 400, 100, 40,
                                     lambda: self.resources[FLOUR][COUNT] / self.resources[FLOUR][MAX])
        # self.meat_bar = ProgressBar(self.background,
        #                             130, 450, 100, 40,
        #                             lambda: self.resources[MEAT][COUNT] / self.resources[MEAT][MAX])
        self.skin_bar = ProgressBar(self.background,
                                    380, 100, 100, 40,
                                    lambda: self.resources[SKIN][COUNT] / self.resources[SKIN][MAX])
        self.armor_bar = ProgressBar(self.background,
                                     380, 150, 100, 40,
                                     lambda: self.resources[ARMOR][COUNT] / self.resources[ARMOR][MAX])
        self.weapon_bar = ProgressBar(self.background,
                                      380, 200, 100, 40,
                                      lambda: self.resources[WEAPON][COUNT] / self.resources[WEAPON][MAX])
        self.clothes_bar = ProgressBar(self.background,
                                       380, 250, 100, 40,
                                       lambda: self.resources[CLOTHES][COUNT] / self.resources[CLOTHES][MAX])
        self.bread_bar = ProgressBar(self.background,
                                     380, 300, 100, 40,
                                     lambda: self.resources[BREAD][COUNT] / self.resources[BREAD][MAX])
        self.gold_bar = ProgressBar(self.background,
                                    380, 350, 100, 40,
                                    lambda: self.resources[GOLD][COUNT] / self.resources[GOLD][MAX])
        self.iron_bar = ProgressBar(self.background,
                                    380, 400, 100, 40,
                                    lambda: self.resources[IRON][COUNT] / self.resources[IRON][MAX])
        self.all_storage.append(self.iron_bar)
        self.all_storage.append(self.gold_bar)
        self.all_storage.append(self.bread_bar)
        self.all_storage.append(self.clothes_bar)
        self.all_storage.append(self.weapon_bar)
        self.all_storage.append(self.armor_bar)
        self.all_storage.append(self.skin_bar)
        # self.all_storage.append(self.meat_bar)
        self.all_storage.append(self.flour_bar)
        self.all_storage.append(self.wheat_bar)
        self.all_storage.append(self.fish_bar)
        self.all_storage.append(self.iron_ore_bar)
        self.all_storage.append(self.gold_ore_bar)
        self.all_storage.append(self.stone_bar)
        self.all_storage.append(self.wood_bar)

        # start_time = time.time()
        # a = (time.time() - start_time) / 20
        # test = ProgressBar(self.background,
        #                    380, 450, 100, 40,
        #                    lambda: 0 + (time.time() - start_time) / 20)

    def start(self):
        for res in self.resources:
            if self.resources[res][COUNT] < self.check_resource[res]:
                self.wood_bar.completedColour = "#e61919"
            elif self.resources[res][COUNT] > self.check_resource[res]:
                self.wood_bar.completedColour = "#0d730d"
            else:
                self.wood_bar.completedColour = "#e5e619"


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

        self.background.fill(pygame.Color(43, 43, 43))
        if self.text_needed:
            navigation_bar.draw_text(self.background, f'Wood {self.resources[PLANK][COUNT]} / {self.resources[PLANK][MAX]}',
                                         15, 55, 115)
            navigation_bar.draw_text(self.background, f'Gold ore {self.resources[GOLD_ORE][COUNT]} / {self.resources[GOLD_ORE][MAX]}',
                                         15, 55, 165)
            navigation_bar.draw_text(self.background, f'Stone {self.resources[STONE][COUNT]} / {self.resources[STONE][MAX]}',
                                         15, 55, 215)
            navigation_bar.draw_text(self.background, f'Iron ore {self.resources[IRON_ORE][COUNT]} / {self.resources[IRON_ORE][MAX]}',
                                         15, 55, 265)
            navigation_bar.draw_text(self.background, f'Fish {self.resources[FISH][COUNT]} / {self.resources[FISH][MAX]}',
                                         15, 55, 315)
            navigation_bar.draw_text(self.background, f'Wheat {self.resources[WHEAT][COUNT]} / {self.resources[WHEAT][MAX]}',
                                         15, 55, 365)
            navigation_bar.draw_text(self.background, f'Flour {self.resources[FLOUR][COUNT]} / {self.resources[FLOUR][MAX]}',
                                         15, 55, 415)
            # navigation_bar.draw_text(self.background, f'Meat {self.resources[MEAT][COUNT]} / {self.resources[MEAT][MAX]}',
            #                              15, 55, 465)
            navigation_bar.draw_text(self.background, f'Skin {self.resources[SKIN][COUNT]} / {self.resources[SKIN][MAX]}',
                                         15, 300, 115)
            navigation_bar.draw_text(self.background, f'Armor {self.resources[ARMOR][COUNT]} / {self.resources[ARMOR][MAX]}',
                                         15, 300, 165)
            navigation_bar.draw_text(self.background, f'Weapon {self.resources[WEAPON][COUNT]} / {self.resources[WEAPON][MAX]}',
                                         15, 300, 215)
            navigation_bar.draw_text(self.background, f'Clothes {self.resources[CLOTHES][COUNT]} / {self.resources[CLOTHES][MAX]}',
                                         15, 300, 265)
            navigation_bar.draw_text(self.background, f'Bread {self.resources[BREAD][COUNT]} / {self.resources[BREAD][MAX]}',
                                         15, 300, 315)
            navigation_bar.draw_text(self.background, f'Gold {self.resources[GOLD][COUNT]} / {self.resources[GOLD][MAX]}',
                                         15, 300, 365)
            navigation_bar.draw_text(self.background, f'Iron {self.resources[IRON][COUNT]} / {self.resources[IRON][MAX]}',
                                         15, 300, 415)
            navigation_bar.draw_text(self.background, f'Population {self.resources[PEOPLE][COUNT]} / {self.resources[PEOPLE][MAX]}',
                                         20, 700, 10)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            self.manager.process_events(event)

        for res in self.check_resource:
            self.check_resource[res] = self.resources[res][COUNT]
        pygame_widgets.update(pygame.event.get())

    def hide_all_storage(self):
        self.background.fill(pygame.Color(43, 43, 43))
        self.text_needed = False
        for element in self.all_storage:
            element.hide()

    def show_all_storage(self):
        self.text_needed = True
        for element in self.all_storage:
            element.show()
            