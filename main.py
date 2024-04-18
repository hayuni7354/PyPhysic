import pygame
import numpy as np
pygame.init() #초기화

#화면 크기 설정
screen_width = 480 #가로 크기
screen_height = 640 #세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("PyPhysic")

# numpy float 출력 옵션 변경(소수점 3자리까지 출력, array의 원소 값 자체가 변경되지는 않음)
np.set_printoptions(precision=3, suppress=True)

class Box:
    def __init__(self, x, y):
        self.s = np.array([float(x),float(y)])
        self.v = np.array([0.0,0.0])
        self.onGround = False
    def move(self):
        force = np.array([0.0,0.0])
        force[1] += 0.01
        m = self.checkGround(grounds)
        if(self.onGround):
            if(m != 0):
                sint = (1 + m**(-2))**(-1/2)
            else:
                sint = 0
            cost = (1 + m**2)**(-1/2)
            rotate = np.array([[cost, -sint],[sint, cost]])
            temp = np.matmul(rotate, force)
            temp[1] *= -100
            rotate = np.array([[cost, sint],[-sint, cost]])
            temp = np.matmul(rotate, temp)
            force = temp
            print(force)
        self.v[0] += force[0]
        self.v[1] += force[1]
        self.s[0] += self.v[0]
        self.s[1] += self.v[1]
    def draw(self):
        pygame.draw.rect(screen, (200,200,200), [self.s[0] - 30, self.s[1] - 30, 30, 30], 3)
    def checkGround(self, gs):
        self.onGround = False
        for g in gs:
            if(abs(self.s[1] + 30 - g.y) < 2 and not b.onGround):
                self.onGround = True
                return g.m
        return None


class Ground:
    def __init__(self, m, y):
        self.m = m
        self.y = y
    def draw(self):
        pygame.draw.line(screen, (255, 0, 255), [0,self.y], [1000, self.y + 1000 * self.m], 2)


#이벤트 루프
running = True #게임 진행 여부에 대한 변수 True : 게임 진행 중
clock = pygame.time.Clock()
boxs = [Box(100,100)]
grounds = [Ground(0, 500)]

while running:
    for event in pygame.event.get(): #이벤트의 발생 여부에 따른 반복문
        if event.type == pygame.QUIT: #창을 닫는 이벤트 발생했는가?
            running = False

    clock.tick(600)
    screen.fill((0, 0, 0))
    for g in grounds:
        g.draw()
    for b in boxs:
        b.move()
        b.draw()

    #screen.blit(background, (0, 0)) #배경에 이미지 그려주고 위치 지정
    pygame.display.update()



#pygame 종료
pygame.quit()