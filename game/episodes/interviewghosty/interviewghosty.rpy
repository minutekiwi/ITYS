init -197 python:
    episodes.append(Episode("Interview With A Ghost!","interviewghosty","episodes/interviewghosty/icon.png"))
label interviewghosty:
stop music fadeout 1
scene bg room
show tara fistup closed grin:
    xpos .25 yalign .5
show morgan phone:
    xpos .75 yalign .5 xzoom -1
with Dissolve(1.0)
tara "It's finally here… The moment you've all been waiting for."
show tara sly
with diz
tara "It's I Told You So's very first…"
show tara wide shock raised yell:
    ease .5 zoom 1.1
    ease .15 yoffset -20
    ease .15 yoffset 0
    ease .15 yoffset -20
    ease .15 yoffset 0
show morgan:
    pause .4
    ease .2 yoffset -5
    ease .2 yoffset 0
    ease .2 yoffset -5
    ease .2 yoffset 0
with diz
tara "INTERVIEW WITH A GHOST!"
show tara closed grin:
    ease .5 zoom 1
with diz
tara "I'm your host, Tara— "
show tara fistup shockaway nyell:
    ease .5 xpos .5
    ease .15 yoffset -20
    ease .15 yoffset 0
    ease .15 yoffset -20
    ease .15 yoffset 0
with diz
tara " — alongside my handsome assistant, Morgan!"
show tara uclosed smile
show morgan standing wink nya
with diz
morgan "Hey."
show tara away grin neutral:
    xzoom -1
    ease .5 xpos .25
    ease .5 xzoom 1
show morgan default smile
with diz
tara "So Morgan, can you tell the audience a little bit about ghosts in your experience?"
show tara smile
show morgan closed sigh
with diz
morgan "Sure. From what I've seen, ghosts like to float around barefoot and turn into little lights when they don't want to be seen."
show morgan wink nya
with diz
morgan "And they're very gay."
show tara closed nyell raised
show morgan default smile
with diz
tara "Ain't that the truth! Long-time listeners will be well aware of my many escapades into the forgotten cemeteries of Salem in search of a ghost… "
show tara fierce shock:
    easein_elastic 1 zoom 1.2
tara "I'm proud to announce every single trip was ONE-HUNDRED percent worth it!"
show tara evil smirk furrow:
    parallel:
        ease .5 zoom 1
    parallel:
        ease .1 xoffset 5
        ease .1 xoffset -5
        ease .1 xoffset 2
        ease .1 xoffset -4
        ease .1 xoffset 4
        ease .1 xoffset -2
        repeat
tara "Every show has its skeptics. Every believer has ten non-believers behind them. But today, I can finally say… "
show ityslogo:
    yalign .5 ypos 0 xalign .5
    easein_bounce 2 ypos .35
show stars:
    xalign .5 xpos .25 rotate 10 zoom .5 yalign .5
    parallel:
        block:
            ease .5 rotate -5
            ease .5 rotate 5
            repeat
    parallel:
        ease .5 zoom 1.0
show stars as stars2:
    xalign .5 xpos .75 rotate 10 zoom .5 yalign .5 ypos .35 yzoom -1 xzoom -1
    parallel:
        block:
            ease .5 rotate -5
            ease .5 rotate 5
            repeat
    parallel:
        ease .5 zoom 1.0
show tara uclosed fierce grin fistup:
    parallel:
        ease .15 yoffset -20
        ease .15 yoffset 0
    parallel:
        ease .15 xzoom -1
        ease .15 xzoom 1
show morgan wink nya raised:
    parallel:
        ease .15 yoffset -20
        ease .15 yoffset 0
    parallel:
        ease .15 xzoom 1
        ease .15 xzoom -1
with diz
taramorgan "I TOLD YOU SO!"
hide stars
hide stars2
hide ityslogo
show tara shock yell raised wide
show morgan smile default neutral
with diz
tara "Come on out, Abigail Dalsing!"

play music snowydays
show abby uclosed open raised oho:
    xpos 1 yalign .5
    ease 1 xpos .5
    ease .15 yoffset -20
    ease .15 yoffset 0
    ease .15 yoffset -20
    ease .15 yoffset 0
