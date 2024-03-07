import pygame
import sys
import random

# Inicializar Pygame
pygame.init()

# Definir colores
LIGHT_GREEN = (144, 238, 144)
ORANGE = (255, 165, 0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)
WHITE = (255, 255, 255)

# Definir dimensiones de la pantalla
WIDTH, HEIGHT = 800, 600

# Crear la ventana del juego
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Roomba Minijuego")

# Definir la clase Roomba
class Roomba(pygame.sprite.Sprite):
    def __init__(self, speed):
        super().__init__()
        self.image = pygame.Surface((40, 40), pygame.SRCALPHA)
        pygame.draw.circle(self.image, ORANGE, (20, 20), 20)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.speed = speed  # Nueva propiedad para la velocidad

    def update(self, keys):
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

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
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((20, 20), pygame.SRCALPHA)
        pygame.draw.circle(self.image, YELLOW, (10, 10), 10)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - 20)
        self.rect.y = random.randint(0, HEIGHT - 20)

    def reset_position(self, obstacles):
        while pygame.sprite.spritecollideany(self, obstacles):
            self.rect.x = random.randint(0, WIDTH - 20)
            self.rect.y = random.randint(0, HEIGHT - 20)

# Definir la clase Button
class Button(pygame.sprite.Sprite):
    def __init__(self, text, x, y, width, height, color, hover_color, text_color, action=None):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.color = color
        self.hover_color = hover_color
        self.text = text
        self.text_color = text_color
        self.action = action
        self.font = pygame.font.SysFont(None, 30)
        self.render_text()

    def render_text(self):
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        self.image.fill(self.color)
        self.image.blit(text_surface, text_rect)

    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            self.image.fill(self.hover_color)
            if pygame.mouse.get_pressed()[0] and self.action:
                self.action()
        else:
            self.image.fill(self.color)
        self.render_text()

# Definir la función para iniciar el juego
def start_game(speed):
    all_sprites = pygame.sprite.Group()
    roomba = Roomba(speed)  # Pasar la velocidad al crear el Roomba
    all_sprites.add(roomba)

    obstacles = pygame.sprite.Group()
    for _ in range(10):  # Añade 10 obstáculos aleatorios
        obstacle = Obstacle(random.randrange(0, WIDTH - 50), random.randrange(0, HEIGHT - 50), 50, 50)
        while obstacle.rect.colliderect(roomba.rect):  # Evita que los obstáculos se generen sobre la Roomba
            obstacle.rect.x = random.randrange(0, WIDTH - 50)
            obstacle.rect.y = random.randrange(0, HEIGHT - 50)
        obstacles.add(obstacle)

    collectibles = pygame.sprite.Group()
    for _ in range(15):  # Añade 15 colectibles
        collectible = Collectible()
        collectible.reset_position(obstacles)  # Ajuste para evitar la generación dentro de los obstáculos
        collectibles.add(collectible)
        all_sprites.add(collectible)

    score = 0

    font = pygame.font.SysFont(None, 30)

    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        roomba.update(keys)

        # Detectar colisiones entre la Roomba y los colectibles
        collectibles_hit = pygame.sprite.spritecollide(roomba, collectibles, True)
        for collectible in collectibles_hit:
            score += 1
            print("¡Has recogido un colectible! Puntos:", score)

        # Detectar colisiones entre la Roomba y los obstáculos
        obstacles_hit = pygame.sprite.spritecollide(roomba, obstacles, False)
        for obstacle in obstacles_hit:
            print("¡Has chocado con un obstáculo!")

        if len(collectibles) == 0:
            end_game(score)

        screen.fill(LIGHT_GREEN)
        obstacles.draw(screen)
        collectibles.draw(screen)
        all_sprites.draw(screen)

        # Mostrar puntuación
        text_surface = font.render("Puntuación: " + str(score), True, BLACK)
        screen.blit(text_surface, (10, 10))

        pygame.display.flip()
        clock.tick(30)

# Definir la función para seleccionar la velocidad
def set_speed(speed_value):
    start_game(speed_value)

# Definir la función para iniciar el juego
def start_screen():
    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(LIGHT_GREEN)
        font = pygame.font.SysFont(None, 50)
        text_surface = font.render("Press any key to start", True, BLACK)
        text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
        screen.blit(text_surface, text_rect)
        pygame.display.flip()
        clock.tick(30)

        keys = pygame.key.get_pressed()
        if any(keys):
            select_speed()

# Definir la función para seleccionar la velocidad
def select_speed():
    screen.fill(LIGHT_GREEN)
    font = pygame.font.SysFont(None, 50)
    text_surface = font.render("Select Speed", True, BLACK)
    text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
    screen.blit(text_surface, text_rect)

    buttons = pygame.sprite.Group()
    button_slow = Button("Slow", 250, 400, 100, 50, BLACK, GRAY, WHITE, lambda: set_speed("Slow"))
    button_normal = Button("Normal", 400, 400, 100, 50, BLACK, GRAY, WHITE, lambda: set_speed("Normal"))
    button_fast = Button("Fast", 550, 400, 100, 50, BLACK, GRAY, WHITE, lambda: set_speed("Fast"))
    buttons.add(button_slow, button_normal, button_fast)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        buttons.update()
        buttons.draw(screen)
        pygame.display.flip()

# Definir la función para finalizar el juego
def end_game(score):
    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(LIGHT_GREEN)
        font = pygame.font.SysFont(None, 50)
        text_surface = font.render("Game Over", True, BLACK)
        text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
        screen.blit(text_surface, text_rect)

        text_surface = font.render("Puntuación final: " + str(score), True, BLACK)
        text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(text_surface, text_rect)

        button_quit = Button("Quit", 350, 400, 100, 50, GRAY, BLUE, BLACK, lambda: pygame.quit())
        button_quit.update()
        screen.blit(button_quit.image, button_quit.rect.topleft)

        pygame.display.flip()
        clock.tick(30)

# Función principal del juego
def main():
    start_screen()

if __name__ == "__main__":
    main()
