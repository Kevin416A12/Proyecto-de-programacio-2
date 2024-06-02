import pygame
import sys
import pygame as pg

pygame.init()
# Configuración de la pantallaz`
screen_width = 800
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Editor de Matriz 12x12 en Pygame")

class Button:
    def __init__(self, x=0, y=0, text="", width= 0, height=0 , elev=6):
        self.font = pg.font.Font(None, 24)
        self.text = self.font.render(text, True, "#EEEEEE")
        self.text_rect = self.text.get_rect()

        self.bottom_rect = pg.Rect((x+elev, y+elev), (width, height))
        self.top_rect = pg.Rect((x, y), (width, height))
        self.text_rect.center = self.top_rect.center

        self.hover = False
        self.pressed = False
        self.clicked = False

    def update(self):
        self.clicked = False
        mouse_pos = pg.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            self.hover = True
            if pg.mouse.get_pressed()[0]:
                self.pressed = True
            else:
                if self.pressed:
                    self.pressed = False
                    self.clicked = True

        else:
            self.pressed = False
            self.hover = False

    def draw(self, display):

        top_rect_color = "#317bcf" if self.hover else "#3194cf"
        if not self.pressed:

            pg.draw.rect(display, "#1a232e", self.bottom_rect)
            pg.draw.rect(display, top_rect_color, self.top_rect)
            self.text_rect.center = self.top_rect.center
        else:
            pg.draw.rect(display, top_rect_color, self.bottom_rect)
            self.text_rect.center = self.bottom_rect.center
        display.blit(self.text, self.text_rect)


# Definir la clase Editor
class Editor:
    def __init__(self, filename):
        self.colores = {
            0: (255, 255, 255),  # Blanco
            1: (0, 0, 0),  # Negro
            2: (255, 0, 0),  # Rojo
            3: (0, 255, 0),  # Verde
            4: (0, 0, 255),  # Azul
        }
        self.matriz = self.cargar_matriz(filename)
        self.tamano_celda = 30

    def cargar_matriz(self, filename):
        matriz = []
        with open(filename, 'r') as file:
            for line in file:
                fila = list(map(int, line.split()))
                matriz.append(fila)
        return matriz

    def dibujar_matriz(self):
        for y, row in enumerate(self.matriz):
            for x, value in enumerate(row):
                color = self.colores.get(value, (255, 255, 255))  # Color por defecto: blanco
                rect = pygame.Rect(x * self.tamano_celda, y * self.tamano_celda, self.tamano_celda, self.tamano_celda)
                pygame.draw.rect(screen, color, rect)


editor = Editor('matriz.txt')
Boton = Button(x=360, y=300, text="Click Me", width= 100, height=100)


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            grid_x = x // 30
            grid_y = y // 30
            if grid_x < len(editor.matriz[0]) and grid_y < len(editor.matriz):
                editor.matriz[grid_y][grid_x] = (editor.matriz[grid_y][grid_x] + 1) % 5

    screen.fill((0, 0, 0))

    editor.dibujar_matriz()

    Boton.draw(screen)
    Boton.update()
    pygame.display.flip()

pygame.quit()
sys.exit()
