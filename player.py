import pygame 
from support import import_folder

class Player(pygame.sprite.Sprite):
	def __init__(self,pos):
		super().__init__()
		#self.import_character_assets()
		#self.frame_index = 0
		#self.animation_speed = 0.15
		self.image = pygame.Surface((32, 64))
		self.image.fill('red')
		self.rect = self.image.get_rect(topleft = pos)
		self.direction = pygame.math.Vector2(0,0)

		#Player movement
		self.direction = pygame.math.Vector2(0,0)
		self.speed = 8
		self.gravity = 0.8
		self.jump_speed = -16
		
	def get_input(self):
		keys = pygame.key.get_pressed()

		if keys[pygame.K_RIGHT]:
			self.direction.x = 1
			self.facing_right = True
		elif keys[pygame.K_LEFT]:
			self.direction.x = -1
			self.facing_right = False
		else:
			self.direction.x = 0

		if keys[pygame.K_SPACE]:
			self.jump()

	def apply_gravity(self):
		self.direction.y += self.gravity
		self.rect.y += self.direction.y

	def jump(self):
		self.direction.y = self.jump_speed


	def update(self):
		self.get_input()
		self.rect.x += self.direction.x * self.speed
		self.apply_gravity()