show tara uclosed smile:
    ease 1 xpos .2
show morgan:
    ease 1 xpos .8
with diz
abby "Hello, hello!"

show tara open uclosed neutral fistup
show abby default smile neutral standing
with diz
tara "So good to see you, Abby!"

show abby uclosed open:
    ease .5 xpos .45
    ease .15 yoffset -20
    ease .15 yoffset 0
    ease .15 yoffset -20
    ease .15 yoffset 0
show tara smile default
with diz
abby "And you too, Tara! I can't believe it has been a full day since we last spoke."

show abby default smile:
    xzoom -1
    ease .5 xpos .5
    ease .1 xzoom 1
show morgan closed nya
with diz
morgan "Time really flies."

show tara fierce shock grin wide
show morgan smile default
with diz
tara "Let's get this show on the road! So, Abs, can you introduce yourself to our audience?"

show tara smile
show abby narrow worry small
with diz
abby "...?"

show tara furrow open default fistup
with diz
tara "Abby?"

show abby sigh angry:
    ease .5 rotate 5 xpos .51 zoom 1.1
    ease .5 rotate -5 xpos .49 zoom 1.1
    ease .5 rotate 0
show tara dot
with diz
abby "Where is the audience? Shouldn't I speak to them?"

show tara shockaway open sweat
show abby small
with diz
tara "Oh, man, Maddie, I thought you told me she was ready!"

# Maddie peeking in
show offscreen_mad:
    xalign .5 xpos .85 yalign .95 ypos .95
    ease 1 yoffset -15
show maddie_nervous_os:
    xpos .85 yalign .95 ypos .95
    ease 1 yoffset -15
with diz
show tara smile
maddie "She is! I… Sweetheart, the audience isn't here. We're {i}streaming{/i}, remember?"
hide offscreen_mad
hide maddie_nervous_os
show tara uclosed neutral -sweat
show abby uclosed laugh raised oho:
    ease .2 xpos .5 zoom 1 rotate 0
    yoffset 0
    ease .1 yoffset -15
    ease .1 yoffset 0
    ease .1 yoffset -15
    ease .1 yoffset 0
with diz
abby "Oh! Right!"

# Abigail gets super close to the screen
show tara -sweat
show abby standing sparkle default neutral open:
    ease .2 zoom 1.5
    ease 5 zoom 1.7
with diz
abby "Hello, audience, my name is Abigail Dalsing. I died two hundred years ago, and-"

show abby narrow uneven sigh:
    ease .1 xzoom -1
    ease .15 yoffset -20
    ease .15 yoffset 0
    ease .15 yoffset -20
    ease .15 yoffset 0

with diz
abby "Or, wait, maybe it was longer ago? Regardless, I'm better now!"
show offscreen_mad:
    xalign .5 xpos .85 yalign .95 ypos .95
    ease 1 yoffset -15
show maddie_agree_os:
    xpos .85 yalign .95 ypos .95
    ease 1 yoffset -15
show abby smile uclosed neutral
with diz
maddie "{i}Sweetie, back up from the camera.{/i}"
hide offscreen_mad
hide maddie_agree_os
with diz
show abby default -sparkle:
    ease .5 xzoom 1 zoom 1 rotate -0
show tara shock open raised:
    ease .15 yoffset -20
    ease .15 yoffset 0
    ease .15 yoffset -20
    ease .15 yoffset 0

with diz
tara "Wow! Two hundred years… What did you do all that time?"

show tara dot
show abby uclosed open
with diz
abby "Well… I mostly just walked around a lot. I sang to the animals, spoke to the fairies— "

show tara sweat horror neutral nyell wide:
    ease .05 xoffset -5
    ease .05 xoffset 0
    repeat 2
show morgan raised
show abby raised horror small:
    ease .05 xoffset -5
    ease .05 xoffset 0
    repeat 2
tara "Abby wait that's another episode!"

show tara -sweat smile fistup
show morgan neutral
show abby worry uclosed open
with diz
abby "Oh, sorry! Let's see… I also spent a lot of time with my friend, the forest spirit— "

