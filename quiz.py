''' Quiz) 하늘에서 떨어지는 똥 피하기 게임을 만드시오

[게임조건]
1. 캐릭터는 화면 가장 아래에 위치, 좌우로만 이동 가능
2. 똥은 화면 가장 위에서 떨어짐, x 좌표는 매번 랜덤으로 설정
3. 똥은 2개씩 떨어짐(하나씩 떨어지면 재미없드라..) 다 떨어지면 다시 또 랜덤으로 떨어짐
4. 캐릭터가 똥과 충돌하면 게임 종료
5. FPS는 30으로 고정

[게임 이미지]
1. 배경: 640 * 480 (세로 가로) - background.png
2. 캐릭터: 70 * 70 - character.png
3. 똥: 70 * 70 - enemy.png

'''

import pygame
from random import *

pygame.init()  # ★초기화 필수

# 배경 사이즈,생성
screen_width = 640
screen_height = 480

screen = pygame.display.set_mode((screen_width, screen_height))

# 타이틀
pygame.display.set_caption("똥 피하기 게임")

# FPS(초당 프레임수)
clock = pygame.time.Clock()

# 현재 tick을 받아옴
# ★ while 안에 작성하면 X! 시간이 안 흐르고 계속 0으로 뜸
start_ticks = pygame.time.get_ticks()

# 배경 이미지 불러오기
background = pygame.image.load("D:\\dev\\PythonWorkspace\\dong_quiz\\dong_background.png")



# 캐릭터(스프라이트) 불러오기. 캐릭터 생성
character = pygame.image.load("D:\\dev\\PythonWorkspace\\dong_quiz\\dong_character.png")
character_size = character.get_rect().size  # 이미지의 가로크기/세로크기를 구해옴
character_width = character_size[0]   # 캐릭터의 가로크기
character_height = character_size[1]  # 캐릭터의 세로크기
character_x_pos = (screen_width / 2) - (character_width / 2)  # 화면 가로의 절반 크기에 해당하는 곳에 위치(캐릭터의 시작위치)
character_y_pos = screen_height - character_height # 화면 세로 크기 가장 아래에 해당하는 곳에 위치(캐릭터의 시작위치)


# 적 불러오기. 적 생성
enemy_1 = pygame.image.load("D:\\dev\\PythonWorkspace\\dong_quiz\\dong_enemy.png")
enemy_1_size = enemy_1.get_rect().size
enemy_1_width = enemy_1_size[0]
enemy_1_height = enemy_1_size[1]

enemy_1_x_pos = randint(0, (screen_width) - (character_width)) #  생성 위치 랜덤 
enemy_1_y_pos = 0  # y값은 스피드로 인해 밑으로 떨어지는거라서 초기값 0
enemy_1_speed = randint(10, 20)


enemy_2 = pygame.image.load("D:\\dev\\PythonWorkspace\\dong_quiz\\dong_enemy.png")
enemy_2_size = enemy_1.get_rect().size
enemy_2_width = enemy_1_size[0]
enemy_2_height = enemy_1_size[1]

enemy_2_x_pos = randint(0, (screen_width) - (character_width))
enemy_2_y_pos = 0
enemy_2_speed = randint(10, 20)





# 폰트 정의
game_font = pygame.font.Font(None, 40)  # 시간표시로 쓸 폰트 정의
gameover_font = pygame.font.Font(None, 60)  # 게임오버시 쓸 폰트 정의
gameover_text = gameover_font.render("Game Over",True,(255,0,0))  # ★ 폰트 정의 후 그려주기(.render)




# 이동할 좌표
to_x = 0
to_y = 0

# 이동 속도
character_speed = 0.8

