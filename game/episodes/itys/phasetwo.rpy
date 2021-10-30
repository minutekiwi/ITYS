init -198 python:
    episodes.append(Episode("I Told You So!","itys","episodes/itys/icon.png"))
label itys:
scene black
stop music fadeout 3
with Dissolve(2.0)
tara "Dun dududun… dun dun dudun… dun dunnnnn…"

maddie "What tune are you trying to replicate right now?"

tara "You know, that one… like, that one. You know?"

maddie "... Sure."
scene bg room
show tara wide shock raised nyell:
    xpos .5 yalign .5
with Dissolve(1.0)
#fade in on tara
play music restlessone fadein 5
tara "Meowdy, everyone! Today’s the day!"
show tara sly grin
with diz
tara "\"The day for what?\" I hear you ask. Well, ladies, sit back and get ready for me to blow your minds."
show tara shock nyell fierce fistup

tara "Today, we enter… PHASE TWO!"
show tara uclosed wide:
    ease .1 yoffset -15
    ease .1 yoffset 0
    ease .15 xzoom -1
    ease .1 yoffset -15
    ease .1 yoffset 0
    ease .15 xzoom 1
    repeat 2
tara "New everything! New name, new content, and even a new co-host!"
show offscreen_abby:
    xalign .5 xpos .15 yalign .95 xzoom -1
    ease 1 yoffset -15
show abby_gasp_os:
    xpos .15 yalign .95 xzoom -1
    ease 1 yoffset -15
show tara smile
with diz
abby "Gasp!"
show tara closed raised fistup
hide abby_gasp_os
hide offscreen_abby
with diz
tara "I know, my dear unscripted friend. It’s quite the shock."
show tara shock nyell wide
with diz
tara "But now that we’ve proven conclusively that paranormal phenomena exist, it’s time to incorporate my status as a pioneer in the field of cryptozoology into the show as a whole."
show tara default worry cat
with diz
tara "And who better to do that with than my partner in discovery, partner in crime, and partner in life?"

#morgan moves on screen
show tara:
    ease 1 xpos .35
show morgan laugh:
    xzoom -1 yalign .5 xpos 1.1
    ease 2 xpos .65
morgan "Sup. I’m Morgan."
show morgan smile
show tara shock yell wide
show loveyhearts:
    xpos .175 yalign .5
#hearts around tara

with diz
tara "Isn’t she awesome? She’s so awesome. You’re so awesome, babe."
show morgan wink nya
with diz
morgan "Thanks, babe. Also, you’re gay."
show tara neutral sly smirk
show morgan smile
with diz
tara "Bet."
hide loveyhearts
show morgan default
show tara uclosed grin fierce
with diz
tara "Anyway, Morgan will be joining me as co-host going forward! The two of us are gonna uncover every hidden secret, every last cover-up, and everything the folks at the top don’t want you to see!"
show offscreen_abby:
    xalign .5 xpos .15 yalign .95 xzoom -1
    ease 1 yoffset -15
show abby_unsure_os:
    xpos .15 yalign .95 xzoom -1
    ease 1 yoffset -15
show tara cat
with diz
abby "Um… forgive me if I am mistaken, but I believe all three of those examples are the same thing, are they not?"
hide offscreen_abby
hide abby_unsure_os
show tara default worry grin
show morgan small raised
with diz
tara "Oh, Abby, you sweet yet misguided soul, all three are {i}very{/i} different. Although that may be because of all the time I’ve spent researching them."
show tara shock fierce nyell fistup
with diz
tara "It takes a level of insight honed by years of study to truly discern the difference."
show tara cat
show morgan away worry sigh
with diz
morgan "Watching your show counts as research, right?"
show morgan smile
show tara uclosed raised wide smirk:
    ease .1 yoffset -15
    ease .1 yoffset 0
tara "Naturally. The best research, even."
show tara cat
show morgan default raised nya
with diz
morgan "Then I’m an expert too. Good to know."
show morgan smile neutral
show tara default neutral grin
with diz
tara "And it’s thanks to the tireless efforts of yours truly and her wonderful girlfriend/research partner that we were able to find real proof of the supernatural deep in the forests of [[REDACTED]."
show offscreen_mad:
    xalign .5 xpos .85 yalign .95
    ease 1 yoffset -15
show maddie_nervous_os:
    xpos .85 yalign .95
    ease 1 yoffset -15

with diz
maddie "No saying the name of the town, please."
hide offscreen_mad
hide maddie_nervous_os
show tara fistup sly fierce nyell
with diz
tara "... Deep in the forests of an unnamed town full of magic."
show offscreen_mad:
    xalign .5 xpos .85 yalign .95
    ease 1 yoffset -15
