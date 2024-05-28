import pygame
import math

pygame.init()

WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gravitational Slingshot Effect")

PLANET_MASS = 100
SHIP_MASS = 5
G = 5
FPS = 60
PLANET_SIZE = 50
OBJ_SIZE = 5
VEL_SCALE = 100

BG = pygame.transform.scale(pygame.image.load("background.jpg"), (WIDTH, HEIGHT))
PLANET = pygame.transform.scale(pygame.image.load("jupiter.png"), (PLANET_SIZE * 2, PLANET_SIZE * 2))

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

class Planet:
    def __init__(self, x, y, mass):
        self.x = x
        self.y = y
        self.mass = mass
    
    def draw(self):
        win.blit(PLANET, (self.x - PLANET_SIZE, self.y - PLANET_SIZE))

class Spacecraft:
    def __init__(self, x, y, vel_x, vel_y, mass):
        self.x = x
        self.y = y
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.mass = mass

    def move(self, main_planet, revolving_planet=None):
        distance_to_main = math.sqrt((self.x - main_planet.x) ** 2 + (self.y - main_planet.y) ** 2)
        force_main = (G * self.mass * main_planet.mass) / distance_to_main ** 2

        if revolving_planet:
            distance_to_revolving = math.sqrt((self.x - revolving_planet.x) ** 2 + (self.y - revolving_planet.y) ** 2)
            force_revolving = (G * self.mass * revolving_planet.mass) / distance_to_revolving ** 2
        else:
            force_revolving = 0

        total_force = force_main + force_revolving

        acceleration = total_force / self.mass
        angle_main = math.atan2(main_planet.y - self.y, main_planet.x - self.x)
        acceleration_x_main = acceleration * math.cos(angle_main)
        acceleration_y_main = acceleration * math.sin(angle_main)

        self.vel_x += acceleration_x_main
        self.vel_y += acceleration_y_main

        self.x += self.vel_x
        self.y += self.vel_y
    
    def draw(self):
        pygame.draw.circle(win, RED, (int(self.x), int(self.y)), OBJ_SIZE)

class RevolvingPlanet:
    def __init__(self, distance, speed, mass):
        self.distance = distance
        self.speed = speed
        self.angle = 0
        self.mass = mass 

    def update_position(self, center_x, center_y):
        self.angle += self.speed
        self.x = center_x + self.distance * math.cos(math.radians(self.angle))
        self.y = center_y + self.distance * math.sin(math.radians(self.angle))

    def draw(self):
        pygame.draw.circle(win, BLUE, (int(self.x), int(self.y)), OBJ_SIZE)

def create_ship(location, mouse):
    t_x, t_y = location
    m_x, m_y = mouse
    vel_x = (m_x - t_x) / VEL_SCALE
    vel_y = (m_y - t_y) / VEL_SCALE
    obj = Spacecraft(t_x, t_y, vel_x, vel_y, SHIP_MASS)
    return obj

def main():
    running = True
    clock = pygame.time.Clock()

    planet = Planet(WIDTH // 2, HEIGHT // 2, PLANET_MASS)
    objects = []
    temp_obj_pos = None
    
    revolving_planet = RevolvingPlanet(150, 1, PLANET_MASS/3)

    while running:
        clock.tick(FPS)

        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            

            if event.type == pygame.MOUSEBUTTONDOWN:
                if temp_obj_pos:
                    obj = create_ship(temp_obj_pos, mouse_pos)
                    objects.append(obj)
                    temp_obj_pos = None
                else:
                    temp_obj_pos = mouse_pos

        win.blit(BG, (0, 0))

        if temp_obj_pos:
            pygame.draw.line(win, WHITE, temp_obj_pos, mouse_pos, 2)
            pygame.draw.circle(win, RED, temp_obj_pos, OBJ_SIZE)
        
        for obj in objects[:]:
            obj.draw()
            obj.move(planet, revolving_planet)
            off_screen = obj.x < 0 or obj.x > WIDTH or obj.y < 0 or obj.y > HEIGHT
            collided = math.sqrt((obj.x - planet.x) ** 2 + (obj.y - planet.y) ** 2) <= PLANET_SIZE
            if off_screen or collided:
                objects.remove(obj)
        
        revolving_planet.update_position(planet.x, planet.y)
        revolving_planet.draw()
        planet.draw()

        pygame.display.update()
    
    pygame.quit()

if __name__ == "__main__":
    main()
