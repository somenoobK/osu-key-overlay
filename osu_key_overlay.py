import pygame,sys,configparser
from win32api import GetAsyncKeyState
from config import *

pygame.init()

win = pygame.display.set_mode((window_width,window_height),pygame.RESIZABLE)
pygame.display.set_caption('OSU Key Overlay')
ico = pygame.image.load('icons/img.ico').convert()
pygame.display.set_icon(ico)
clock = pygame.time.Clock()

#main code
class Key:
	def __init__(self,color,trail_color,trail_length,distance_val,key_code,knt,text_color,trail_speed,adaptive_button_size):
		self.key_code = key_code
		self.color = color
		self.knt = knt
		self.distance_val = distance_val
		self.trail_length = trail_length
		self.trail_color = trail_color
		self.trail_recth = 0
		self.keys = GetAsyncKeyState
		self.text_color = text_color
		self.speed = trail_speed
		self.up_increment_val = self.speed
		self.down_increment_val = self.speed
		self.adaptive_button_size = adaptive_button_size
		self.button_size = int(pygame.display.get_window_size()[0]/3)

	def make_key(self):
		if self.adaptive_button_size > 0:
			self.button_size = int(pygame.display.get_window_size()[0]/3)
		self.posw = int((pygame.display.get_window_size()[0])/4)*self.distance_val
		self.posh = int((pygame.display.get_window_size()[1])-int(self.button_size/2)-20)
		self.button = pygame.Surface((self.button_size,self.button_size))
		self.button.fill(self.color)
		self.button_center = (self.posw,self.posh)
		self.button_rect = self.button.get_rect(center = self.button_center)
		#button overlay
		self.button_overlay = pygame.Surface((self.button_size-10,self.button_size-10))
		self.button_overlay_rect = self.button_overlay.get_rect(center = self.button_center)
		self.button_overlay.fill((int(color1[0]/3),int(color1[1]/3),int(color1[2]/3)))

	def key_logic(self):
		if self.keys(self.key_code):
			self.button.fill(self.trail_color)
		else:
			self.button.fill(self.color)

	def key_name(self):
		self.font = pygame.font.Font('fonts/freesansbold.ttf', int(self.button_size/2))
		self.keyname = self.font.render(self.knt,True,self.text_color)
		self.keyname_rect = self.keyname.get_rect(center = self.button_center)

	def button_trail(self):
		self.trail_rect = pygame.Rect((0,0),(self.button_size,self.trail_recth))
		if self.keys(self.key_code):
			if self.trail_recth < self.trail_length:
				self.trail_recth += self.up_increment_val
				self.up_increment_val += self.speed
				if self.trail_recth >= self.trail_length:
					self.trail_recth = self.trail_length
			elif self.trail_recth >= self.trail_length:
				self.trail_recth = self.trail_length
			self.down_increment_val = self.speed
		else:
			if self.trail_recth > 0:
				self.trail_recth -= self.down_increment_val
				self.down_increment_val += self.speed
				if self.trail_recth <= 0:
					self.trail_recth = 0
			elif self.trail_recth <= 0:
				self.trail_recth = 0
			self.up_increment_val = self.speed
		self.trail_rect.bottomleft = self.button_rect.topleft

		pygame.draw.rect(win,self.trail_color,self.trail_rect,border_top_left_radius = 20,border_top_right_radius = 20)

	def draw(self):
		self.make_key()
		self.key_name()
		self.key_logic()
		self.button_trail()
		win.blit(self.button,self.button_rect)
		win.blit(self.button_overlay,self.button_overlay_rect)
		win.blit(self.keyname,self.keyname_rect)

#----------------------------------------|.3.|-------------------------------------------#
key1 = Key(color1,color2,trail_length,key1_position,k1c,k1t.upper(),color3,trail_speed,adaptive_button_size)
key2  = Key(color1,color2,trail_length,key2_position,k2c,k2t.upper(),color3,trail_speed,adaptive_button_size)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	win.fill(background_color)
	key1.draw()
	key2.draw()
	pygame.display.update()
	clock.tick(FPS)
