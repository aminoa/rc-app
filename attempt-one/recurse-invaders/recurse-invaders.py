# Base of Recurse Invaders with PyGame

import pygame
import random

pygame.init()
pygame.joystick.init()
pygame.display.set_caption("Recurse Invaders")

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surface = pygame.Surface((40, 40))
        loaded_image = pygame.image.load("./ship.png").convert()
        self.image = pygame.transform.scale(loaded_image, (self.surface.get_width(), self.surface.get_height()), self.surface)
        self.rect = self.surface.get_rect()

        self.rect.x = SCREEN_WIDTH * (1/2)
        self.rect.y = SCREEN_HEIGHT * (9/10)
    
    def update(self, pressed_keys):
        if pressed_keys[pygame.K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[pygame.K_RIGHT]:
            self.rect.move_ip(5, 0)
        
        # Walls
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
    
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surface = pygame.Surface((40, 40))
        loaded_image = pygame.image.load("./metroid.gif").convert()
        self.image = pygame.transform.scale(loaded_image, (self.surface.get_width(), self.surface.get_height()), self.surface)
        self.rect = self.surface.get_rect()

        self.rect.x = SCREEN_HEIGHT * (1/2)
        self.rect.y = SCREEN_HEIGHT * (1/2)

        self.speed = 2
    
    def update(self, flip_direction=False):
        self.rect.move_ip(-self.speed, 0)
        if flip_direction:
            self.speed = -self.speed
            # added to prevent enemies from getting stuck
            self.rect.x += 2 * -self.speed
    

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.player = Player()
        self.enemies = pygame.sprite.Group()
        
        # create initial list of metroids
        for i in range(1, 11):
            for j in range(1, 4):
                new_enemy = Enemy()
                new_enemy.rect.x = (i) * (1/10 * SCREEN_WIDTH)
                new_enemy.rect.y = (j) * (1/10 * SCREEN_HEIGHT)
                self.enemies.add(new_enemy)
    
    def update(self, pressed_keys):
        self.player.update(pressed_keys)

        # check if an enemy hits a boundary  
        flip_direction = False
        for enemy in self.enemies:
            if enemy.rect.left < -40 or enemy.rect.right > SCREEN_WIDTH + 40:
                flip_direction = True
                
        for enemy in self.enemies:
            enemy.update(flip_direction)


    def render(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.player.surface, self.player.rect)
        for entity in self.enemies:
            self.screen.blit(entity.surface, entity.rect)

        pygame.display.update()

        # limit game to 60fps
        self.clock.tick(60)

def main():
    game = Game()
    running = True

    while running:
        # poll for inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        
        # update inputs
        pressed_keys = pygame.key.get_pressed()

        game.update(pressed_keys)
        game.render()
        
    pygame.quit()

if __name__ == '__main__':
    main()