show maddie_happy_os:
    xpos .85 yalign .95
    ease 1 yoffset -15
with diz
maddie "Much better."
show tara shock raised wide:
    ease .1 rotate 5 yoffset 15
    ease .1 yoffset 0
hide offscreen_mad
hide maddie_happy_os
with diz
tara "Our footage of fairies, forest spirits, and other magical instances in this unnamed town catapulted us from indie darlings to worldwide sensations. It was pretty rad."
show tara shock raised wide:
    ease .1 rotate -5 yoffset 15
    ease .1 yoffset 0

with diz
tara "So rad, in fact, that we realized we had to update the show to reflect that. And that update includes…"
show morgan away raised laugh:
    ease .1 yoffset -15
    ease .1 yoffset 0
show tara uclosed fierce fistup:
    ease .1 yoffset -15 rotate 0
    ease .1 yoffset 0
taramorgan "A BRAND NEW NAME!"
show morgan smile
show tara shock wide raised grin
with diz
tara "That’s right, folks! It’s time to say goodbye to Taranormal, and say hello to the new and improved, extremely relevant, and very accurate title of our wonderful show!"

#show itys logo
show morgan:
    ease 1 xpos .85
show tara nyell fistup:
    ease 1 xpos .15
show ityslogo:
    yalign .5 ypos 0 xalign .5
    easein_bounce 2 ypos .35
tara "{i}I TOLD YOU SO!{/i}"
show offscreen_mad:
    xalign .5 xpos .85 yalign .95
    ease 1 yoffset -15
show maddie_nervous_os:
    xpos .85 yalign .95
    ease 1 yoffset -15

with diz
show tara cat
show morgan away neutral small
with diz
maddie "Wait, hang on. You told me that title was a joke. You aren’t actually going with that, are you?"
hide offscreen_mad
hide maddie_nervous_os
show tara sly fierce wide sigh
with diz
tara "You bet your ghost-loving ass I am."
show tara evil grin furrow
with diz
tara "So many of you people out there doubted me. They said I was crazy. That I was on a wild goose chase. That what I was after was fake."
show tara default fierce fistup nyell
with diz
tara "Well guess what? I was RIGHT! And now I’m gonna brag about it all I want!"
show tara horror fierce yell wide:
    parallel:
        ease 1 zoom 1.2
    parallel:
        ease .1 xoffset 5
        ease .1 xoffset -5
        ease .1 xoffset 2
        ease .1 xoffset -4
        ease .1 xoffset 4
        ease .1 xoffset -2
        repeat

tara "I TOLD YOU! I TOLD YOU F-"
show morgan wink laugh
with diz
morgan "Okay, babe. Time to take it down a notch."
show morgan smile
with diz
show tara sly raised sigh:
    easein_bounce .5 zoom 1.0
tara "Fiiiiiiine. But I {i}did{/i} tell you. Which means I have every right to rub it in."
show morgan default neutral laugh
show tara tongue
with diz
morgan "And I’m pretty good at rubbing it in, too."
show morgan smile
show tara shockaway raised grin
with diz
tara "She’s not kidding. I’ve seen her really go to town on someone, and it ruled."
show offscreen_abby:
    xalign .5 xpos .15 yalign .95 xzoom -1
    ease 1 yoffset -15
show abby_laugh_os:
    xpos .15 yalign .95 xzoom -1
    ease 1 yoffset -15
show tara smile
show morgan away
with diz
abby "She made him cry!"
hide offscreen_abby
hide abby_laugh_os
show morgan closed nya
with diz
morgan "Thanks for the reminder, sis."
show morgan default neutral laugh
with diz
morgan "Anyway, I’m looking forward to getting to know all of you from a perspective other than posting in the comments section."
show morgan smile
show tara away worry nyell fistup
with diz
tara "You’re still gonna post comments though, right? Cuz yours were always super sweet."
show morgan wink phone nya
show tara smile
with diz
morgan "Anything for you, babe."
show tara shock raised grin
show morgan smile
with diz
tara "Okay, that’s kinda gay. But also I love you."
stop music fadeout 5
show tara smile
show morgan wink laugh raised
with diz
morgan "Love you too. Ready to tell them about our new plans?"
play music snowydays fadein 5
show ityslogo:
    easeout_bounce 2 ypos -0.5
show morgan smile standing:
    ease 3 xpos .65
show tara uclosed fierce nyell wide:
    ease 3 xpos .35
tara "Boy am I! We’ve got so much new stuff coming your way that I don’t even know where to start!"
show tara shockaway raised smile
show morgan away
show abby oho raised laugh:
    rotate 10 xpos -2.5 yalign .5 xzoom -1
    ease 1 rotate 15 xpos 0
