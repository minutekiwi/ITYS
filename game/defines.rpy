init -1 python:
    renpy.music.register_channel("mroom", "music", True)
    renpy.music.register_channel("ambient", "sfx", True)
    renpy.music.register_channel("movie_mono", "voice", False)
#the parameter, cursorlist, expects a list of list containg an image, a pos, and an offset, with the exception that the default cursor should have "default" instead of a position
define config.optimize_texture_bounds = True

define config.say_attribute_transition = {"master" : Dissolve(0.25)}
define diz = { "master" : Dissolve(0.25) }
define fadehold = Fade(0.5, 1.5, 0.5)
define flash = Fade(.25, 0, .75, color="#fff")
##Transforms
default chapter = 1
image chapterimage1:
    "gui/button/chapter1.png"
image chapterimage2:
    "gui/button/chapter2.png"
image chapterimage3:
    "gui/button/chapter3.png"
image chapterimage5:
    "gui/button/chapter5.png"
default save_name = "Trick or Truth"