show tara sweat uclosed nyell fierce wide:
    ease .05 xoffset -5
    ease .05 xoffset 0
    repeat 3
show abby raised horror small:
    ease .05 xoffset -5
    ease .05 xoffset 0
    repeat 2
tara "That's also gonna be another episode! Don't worry folks, we'll fill you all in with due time!"

show tara -sweat default smile neutral
show abby narrow open worry
with diz
abby "All of my activities were quite magical now that I think about it."

show tara grin
show abby default smile neutral
with diz
tara "What do you think is society's biggest misconceptions about ghosts?"

show tara smile
show abby angry sigh narrow
with diz
abby "Oh, absolutely how scary they are! Ghosts in stories and films terrify me!"

show abby uclosed open blush neutral
with diz
abby "But cuddling with Madison while we watch horror films isn't so bad… So maybe it's a good thing!"

show abby narrow pout
show tara sly smirk:
    ease 2 xpos .24

with diz
tara "Gay."

show abby -blush nya default
show tara closed nyell fierce fistup:
    ease .5 xpos .2
    ease .15 yoffset -20
    ease .15 yoffset 0
    ease .15 yoffset -20
    ease .15 yoffset 0
with diz
tara "Our viewers demand proof for everything. That's why I put my life on the line {b}DAILY{/b} to bring them the content they deserve."

show tara shock raised:
    ease .5 rotate 5 zoom 1.1
with diz
tara "We asked you to bring a souvenir from your time as a ghost. What do you got for us?"

show tara smile:
    ease .2 rotate 1 zoom 1
show abby uclosed open sparkle
with diz
abby "I couldn't think of much, so instead, I thought I could demonstrate. A skill only a former ghost could perform."

show tara shock open raised wide:
    yoffset 0
    ease .15 yoffset -20
    ease .15 yoffset 0
    ease .15 yoffset -20
    ease .15 yoffset 0
show abby nya default -sparkle
with diz
tara "Woah! A real former-ghost demonstration!"

stop music fadeout 1
show tara cat default fistup
show abby uclosed sigh
with diz
abby "Ah-hem-hem."

show black behind abby:
    alpha 0
    ease 3 alpha .9
show abby small
with diz
abby "..."

show abby:
    ease .05 xoffset -5
    ease .05 xoffset 0
    repeat
abby "... …. ……. … "

hide black
show abby horror yell raised:
    easein_elastic .3 zoom 2
show tara dot raised shock:
    ease .05 xoffset -5
    ease .05 xoffset 0
    repeat 2
show morgan raised sigh
abby "... …. ………… Boo!"

show abby angry sparkle nya narrow:
    ease .5 zoom 1
show tara dot raised shock wide:
    ease .05 xoffset -5
    ease .05 xoffset 0
    repeat 2
show morgan away
with diz
tara "..."
show morgan closed worry
with diz
morgan "... ..."

show morgan raised default laugh
with diz
morgan "... Ahhhh...?"

show morgan small neutral
show tara horror woah yell:
    ease .05 xoffset 5
    ease .05 xoffset -5
    ease .05 xoffset 2
    ease .05 xoffset -4
    ease .05 xoffset 4
    ease .05 xoffset -2
    repeat
show abby horror small -sparkle:
    ease .05 xoffset -5
    ease .05 xoffset 0
    repeat 2
tara "!!!! AHHHHHH!!!"

play music restlessone
show tara dot:
    xoffset 0
show morgan smile default
show abby yell uclosed worry
with diz
abby "It was merely a joke, Tara! Please don't get scared!"

show abby oho narrow laugh angry:
    yoffset 0
    ease .15 yoffset -20
    ease .15 yoffset 0
    ease .15 yoffset -20
    ease .15 yoffset 0
with diz
abby "... That was pretty good though, wasn't it?"

show abby nya
show tara fierce uclosed nyell:
    yoffset 0
    ease .15 yoffset -20
    ease .15 yoffset 0
    ease .15 yoffset -20
    ease .15 yoffset 0
with diz
tara "Absolutely! See right there, folks? Pure, unfiltered, fool-proof evidence!"

