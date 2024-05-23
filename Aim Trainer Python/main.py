import pygame
import random
import math 
import time

pygame.init()

width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Aim Trainer")

top_bar_height = 50

target_increment = 400
target_event = pygame.USEREVENT

target_padding = 30

lives = 10

label_font = pygame.font.SysFont("comicsans", 24)


class Target():
    """
    A class to represent a target in the Aim Trainer game.

    ...

    Attributes
    ----------
    x : int
        x-coordinate of the target
    y : int
        y-coordinate of the target
    size : float
        current size of the target
    grow : bool
        indicates if the target is growing or shrinking
    max_size : int
        maximum size of the target
    growth_rate : float
        rate at which the target grows or shrinks
    color_1 : str
        primary color of the target
    color_2 : str
        secondary color of the target

    Methods
    -------
    update():
        Updates the size of the target.
    draw(win):
        Draws the target on the given window.
    collide(x, y):
        Checks if a point (x, y) collides with the target.
    """
    max_size = 30
    growth_rate = 0.2
    color_1 = "red"
    color_2 = "white"
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 0
        self.grow = True
        
    def update(self):
        if self.size + self.growth_rate >= self.max_size:
            self.grow = False
            
        if self.grow:
            self.size += self.growth_rate
        else:
            self.size -= self.growth_rate
    def draw(self, win):
        pygame.draw.circle(win, self.color_1, (self.x, self.y), self.size)
        pygame.draw.circle(win, self.color_2, (self.x, self.y), self.size * 0.8)
        pygame.draw.circle(win, self.color_1, (self.x, self.y), self.size * 0.6)
        pygame.draw.circle(win, self.color_2, (self.x, self.y), self.size * 0.4)
        
    def collide(self, x, y):
        distance = math.sqrt((self.x-x)**2 + (self.y-y)**2) 
        return distance <= self.size


def draw(win, targets):
    win.fill("black")
    
    for target in targets:
        target.draw(win)
        

def format_time(secs):
    milli = math.floor(int(secs * 1000 % 1000) / 100)
    seconds = int(round(secs % 60, 1))
    minutes = int(secs // 60)
    
    return (f"{minutes:02d}: {seconds:02d}.{milli}")
    
def draw_top_bar(win, elapsed_time, targets_pressed, misses):
    pygame.draw.rect(win, "grey", (0, 0, width, top_bar_height))
    
    time_label = label_font.render(f"Time: {format_time(elapsed_time)}", 1, "black")
    
    if elapsed_time != 0:
        speed = round(targets_pressed / elapsed_time, 1)
    else:
        speed = 0
    speed_label = label_font.render(f"Speed: {speed} t/s", 1, "black")

    hits_label = label_font.render(f"Hits: {targets_pressed}", 1, "black")
    
    lives_label = label_font.render(f"Lives: {lives - misses}", 1, "black")
    
    win.blit(time_label, (5, 5))
    win.blit(speed_label, (200, 5))
    win.blit(hits_label, (450, 5))
    win.blit(lives_label, (650, 5))

    
def end_screen(win, elapsed_time, targets_pressed, clicks):
    win.fill("black")
    
    time_label = label_font.render(f"Time: {format_time(elapsed_time)}", 1, "white")
    
    speed = round(targets_pressed / elapsed_time, 1)
    speed_label = label_font.render(f"Speed: {speed} t/s", 1, "white")

    hits_label = label_font.render(f"Hits: {targets_pressed}", 1, "white")
    
    if clicks != 0:
        accuracy = round(targets_pressed / clicks * 100, 1)
    else:
        accuracy = 0
    accuracy_label = label_font.render(f"Accuracy: {accuracy}%", 1, "white")
    
    win.blit(time_label, (get_middle(time_label), 110))
    win.blit(speed_label, (get_middle(speed_label), 230))
    win.blit(hits_label, (get_middle(hits_label), 350))
    win.blit(accuracy_label, (get_middle(accuracy_label), 470))
    
    pygame.display.update()
    
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                quit()
    
def get_middle(surface):
    return width / 2 - surface.get_width()/2
        
def main():
    run = True
    targets = []
    clock = pygame.time.Clock()
    
    
    target_pressed = 0
    clicks = 0
    misses = 0
    start_time = time.time()
    
    pygame.time.set_timer(target_event, target_increment)
    
    while run:
        
        elapsed_time = time.time() - start_time
        
        clock.tick(60)
        click = False
        mouse_position = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            
            if event.type == target_event:
                x = random.randint(target_padding, width - target_padding)
                y = random.randint(target_padding + top_bar_height, height - target_padding)
                target = Target(x,y)
                targets.append(target)
                
            if event.type ==  pygame.MOUSEBUTTONDOWN:
                click = True
                clicks += 1
            
        for target in targets:
            target.update()
            
            if target.size <= 0:
                targets.remove(target)
                misses += 1
                
            if click and target.collide(*mouse_position):
                targets.remove(target)
                target_pressed += 1
            
        if misses >= lives:
            end_screen(window, elapsed_time, target_pressed, clicks)
        
        draw(window, targets)
        draw_top_bar(window, elapsed_time, target_pressed, misses)
        pygame.display.update()

            
    pygame.quit()
    
if __name__ == "__main__":
    main()