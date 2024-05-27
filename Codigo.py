import pygame

pygame.init()

screen_width = 400
screen_height = 400

screen = pygame.display.set_mode((screen_width, screen_height))

class Editor:

    def __init__(self):
        self.colores = {
            0: (255, 255, 255),  # Blanco
            1: (0, 0, 0),        # Negro
            2: (255, 0, 0),      # Rojo
            3: (0, 255, 0),      # Verde
            4: (0, 0, 255),      # Azul
    }

        self.matriz = [
            [0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1],
            [1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2],
            [2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3],
            [3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4],
            [4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0],
            [0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1],
            [1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2],
            [2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3],
            [3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4],
            [4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0],
            [0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1],
            [1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2],
    ]
        self.tamano_celda = 30


    def dibujar_matriz(self):
        for y, row in enumerate(self.matriz):
            for x, value in enumerate(row):
                color = self.colores.get(value, (255, 255, 255))  # Color por defecto: blanco
                rect = pygame.Rect(x * self.tamano_celda, y * self.tamano_celda, self.tamano_celda, self.tamano_celda)
                pygame.draw.rect(screen, color, rect)

editor = Editor()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    screen.fill((255, 255, 255 ))

    editor.dibujar_matriz()

    pygame.display.flip()
pygame.quit()
