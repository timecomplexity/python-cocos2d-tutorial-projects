# Game development with Python and Cocos2d
# Part 2: First program in Saturn Valley

# Alex Silcott (alexsilcott@gmail.com)


# Imports

import pyglet
from pyglet.window import key

import cocos
from cocos import actions, layer, sprite, scene, tiles # Add new import statement for background tiles
from cocos.director import director
from cocos.layer import Layer # new import statement so we can create an object of the Layer class

# New import statement so we can create a label
from cocos.text import Label


# Player class

class Player(actions.Move):
		
	def step(self, dt):
		super(Player, self).step(dt)
		velocity_x = 140 * (keyboard[key.RIGHT] - keyboard[key.LEFT])
		velocity_y = 140 * (keyboard[key.UP] - keyboard[key.DOWN])
		self.target.velocity = (velocity_x, velocity_y)
		
		scroller.set_focus(self.target.x, self.target.y)
		

# Big Text Class inherits from Layer
		
class BigText(Layer):
	
		# We have to initialize this class with this function:
		def __init__(self):
			# Here, we initialize the parent class by calling the super function
			super(BigText, self).__init__()
			# We then create the label itself
			big_text_label = Label(
				"Hello World, ZOOM!", # This argument holds the string to display
				font_name = "Arial", # Assigns font face
				font_size = 18, # Assigns font size
				anchor_x = 'left', # anchors text to left side of x-axis
				anchor_y = 'center' # anchors text to middle of y-axis
			)
			
			# Set position of text
			big_text_label.position= 5,590
			
			# Add label to the layer using the self identifier
			self.add(big_text_label)
		
# Main Function
		
def main():
	global keyboard
	global scroller # This variable is going to become a scrolling manager to enable us to scroll along the map
	
	# Initialize director
	director.init(width=800, height=600, caption="In the beginning everything was Kay-O", autoscale=True, resizable=True)
	
	# Create player layer and add player onto it
	# This time make it a ScrollableLayer type rather than simply Layer
	player_layer = layer.ScrollableLayer()
	player = sprite.Sprite('images/mr-saturn.png')
	player_layer.add(player)

	# Sets initial position and velocity of player
	player.position = (750, 1200)
	player.velocity = (0, 0)

	# Set the sprite's movement class
	player.do(Player())
	
	# Create a new ScrollingManager object so we can scroll the view along with the player
	# The ScrollingManager object lets us separate "world" coordinates and "screen" coordinates
	# In this way, we can keep track of where the player is across the entire map but keep the viewport local
	#(http://python.cocos2d.org/doc/api/cocos.layer.scrolling.html#cocos.layer.scrolling.ScrollingManager)
	scroller = layer.ScrollingManager()
	
	# Now we will create a map layer based on our TMX file
	# I called the ground layer "Ground" in the tmx file, which is what we specify here as an identifier
	# This is located in the <layer> tags in map.tmx
	# We do the same thing for TopLayer
	# See README in this folder for more information
	ground_layer = tiles.load('tiles/map.tmx')['Ground']
	top_layer = tiles.load('tiles/map.tmx')['TopLayer']
	
	# Creates a text layer and adds an instance of BigText() to it
	text_layer = BigText()
	
	# Add player sprite and player_layer to the ScrollingManager
	# We have also added a second argument to the add() calls
	# This is the z-index, which explicity determines the order of layers.
	# Here, the player has a z-index of 1 and the text has an index of 2 so it will overlay the player.
	# And 0 will be the background
	scroller.add(ground_layer, z = 0)
	scroller.add(top_layer, z = 1)
	scroller.add(player_layer, z = 1) 
	
	# Here we initialize the scene with initial layer "scroller" which holds all of the layers
	main_scene = scene.Scene(scroller)
	# Here we add the text_layer containing the instance of BigText() to the main scene
	main_scene.add(text_layer, z = 2)

	keyboard = key.KeyStateHandler()
	director.window.push_handlers(keyboard)
	
	# Run the scene we've built in the window
	director.run(main_scene)
	
# This is a neato python trick so that modules can remain...modular
# (http://effbot.org/pyfaq/tutor-what-is-if-name-main-for.htm)
if __name__ == '__main__':
	main()
