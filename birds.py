import pygame
import neat
import time
import random
import os


win_width = 600
win_height = 800


#load bird sprites
bird_pics = [pygame.transform.scale2x(pygame.image.load(os.path.join("assets","bird1.png"))),
			pygame.transform.scale2x(pygame.image.load(os.path.join("assets","bird2.png"))),
			pygame.transform.scale2x(pygame.image.load(os.path.join("assets","bird3.png")))]

#load pipe sprite
pipe_pic = pygame.transform.scale2x(pygame.image.load(os.path.join("assets","pipe.png")))

#load base sprite
base_pic = pygame.transform.scale2x(pygame.image.load(os.path.join("assets","base.png")))

#load background sprite
# bg_pic = pygame.transform.scale2x(pygame.image.load(os.path.join("assets","bg.png")))
bg_pic = pygame.image.load(os.path.join("assets","PK.JPG"))

class Bird:
	pics = bird_pics	
	#defines bird tilt upon jump and fall
	max_rotation = 25
	#defines rotation degree @ each frame
	rot_vel = 20
	#defines how long each bird frame is shown (speed of flap)
	animation_time = 5

	def __init__(self,x,y):
		#starting position of bird (x,y) on screen
		self.x = x 
		self.y = y

		self.tilt = 0
		#represents time units we've been moving for 
		self.tick_count = 0
		#begins @ 0
		self.vel = 0
		self.height = self.y
		self.img_count = 0
		self.img = self.pics[0]

	def jump(self):
		#negative velocity because upward velocity is associated with a negative velocity in pygame
		self.vel = -10.5
		# keep track of last jump, reset to 0
		self.tick_count = 0
		# where does the bird start moving from? 
		self.height = self.y 

	def move(self):
		self.tick_count += 1
		#displacement | 
		d = self.vel * self.tick_count +1.5*self.tick_count**2
		if d >= 16:
			d = 16

		if d <0:
			d -= 2
		#move bird based on displacement 
		self.y = self.y + d 
		#tilt bird 
		if d < 0 or self.y < self.height + 50:
			if self.tilt < self.max_rotation:
				self.tilt = self.max_rotation
		#rotate bird 90 degrees
		else:
			if self.tilt > -90:
				self.tilf -= self.rot_vel

	def draw(self, win):
		self.img_count += 1
		#set the correct image sequence  based on tick count 
		if self.img_count < self.animation_time:
			self.img = self.pics[0]

		elif self.img_count <self.animation_time*2:
			self.img = self.pics[1]

		elif self.img_count <self.animation_time*3:
			self.img = self.pics[2]

		elif self.img_count <self.animation_time*4:
			self.img = self.pics[1]

		elif self.img_count <self.animation_time*4 +1:
			self.img = self.pics[0]
			self.img_count = 0 

		if self.tilt <= -80:
			self.img = self.pics[1]
			self.img_count = self.animation_time*2

		#rotate the sprite around itsself based on the current tilt 
		rotated_image = pygame.transform.rotate(self.img,self.tilt)
		new_rect = rotated_image.get_rect(center = self.img.get_rect(topleft = (self.x,self.y)).center)
		win.blit(rotated_image,new_rect.topleft)

	def get_mask(self):
		return pygame.mask.from_surface(self.img)

def draw_window(win,bird):
	#put the background
	win.blit(bg_pic,(0,0))
	bird.draw(win)
	pygame.display.update()

def main():
	bird = Bird(200,200)
	win = pygame.display.set_mode((win_width,win_height))
	run = True
	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

		draw_window(win,bird)
	pygame.quit()
	quit()


main()

# while True:
# 	bird.move()
