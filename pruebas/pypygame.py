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
RED = pygame.Color(71, 98, 79)
BORDE_GUIA = pygame.Color(82, 173, 156)
circle = pygame.Surface(size_borde)
circle_filled = pygame.Surface(size)
pygame.draw.circle(circle, BORDE_GUIA, (radio_borde, radio_borde), radio_borde, 5)
pygame.draw.circle(circle_filled, RED, (radius, radius), radius)
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

	
