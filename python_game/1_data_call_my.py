import pygame
import os #운영체제 연결하는
import random
pygame.font.init()
pygame.init()

WIDTH, HEIGHT = 750, 800 #창만들기 변수 선언
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mygame") #게임 제목 나타내는

ENEMY_RED = pygame.image.load(os.path.join("image", "enemy_red.png"))

