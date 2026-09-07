import pygame
from logger import log_state
from constants import SCREEN_HEIGHT,SCREEN_WIDTH
def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type==pygame.quit:
                return
        screen.fill("black")
        pygame.display.flip()

if __name__ == "__main__":
    main()
