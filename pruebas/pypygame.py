import pygame

pygame.init()
screen = pygame.display.set_mode((400,300))
done = False
size = (50, 50)
size_borde = (100,100)
radius = 25
radio_borde = 50
position = (100,100)
position2 = (200,70)
position3 = (250, 140)
position4 = (300, 90)

# COLORES
COLOR_CIRCULO = pygame.Color(71, 98, 79)
COLOR_BORDE = pygame.Color(82, 173, 156)
# FIN COLORES

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	screen.blit(circle, (25, 25))		
	screen.blit(circle_filled, size)
	screen.blit(circle_filled, position)
	screen.blit(circle_filled, position2)
	screen.blit(circle_filled, position3)
	screen.blit(circle_filled, position4)
	pygame.display.update()
	pygame.display.flip()

def dibujar_circulo(tamanio, radio, borde = 5):
	circle = pygame.Surface(tamanio)	
	if(borde):
		pygame.draw.circle(circle, COLOR_BORDE, (radio, radio), radio, borde)
	else:
		pygame.draw.circle(circle, COLOR_CIRCULO, (radio, radio), radio)
	return circle
	
	
