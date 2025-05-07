from constants import *
import contextlib
import io

with contextlib.redirect_stdout(io.StringIO()):
	import pygame


def main():
	pygame.init()
	clock = pygame.time.Clock()
	dt = 0
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		screen.fill(0)
		pygame.display.flip()
		time = clock.tick(60)
		dt = (time / 1000)


if __name__ == "__main__":
	main()
