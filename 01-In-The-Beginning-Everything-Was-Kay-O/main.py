# Game development with Python and Cocos2d
# Part 1: In the beginning everything was Kay-O

# Alex Silcott (alexsilcott@gmail.com)


# Imports

import pyglet
from pyglet.window import key

import cocos
from cocos import actions, layer, sprite, scene
from cocos.director import director


# Player class

# the argument given to this class gives it the base class of actions.Move (http://python.cocos2d.org/doc/api/cocos.actions.move_actions.html)
class Player(actions.Move):
	
	# creates the step function and is called on every frame. dt stands for delta time which is seconds elapsed since last call
	def step(self, dt):
		super(Player, self).step(dt) # Run step function on the parent (super) class
		# Determine velocity based on keyboard inputs and store it in a variable
		velocity_x = 140 * (keyboard[key.RIGHT] - keyboard[key.LEFT])
		velocity_y = 140 * (keyboard[key.UP] - keyboard[key.DOWN])
		# Set player object's velocity
		self.target.velocity = (velocity_x, velocity_y)

		
		
# Main Function
		
def main():
	global keyboard # This is declared as global so that it can be accessed by all class methods
	
	# Initialize director and create scene.
	# Arguments passed set the size of the window.
	# autoscale allows the graphics to be scaled according to the window being resized.
	# Caption sets window title. Have some fun with that!
	# (http://python.cocos2d.org/doc/api/cocos.director.html)
	director.init(width=500, height=300, caption="In the beginning everything was Kay-O", autoscale=True, resizable=True)

	# Create a layer and add a sprite to the layer.
	# Layers help to separate out different parts of a scene.
	# Typically, the highest layer will go to dialogue boxes and menus
	# Followed by the player layer with the background on the bottom
	player_layer = layer.Layer() # Creates an instance of a new layer
	player = sprite.Sprite('images/mr-saturn.png') #initializes a sprite object and includes a path to default image.
	player_layer.add(player)  # Adds player to instance of layer we just created

	# Sets initial position and velocity of player
	player.position = (250, 150)
	player.velocity = (0, 0)
	
	# Set the sprite's movement class
	player.do(Player())
	
	# Create a scene and set its initial layer
	main_scene = scene.Scene(player_layer)

	# Creates a KeyStateHandler on the keyboard object so we can accept input from the keyboard (KeyStateHandler is part of the pyglet library)
	# And pushes it to director
	keyboard = key.KeyStateHandler()
	director.window.push_handlers(keyboard)
	
	# Run the scene we've built in the window
	director.run(main_scene)
	
# This is a neato python trick so that modules can remain...modular
# (http://effbot.org/pyfaq/tutor-what-is-if-name-main-for.htm)
if __name__ == '__main__':
	main()
