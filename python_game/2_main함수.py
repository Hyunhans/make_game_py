import pygame
import os
import random
pygame.font.init()
pygame.init()

WIDTH, HEIGHT = 750, 800
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))  # 보여지는 윈도우(화면)을 셋팅한다. 클라스
pygame.display.set_caption("Mygame")

##################################
#01#  <게임에 사용할 이미지, 음악을 불러옵니다>
################################

# 이미지 로드
ENEMY_RED = pygame.image.load(
    os.path.join("image and sound", "enemy_red.png"))
ENEMY_YELLOW = pygame.image.load(
    os.path.join("image and sound", "enemy_green.png"))
ENEMY_PUPPLE = pygame.image.load(
    os.path.join("image and sound", "enemy_purple.png"))

# 플레이어 캐릭터
PLAYER_CHARACTER = pygame.image.load(
    os.path.join("image and sound", "player1.png"))
PLAYER_CHARACTER_1 = pygame.image.load(
    os.path.join("image and sound", "player1.png"))
PLAYER_CHARACTER_2 = pygame.image.load(
    os.path.join("image and sound", "player2.png"))
PLAYER_CHARACTER_3 = pygame.image.load(
    os.path.join("image and sound", "player3.png"))

# 레이져 이미지 로드
MISSILE_RED = pygame.image.load(
    os.path.join("image and sound", "enemy_red_missile.png"))
MISSILE_YELLOW = pygame.image.load(
    os.path.join("image and sound", "enemy_green_missile.png"))
MISSILE_PUPPLE = pygame.image.load(
    os.path.join("image and sound", "enemy_purple_missile.png"))

MISSILE_PLAYER = pygame.image.load(
    os.path.join("image and sound", "player1_missile.png"))
MISSILE_PLAYER_1 = pygame.image.load(
    os.path.join("image and sound", "player1_missile.png"))
MISSILE_PLAYER_2 = pygame.image.load(
    os.path.join("image and sound", "player2_missile.png"))
MISSILE_PLAYER_3 = pygame.image.load(
    os.path.join("image and sound", "player3_missile.png"))

# 배경
BG = pygame.transform.scale(pygame.image.load(
    os.path.join("image and sound", "background_forest.png")), (WIDTH, HEIGHT))

bg_music = pygame.mixer.music.load(
    os.path.join("image and sound", "background_music.mp3"))
pygame.mixer.music.play(-1) #-1은 연속적으로 사용한다는 의미

missile_sound = pygame.mixer.Sound(
    os.path.join("image and sound", "missile_sound.wav"))

#################################################################



###
#MAIN함수를 정의 합니다.
#MAIN함수는 게임의 실제 실행부분입니다.
#키조작, 적생성, 레벨업등등의 기능을 여기서 구현합니다.

def main():
   # pass  #그냥 형식적으로 사용해 둔
################
    FPS = 60   #
    clock = pygame.time.Clock()   #clock 실제시간을 가져오는 것
    run = True
    lost = False

    level = 0
    kill_score = 0
    main_font = pygame.font.SysFont("comicsans", 50)   #pygame 은 폰트를 설정해줘야 글을 쓸 수 있다. 

    while run:
        clock.tick(FPS)  #FPS 값에 따라서 FPS 이상으로 계산이 되지않도록 제어를 걸어주는 것.
        WINDOW.blit(BG, (0,0))

        level_label = main_font.render(f"LEVEL : {level}", 1, (255,255,255))
        WINDOW.blit(level_label, (WIDTH - level_label.get_width()-10, 10))
        kill_label = main_font.render(f"KILL : {kill_score}", 1, (255,255,255))
        WINDOW.blit(kill_label, (kill_label.get_width()+80, 10))
        
        pygame.display.update()#while roup 에 한번만 해주면 됨


        for event in pygame.event.get():  #일어난 event를 가져오는것
            if event.type == pygame.QUIT:  #x창을 누르는 행위
                quit()
                

main()