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

#class snake():
#class apple():
#class game():

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
            t=pg.Surface((10, 10))
            t.fill(color)
            self.blocks.append([t, [x, 0]])
        
        # Down bar
        for x in range(0, 800, 10):
            t=pg.Surface((10, 10))
            t.fill(color)
            self.blocks.append([t, [x, 590]])

        # Left bar
        for x in range(0, 600, 10):
            t=pg.Surface((10, 10))
            t.fill(color)
            self.blocks.append([t, [0, x]])

        # Right bar
        for x in range(0, 600, 10):
            t=pg.Surface((10, 10))
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
        self.b1 = '(150, 300,100,50),"Normal", [(0,255,0), (0,150,0)], action = self.start3'
        self.b2 = '(550, 300,100,50),"Big", [(0,255,0), (0,150,0)], action = self.start4'
        self.buttons = [self.b1,self.b2]
    
    # Game Dificulties for normal mode
    def start3(self):
        self.b1 = '(150, 300,100,50),"Easy", [(0,255,0), (0,150,0)], action = self.e'
        self.b2 = '(283, 300,100,50),"Normal", [(0,255,0), (0,150,0)], self.n'
        self.b3 = '(417, 300,100,50),"Hard", [(0,255,0), (0,150,0)], action = self.h'
        self.b4 = '(550, 300,100,50),"Expert", [(0,255,0), (0,150,0)], action = self.ex'
        self.buttons = [self.b1, self.b2,self.b3,self.b4]

    # Game Dificulties for big mode
    def start4(self):
        self.size = 2
        self.b1 = '(150, 300,100,50),"Easy", [(0,255,0), (0,150,0)], action = self.e'
        self.b2 = '(283, 300,100,50),"Normal", [(0,255,0), (0,150,0)], self.n'
        self.b3 = '(417, 300,100,50),"Hard", [(0,255,0), (0,150,0)], action = self.h'
        self.b4 = '(550, 300,100,50),"Expert", [(0,255,0), (0,150,0)], action = self.ex'
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