with diz
abby "I made you a numbered list, Tara!"
show abby smile
show tara default uneven grin fistup
with diz
tara "You see this? Being awesome literally runs in their family. How’s {i}that{/i} for evolution?"
show abby raised sigh:
    ease 3 xpos .25 rotate 0
abby "Perhaps it has something to do with our bloodline being mixed with fair-{w=4.65}{nw}" id itys_f977e68d
show maddie shock yell:
    rotate -12 xpos -.15 yalign .5 xzoom -1
    ease .15 xpos .15
    ease .35 xpos -.15
show abby horror raised:
    ease .1 yoffset -10
    ease .1 yoffset 0
    ease .35 xpos -.15
#abby yanked off screen
show tara horror nyell wide raised sweat
show morgan small
with diz
tara "That’s right! Your bloodline was mixed with, uh… fair maidens! Everyone loves a good fair maiden."
show offscreen_mad:
    xalign .5 xpos .85 yalign .95
    ease 1 yoffset -15
show maddie_lovey_os:
    xpos .85 yalign .95
    ease 1 yoffset -15
show loveyhearts:
    xalign .5 xpos .825 yalign .95
show tara smile
with diz
maddie "I know I do."

show offscreen_abby:
    xalign .5 xpos .15 yalign .95 xzoom -1
    ease 1 yoffset -15
show abby_lovey_os:
    xpos .15 yalign .95 xzoom -1
    ease 1 yoffset -15
show loveyheartsrev:
    xalign .5 xpos .15 xzoom -1 yalign .95
abby "Oh, Madison…"
show tara default worry grin wide -sweat
with diz
tara "Oh my God, you two. What am I going to do with you?"
hide abby_lovey_os
hide maddie_lovey_os
hide offscreen_mad
hide offscreen_abby
hide loveyhearts
hide loveyheartsrev
show morgan default neutral sigh
with diz
morgan "Tara. The list?"
show morgan smile
show tara fistup default worry grin
with diz
tara "Right, yeah. The list. Um… let’s see, first…"
show tara shock wide raised:
    ease .1 yoffset -10
    ease .1 yoffset 0

with diz
tara "First, you can expect a lot more interviews going forward!"
show tara uclosed fistup
with diz
tara "Since we got our hands on some conclusive proof, tons of experts have finally started to return my c- I mean, have been asking enthusiastically to be on our show!"
show morgan phone raised laugh
show tara smile
with diz
morgan "We even got that one guy from that alien history show. You know the one."
show morgan smile
show tara grin sly uneven
with diz
tara "Plus…… have any of you ever wanted an interview with an actual, real-life paranormal being? Well, get ready, because we just might have a little something for you there, too!"
show morgan closed standing laugh neutral
show tara cat
with diz
morgan "But that’s not all. We’ve got non-interview stuff, too."
show morgan smile default
show tara shock angled nyell wide
with diz
tara "That’s right! We’re gonna be doing something even more fun! One of my favorite things to do, in fact."
show offscreen_mad:
    xalign .5 xpos .85 yalign .95
    ease 1 yoffset -15
show maddie_fear_os:
    xpos .85 yalign .95
    ease 1 yoffset -15
show tara cat
with diz
maddie "Wait, hang on, no-"
hide offscreen_mad
hide maddie_fear_os
with diz
show stars:
    xalign .5 xpos .35 rotate 10 zoom .5 yalign .5
    parallel:
        block:
            ease .5 rotate -5
            ease .5 rotate 5
            repeat
    parallel:
        ease .5 zoom 1.0
show stars as stars2:
    xalign .5 xpos .67 rotate 10 zoom .5 yalign .5 ypos .35 yzoom -1 xzoom -1
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
taramorgan "Breaking and entering!"
show offscreen_mad:
    xalign .5 xpos .85 yalign .95
    ease 1 yoffset -15
show maddie_sigh_os:
    xpos .85 yalign .95
    ease 1 yoffset -15
show morgan smile
show tara smile
with diz
maddie "You do realize that announcing your intentions in a publicly viewable announcement video is absolutely going to be considered incriminating, right? You realize how bad an idea that is, right?"
hide maddie_sigh_os
hide offscreen_mad
hide stars
hide stars as stars2
show tara sly uneven sigh
with diz
tara "Pfff, it’ll be fine. We’re celebrities now. Celebrities never get in trouble."
show offscreen_abby:
    xalign .5 xpos .15 yalign .95 xzoom -1
    ease 1 yoffset -15
