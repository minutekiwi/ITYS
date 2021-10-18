init -197 python:
    episodes.append(Episode("Interview With A Ghost!","interviewghosty","episodes/interviewghosty/icon.png"))
label interviewghosty:
scene bg room
show tara fistup closed grin:
    xpos .25 yalign .5
show morgan:
    xpos .75 yalign .5 xzoom -1
with Dissolve(1.0)
tara "It's finally here… The moment you've all been waiting for."
show tara sly
with diz
tara "It's I Told You So's very first…"
show tara wide shock raised yell
with diz
tara "INTERVIEW WITH A GHOST!"
show tara closed grin
with diz
tara "I'm your host, Tara— "
show tara fistup shockaway nyell
with diz
tara " — alongside my handsome assistant, Morgan!"
show tara uclosed smile
with diz
morgan "Hey."
show tara away grin neutral
with diz
tara "So Morgan, can you tell the audience a little bit about ghosts in your experience?"
show tara smile
with diz
morgan "Sure. From what I've seen, ghosts like to float around barefoot and turn into little lights when they don't want to be seen."

morgan "And they're very gay."
show tara closed nyell raised
with diz
tara "Ain't that the truth! Long-time listeners will be well aware of my many escapades into the forgotten cemeteries of Salem in search of a ghost… "
show tara fierce shock
tara "I'm proud to announce every single trip was ONE-HUNDRED percent worth it!"
show tara evil smirk furrow:
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
taramorgan "I TOLD YOU SO!"
hide stars
hide stars2
hide ityslogo
show tara shock yell raised wide
with diz
tara "Come on out, Abigail Dalsing!"

show abby:
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

abby "Hello, hello!"

show tara open default neutral
tara "So good to see you, Abby!"

show abby:
    ease .5 xpos .45
show tara smile
abby "And you too, Tara! I can't believe it has been a full day since we last spoke."

show abby:
    ease .5 xpos .5
morgan "Time really flies."

show tara fierce shock grin
tara "Let's get this show on the road! So, Abs, can you introduce yourself to our audience?"

show tara smile
abby "...?"

show tara furrow open
tara "Abby?"

show abby:
    ease .5 rotate 5 xpos .51 zoom 1.1
    ease .5 xpos .5 zoom 1 rotate 0
    ease .5 rotate -5 xpos .49 zoom 1.1
show tara dot
abby "Where is the audience? Shouldn't I speak to them?"

show tara shockaway open sweat
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
show tara uclosed neutral
show abby:
    ease .1 yoffset -15
    ease .1 yoffset 0
with diz
abby "Oh! Right!"

# Abigail gets super close to the screen

show abby:
    ease .2 zoom 1.5
    ease 5 zoom 1.7
abby "Hello, audience, my name is Abigail Dalsing. I died two hundred years ago, and-"

show abby:
    ease .1 xzoom -1
abby "Or, wait, maybe it was longer ago? Regardless, I'm better now!"
show offscreen_mad:
    xalign .5 xpos .85 yalign .95 ypos .95
    ease 1 yoffset -15
show maddie_agree_os:
    xpos .85 yalign .95 ypos .95
    ease 1 yoffset -15
with diz
maddie "{i}Sweetie, back up from the camera.{/i}"
hide offscreen_mad
hide maddie_agree_os
with diz
show abby:
    ease .5 xzoom 1 zoom 1 rotate -0

tara "Wow! Two hundred years… What did you do all that time?"

abby "Well… I mostly just walked around a lot. I sang to the animals, spoke to the fairies— "

tara "Abby wait that's another episode!"

abby "Oh, sorry! Let's see… I also spent a lot of time with my friend, the forest spirit— "

tara "That's also gonna be another episode! Don't worry folks, we'll fill you all in with due time!"

abby "All of my activities were quite magical now that I think about it."

tara "What do you think is society's biggest misconceptions about ghosts?"

abby "Oh, absolutely how scary they are! Ghosts in stories and films terrify me!"

abby "But cuddling with Madison while we watch horror films isn't so bad… So maybe it's a good thing!"

tara "Gay."

tara "Our viewers demand proof for everything. That's why I put my life on the line {b}DAILY{/b} to bring them the content they deserve."

tara "We asked you to bring a souvenir from your time as a ghost. What do you got for us?"

abby "I couldn't think of much, so instead, I thought I could demonstrate. A skill only a former ghost could perform."

tara "Woah! A real former-ghost demonstration!"

abby "Ah-hem-hem."

abby "..."

abby "... …. ……. … "

abby "... …. ………… Boo!"
tara "..."
morgan "... ..."

morgan "... Ahhhh...?"

tara "!!!! AHHHHHH!!!"

abby "It was merely a joke, Tara! Please don't get scared!"

abby "... That was pretty good though, wasn't it?"

tara "Absolutely! See right there, folks? Pure, unfiltered, fool-proof evidence!"

tara "Before we go, what's one thing you'd like to tell all the other ghosts out there?"

abby "Hm… Don't lose hope! You'll find your very own someone someday soon."

abby "Love is the greatest magic! You'll find a way to be together!"

abby "Also, learn how to turn book pages if you haven't yet… Then try to find something called {i}manga{/i}, they're so much more fun than stuffy old 1800's texts."

abby "Oh! And try floating on a plane! I never got the chance, but I bet it's really fun!"

abby "And don't forget to brush your teeth!"

abby "And-"

morgan "I think she's gonna keep going."

tara "Probably."

morgan "Well, that's all for this episode."

tara "I'm Tara!"

morgan "I'm Morgan."

taramorgan "And we told you so."

# Minor cut to black, comes back with overlay like STREAM ENDED

tara "You did awesome, Abby!"

morgan "Great job."

maddie "Seriously, sweetheart, you were amazing."

abby "Aww, thank you girls… I couldn't do it without you!"

morgan "Anyone hungry? I'm going to order a pizza."

tara "With pineapples?"

morgan "Of course babe."

maddie "Sure, we can stay for a bit. We've got time."
