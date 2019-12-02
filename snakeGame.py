# Game Made by Rúben Príncipe
# Inspiration and help https://www.pygame.org/project/3314
# Importing pygame, system and random
import pygame as pg
import sys, random

def collide(x1, y1, x2, y2, x3, y3, x4, y4):
    if (x3 + x4) > x1 > x3 and\
    (y3 + y4) > y1 > y3 or\
    (x3 + x4) > x2 >x3 and\
    (y3 + y4) > y2 > y3:
        return True
    else:
        return False

def collide2(x1, y1, x2, y2, x3, y3, x4, y4, size):
    if (x3 + (11 * size)) > x1 > x3 - 1 and\
    (y3 + (11 * size)) > y1 > y3 - 1 or\
    (x3 + (11 * size)) > x2 >x3 - 1 and\
    (y3 + (11 * size)) > y2 > y3 - 1:
        return True
    else:
        return False

def collide3(x1, y1, x2, y2, x3, y3, x4, y4, size):
    if (x3 + (10 * size)) > x1 > x3 and\
    (y3 + (10 * size)) > y1 > y3 or\
    (x3 + (10 * size)) > x2 > x3 and\
    (y3 + (10 * size)) > y2 > y3:
        return True
    else:
        return False

class snake():
    def __init__(self, speed, size):
        # Snake Start position
        self.pos = [random.randrange(10, 780, 10),random.randrange(10, 580, 10)]
        # Snake Size
        self.image = pg.Surface((10 * size, 10 * size))
        # Snake color
        self.image.fill((255, 255, 255))
        # Snake speed
        self.speed = speed
        self.size = size
        self.images = []
        self.old_pos = [[20,20]]
        self.direction = [0,0]
        self.score = 0

    # Turn right
    def right(self):
        self.direction = [self.speed, 0]

    # Turn left
    def left(self):
        self.direction = [-self.speed, 0]

    # Turn up
    def up(self):
        self.direction = [0, -self.speed]

    # Turn down
    def down(self):
        self.direction = [0, self.speed]

    def update(self):
        if self.old_pos[-1] != self.pos:
            self.old_pos.append([self.pos[0], self.pos[1]])
        self.pos[0] += self.direction[0]
        self.pos[1] += self.direction[1]
        a = 1
        for x in self.images:
            x[1] = self.old_pos[int(a * ((-11 * self.size) / self.speed))]
            a += 1

    def check_collisions(self, x):
        c = collide(self.pos[0], self.pos[1], self.pos[0]\
        + 10,self.pos[1] + 10,
        x[0], x[1], x[0] + 10, x[1] + 10)
        return c

    def check_apple(self, x):
        c = collide2(self.pos[0], self.pos[1],\
        self.pos[0] + 10, self.pos[1] + 10, x[0],\
        x[1], x[0] + 10, x[1] + 10, self.size)
        return c

    def check_collisions2(self, x):
        c = collide3(self.pos[0], self.pos[1],\
        self.pos[0] + 10, self.pos[1] + 10, x[0],\
        x[1], x[0] + 10, x[1] + 10, self.size)
        return c

    def add_apple(self):
        self.score += 1
        block = pg.Surface((10 * self.size, 10 * self.size))
        block.fill((200, 200, 200))
        self.images.append([block, [10, 10]])

class apple():
    def __init__(self,size):
        # apple position
        self.pos = [random.randrange(10, 780, 10),random.randrange(10, 580, 10)]
        # Apple size
        self.image = pg.Surface((10 * size, 10 * size))
        # Apple colour
        clr1 = random.randint(0, 255)
        clr2 = random.randint(0, 255)
        clr3 = random.randint(0, 255)
        self.image.fill((clr1, clr2, clr3))

