import pygame
from csv import reader
from code.uploadfiles import import_csv, import_cut_files

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos: tuple|list, size: tuple|list) -> None:
        super().__init__()
        self.image = pygame.Surface(size)
        self.image.fill("white")
        self.rect = self.image.get_rect(topleft = pos)
        self.type = None

class StaticTile(Tile):

    def __init__(self, pos: tuple | list, size: tuple | list, image: pygame.Surface) -> None:
        super().__init__(pos, size)
        self.image = image
        self.hitbox = self.rect.inflate(-10, -5)
    
class Dice(StaticTile):

    def __init__(self, pos: tuple | list, size: tuple | list, image: pygame.Surface, TILE_SIZE: tuple|list) -> None:
        super().__init__(pos, size, image)
        self.hitbox = self.rect
        self.type = "dice"
        self.TILE_SIZE = TILE_SIZE
        self.last_coords = pos

    def roll(self, align: str) -> None:
        
        self.last_coords = self.hitbox.center
        match align:
            case "right":
                self.hitbox.x += self.TILE_SIZE[0]
            case "left":
                self.hitbox.x -= self.TILE_SIZE[0]
            case "bottom":
                self.hitbox.y += self.TILE_SIZE[1]
            case "top":
                self.hitbox.y -= self.TILE_SIZE[1]

    def collide_check(self, collide_groups) -> None:

        for collide_group in collide_groups:
            for sprite in collide_group:
                if sprite.hitbox.colliderect(self.hitbox):
                    self.hitbox.center = self.last_coords
    
    def update(self, collide_groups) -> None:
        self.collide_check(collide_groups)

class Map:

    def __init__(self, paths: str, TILE_SIZE: tuple|list, ORIGINAL_TILE_SIZE: tuple|list) -> None:

        self.terrain = import_csv(paths[0])
        self.walls = import_csv(paths[1])
        self.dices = import_csv(paths[2])

        self.TILE_SIZE = TILE_SIZE
        
        self.tile_list = import_cut_files(r"images\bricks.png", ORIGINAL_TILE_SIZE, self.TILE_SIZE)
        self.dice_list = import_cut_files(r"images\dice5.png", ORIGINAL_TILE_SIZE, self.TILE_SIZE)
        
        self.bg_groups = [self.create_tile_group("floor", self.terrain)]
        self.fg_groups = [self.create_tile_group("wall", self.walls), self.create_tile_group("dice", self.dices)]

    def create_tile_group(self, type: str, terrain: list):

        sprite_group = pygame.sprite.Group()

        for row_index, row in enumerate(terrain):
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

                    elif type == "dice":

                        tile_surface = self.dice_list[int(val)]
                        sprite = Dice(pos, self.TILE_SIZE, tile_surface, self.TILE_SIZE)
                        sprite_group.add(sprite)

        return sprite_group