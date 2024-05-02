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
        self.delay = 0
    def move(self):
        force = np.array([0.0,0.0])
        force[1] += 0.0001
        m = self.checkGround(grounds)
        if(self.onGround):
            if(m != 0):
                sint = m / ((1 + m**2)**1/2)
                print(sint)
            else:
                sint = 0
            cost = 1 / ((1 + m**2)**1/2)
            rotate = np.array([[cost, -sint],[sint, cost]])
            tempf = np.matmul(rotate, force)
            tempv = np.matmul(rotate, self.v)
            tempf[1] = 0
            tempv[1] *= -0.5
            rotate = np.array([[cost, sint],[-sint, cost]])
            tempf = np.matmul(rotate, tempf)
            tempv = np.matmul(rotate, tempv)
            force = tempf
            self.v = tempv
        self.v[0] += force[0]
        self.v[1] += force[1]
        self.s[0] += self.v[0]
        self.s[1] += self.v[1]
    def draw(self):
        #pygame.draw.rect(screen, (200,200,200), [self.s[0] - 15, self.s[1] - 15, 30, 30], 3)
        pygame.draw.circle(screen, (200,200,200), [self.s[0] - 15, self.s[1]], 15, 3)
    def checkGround(self, gs):
        self.onGround = False
        for g in gs:
            if(g.m != 0):
                sint = g.m / ((1 + g.m**2)**1/2)
            else:
                sint = 0
            cost = 1 / ((1 + g.m**2)**1/2)
            if(abs((self.s[1] + 15*cost) - (g.y - g.m * self.s[0])) < cost and not b.onGround):
                self.onGround = True
                return g.m
                


class Ground:
    def __init__(self, m, y):
        self.m = m
        self.y = y
    def draw(self):
        pygame.draw.line(screen, (255, 0, 255), [0,self.y], [1000, self.y - 1000 * self.m], 3)



class Scene1: #제미니 사용
    def __init__(self):
        global boxs
        global grounds
        boxs = [Box(100,84)]
        grounds = [Ground(0, 500)]
        self.delay = 0
        self.obcount = 0
        pygame.display.flip()

    def observe(self):
        for b in boxs:
            if(self.delay > 0):
               self.delay  -= 1
            elif(abs(b.v[1]) < 0.001):
                print(484 - b.s[1])
                self.obcount += 1
                self.delay = 1000
                if(self.obcount >= 5):
                    global game
                    game = Scene2()

class Scene2:
    def __init__(self):
        global boxs
        global grounds
        boxs = [Box(400,-16)]
        grounds = [Ground(1/10, 500)]
        self.delay = 1
        self.obcount = 0
        pygame.display.flip()

    def observe(self):
        for b in boxs:
            if(self.delay > 0):
               self.delay  -= 1
            elif(abs(b.v[1]) < 0.001):
                print(484 - b.s[1])
                self.obcount += 1
                self.delay = 1000
                if(self.obcount >= 5):
                    global game
                    game = Scene2()

#이벤트 루프
running = True #게임 진행 여부에 대한 변수 True : 게임 진행 중
clock = pygame.time.Clock()
boxs = []
grounds = []
game = Scene2()

while running:
    for event in pygame.event.get(): #이벤트의 발생 여부에 따른 반복문
        if event.type == pygame.QUIT: #창을 닫는 이벤트 발생했는가?
            running = False

    clock.tick(6000)
    screen.fill((0, 0, 0))
    for g in grounds:
        g.draw()
    for b in boxs:
        b.move()
        b.draw()
    game.observe()

    #screen.blit(background, (0, 0)) #배경에 이미지 그려주고 위치 지정
    pygame.display.flip()



#pygame 종료
pygame.quit()