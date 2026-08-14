from pdb import runctx
from pickle import TRUE
import pygame
import math
import random
import time
pygame.init()


WIDTH, HEIGHT = 800, 800
TOP_BAR_HEIGHT = 50

# MILISECONDS TO DELAY TILL ANOTHER TARGET IS CREATED
TARGET_INCREMENT = 400
# DISTANCE OFF SET FROM SCREEN
TARGET_PADDING = 30
TARGET_EVENT = pygame.USEREVENT

LABEL_FONT = pygame.font.SysFont("Arial", 24)
BG_COLOR = (0, 25, 40)
LIVES = 3

# Initialize pyscreen with width and height
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Aim Trainer")

class Target:
    MAX_GROWTH = 30
    GROWTH_RATE = 0.2
    COLOR = "red"
    SECOND_COLOR = "white"
    
    def __init__(self, x, y):
        # Defining targets position (x, y)
        # Defining starting size and immediately start growth
        self.x = x
        self.y = y
        self.size = 0
        self.grow = True

    # Function that handles whether the target will grow or shrink
    def update(self):
        if self.size + self.GROWTH_RATE >= self.MAX_GROWTH:
            self.grow = False
            
        if self.grow:
            self.size += self.GROWTH_RATE
        else:
            self.size -= self.GROWTH_RATE
    
    def draw(self, win):
        # win is the window location, color of target, position on window, size of target
        pygame.draw.circle(win, self.COLOR, (self.x, self.y), self.size)
        pygame.draw.circle(win, self.SECOND_COLOR, (self.x, self.y), self.size * 0.8)
        pygame.draw.circle(win, self.COLOR, (self.x, self.y), self.size * 0.6)
        pygame.draw.circle(win, self.SECOND_COLOR, (self.x, self.y), self.size * 0.4)

    def collide(self, x, y):
        # Point of distance between 2 spots
        dist = math.sqrt((self.x - x)**2 + (self.y - y)**2)
        return dist <= self.size

def draw(win, targets):
    win.fill(BG_COLOR)
    for target in targets:
        target.draw(win)
    

def format_time(sec):
    milli = math.floor(int(sec * 1000 % 1000) / 100)
    seconds = int(round(sec % 60, 1))
    minutes = int(sec // 60)

    return f"{minutes:02d}:{seconds:02d}.{milli}"


def draw_top_bar(win, elapsed_time, targets_pressed, misses):
    speed = round(targets_pressed / elapsed_time, 1)

    pygame.draw.rect(win, "grey", (0, 0, WIDTH, TOP_BAR_HEIGHT))
    time_label = LABEL_FONT.render(
        f"Time: {format_time(elapsed_time)}", 1, "black"
    )
    speed_label = LABEL_FONT.render(
        f"Speed: {speed} t/s", 1, "black"
    )
    hits_label = LABEL_FONT.render(
        f"Hits: {targets_pressed}", 1, "black"
    )
    lives_label = LABEL_FONT.render(
        f"Lives: {LIVES - misses}", 1, "black"
    )
    # blit() will write this object on the screen with its set coordinates
    win.blit(time_label, (5, 5))
    win.blit(speed_label, (200, 5))
    win.blit(hits_label, (450, 5))
    win.blit(lives_label, (650, 5))

def end_screen(win, elapsed_time, targets_pressed, clicks):
    speed = round(targets_pressed / elapsed_time, 1)
    accuracy = round(targets_pressed / clicks * 100, 1)

    win.fill(BG_COLOR)
    time_label = LABEL_FONT.render(
        f"Time: {format_time(elapsed_time)}", 1, "white"
    )
    speed_label = LABEL_FONT.render(
        f"Speed: {speed} t/s", 1, "white"
    )
    hits_label = LABEL_FONT.render(
        f"Hits: {targets_pressed}", 1, "white"
    )
    accuracy_label = LABEL_FONT.render(
        f"Accuracy: {accuracy}", 1, "white"
    )

    win.blit(time_label, (get_middle(time_label), 100))
    win.blit(speed_label, (get_middle(speed_label), 200))
    win.blit(hits_label, (get_middle(hits_label), 300))
    win.blit(accuracy_label, (get_middle(accuracy_label), 400))

    pygame.display.update()

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                quit()


def get_middle(surface):
    return WIDTH / 2 - surface.get_width()/2


def main():
    run = True
    targets = []
    clock = pygame.time.Clock()
    # Below returns (x, y) position of mouse
    mouse_pos = pygame.mouse.get_pos()


    targets_pressed = 0
    clicks = 0
    misses = 0
    start_time = time.time()

    pygame.time.set_timer(TARGET_EVENT, TARGET_INCREMENT)

    while run:
        # Regulate the speed at which the code will run at 60 seconds
        clock.tick(60)
        click = False
        elapsed_time = time.time() - start_time
        
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            # Monitor "x" to cancel game
            if event.type == pygame.QUIT:
                run = False
                break

            # Get random (x, y) position on screen
            if event.type == TARGET_EVENT:
                x = random.randint(TARGET_PADDING + TOP_BAR_HEIGHT, WIDTH - TARGET_PADDING)
                y = random.randint(TARGET_PADDING, HEIGHT - TARGET_PADDING)
                target = Target(x, y)
                targets.append(target)
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                clicks += 1
                click = True


        for target in targets:
            target.update()
            # Quick removal from list
            if target.size <= 0:
                targets.remove(target)
                # Failed to hit the target before it disappears
                misses += 1

            if click and target.collide(*mouse_pos):
                targets.remove(target)
                targets_pressed += 1
            
        if misses >= LIVES:
            end_screen(WIN, elapsed_time, targets_pressed, clicks)
    
        draw(WIN, targets)
        draw_top_bar(WIN, elapsed_time, targets_pressed, misses)

        # Update the display after filling BG and drawing target
        pygame.display.update()


    pygame.quit()

if __name__ == "__main__":
    main()