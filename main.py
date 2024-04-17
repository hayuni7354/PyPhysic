import pygame
pygame.init() #초기화

#화면 크기 설정
screen_width = 480 #가로 크기
screen_height = 640 #세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("PyPhysic")

class Box:
    def __init__(self, x, y):
        self.s = [x,y]
        self.v = [0,0]
    def move(self):
        force = [0,0]
        force[1] += 1
        self.v[0] += force[0]
        self.v[1] += force[1]
        self.s[0] += self.v[0]
        self.s[1] += self.v[1]
    def draw(self):
        pygame.draw.rect(screen, (200,200,200), [self.s[0] - 30, self.s[1] - 30, 30, 30], 3)
    def grounding(self, g):
        return abs(self.s[1] + 30 - g.y) < 1


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

    clock.tick(60)
    screen.fill((0, 0, 0))
    for g in grounds:
        g.draw()
    for b in boxs:
        onGround = False
        for g in grounds:
            if(b.grounding(g)):
                onGround = True
        if(not onGround):
            b.move()
        b.draw()

    #screen.blit(background, (0, 0)) #배경에 이미지 그려주고 위치 지정
    pygame.display.update()



#pygame 종료
pygame.quit()