import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self, cords: tuple|list, TILE_SIZE: tuple|list) -> None:
        super().__init__()

        self.frames = [pygame.image.load(r"images\player_stand.png")]

        self.frames = [pygame.transform.scale(image.convert_alpha(), TILE_SIZE) for image in self.frames]

        self.image = self.frames[0]
        self.rect = self.image.get_rect(topleft=cords)
        self.hitbox = self.rect.inflate(-5, -15)

        self.TILE_SIZE = TILE_SIZE
        self.speed = 5

        self.facing = pygame.Vector2()

    def get_input(self) -> None:

        self.keys = pygame.key.get_pressed()

        if self.keys[pygame.K_LEFT] or self.keys[pygame.K_a]:
            self.facing.x = -1
            self.image = self.frames[0]
        elif self.keys[pygame.K_RIGHT] or self.keys[pygame.K_d]:
            self.facing.x = 1
            self.image = self.frames[0]
        else: self.facing.x = 0
        if self.keys[pygame.K_UP] or self.keys[pygame.K_w]:
            self.facing.y = -1
            self.image = self.frames[0]
        elif self.keys[pygame.K_DOWN] or self.keys[pygame.K_s]:
            self.facing.y = 1
            self.image = self.frames[0]
        else: self.facing.y = 0

    def move(self, collide_groups:list) -> None:

        if self.facing.magnitude() != 0:
            self.facing = self.facing.normalize()

        self.hitbox.x += self.facing.x * self.speed
        self.check_collisions(collide_groups, "horizontal")
        self.hitbox.y += self.facing.y * self.speed
        self.check_collisions(collide_groups, "vertical")
        self.rect.center = self.hitbox.center

    def check_collisions(self, collide_groups: list, direction: str) -> None:

        if direction == "horizontal":
            for colliding_group in collide_groups:
                for sprite in colliding_group:
                    if sprite.hitbox.colliderect(self.hitbox):

                        move_dice = True if sprite.type == "dice" else False

                        if self.facing.x > 0: # move right
                            self.hitbox.right = sprite.hitbox.left
                            if move_dice:
                                sprite.roll("right")
                        elif self.facing.x < 0: # move left
                            self.hitbox.left = sprite.hitbox.right
                            if move_dice:
                                sprite.roll("left")

        elif direction == "vertical":
            for colliding_group in collide_groups:
                for sprite in colliding_group:
                    if sprite.hitbox.colliderect(self.hitbox):

                        move_dice = True if sprite.type == "dice" else False

                        if self.facing.y > 0: # move down
                            self.hitbox.bottom = sprite.hitbox.top
                            if move_dice:
                                    sprite.roll("bottom")
                        elif self.facing.y < 0: # move up
                            self.hitbox.top = sprite.hitbox.bottom
                            if move_dice:
                                    sprite.roll("top")

    def update(self, collide_groups: list) -> None:
        
        self.get_input()
        self.move(collide_groups)