class game():
    def __init__(self, speed, size = 1):
        self.screen = pg.display.set_mode((800, 600))
        pg.display.set_caption('Snake Game')
        self.snake = snake(speed, size)
        self.blocks = []
        self.score = 0
        self.size = size
        self.left, self.right, self.up, self.down = False, False, False, False
        self.hover = False
        self.click0 = False
        color = (255, 255, 255)

        txts = pg.font.SysFont('Courier New', 50).render(str(self.snake.score), True, (255, 255, 255))
        txtrect = txts.get_rect()
        txtrect.topleft = (480, 200)
        self.screen.blit(txts, txtrect)

        # Up bar
        for x in range(0, 800, 10):
            t = pg.Surface((10, 10))
            t.fill(color)
            self.blocks.append([t, [x, 0]])
        
        # Down bar
        for x in range(0, 800, 10):
            t = pg.Surface((10, 10))
            t.fill(color)
            self.blocks.append([t, [x, 590]])

        # Left bar
        for x in range(0, 600, 10):
            t = pg.Surface((10, 10))
            t.fill(color)
            self.blocks.append([t, [0, x]])

        # Right bar
        for x in range(0, 600, 10):
            t = pg.Surface((10, 10))
            t.fill(color)
            self.blocks.append([t, [790, x]])

        self.apple = apple(size)

    # When player lose
    def over(self):
        while 1:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()

            for x in self.blocks:
                self.screen.blit(x[0], x[1])

            txts = pg.font.SysFont('Courier New', 50).render('Game Over!', True, (255, 255, 255))
            txtrect = txts.get_rect()
            txtrect.topleft = (250, 150)
            self.screen.blit(txts, txtrect)

            txts = pg.font.SysFont('Courier New', 50).render('Score:', True, (255, 255, 255))
            txtrect = txts.get_rect()
            txtrect.topleft = (260, 200)
            self.screen.blit(txts, txtrect)

            txts = pg.font.SysFont('Courier New', 50).render(str(self.snake.score), True, (255, 255, 255))
            txtrect = txts.get_rect()
            txtrect.topleft = (480, 200)
            self.screen.blit(txts, txtrect)

            pg.display.update()
            self.make_button((330, 400, 100, 50),'Restart', [(255, 255, 255), (200, 200, 200)], action = lambda:restart())

            if self.hover == True:
                click = pg.mouse.get_pressed()
                if click[0] == 1:
                    self.click0 = True

                if self.click0 == True:
                    if click[0] == 0:
                        self.buttonclick()
                        self.click0 = False

    # Used to make buttons
    def make_button(self, pos, text, color, action = None, textsize = 20):
        mouse = pg.mouse.get_pos()
        oldpos = pos
        rect = pg.Rect(pos)
        pos = rect.topleft
        rect.topleft = 0, 0
        rectangle = pg.Surface(rect.size, pg.SRCALPHA)
        
        circle = pg.Surface([min(rect.size) * 3] * 2, pg.SRCALPHA)
        pg.draw.ellipse(circle, (0, 0, 0), circle.get_rect(), 0)
        circle  = pg.transform.smoothscale(circle, [int(min(rect.size) * 0.5)] * 2)
        
        radius = rectangle.blit(circle, (0, 0))
        radius.bottomright = rect.bottomright
        rectangle.blit(circle, radius)
        radius.topright = rect.topright
        rectangle.blit(circle, radius)
        radius.bottomleft = rect.bottomleft
        rectangle.blit(circle, radius)
        

        rectangle.fill((0, 0, 0), rect.inflate(-radius.w, 0))
        rectangle.fill((0, 0, 0), rect.inflate(0, -radius.h))
        pos = oldpos

        if (pos[0] + pos[2]) > mouse[0] > pos[0] and (pos[1] + pos[3]) > mouse[1] > pos[1]:
            self.hover = True
            self.buttonclick = action
            color = pg.Color( * color[1])
            alpha = color.a
            color.a = 0
        else:
            color = pg.Color( * color[0])
            alpha = color.a
            color.a = 0
            self.hover = False
            
        rectangle.fill(color, special_flags = pg.BLEND_RGBA_MAX)
        rectangle.fill((255, 255, 255, alpha), special_flags = pg.BLEND_RGBA_MIN)   
        self.screen.blit(rectangle, pos)
        txts = pg.font.SysFont('Courier New', textsize).render(text, True, (0, 0, 0))
        txtrect = txts.get_rect()
        txtrect.center =(pos[0] + pos[2] / 2), (pos[1] + pos[3] / 2)
        self.screen.blit(txts, txtrect)

    def reset(self):
        self.left, self.right, self.up, self.down = False, False, False, False

    def loop(self):
        self.game_over = False

        while self.game_over != True:

            self.screen.fill((0, 0, 0))
            self.snake.update()

            for x in self.blocks:
                if self.snake.check_collisions(x[1]) == True:
                    self.over()
                self.screen.blit(x[0], x[1])
            a = 0

            for x in self.snake.images:
                if a !=0:
                    if self.snake.check_apple(x[1]) == True:
                        self.over()
                self.screen.blit(x[0], x[1])
                a += 1

            if self.snake.check_apple(self.apple.pos) == True:
                self.snake.add_apple()
                del self.apple
                self.apple = apple(self.size)
            self.screen.blit(self.apple.image, self.apple.pos)
            self.screen.blit(self.snake.image, self.snake.pos)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_RIGHT:
                        if self.left == False:
                            self.reset()
                            self.snake.right()
                            self.right = True
                            
                    if event.key == pg.K_LEFT:
                        if self.right == False:
                            self.reset()
                            self.snake.left()
                            self.left = True

                    if event.key == pg.K_UP:
                        if self.down == False:
                            self.reset()
                            self.snake.up()
                            self.up = True

                    if event.key == pg.K_DOWN:
                        if self.up == False:
                            self.reset()
                            self.snake.down()
                            self.down = True
            pg.display.update()

