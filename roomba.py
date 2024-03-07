import pygame
import sys
import random

# Inicializar Pygame
pygame.init()

# Definir colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)

# Definir dimensiones de la pantalla
WIDTH, HEIGHT = 800, 600

# Crear la ventana del juego
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Roomba Minijuego")

# Definir la clase Roomba
class Roomba(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 40), pygame.SRCALPHA)
        pygame.draw.circle(self.image, BLACK, (20, 20), 20)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)

    def update(self):
        pass

# Definir la clase Obstáculo
class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# Definir la clase Collectible
class Collectible(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((20, 20), pygame.SRCALPHA)
        pygame.draw.circle(self.image, YELLOW, (10, 10), 10)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

# Definir la clase Button
class Button(pygame.sprite.Sprite):
    def __init__(self, text, x, y, width, height, color, hover_color, action):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.color = color
        self.hover_color = hover_color
        self.text = text
        self.action = action
        self.font = pygame.font.SysFont(None, 30)
        self.render_text()

    def render_text(self):
        text_surface = self.font.render(self.text, True, BLACK)
        text_rect = text_surface.get_rect(center=self.rect.center)
        self.image.fill(self.color)
        self.image.blit(text_surface, text_rect)

    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            self.image.fill(self.hover_color)
            if pygame.mouse.get_pressed()[0]:
                self.action()
        else:
            self.image.fill(self.color)
        self.render_text()

# Definir la función para iniciar el juego
def start_game():
    global speed
    running = True
    all_sprites = pygame.sprite.Group()
    roomba = Roomba()
    all_sprites.add(roomba)

    obstacles = pygame.sprite.Group()
    for _ in range(10):  # Añade 10 obstáculos aleatorios
        obstacle = Obstacle(random.randrange(0, WIDTH - 50), random.randrange(0, HEIGHT - 50), 50, 50)
        obstacles.add(obstacle)
        all_sprites.add(obstacle)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            roomba.rect.y -= 5
        if keys[pygame.K_DOWN]:
            roomba.rect.y += 5
        if keys[pygame.K_LEFT]:
            roomba.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            roomba.rect.x += 5

        obstacles_hit = pygame.sprite.spritecollide(roomba, obstacles, True)
        # Manejar colisiones con obstáculos
        for obstacle in obstacles_hit:
            print("¡Has chocado con un obstáculo!")

        screen.fill(WHITE)
        obstacles.draw(screen)
        all_sprites.draw(screen)
        pygame.display.flip()

# Definir la función para seleccionar la velocidad
def set_speed(speed_value):
    global speed
    speed = speed_value
    start_game()

# Crear botones
buttons = pygame.sprite.Group()
button_slow = Button("Slow", 200, 400, 100, 50, GRAY, BLUE, lambda: set_speed("Slow"))
button_normal = Button("Normal", 350, 400, 100, 50, GRAY, BLUE, lambda: set_speed("Normal"))
button_fast = Button("Fast", 500, 400, 100, 50, GRAY, BLUE, lambda: set_speed("Fast"))
buttons.add(button_slow, button_normal, button_fast)

# Puntuación inicial
score = 0
speed = None

# Función principal del juego
def main():
    global speed
    running = True
    clock = pygame.time.Clock()

    # Pantalla de inicio
    while not speed:
        screen.fill(WHITE)
        font = pygame.font.SysFont(None, 50)
        text_surface = font.render("Select Speed", True, BLACK)
        text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
        screen.blit(text_surface, text_rect)
        buttons.update()
        buttons.draw(screen)
        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    main()
