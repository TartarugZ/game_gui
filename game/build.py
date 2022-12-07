# import pygame
# from config import *
# import buildings
# import place
#
#
# def show_place(game, building):
#     for i, row in enumerate(town_map):
#         for j, column in enumerate(row):
#             if column == building[PLACE]:
#                 if check_building(game, j + FIELD[X], i + FIELD[Y]):
#                     pl = place.Place(game, j + FIELD[X], i + FIELD[Y])
#                     game.town_sprites.add(pl)
#                     game.places.add(pl)
#
#
# def delete_places(game):
#     for s in game.places:
#         s.kill()
#
#
# def build_building(game, x, y, building_type):
#     try:
#         if check_place(game, x * TILESIZE, y * TILESIZE) and \
#                 check_building(game, x * TILESIZE, y * TILESIZE) and \
#                 check_cost(game, building_type[COST]):
#             if put_building(game, x, y, building_type) is None:
#                 return
#             pay(game, building_type[COST])
#     except IndexError:
#         pass
#
#
# def put_building(game, x, y, building_type):
#     if building_type[TYPE] == DYNAMIC:
#         new_house = buildings.DynamicBuilding(game, x, y, building_type)
#     elif building_type[TYPE] == STATIC:
#         new_house = buildings.StaticBuilding(game, x, y, building_type)
#     elif building_type[TYPE] == WAREHOUSE:
#         new_house = buildings.StorageBuilding(game, x, y, building_type)
#     else:
#         return None
#     game.houses.add(new_house)
#     game.town_sprites.add(new_house)
#     return new_house
#
#
# def check_place(game, b_x, b_y):
#     for p in game.places:
#         if p.x == b_x and p.y == b_y:
#             return True
#     return False
#
#
# def check_building(game, new_x, new_y):
#     for h in game.houses:
#         if h.x == new_x and h.y == new_y:
#             return False
#     return True
#
#
# def check_cost(game, cost):
#     for res in cost:
#         if cost[res] > game.resources[res][COUNT]:
#             return False
#     return True
#
#
# def pay(game, cost):
#     for res in cost:
#         game.resources[res][COUNT] -= cost[res]