show tara default
with diz
tara "Before we go, what's one thing you'd like to tell all the other ghosts out there?"

show tara smile
show abby default standing open neutral
with diz
abby "Hm… Don't lose hope! You'll find your very own someone someday soon."

show abby uclosed blush raised
with diz
abby "Love is the greatest magic! You'll find a way to be together!"

show tara dot raised
show morgan raised
show abby -blush default
with diz
abby "Also, learn how to turn book pages if you haven't yet… Then try to find something called {i}manga{/i}, they're so much more fun than stuffy old 1800's texts."

show abby default sparkle laugh raised:
    yoffset 0
    ease .15 yoffset -20
    ease .15 yoffset 0
    ease .15 yoffset -20
    ease .15 yoffset 0

with diz
abby "Oh! And try floating on a plane! I never got the chance, but I bet it's really fun!"

show abby uclosed neutral open -sparkle:
    yoffset 0
    ease .15 yoffset -20
    ease .15 yoffset 0
    ease .15 yoffset -20
    ease .15 yoffset 0
show tara raised
show morgan away
with diz
abby "And don't forget to brush your teeth!"

show tara smile furrow uclosed
show abby uclosed:
    ease .15 yoffset -20
    ease .15 yoffset 0
    ease .15 yoffset -20
    ease .15 yoffset 0
with diz
abby "And-"

show abby behind tara, morgan:
    ease .5 xoffset -15
    ease .1 yoffset -10
    ease .1 yoffset 0
    ease .1 yoffset -10
    ease .1 yoffset 0
    ease .5 xoffset 0
    ease .1 yoffset -10
    ease .1 yoffset 0
    ease .1 yoffset -10
    ease .1 yoffset 0
    repeat
show tara:
    ease 1 zoom 1.3 xpos .35
show morgan raised nya:
    ease 1 zoom 1.3 xpos .65
morgan "I think she's gonna keep going."

show tara away open
show morgan smile
with diz
tara "Probably."

show tara smile
show morgan default laugh
with diz
morgan "Well, that's all for this episode."

show tara fierce shock nyell:
    yoffset 0
    ease .15 yoffset -20
    ease .15 yoffset 0
    ease .15 yoffset -20
    ease .15 yoffset 0
show morgan smile
with diz
tara "I'm Tara!"

show tara smile
show morgan nya:
    yoffset 0
    ease .15 yoffset -10
    ease .15 yoffset 0
    ease .15 yoffset -10
    ease .15 yoffset 0
with diz
morgan "I'm Morgan."

show stars:
    xalign .5 xpos .35 rotate 10 zoom .8 yalign .5
    parallel:
        block:
            ease .5 rotate -5
            ease .5 rotate 5
            repeat
    parallel:
        ease .5 zoom 1.0
show stars as stars2:
    xalign .5 xpos .65 rotate 10 zoom .8 yalign .5 ypos .35 yzoom -1 xzoom -1
    parallel:
        block:
            ease .5 rotate -5
            ease .5 rotate 5
            repeat
    parallel:
        ease .5 zoom 1.0
show tara nyell shock fierce
show morgan wink

with diz
taramorgan "And we told you so." id interviewghosty_d6bf49f0

show black zorder 5:
    alpha 0
    ease 10 alpha .9
# Minor cut to black, comes back with overlay like STREAM ENDED
hide stars
hide stars2
show tara:
    pause .2
    ease 1 xpos 1.2
show morgan smile default:
    ease .2 xzoom 1
    ease 1 xpos 1.2
show abby:
    ease .2 xzoom -1
    ease 1 xpos 1.2

with diz
tara "You did awesome, Abby!"

morgan "Great job."

maddie "Seriously, sweetheart, you were amazing."

abby "Aww, thank you girls… I couldn't do it without you!"

morgan "Anyone hungry? I'm going to order a pizza."

tara "With pineapples?"

morgan "Of course babe."

maddie "Sure, we can stay for a bit. We've got time."

window hide
scene black with Dissolve(2.0)
stop music fadeout 2.5
$ renpy.pause(2.5)
return