running = True  # 게임이 진행중인가?
while running:
    dt = clock.tick(30)  # 게임화면의 초당 프레임 수를 설정



    for event in pygame.event.get():   # 사용자로 인한 동작이 들어오는지 체크
        if event.type == pygame.QUIT:  # 만약 사용자가 창을 닫으면
            running = False  # 게임 진행중 X


        ''' 게임 캐릭터 움직임 처리 '''
        if event.type == pygame.KEYDOWN:  
            if event.key == pygame.K_LEFT:  # 캐릭터를 왼쪽으로
                to_x -= character_speed  # to_x = to_x - 5 
            elif event.key == pygame.K_RIGHT: #캐릭터를 오른쪽으로
                to_x += character_speed

        # 키를 떼면 멈춤(pygame.KEYUP)
        if event.type == pygame.KEYUP:  
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:   
                to_x = 0



    ''' ★경과 시간 계산 while문 안에 작성할것 '''
    # 경과 시간 계산 (경과 시간을 '초' 로 환산하기 위해 1000으로 나눔)
    # (현재tick - 시작tick) / 1000  => 시작으로 부터 1초경과 2초경과 3초경과 그런 값 얻어냄
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000  


    # ★ 시간(elapsed_time)을 str 형태로 변환해주고 출력할수있게 바꿔주는 과정
    # game_font.render( str(int(출력할글자)), True, (글자,색상,이다) )
    # .render 텍스트를 그려줄때 사용
    timer = game_font.render(str(int(elapsed_time)), True, (255, 255, 255))


    ''' 게임 캐릭터 위치 처리 '''
    # 프레임이 달라진다고 해서 이동 속도가 달라져선 안됨 -> 고로, 키보드 입력에 따라 위치가 달라지는 부분에 * dt를 해준다
    character_x_pos += to_x * dt  # if event.type == pygame.KEYDOWN: 문에서 받아낸 결과를 캐릭터의 x 위치에 더해줌
                                  
    # 가로 경계값 처리
    if character_x_pos < 0:  # 0 보다 작다-> 왼쪽 화면에서 벗어남
       character_x_pos = 0  
    elif character_x_pos > screen_width - character_width:  # 스크린 화면보다 크다 -> 오른쪽 화면에서 벗어남
         character_x_pos = screen_width - character_width
 

    ''' 적 위치 처리 '''
    # 아래로만 떨어짐(y만 필요) 이 y값이 스피드값으로 인해 점점 밑으로 떨어진다
    # 그래서 y좌표에 speed를 더함
    enemy_1_y_pos += enemy_1_speed

    # 화면 밑까지 다 떨어졌다(화면을 넘어서서 떨어졌다)
    if enemy_1_y_pos > screen_height:
        enemy_1_y_pos = 0  # 다시 화면 맨 위로 올림
        enemy_1_x_pos = randint(0, (screen_width) - (character_width)) # 랜덤으로 적 생성이 또 되어야하니까!


    enemy_2_y_pos += enemy_2_speed

    if enemy_2_y_pos > screen_height:
        enemy_2_y_pos = 0
        enemy_2_x_pos = randint(0, (screen_width) - (character_width))


    ''' 화면에 표시하기 '''
    # 배경/캐릭터/적/시간 화면에 띄우기
    screen.blit(background,(0,0))
    screen.blit(character,(character_x_pos,character_y_pos))
    screen.blit(enemy_1,(enemy_1_x_pos,enemy_1_y_pos))
    screen.blit(enemy_2,(enemy_2_x_pos,enemy_2_y_pos))
    screen.blit(timer, (10,10))
    

    ''' 충돌 처리 '''
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_1_rect = enemy_1.get_rect()
    enemy_1_rect.left = enemy_1_x_pos
    enemy_1_rect.top = enemy_1_y_pos

    enemy_2_rect = enemy_2.get_rect()
    enemy_2_rect.left = enemy_2_x_pos
    enemy_2_rect.top = enemy_2_y_pos

    

    if character_rect.colliderect(enemy_1_rect):
        screen.blit(gameover_text,(210,125))
        print("충돌 발생")
        running = False
    elif character_rect.colliderect(enemy_2_rect):
        screen.blit(gameover_text,(210,125))
        print("충돌 발생")
        running = False 

    
    # ★ 화면을 계속계속 호출->배경이 쭉 있는것처럼 보이게
    # ★ 충돌 시 Game over라고 띄우고 싶은데, 이게 위쪽의 '화면에 표시하기' 파트에 함께 있으면
    # ★ Game over 띄워주는건 갱신이 안되서 안보임 그래서 맨 아래에 위치
    pygame.display.update()
     

pygame.time.delay(2000)  # 충돌 후 바로 꺼지는게 아니라, 2초 딜레이
pygame.quit() 