class startmenu():

    # Define screen size, buttons colours
    def __init__(self):
        self.screen = pg.display.set_mode((800, 600))
        # Position, Size, Colour, Hover Colour
        self.b1 = '(150, 450, 100, 50), "Start", [(255, 255, 255), (200, 200, 200)], action = self.start'
        self.b2 = '(550, 450, 100, 50), "Exit", [(255, 255, 255), (200, 200, 200)], action = self.exit'
        self.buttons = [self.b1, self.b2]
        self.blocks = []
        self.size = 1
        self.click0, self.loads = False, False
        color = (255, 255, 255)

        # Up bar
        for x in range(0, 800, 10):
            t = pg.Surface((10, 10))
            t.fill(color)
            self.blocks.append([t, [x, 0]])
        
        # Down bar
        for x in range(0, 800, 10):
            t = pg.Surface((10, 10))
            t.fill(color)
            self.blocks.append([t, [x, 590]])

        # Left bar
        for x in range(0, 600, 10):
            t = pg.Surface((10, 10))
            t.fill(color)
            self.blocks.append([t, [0, x]])

        # Right bar
        for x in range(0, 600, 10):
            t = pg.Surface((10, 10))
            t.fill(color)
            self.blocks.append([t, [790, x]])
    
    # After used to make text's
    def make_text(self, x, y, text, size = 20, color = (0, 0, 0), a = False):
        txts = pg.font.SysFont('Courier New', size).render(text, True, color)
        txtrect = txts.get_rect()
        txtrect.topleft = (x, y)

        if a == True:
            txtrect.center = (x, y)
        self.screen.blit(txts, txtrect)
    
    # After used to make buttons
    def make_button(self, pos, text, color, action = None, textsize = 20):
        mouse = pg.mouse.get_pos()
        oldpos = pos
        rect = pg.Rect(pos)
        pos = rect.topleft
        rect.topleft = 0,0
        rectangle = pg.Surface(rect.size,pg.SRCALPHA)
        
        circle = pg.Surface([min(rect.size) * 3] * 2, pg.SRCALPHA)
        pg.draw.ellipse(circle, (0, 0, 0), circle.get_rect(), 0)
        circle  = pg.transform.smoothscale(circle, [int(min(rect.size) * 0.5)] * 2)
        
        radius = rectangle.blit(circle, (0, 0))
        radius.bottomright = rect.bottomright
        rectangle.blit(circle, radius)
        radius.topright = rect.topright
        rectangle.blit(circle, radius)
        radius.bottomleft = rect.bottomleft
        rectangle.blit(circle, radius)
        

        rectangle.fill((0, 0, 0), rect.inflate(-radius.w, 0))
        rectangle.fill((0, 0, 0), rect.inflate(0, -radius.h))
        pos = oldpos

        if (pos[0] + pos[2]) > mouse[0] > pos[0] and (pos[1] + pos[3]) > mouse[1] > pos[1]:
            self.hover = True
            self.buttonclick = action
            color = pg.Color( * color[1])
            alpha = color.a
            color.a = 0
        else:
            color = pg.Color( * color[0])
            alpha = color.a
            color.a = 0
            self.hover = False
            
        rectangle.fill(color, special_flags = pg.BLEND_RGBA_MAX)
        rectangle.fill((255, 255, 255, alpha), special_flags = pg.BLEND_RGBA_MIN)   
        self.screen.blit(rectangle, pos)
        self.make_text((pos[0] + pos[2] / 2), (pos[1] + pos[3] / 2), text, a = True, size = textsize)

    # Menu main loop
    def mainloop(self):
        while 1:
            # Background colour
            self.screen.fill((0, 0, 0))
            self.make_text(400, 200, 'SNAKE GAME', color = (255, 255, 255), size = 80, a = True)

            # Quit
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()

            for x in self.blocks:
                self.screen.blit(x[0],x[1])

            for x in self.buttons:
                exec('self.make_button(' + x + ')')
                if self.hover == True:
                    click = pg.mouse.get_pressed()
                    if click[0] == 1:
                        self.click0 = True
                    if self.click0 == True:
                        if click[0] == 0:
                            self.buttonclick()
                            self.click0 = False
            pg.display.update()

    # Game types
    def start(self):
        self.b1 = '(150, 450, 100, 50),"Normal", [(255, 255, 255), (200, 200, 200)], action = self.start3'
        self.b2 = '(550, 450, 100, 50),"Big", [(255 ,255, 255), (200, 200, 200)], action = self.start4'
        self.buttons = [self.b1,self.b2]
    
    # Game Dificulties for normal mode
    def start3(self):
        self.b1 = '(150, 450, 100, 50),"Easy", [(255, 255, 255), (200, 200, 200)], action = self.e'
        self.b2 = '(283, 450, 100, 50),"Normal", [(255, 255, 255), (200, 200, 200)], self.n'
        self.b3 = '(417, 450, 100, 50),"Hard", [(255, 255, 255), (200, 200, 200)], action = self.h'
        self.b4 = '(550, 450, 100, 50),"Expert", [(255, 255, 255), (200, 200, 200)], action = self.ex'
        self.buttons = [self.b1, self.b2,self.b3,self.b4]

    # Game Dificulties for big mode
    def start4(self):
        self.size = 2
        self.b1 = '(150, 450, 100, 50),"Easy", [(255, 255, 255), (200, 200, 200)], action = self.e'
        self.b2 = '(283, 450, 100, 50),"Normal", [(255, 255, 255), (200, 200, 200)], self.n'
        self.b3 = '(417, 450, 100, 50),"Hard", [(255, 255, 255), (200, 200, 200)], action = self.h'
        self.b4 = '(550, 450, 100, 50),"Expert", [(255, 255, 255), (200, 200, 200)], action = self.ex'
        self.buttons = [self.b1, self.b2,self.b3,self.b4]
    
    # Game Velocities low
    def e(self):
        start(0.25, self.size)

    # Game Velocities medium
    def n(self):
        start(0.5, self.size)

    # Game Velocities fast
    def h(self):
        start(1, self.size)

    # Game Velocities very fast
    def ex(self):
        start(2, self.size)

    # Exit
    def exit(self):
        sys.exit()

def start(speed, size):
    global g, m
    del m
    g = game(speed, size)
    g.loop()

def restart():
    global g
    del g
    menu()

def menu():
    global m
    pg.init()
    m = startmenu()
    m.mainloop()

menu()