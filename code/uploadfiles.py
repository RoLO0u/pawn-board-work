from csv import reader
import pygame

def import_csv(path: str) -> list:

    terrain_map = []

    with open(path) as raw:

        level = reader(raw, delimiter=",")

        for row in level:
            terrain_map.append(list(row))

    return terrain_map

def import_cut_files(path: str, TILE_SIZE: tuple|list, RESIZE_TO: tuple|list):
    
    image = pygame.image.load(path).convert_alpha()
    
    tile_num_x = int(image.get_size()[0] / TILE_SIZE[0])
    tile_num_y = int(image.get_size()[1] / TILE_SIZE[1])

    cut_tiles = []
    for row in range(tile_num_y):
        y = row * TILE_SIZE[1]
        for col in range(tile_num_x):
            x = col * TILE_SIZE[0]
            new_image = pygame.Surface(TILE_SIZE)
            new_image.blit(image,(0, 0), pygame.Rect(x, y, *TILE_SIZE))
            new_image = pygame.transform.scale(new_image, RESIZE_TO)
            cut_tiles.append(new_image)
    
    return cut_tiles