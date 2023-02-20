import pygame as pg
import math

class Cardioid:
	def __init__(self, app):
		self.app = app
		self.radius = 200
		self.num_lines = 200
		self.translate = self.app.screen.get_width() // 2, self.app.screen.get_height() // 2
	def draw(self):
		time = pg.time.get_ticks()
		factor = 1 + 0.0001 * time
		for i in range(self.num_lines):
			theta = (2*math.pi/self.num_lines)*i
			x1 = self.radius * math.cos(theta) + self.translate[0]
			y1 = self.radius * math.sin(theta) + self.translate[1]

			x2 = self.radius * math.cos(factor*theta) + self.translate[0]
			y2 = self.radius * math.sin(factor*theta) + self.translate[1]

			pg.draw.aaline(self.app.screen, 'green', (x1, y1), (x2, y2))


class App:
	def __init__(self):
		self.screen = pg.display.set_mode([1200,900])
		self.clock = pg.time.Clock()
		self.cardioid = Cardioid(self)

	def draw(self):
		self.screen.fill('blue')
		self.cardioid.draw()
		pg.display.flip()
	
	def run(self):
		while True:
			self.draw()
			[exit() for i in pg.event.get() if i.type == pg.QUIT]
			self.clock.tick(60)


if __name__ == '__main__':
	app = App()
	app.run()
