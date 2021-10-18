init -199 python:
    episodes.append(Episode("Stay Spooky, Maddie!","stayspooky","episodes/stayspooky/icon.png"))
label stayspooky:
scene bg room
show tara open:
    xpos .25 yalign .5
show maddie:
    xpos .75 yalign .5
with Dissolve(1.0)
tara "And {i}that’s{/i} why you should never follow faceless versions of your super cool best friend into the woods during a snowstorm. It’s really not that hard to understand."
show tara smile
show maddie sly flat sigh
with diz
maddie "You don’t have to rub it in."
show tara closed raised nyell
show maddie small
with diz
tara "Yes I do. Now then…"
show tara wide sly uneven open
with diz
tara "I guess that just leaves us with the grand finale, doesn’t it? The moment you’ve all been waiting for."
show tara dot
show maddie narrow worry laugh
with diz
maddie "That makes it sound like they’re excited to get rid of me."
show tara uclosed furror sigh fistup
show maddie smile
with diz
tara "Okay, maybe not waiting for. Uh… dreading?"
show tara dot
show maddie away sigh neutral
with diz
maddie "Closer."
show abby sigh:
    xpos 1.25 zoom 1.2
    ease 1 xpos 1.0 rotate -30
show maddie small
with diz
abby "Despondent over?"
show abby small
show morgan sigh:
    zoom 1.25 xpos -.25
    ease 1 xpos 0.0 rotate 30
morgan "Bummed about?"
show morgan smile
show tara shock raised nyell wide:
    ease .1 yoffset -15
    ease .1 yoffset 0
with diz
tara "Yeah! Those!"
show abby:
    ease 2 xpos 1.25 rotate 0
show morgan:
    ease 2 xpos -.25 rotate 0
show tara fistup furror open
with diz
tara "The moment you’ve all been despondebummed about… saying farewell to my wonderful co-host, Maddie Raines."
show tara powercry powerworry sigh
show maddie worry smile
with diz
tara "As you all know, she’s been with Taranormal since the very beginning. And with her departure, we say farewell to this first era of Taranormal that she helped build."
show tara wide shock raised nyell:
    ease .1 yoffset -15
    ease .1 yoffset 0
tara "But hold off on those tears, ladies! Our lovely Mads is moving on to bigger and better things: first, a college degree!"
show maddie default laugh neutral
show tara smile
with diz
maddie "As a film major, of course."
show maddie smile
show tara sly uneven open fistup
with diz
#smug tara

tara "And secondly, to spend more time with her brand new bae~"

#abby pops in from off screen
show tara horror smile raised wide:
    ease .1 yoffset -15
    ease .1 yoffset 0
show maddie uclosed
# show abby_window behind abby:
#     xalign 0.5
#     yalign .95
show abby laugh:
    xpos .85 zoom 1.5 ypos 1.0 rotate -15
    easein_elastic 1 ypos .15 zoom 1.35
abby "{space=30}{size=150}Boo!" #(window_background=Transform(Frame("gui/textbox_abby.png"),alpha=0.0))
hide abby
hide abby_window
show abby:
    xpos 1.25  zoom 1.0 yalign .5
    ease 2 xpos .85
show tara horror raised nyell
show maddie:
    ease 1 xpos .65
with diz
tara "Whoa. Deja vu. I could have sworn you did that to us before once."
show abby uclosed laugh
show tara smile
with diz
#abby moves fully onto screen

abby "I don’t think so. I’ve never been on camera before. At least not for anyone other than Madison."
show abby smile
show tara default
show maddie default neutral laugh
with diz
maddie "No time like the present, sweetie."
show maddie smile
show tara away open fistup
with diz
tara "Go ahead and introduce yourself!"
show abby uclosed open oho raised
show tara smile
with diz
abby "Ah, yes! Well! My name is Abigail Dalsing, and I am Madison’s beloved. It is a pleasure to meet all of you!"
show abby default neutral smile
show tara uclosed neutral nyell:
    easeout .11 xoffset 5
    easein .11 xoffset 0
    easeout .11 xoffset -5
    easein .11 xoffset 0
    repeat 2
with diz
tara "Isn’t she great, folks?"
show maddie gentle blush heart laugh guard:
    ypos .5
show tara smile
with diz
maddie "She’s amazing. You’re amazing, sweetie."
show loveyheartsrev:
    yalign .5 xpos .675