show abby_laugh_os:
    xpos .15 yalign .95 xzoom -1
    ease 1 yoffset -15
show tara dot
with diz
abby "She does have a point, Madison."
hide abby_laugh_os
hide offscreen_abby
show morgan away raised sigh
with diz
morgan "We won’t be breaking into any houses or anything. Just graveyards, ghost towns…"
show morgan default small
show tara wide smirk raised
with diz
tara "Secret government facilities…"
show morgan phone closed worry laugh
show tara cat
with diz
morgan "Babe, we agreed. No telling them about that one yet."
show morgan smile
show tara shock fierce fistup yell:
    ease .1 yoffset -10
    ease .1 yoffset 0
with diz
tara "YET."
show morgan standing wink neutral nya
show tara smile
with diz
morgan "We’ll also be discussing how to successfully incorporate cryptid study into a healthy relationship."
show offscreen_abby:
    xalign .5 xpos .15 yalign .95 xzoom -1
    ease 1 yoffset -15
show abby_loveyu_os:
    xpos .15 yalign .95 xzoom -1
    ease 1 yoffset -15
show morgan smile
with diz
abby "I see! So you’ll just be talking about how much you love each other for a section of each video."
hide offscreen_abby
hide abby_loveyu_os
show tara away worry wide lovey cat
with diz
tara "I mean, it’s more complicated than that…"
show morgan nya raised closed
with diz
morgan "That’s actually exactly what we’re going to do."
show offscreen_abby:
    xalign .5 xpos .15 yalign .95 xzoom -1
    ease 1 yoffset -15
show abby_laugh_os:
    xpos .15 yalign .95 xzoom -1
    ease 1 yoffset -15
show morgan smile
with diz
abby "Lovely!"
hide offscreen_abby
hide abby_laugh_os
show tara default raised grin -lovey
with diz
tara "And all your favorites will be returning, of course! Fanart Friday, Fact or Faketion, and Reader Mail will always be staples of the show."
show offscreen_mad:
    xalign .5 xpos .85 yalign .95
    ease 1 yoffset -15
show maddie_sigh_os:
    xpos .85 yalign .95
    ease 1 yoffset -15
show tara smile
with diz
maddie "Don’t forget the rants."
hide maddie_sigh_os
hide offscreen_mad
show tara sly uneven smirk
with diz
tara "I think you mean the {i}lectures,{/i} Mads."
show tara closed fistup raised grin
with diz
tara "And if you want to talk rants, we can always bring back your little \"monologues\"..."
show tara smile
show morgan away raised sigh
with diz
morgan "Those were actually really fun."
show morgan small
show tara away raised wide sigh
with diz
tara "Should we do Morgan Movie Monologues?"
show morgan default worry laugh
show tara dot
with diz
morgan "That would require watching movies."
show offscreen_mad:
    xalign .5 xpos .85 yalign .95
    ease 1 yoffset -15 zoom 1.2 xoffset -50
show maddie_films1_os:
    xpos .85 yalign .95
    ease 1 yoffset -15 zoom 1.2 xoffset -50
show morgan smile
with diz
maddie "They’re FIL…{w=1}{nw}"
hide maddie_films1_os
show offscreen_mad:
    xalign .5 xpos .85 yalign .95 yoffset -15 zoom 1.2 xoffset -50
    ease 1 zoom 1.0 yoffset 10 xoffset -20
show maddie_films2_os:
    xpos .85 yalign .95 yoffset -15 zoom 1.2 xoffset -50
    ease 1 zoom 1.0 yoffset 10 xoffset -20
extend " you know what, never mind."
hide offscreen_mad
hide maddie_films2_os
show tara default uneven sigh fistup
with diz
tara "Damn, college really did change you."
show morgan neutral
show tara shock wide grin raised
with diz
tara "Anyway! As you can see, we won’t deprive you of any of your favorites. We’ll just be giving you even more on top of it! It’s totally win-win."
show offscreen_abby:
    xalign .5 xpos .15 yalign .95 xzoom -1
    ease 1 yoffset -15
show abby_laugh_os:
    xpos .15 yalign .95 xzoom -1
    ease 1 yoffset -15

with diz
abby "Don’t forget the smug sense of satisfaction, Tara!" id itys_fa0da4e3
show tara uclosed fierce yell fistup
hide offscreen_abby
hide abby_laugh_os
with diz
tara "Oh right! That’s the most important part! We’re gonna have a ton of that."
show offscreen_mad:
    xalign .5 xpos .85 yalign .95
    ease 1 yoffset -15
show maddie_annoy_os:
    xpos .85 yalign .95
    ease 1 yoffset -15
