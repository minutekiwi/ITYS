# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

default voiced_episode = False
init -1 python:
    renpy.music.register_channel("beep", mixer="voice", loop=True, stop_on_mute=True, tight=False, buffer_queue=True)
    def maddie_beep(event, **kwargs):
        global voiced_episode
        if event == "show" and not voiced_episode:
            renpy.music.play("maddieboop.ogg", channel="beep", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="beep")
    def tara_beep(event, **kwargs):
        global voiced_episode
        if event == "show" and not voiced_episode:
            renpy.music.play("taraboop.ogg", channel="beep", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="beep")
    def abby_beep(event, **kwargs):
        global voiced_episode
        if event == "show" and not voiced_episode:
            renpy.music.play("abbyboop.ogg", channel="beep", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="beep")
    def morgan_beep(event, **kwargs):
        global voiced_episode
        if event == "show" and not voiced_episode:
            renpy.music.play("morganboop.ogg", channel="beep", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="beep")
    def taramorgan_beep(event, **kwargs):
        global voiced_episode
        if event == "show" and not voiced_episode:
            renpy.music.play("taramorganboop.ogg", channel="beep", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="beep")

    def add_waits( str_to_test ):

        # our map of wait duration : strings to add those durations to
        global voiced_episode
        waits_map = {
          0.125 : [', '],
          0.25 : ['...',"…"],
          0.2 : ['. ', '? ', '! '] }

        for duration in waits_map:
            for substr in waits_map[duration]:
                if not voiced_episode:
                    str_to_test = str_to_test.replace(
                        substr,
                        "{}{{w={}}}".format(substr, duration) )

        return str_to_test

define config.say_menu_text_filter = add_waits

# The game starts here.



label start:

# Show a background. This uses a placeholder by default, but you can
# add a file (named either "bg room.png" or "bg room.jpg") to the
# images directory to show it.
scene bg roomblur with Dissolve(2.0)
call screen choose_episode with Dissolve(1.0)
#***

#black screen
