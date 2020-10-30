import sys
import pygame
from pygame.locals import QUIT, Rect

pygame.init()

SURFACE = pygame.display.set_mode((1920,1080))
FPSCLOCK = pygame.time.Clock()
pygame.display.set_caption("Game")

class Player:
    p = [10,10]
    d = 'down'
    player = [0,0,0,0]
    player[0] = pygame.image.load("Player_00.png")
    player[1] = pygame.image.load("Player_04.png")
    player[2] = pygame.image.load("Player_08.png")
    player[3] = pygame.image.load("Player_12.png")
    def draw(n):
        if n == 'up':
            SURFACE.blit(Player.player[3],Player.p)
        elif n == 'down':
            SURFACE.blit(Player.player[0],Player.p)
        elif n == 'left':
            SURFACE.blit(Player.player[0],Player.p)
        elif n == 'right':
            SURFACE.blit(Player.player[0],Player.p)
    def move(d):
        if d == 'up':
            Player.p[1] -= 3
        elif d == 'down':
            Player.p[1] += 3
        elif d == 'left':
            Player.p[0] -= 3
        elif d == 'right':
            Player.p[0] += 3
            

def main():
    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                
            elif event.type == QUIT:
                pygame.quit()
                sys.exit()
         
        SURFACE.fill((255,255,255))

        key = pygame.key.get_pressed()
        
        if key[pygame.K_w]:
            Player.d = 'up'
            Player.move(Player.d)
        elif key[pygame.K_s]:
            Player.d = 'down'
            Player.move(Player.d)
        elif key[pygame.K_a]:
            Player.d = 'left'
            Player.move(Player.d)
        elif key[pygame.K_d]:
            Player.d = 'right'
            Player.move(Player.d)
        
        Player.draw(Player.d)
        
        pygame.display.update()
        FPSCLOCK.tick(30)

if __name__ == '__main__':
    main()