with diz
show tara smile
maddie "Great. I’m sure that’s a huge selling point."
hide maddie_annoy_os
show maddie_annoy2_os:
    xpos .85 yalign .95 yoffset -15
show morgan away raised sigh
with diz
morgan "I’m pretty sure it actually is, Maddie."
show morgan smile
maddie "...{w=.5}{nw}" id itys_d5231967
hide maddie_annoy2_os
show offscreen_mad:
    xalign .5 xpos .85 yalign .95 yoffset -15
    ease 1 yoffset 0
show maddie_agree_os:
    xpos .85 yalign .95 yoffset -15
    ease 1 yoffset 0
with diz
extend " Yeah, it is."
hide offscreen_mad
hide maddie_agree_os
show tara default worry nyell wide
with diz
tara "Plus, if you ask nicely, maybe Morgan will do a segment on her workout routine."
show tara cat
show offscreen_mad:
    xalign .5 xpos .85 yalign .95
    ease 1 yoffset -15
show maddie_nervous_os:
    xpos .85 yalign .95
    ease 1 yoffset -15
with diz
maddie "How is that relevant to the show?"
show tara away
hide offscreen_mad
hide maddie_nervous_os
show morgan closed nya raised
with diz
morgan "It’s just a little gift from us to them. We know what the people want."
show tara away lovey nyell wide worry
show morgan smile
with diz
tara "I’m people."
show offscreen_abby:
    xalign .5 xpos .15 yalign .95 xzoom -1
    ease 1 yoffset -15
show abby_loveyu_os:
    xpos .15 yalign .95 xzoom -1
    ease 1 yoffset -15
show tara cat
with diz
abby "I think that’s very kind of you, Morgan! I look forward to following along."
hide abby_loveyu_os
hide offscreen_abby
show tara shock raised nyell fistup -lovey
with diz
tara "I’m sure we all are! Just one more reason to tune in!"
show tara uclosed grin wide
with diz
tara "And we’ve got even more reasons, too! So many reasons that I’m not even gonna bother naming them all off cuz there’s just SO MANY. Trust me." id itys_0e706ffc
show morgan wink raised laugh
with diz
morgan "And not because she’s making them up as she goes along."
show morgan smile
show tara sly uneven smirk fistup
with diz
tara "Of course not. Preparedness is my middle name."
show tara default pout raised
show offscreen_abby:
    xalign .5 xpos .15 yalign .95 xzoom -1
    ease 1 yoffset -15
show abby_unsure_os:
    xpos .15 yalign .95 xzoom -1
    ease 1 yoffset -15
with diz
abby "I thought it was Muriel."
show offscreen_mad:
    xalign .5 xpos .85 yalign .95
    ease 1 yoffset -15
show maddie_lovey_os:
    xpos .85 yalign .95
    ease 1 yoffset -15

with diz
maddie "It’s an expression, sweetie."
hide abby_unsure_os
show tara uclosed neutral smile wide
show offscreen_abby:
    xalign .5 xpos .15 yalign .95 xzoom -1 yoffset -15
    ease .1 yoffset -25
    ease .1 yoffset -15
show abby_excited_os:
    xpos .15 yalign .95 xzoom -1 yoffset -15
    ease .1 yoffset -25
    ease .1 yoffset -15
with diz
abby "Oh! Can I pick a middle name?"
hide maddie_lovey_os
show maddie_happy_os:
    xpos .85 yalign .95 yoffset -15
with diz
maddie "Of course, honey. Although we should probably save that for later."
show tara away
show morgan away
hide abby_excited_os
hide offscreen_abby
hide maddie_happy_os
show maddie_asking_os:
    xpos .85 yalign .95 yoffset -15
with diz
maddie "You two are going to be wrapping up now, I assume?"
hide maddie_asking_os
hide offscreen_mad
show tara default raised grin
with diz
tara "Sadly, yes. I’m sure you’re all craving more, and we’ll have it for you very very soon! So just hold on a bit longer, and we’ll deliver like you wouldn’t believe."
show tara smile
show morgan closed raised laugh
with diz
morgan "We won’t be holding out on you. After all, there’s no holding back when it comes to saying…"
show stars:
    xalign .5 xpos .35 rotate 10 zoom .5 yalign .5
    parallel:
        block:
            ease .5 rotate -5
            ease .5 rotate 5
            repeat
    parallel:
        ease .5 zoom 1.0
show stars as stars2:
    xalign .5 xpos .67 rotate 10 zoom .5 yalign .5 ypos .35 yzoom -1 xzoom -1
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
stop music fadeout 4
window hide
show white with Dissolve(5.0)
$renpy.pause(6)
    # This ends the game.

return
