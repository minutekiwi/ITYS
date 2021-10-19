
# Episode class
init -500 python:
    class Episode:
        def __init__(self, title, script, icon, has_va=True):
            self.title = title
            self.script = script
            self.icon = icon
            self.has_va = has_va
    episodes = []
# Animation for button
transform ep_button:
    zoom .8
    yoffset 15
    alpha .9
    on hover,selected_hover:
        ease .25 alpha 1.0 yoffset 0
    on idle,selected_idle:
        ease .1 alpha .9 yoffset 15

# Episode select screen
screen choose_episode():
    add "bg roomblur":
        xalign 0.5 yalign 0.5

    vpgrid id "ep":
        cols 3
        spacing 50
        xalign .5 yalign .5
        mousewheel True
        for i in episodes:
            hbox:
                button:
                    background i.icon
                    action SetVariable("voiced_episode", i.has_va),SetVariable("save_name",i.title), Jump(i.script)
                    xsize 732 ysize 590
                    at ep_button
                    has vbox
                    xfill True yfill True
                    text i.title size 50 xalign .5 text_align .5 yalign .92
    vbar value YScrollValue("ep") style "vbar" xalign 0.975 unscrollable "hide" ysize 500 yalign .5
