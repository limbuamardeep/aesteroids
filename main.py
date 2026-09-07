import pygame
from logger import log_state
from constants import SCREEN_HEIGHT,SCREEN_WIDTH
from player import Player
def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    clock=pygame.time.Clock()
    dt=0.0
    player=Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type==pygame.quit:
                return
        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()
        dt=clock.tick(60)/1000
        player.update(dt)

if __name__ == "__main__":
    main()
