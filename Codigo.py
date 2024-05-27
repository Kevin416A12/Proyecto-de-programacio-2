import pygame
import sys

pygame.init()

# Configuración de la pantalla
screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Editor de Matriz 12x12 en Pygame")

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


# Crear una instancia de la clase Editor con el archivo de texto
editor = Editor('matriz.txt')



# Bucle principal
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

    # Rellenar el fondo
    screen.fill((255, 255, 255))

    # Dibujar la matriz
    editor.dibujar_matriz()


    # Actualizar la pantalla
    pygame.display.flip()

pygame.quit()
sys.exit()
