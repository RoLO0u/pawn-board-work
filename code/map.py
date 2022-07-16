import pygame
from csv import reader
from code.uploadfiles import import_csv, import_cut_files

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos: tuple|list, size: tuple|list) -> None:
        super().__init__()
        self.image = pygame.Surface(size)
        self.image.fill("white")
        self.rect = self.image.get_rect(topleft = pos)

class StaticTile(Tile):

    def __init__(self, pos: tuple | list, size: tuple | list, image: pygame.Surface) -> None:
        super().__init__(pos, size)
        self.image = image

class Map:

    def __init__(self, paths: str, TILE_SIZE: tuple|list, ORIGINAL_TILE_SIZE: tuple|list) -> None:

        self.terrain = import_csv(paths[0])

        self.TILE_SIZE = TILE_SIZE
        
        self.tile_list = import_cut_files(r"images\bricks.png", ORIGINAL_TILE_SIZE, self.TILE_SIZE)
        
        self.terrain_sprites = self.create_tile_group("floor")
        self.wall_sprites = self.create_tile_group("wall")
        print(self.wall_sprites.sprites())

    def create_tile_group(self, type: str):

        sprite_group = pygame.sprite.Group()

        for row_index, row in enumerate(self.terrain):
            for col_index, val in enumerate(row):
                if val != "-1":
                    pos = col_index * self.TILE_SIZE[0], row_index * self.TILE_SIZE[1]

                    if type == "floor":
                        
                        tile_surface = self.tile_list[int(val)]
                        sprite = StaticTile(pos, self.TILE_SIZE, tile_surface)
                        sprite_group.add(sprite)
                    
                    elif type == "wall":

                        tile_surface = self.tile_list[int(val)]
                        sprite = StaticTile(pos, self.TILE_SIZE, tile_surface)
                        sprite_group.add(sprite)

        return sprite_group