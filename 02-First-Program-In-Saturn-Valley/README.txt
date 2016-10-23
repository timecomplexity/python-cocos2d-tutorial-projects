For this project, we are going to add in some tiles for the background which goes a little beyond the scope of just python and cocos2d.
We will be using XML or TMX to accomplish this.

I personally am not enough of a masochist to go through the pain of making my own XML files for this, so we're going to use Tiled: (http://mapeditor.org/).
Tiled is a free and open source map editor that can be used to create maps for your games.
It will produce TMX files based on the map you've created so you can import it into your cocos2d project. There are many game development platforms that support TMX beyond cocos2d.
The TMX file that is generated will correlate to the layers you created in Tiled and will be seamlessly usable in your cocos2d project in the call to the tiles.load() defintion.
Pay attention to what you call your layers in Tiled. They will be specified in the <layer> tags in the .tmx file.


-----------------
For example:
-----------------

In map.tmx in the /tiles directory, we have this line:

	<layer name="Ground" width="50" height="50">

Which correlates to:

	ground_layer = tiles.load('tiles/map.tmx')['Ground']
	
In the main.py file. Easy peasy.

-----------------


Tiled is very easy to use. If you are not familiar with it, watch this 20-minute video and you'll have the basics down:
https://www.youtube.com/watch?v=ZwaomOYGuYo


====================
IMPORTANT LINKS:
	- http://spritedatabase.net/ - Excellent source for sprite sheets
	- http://opengameart.org/ - Another Awesome source for game art
	- http://www.mapeditor.org/ - Neato map editor that will create maps in the TMX format
	- https://github.com/bjorn/tiled - github page for Tiled