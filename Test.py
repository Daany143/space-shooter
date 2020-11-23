import pygame, random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE=(65, 193, 244)
GREY=(135, 147, 165)
X = 0
Y = 1

# Set the width and height of the screen [width, height]
size = (400, 500)
screen = pygame.display.set_mode(size)

# Add images to be used
pygame.display.set_caption("My Game")
asteroid1 = pygame.image.load("asteroid.png").convert_alpha()
space_ship = pygame.image.load("spaceship5.png").convert_alpha()
bullet = pygame.image.load("bullet.png").convert_alpha()
spaceship_lives=pygame.image.load("SpaceshipLives.png").convert_alpha()
background_image = pygame.image.load("EditedBackgroundGameImager.jpg").convert()
background_image1 = pygame.image.load("backgroundstartimage.jpg").convert()
start_button = pygame.image.load("startbutton.png").convert_alpha()
modes = pygame.image.load("modes.png").convert_alpha()
modes1 = pygame.image.load("modes1.png").convert_alpha()
modes2 = pygame.image.load("modes2.png").convert_alpha()

# Code for space ship
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=space_ship
        self.rect=self.image.get_rect()
        self.rect.center=(200,450)
    #Space ship moving code
    def update(self):
        self.x_speed = 0
        self.y_speed = 0
        if event.type == pygame.KEYDOWN:
            # Figure out if it was an arrow key. If so
            # adjust speed.
            if event.key == pygame.K_LEFT:
                self.x_speed = -4

            elif event.key == pygame.K_RIGHT:
                self.x_speed = 4

            elif event.key == pygame.K_UP:
                self.y_speed = -3

            elif event.key == pygame.K_DOWN:
                self.y_speed = 3

            self.rect.y += self.y_speed
            self.rect.x += self.x_speed

            #Makes sure space ship doesnt move out of screen
            if self.rect.x > 320:
                self.rect.x = 320
            if self.rect.x < 1:
                self.rect.x = 1
            if self.rect.y > 415:
                self.rect.y = 415
            if self.rect.y < 2:
                self.rect.y = 1

        # User let up on a key
        elif event.type == pygame.KEYUP:
            # If it is an arrow key, reset vector back to zero
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                self.x_speed = 0
                self.rect.x += self.x_speed
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                self.y_speed = 0
                self.rect.y += self.y_speed

    #Position of laser to shoot from
    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)

#Laser code
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image=bullet
        self.rect=self.image.get_rect()
        self.rect.bottom=y
        self.rect.centerx=x
        self.speedy=-10
    def update(self):
        self.rect.y+=self.speedy
        if self.rect.bottom<0:
            self.kill()

#Asteroid mob code
asteroids=[]
class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image=asteroid1
        self.rect=self.image.get_rect()

        self.rect.y=random.randint(-400, 0)
        self.rect.x=random.randint(1, 400)
        asteroids.append([self.rect.x, self.rect.y])
    def update(self):
        self.rect.y += 2
        if self.rect.y > 499 :
            self.rect.x = random.randint(1, 400)
            self.rect.y = random.randint(-400,0)
pygame.init()
pygame.mixer.init()

# Loop until the user clicks the close button.
done = False

# Variables to be used
lives=5
score=0
clock = pygame.time.Clock()
all_sprites=pygame.sprite.Group()
mobs=pygame.sprite.Group()
bullets=pygame.sprite.Group()
player=Player()
screen_number = 0

all_sprites.add(player)


# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                player.shoot()

    #First starting screen
    if screen_number == 0:
        screen.fill(GREEN)
        #Mouse code
        mouse_pressed = pygame.mouse.get_pressed()[0]
        mouseX = pygame.mouse.get_pos()[0]
        mouseY = pygame.mouse.get_pos()[1]

        #Check to see if start button has been clicked
        if mouseX > 130 and mouseX < 269 and mouseY > 380 and mouseY < 442:
            if mouse_pressed == 1:
                screen_number = 1

        #Start screen text and start button image.
        screen.blit(background_image1, [0, -500])
        screen.blit(start_button, [130, 380])
        font2 = pygame.font.SysFont('Calibri', 65, True, False)
        text3 = font2.render("Space", True, BLUE)
        text9 = font2.render("Guardians", True, BLUE)
        screen.blit(text9, [60, 205])
        screen.blit(text3, [120, 150])
            # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

            # --- Limit to 60 frames per second
        clock.tick(60)


    #Second screen. Select user difficulty.
    if screen_number==1:
        screen.fill(GREEN)
        #Mouse positions
        mouse_pressed = pygame.mouse.get_pressed()[0]
        mouseX = pygame.mouse.get_pos()[0]
        mouseY = pygame.mouse.get_pos()[1]


        screen.blit(background_image1, [0, -500])
        screen.blit(modes1, [150, 180])
        screen.blit(modes2, [120, 240])
        screen.blit(modes, [150, 300])
        font10 = pygame.font.SysFont('Calibri', 45, True, False)
        text10 = font10.render("Select a difficulty:", True, GREY)
        screen.blit(text10, [10, 85])

        #Checks to see if specific difficulty was chosen.
        if mouseX >150 and mouseX<248 and mouseY>180 and mouseY<221:
            if mouse_pressed==1:
                for i in range(10):
                    m = Mob()
                    all_sprites.add(m)
                    mobs.add(m)
                screen_number=2

        if mouseX >120 and mouseX<276 and mouseY>240 and mouseY<286:
            if mouse_pressed==1:
                for i in range(20):
                    m = Mob()
                    all_sprites.add(m)
                    mobs.add(m)
                screen_number=2

        if mouseX >150 and mouseX<243 and mouseY>300 and mouseY<340:
            if mouse_pressed==1:
                for i in range(30):
                    m = Mob()
                    all_sprites.add(m)
                    mobs.add(m)
                screen_number=2

        pygame.display.flip()


    #Third screen. Game screen.
    if screen_number == 2:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        all_sprites.update()

        asteroids_to_delete = []
        # Check to see if laser hit asteroid
        hits2=pygame.sprite.groupcollide(mobs, bullets, True, True)
    #Deletes asteroid that laser hit.
        for i in range(len(asteroids)):
            current_asteroid = asteroids[i]
            if hits2:
                asteroids_to_delete.append(current_asteroid)
                score += 100
                break

        #Checks to see if asteroid space ship
        hits=pygame.sprite.spritecollide(player, mobs, True)
        #Will delete asteroid that hit space ship
        for i in range(len(asteroids)):
            current_asteroid = asteroids[i]
            if hits:
                asteroids_to_delete.append(current_asteroid)
                lives -= 1
                break
        for asteroid in asteroids_to_delete:
            asteroids.remove(asteroid)

        #Checks to see if user has died or destroyed all the asteroids.
        if len(asteroids)==0:
            screen_number = 3
        if lives==0:
            screen_number = 3
        # If you want a background image, replace this clear with blit'ing the
        # background image.
        screen.fill(BLACK)
        screen.blit(background_image, [0, 0])
        all_sprites.draw(screen)

        #Live counter
        for i in range(lives):
            f=40*i
            screen.blit(spaceship_lives,[f,0])
        font5 = pygame.font.SysFont('Calibri', 25, True, False)
        text6 = font5.render(str(score), True, WHITE)
        screen.blit(text6, [340, 10])

        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

    #Last screen
    if screen_number == 3:
        #Mouse code
        mouse_pressed = pygame.mouse.get_pressed()[0]
        mouseX = pygame.mouse.get_pos()[0]
        mouseY = pygame.mouse.get_pos()[1]

        screen.fill(RED)
        screen.blit(background_image1, [-180, -300])

        #Determines what text to be printed, in the case that that user succeds or loses.
        if lives==0:
            font = pygame.font.SysFont('Calibri', 50, True, False)
            text = font.render("Game Over!", True, RED)
            screen.blit(text, [85, 220])
        else:
            font7 = pygame.font.SysFont('Calibri', 70, True, False)
            text7 = font7.render("Victory!", True, BLUE)
            screen.blit(text7, [90, 220])
            font10 = pygame.font.SysFont('Calibri', 40, True, False)
            text10 = font10.render("You Scored:" + " " +str(score), True, GREY)
            screen.blit(text10, [40, 290])

        pygame.display.flip()
    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()