# IMPORT MODULES
import pygame as pg
import random

pg.font.init()
pg.mixer.init()

# DEFINE WINDOW SIZE
WIDTH = 800
HEIGHT = 600

# DEFINE COLORS
BLACK = (0, 0, 0)
RED = (255, 0 , 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

# ------ MAKE WINDOW CLASS ------
class Window (object):

    def __init__(self):
        # SETUP WINDOW CONSTANTS
        self.running = False
        self.background = pg.image.load("space.png")
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()
        self.FPS = 60
        self.POINTS = 0
        pg.mixer.music.load("Drama_Music.ogg")
        pg.mixer.music.play(-1)
        self.enemy_dead = pg.mixer.Sound("gunshot.ogg")
        self.player_dead = pg.mixer.Sound("explosion.ogg")

    # --- MAKE FUNCTION THAT RESETS THE ENTIRE GAME ---
    def START(self):
        # DEFINE PLAYER ATTRIBUTES
        self.player = pg.image.load("player_ship.png")
        self.total_moves = 0
        self.x = WIDTH / 2
        self.y = 500
        self.vx = 0
        
        # DEFINE LASER ATTRIBUTES
        self.laser = pg.image.load("laser.png")
        self.laser_sound = pg.mixer.Sound("laser.wav")
        self.lx = self.x + 9
        self.ly = 625
        self.lyv = 0
        
        # DEFINE ENEMY 1 ATTRIBUTES
        self.enemy1 = pg.image.load("enemy_ship.png")
        self.ex1 = random.randint(15, 215)
        self.ey1 = 25
        self.evy1 = random.randint(1, 4)
        # DEFINE ENEMY 2 ATTRIBUTES
        self.enemy2 = pg.image.load("enemy_ship.png")
        self.ex2 = random.randint(230, 430)
        self.ey2 = 25
        self.evy2 = random.randint(1, 4)
        # DEFINE ENEMY 3 ATTRIBUTES
        self.enemy3 = pg.image.load("enemy_ship.png")
        self.ex3 = random.randint(445, 660)
        self.ey3 = 25
        self.evy3 = random.randint(1, 4)
        # DEFINE ENEMY 4 ATTRIBUTES
        self.enemy4 = pg.image.load("enemy_ship.png")
        self.ex4 = random.randint(685, WIDTH - 15)
        self.ey4 = 25
        self.evy4 = random.randint(1, 4)
        
        # DEFINE FONT ATTRIBUTES
        self.font = pg.font.SysFont("Comic Sans MS", 30)

        # ------ MAKE START MENU ------
        self.screen.blit(self.background, [0, 0])
        
        # INSTRUCTIONS
        self.start_text = self.font.render("Press Anywhere To Continue", False, GREEN)
        self.screen.blit(self.start_text, [WIDTH / 2 - 200, HEIGHT / 2 - 45])

        # MAKE HIGH SCORE SYSTEM
        self.highscore = open("highscore.txt", "r").read()
        self.highscore_text = self.font.render("HighScore: " + str(self.highscore), False, GREEN)
        
        # HIGHSCORE
        self.screen.blit(self.highscore_text, [WIDTH / 2 - 100, HEIGHT - 145])

        # MAKE "YOUR SCORE" TEXT
        self.your_score = self.font.render("Your Score: " + str(self.POINTS), False, WHITE)
        
        # PLAYER'S SCORE
        self.screen.blit(self.your_score, [WIDTH / 2 - 100, HEIGHT - 100])
        
        pg.display.update()
        
        # RESET POINTS
        self.POINTS = 0
        self.point_counter = self.font.render("Score: " + str(self.POINTS), False, RED)
        
        # MAKE USER-CLICK START GAME
        button_pressed = False
        while button_pressed == False:
            for event in pg.event.get():
                if event.type == pg.MOUSEBUTTONDOWN:
                        self.running = True
                        return 0

    # --- MAKE FUNCTION THAT STARTS PYGAME WINDOW ---
    def start_window(self):
        pg.init()

    # --- MAKE FUNCTION THAT PROCESSES GAME EVENTS ---
    def event_handling(self):
        # CHECK FOR QUIT EVENT
        for event in pg.event.get():
            if event.type == pg.QUIT:
                quit()
            # PLAYER CONTROLS
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    self.vx = -5
                    self.total_moves = -5
                if event.key == pg.K_RIGHT:
                    self.vx = 5
                    self.total_moves = 5
                # LASER CONTROLS
                if (self.ly == 625):
                    if event.key == pg.K_SPACE:
                        pg.mixer.Sound.play(self.laser_sound)
                        self.ly = self.y - 28
                        self.lyv = -5
            # MAKE PLAYER STOP WHEN MOVEMENT KEY IS RELEASED
            if event.type == pg.KEYUP:
                if event.key == pg.K_LEFT:
                    self.vx = 0
                if event.key == pg.K_RIGHT:
                    self.vx = 0

        # ADD VELOCITY CHANGE TO PLAYER POSITION
        self.x += self.vx

        # ADD VELOCITY TO LASER
        if (self.ly == 625):
             self.lx += self.vx
        self.ly += self.lyv

        # ADD VELOCITY CHANGE TO ENEMY POSITIONS
        self.ey1 += self.evy1
        self.ey2 += self.evy2
        self.ey3 += self.evy3
        self.ey4 += self.evy4

    # --- MAKE FUNCTION THAT CHECKS FOR OBJECT COLLSIONS ---
    def collision(self):
        # MAKE PLAYER WRAP AROUND SCREEN
        if (self.x > WIDTH):
            self.x = 0
        elif (self.x < 0):
            self.x = WIDTH
        elif (self.y > HEIGHT):
            self.y = 0
        if (self.y < 0):
            self.y = HEIGHT
            
        # MAKE ENEMIES RESPAWN
        if (self.ey1 > HEIGHT):
            self.enemy1 = pg.image.load("enemy_ship.png")
            self.ex1 = random.randint(15, 215)
            self.ey1 = 25
            self.evy1 = random.randint(2, 5)           
        if (self.ey2 > HEIGHT):
            self.enemy2 = pg.image.load("enemy_ship.png")
            self.ex2 = random.randint(230, 430)
            self.ey2 = 25
            self.evy2 = random.randint(2, 5)
        if (self.ey3 > HEIGHT):
            self.enemy3 = pg.image.load("enemy_ship.png")
            self.ex3 = random.randint(445, 660)
            self.ey3 = 25
            self.evy3 = random.randint(2, 5)
        if (self.ey4 > HEIGHT):
            self.enemy4 = pg.image.load("enemy_ship.png")
            self.ex4 = random.randint(685, WIDTH - 15)
            self.ey4 = 25
            self.evy4 = random.randint(2, 5)
            
        # MAKE PLAYER DIE WHEN HIT BY ENEMY
        self.x = int(self.x) ; self.y = int(self.y)
        if (self.ex1 in range(self.x - 30, self.x + 40) and self.ey1 in range(self.y, self.y + 30)):
            self.player = pg.image.load("explosion.png")
            pg.mixer.Sound.play(self.player_dead)
            self.running = False
        if (self.ex2 in range(self.x - 30, self.x + 40) and self.ey2 in range(self.y, self.y + 30)):
            self.player = pg.image.load("explosion.png")
            pg.mixer.Sound.play(self.player_dead)
            self.running = False
        if (self.ex3 in range(self.x - 30, self.x + 40) and self.ey3 in range(self.y, self.y + 30)):
            self.player = pg.image.load("explosion.png")
            pg.mixer.Sound.play(self.player_dead)
            self.running = False
        if (self.ex4 in range(self.x - 30, self.x + 40) and self.ey4 in range(self.y, self.y + 30)):
            self.player = pg.image.load("explosion.png")
            pg.mixer.Sound.play(self.player_dead)
            self.running = False

        # MAKE ENEMIES DIE WHEN HIT BY LASER
        if (self.lx in range(self.ex1, self.ex1 + 30) and self.ly in range(self.ey1, self.ey1 + 30)):
            self.enemy1 = pg.image.load("explosion.png")
            pg.mixer.Sound.play(self.enemy_dead)
            self.POINTS += 5
            self.lx = self.x + 9
            self.lyv = 0
            self.ly = 625
            self.point_counter = self.font.render("Score: " + str(self.POINTS), False, RED)
        if (self.lx in range(self.ex2, self.ex2 + 30) and self.ly in range(self.ey2, self.ey2 + 30)):
            self.enemy2 = pg.image.load("explosion.png")
            pg.mixer.Sound.play(self.enemy_dead)
            self.POINTS += 5
            self.lx = self.x + 9
            self.lyv = 0
            self.ly = 625
            self.point_counter = self.font.render("Score: " + str(self.POINTS), False, RED)
        if (self.lx in range(self.ex3, self.ex3 + 30) and self.ly in range(self.ey3, self.ey3 + 30)):
            self.enemy3 = pg.image.load("explosion.png")
            pg.mixer.Sound.play(self.enemy_dead)
            self.POINTS += 5
            self.lx = self.x + 9
            self.lyv = 0
            self.ly = 625
            self.point_counter = self.font.render("Score: " + str(self.POINTS), False, RED)
        if (self.lx in range(self.ex4, self.ex4 + 30) and self.ly in range(self.ey4, self.ey4 + 30)):
            self.enemy4 = pg.image.load("explosion.png")
            pg.mixer.Sound.play(self.enemy_dead)
            self.POINTS += 5
            self.lx = self.x + 9
            self.lyv = 0
            self.ly = 625
            self.point_counter = self.font.render("Score: " + str(self.POINTS), False, RED)

        # MAKE LASER POSITION RESET WHEN IT GOES OFF THE SCREEN
        if (self.ly < -30):
            self.lx = self.x + 9
            self.lyv = 0
            self.ly = 625

    # --- MAKE FUNCTION THAT DRAWS OBJECTS TO SCREEN ---
    def draw(self):
        # DRAW BACKGROUND IMAGE
        self.screen.blit(self.background, [0, 0])
        # DRAW PLAYER
        self.screen.blit(self.player, [self.x, self.y])
        # DRAW LASER
        self.screen.blit(self.laser, [self.lx, self.ly])
        # DRAW ENEMIES
        self.screen.blit(self.enemy1, [self.ex1, self.ey1]) #1
        self.screen.blit(self.enemy2, [self.ex2, self.ey2]) #2
        self.screen.blit(self.enemy3, [self.ex3, self.ey3]) #3
        self.screen.blit(self.enemy4, [self.ex4, self.ey4]) #4
        # DRAW SCORE COUNTER
        self.screen.blit(self.point_counter, [10, HEIGHT - 50])
        

    # --- MAKE A FUNCTION THAT RENDERS DRAWN OBJECTS TO THE SCREEN ---
    def render(self):
        pg.display.update()
        self.clock.tick(self.FPS)

# ASSIGN VARIABLE TO WINDOW CLASS
Game = Window()

# -- MAKE A FUNCTION THAT STARTS RESET
def START_SCREEN():
    if __name__ == '__main__':
        Game.start_window()
        Game.START()
        LOOP()

# --- MAKE A FUNCTION THAT ACTS AS A GAME LOOP ---
def LOOP():
        while Game.running:
            Game.event_handling()
            Game.collision()
            Game.draw()
            Game.render()
        if (Game.POINTS > int(Game.highscore)):
            Game.new_highscore = open("highscore.txt", "w")
            Game.new_highscore.write(str(Game.POINTS))
            Game.new_highscore.close()
        START_SCREEN()

# CALL ON START FUNCTION TO INITIALIZE THE GAME
START_SCREEN()
    

