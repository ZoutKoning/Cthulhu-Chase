import pygame 
from tiles import Tile 
from settings import tile_size, screen_width
from player import Player
from enemy import Enemy
from goalpost import Goalpost
from glider import Glider
from lava import Lava
from cultist import Cultist
from particles import ParticleEffect

class Level:
	def __init__(self,level_data,surface):
		
		# level setup
		self.display_surface = surface 
		self.setup_level(level_data)
		self.world_shift = 0
		self.current_x = 0

		# dust 
		self.dust_sprite = pygame.sprite.GroupSingle()
		self.player_on_ground = False

	def create_jump_particles(self,pos):
		if self.player.sprite.facing_right:
			pos -= pygame.math.Vector2(10,5)
		else:
			pos += pygame.math.Vector2(10,-5)
		jump_particle_sprite = ParticleEffect(pos,'jump')
		self.dust_sprite.add(jump_particle_sprite)

	def get_player_on_ground(self):
		if self.player.sprite.on_ground:
			self.player_on_ground = True
		else:
			self.player_on_ground = False

	def create_landing_dust(self):
		if not self.player_on_ground and self.player.sprite.on_ground and not self.dust_sprite.sprites():
			if self.player.sprite.facing_right:
				offset = pygame.math.Vector2(10,15)
			else:
				offset = pygame.math.Vector2(-10,15)
			fall_dust_particle = ParticleEffect(self.player.sprite.rect.midbottom - offset,'land')
			self.dust_sprite.add(fall_dust_particle)

	def setup_level(self,layout):
		self.tiles = pygame.sprite.Group()
		self.lava = pygame.sprite.Group()
		self.player = pygame.sprite.GroupSingle()
		self.enemy = pygame.sprite.GroupSingle()
		self.goalpost = pygame.sprite.GroupSingle()
		self.cultist = pygame.sprite.GroupSingle()
		self.glider = pygame.sprite.GroupSingle()

		for row_index,row in enumerate(layout):
			for col_index,cell in enumerate(row):
				x = col_index * tile_size
				y = row_index * tile_size
				
				if cell == 'X':
					tile = Tile((x,y),tile_size)
					self.tiles.add(tile)
				if cell == 'L':
					lava = Lava((x,y),tile_size)
					self.lava.add(lava)
				if cell == 'P':
					player_sprite = Player((x,y),self.display_surface,self.create_jump_particles)
					self.player.add(player_sprite)
				if cell == 'E':
					enemy_sprite = Enemy((x,y),self.display_surface)
					self.enemy.add(enemy_sprite)
				if cell == 'G':
					goal_sprite = Goalpost((x,y),self.display_surface)
					self.goalpost.add(goal_sprite)
				if cell == 'C':
					cultist_sprite = Cultist((x,y),self.display_surface)
					self.cultist.add(cultist_sprite)
				if cell == 'J':
					glider_sprite = Glider((x,y),self.display_surface)
					self.glider.add(glider_sprite)

	def scroll_x(self):
		player = self.player.sprite
		player_x = player.rect.centerx
		direction_x = player.direction.x

		if player_x < screen_width / 4 and direction_x < 0:
			self.world_shift = 8
			player.speed = 0
		elif player_x > screen_width - (screen_width / 4) and direction_x > 0:
			self.world_shift = -8
			player.speed = 0
		else:
			self.world_shift = 0
			player.speed = 8

	def horizontal_movement_collision(self):
		player = self.player.sprite
		player.rect.x += player.direction.x * player.speed

		for sprite in self.tiles.sprites():
			if sprite.rect.colliderect(player.rect):
				if player.direction.x < 0: 
					player.rect.left = sprite.rect.right
					player.on_left = True
					self.current_x = player.rect.left
				elif player.direction.x > 0:
					player.rect.right = sprite.rect.left
					player.on_right = True
					self.current_x = player.rect.right

		if player.on_left and (player.rect.left < self.current_x or player.direction.x >= 0):
			player.on_left = False
		if player.on_right and (player.rect.right > self.current_x or player.direction.x <= 0):
			player.on_right = False

	def vertical_movement_collision(self):
		player = self.player.sprite
		player.apply_gravity()

		for sprite in self.tiles.sprites():
			if sprite.rect.colliderect(player.rect):
				if player.direction.y > 0: 
					player.rect.bottom = sprite.rect.top
					player.direction.y = 0
					player.on_ground = True
				elif player.direction.y < 0:
					player.rect.top = sprite.rect.bottom
					player.direction.y = 0
					player.on_ceiling = True

		if player.on_ground and player.direction.y < 0 or player.direction.y > 1:
			player.on_ground = False
		if player.on_ceiling and player.direction.y > 0.1:
			player.on_ceiling = False

	
	def horizontal_enemy_collision(self):
		player = self.player.sprite

		for sprite in self.enemy.sprites():
			if sprite.rect.colliderect(player.rect):
				return True
			
		for sprite in self.cultist.sprites():
			if sprite.rect.colliderect(player.rect):
				return True
			
		for sprite in self.lava.sprites():
			if sprite.rect.colliderect(player.rect):
				return True

		return False
	
	def horizontal_goalpost_collision(self):
		player = self.player.sprite

		for sprite in self.goalpost.sprites():
			if sprite.rect.colliderect(player.rect):
				return True
		return False
	
	def horizontal_cultist_collision(self):
		cultist = self.cultist.sprite
		cultist.rect.x += cultist.direction.x * cultist.speed

		for sprite in self.tiles.sprites():
			if sprite.rect.colliderect(cultist.rect):
				cultist.speed*=-1
				if cultist.facing_right == True:
					cultist.facing_right = False
				else:
					cultist.facing_right = True

	def horizontal_glider_collision(self):
		player = self.player.sprite

		for sprite in self.glider.sprites():
			if sprite.rect.colliderect(player.rect):
				self.player.has_glider = True
		#self.horizontal_enemy_collision()
		#self.player.has_glider = False

	def run(self):
		# dust particles 
		self.dust_sprite.update(self.world_shift)
		self.dust_sprite.draw(self.display_surface)

		# level tiles
		self.tiles.update(self.world_shift)
		self.tiles.draw(self.display_surface)
		self.scroll_x()

		# lava
		self.lava.update(self.world_shift)
		self.lava.draw(self.display_surface)


		# player
		self.player.update()
		self.horizontal_movement_collision()
		self.get_player_on_ground()
		self.vertical_movement_collision()
		self.create_landing_dust()
		self.player.draw(self.display_surface)

		#enemy
		#self.enemy.update(self.world_shift, self.player.sprite)
		#self.enemy.draw(self.display_surface)
		#self.horizontal_enemy_collision()

		#goalpost
		self.goalpost.update(self.world_shift)
		self.goalpost.draw(self.display_surface)
		self.horizontal_goalpost_collision()

		#cultist
		self.cultist.update(self.world_shift)
		self.cultist.draw(self.display_surface)
		self.horizontal_cultist_collision()

		#glider
		self.glider.update(self.world_shift)
		self.glider.draw(self.display_surface)
		self.horizontal_glider_collision()