show abby narrow open standing
show tara default
show maddie smile
with diz
abby "Oh, thank you, my love. You never fail to set my heart aflutter."
show abby smile default raised
show tara sly open
with diz
tara "Guys. Camera. Show."
show abby neutral
show tara smile
show maddie away sigh -heart
with diz
maddie "Oh! Right, right. Sorry."
show maddie narrow neutral laugh heart
with diz
#maddie sprite leans over to abby like she’s whispering

maddie "We’ll pick this up later, honey."
show abby narrow raised open oho
show maddie uclosed smile
with diz
abby "Oooh, yes please!"
hide loveyheartsrev
show maddie -heart -blush
show tara shock raised nyell
show abby smile uclosed
with diz
tara "As you can see, Mads definitely has her priorities straight. Well, not {b}straight,{/b} obviously, but you know what I mean."
show morgan laugh:
    zoom 1.25 xpos -.25
    ease .5 xpos 0.0 rotate 30
show tara smile
with diz
morgan "Priorities gay."
show tara uclosed nyell wide:
    ease .1 yoffset -10
    ease .1 yoffset 0
    easeout .11 xoffset 5
    easein .11 xoffset 0
    easeout .11 xoffset -5
    easein .11 xoffset 0

with diz
tara "This guy gets it!"
show abby:
    ease 0.25 yoffset -50 xzoom -1.0
    ease .25 yoffset 0
    ease 3 xpos 1.5
show morgan:
    ease 2 xpos -.25 rotate 0
#abby goes offscreen
show tara default open wide:
    ease 2 xpos .35 zoom 1.1
show maddie default smile standing:
    ease 2 xpos .65 zoom 1.1
with diz
tara "Before we say our goodbyes, I want to reassure all my loving fans that the show is far from over!"
show tara fistup sly uneven sigh
show maddie sly small
with diz
tara "In fact, now that we’ve proved that I was right about everything all along and should never be doubted about anything ever… "
show tara shock raised nyell
show maddie default smile
with diz
tara "I think we might be due for a rebranding of sorts."
show tara smile
show maddie guard laugh
with diz
maddie "But that’s a story for another time."
show tara away sigh
show maddie away smile
with diz
tara "That’s right, Mads. For now, it’s time for the big farewell."
show tara default furror open wide
show maddie worry
with diz
tara "I’m… I’m gonna miss you, Mads."
show tara smile
show maddie uclosed standing laugh
with diz
maddie "I’ll miss you too. And I’ll miss this show. But I won’t be going far!"
show maddie narrow neutral
with diz
maddie "I do still live with you, after all."
show tara uclosed open
with diz
tara "And you’ll be a guest on the show every now and then, right?"
hide abby
show maddie sly sigh
with diz
maddie "I never said that I-"
show maddie default guard
show tara wide horror smile raised
with diz
#show abby_window
show abby laugh:
    xpos .85 zoom 1.5 ypos 1.0 rotate -15
    easein_elastic 1 ypos .15 zoom 1.35
abby "{space=30}{size=100}Of course she will!" #(window_background=Transform(Frame("gui/textbox_abby.png"),alpha=0.0))
hide abby_window
show abby oho uclosed smile:
    xpos .85 zoom 1.35 ypos .15 rotate -15
    ease 1 ypos 1.5
show tara shock nyell
show maddie uclosed worry smile standing
with diz
tara "I’m taking that as a guarantee."
show tara default furror open
show maddie default neutral
with diz
tara "Now then, I hope you’ll join me in wishing a very fond farewell to Maddie, and to the first era of our show."
show maddie gentle laugh
show tara neutral smile fistup
with diz
maddie "Thank you very much for all your support over the years. I’ll always be grateful for it."
show maddie smile
show tara uclosed nyell
with diz
tara "Aww, you softie."
show maddie guard away worry laugh
show tara away tongue
with diz
maddie "Oh, hush."
show tara default neutral smile
show maddie standing default laugh neutral
with diz
maddie "And yes, this is an ending. But it’s a beginning, too. You’ll see what we mean by that tomorrow."
show maddie smile
show tara shock nyell raised wide
with diz
tara "Trust us when we tell you that you’re gonna love it."
show tara default neutral open fistup
with diz
tara "Now would you like to do the honors, Mads?"
show maddie uclosed guard laugh
show tara uclosed smile wide
with diz
maddie "Oh, why not?"
show maddie gentle sigh
with diz
maddie "Until then…"
hide tara
show bg roomblur
show white behind maddie:
    alpha .15
show maddie standing uclosed laugh:
    xpos .5 yalign .5 zoom 1.2
with Dissolve(.5)
maddie "{size=50}{i}Stay spooky, everyone!{/i}{/size}"
scene black with Dissolve(2.0)
$ renpy.pause(2.5)
return
