init -200 python:
    episodes.append(Episode("Trick or Truth","halloween2018","episodes/halloween/icon.png",True))

default display = "pumpkinkoma"

    #Title, label, icon, desc
default annotation = True
transform cd_transform:
    # This is run before appear, show, or hide.
    xalign 0.5 yalign 0.0 alpha 0.0 yoffset 15

    on appear:
        alpha 1.0
    on show:
        zoom .75
        linear .25 zoom 1.0 alpha 1.0 yalign 0.0
    on hide:
        linear .25 yalign 1.0 alpha 0.0 zoom .75
transform stamp:
    alpha 0.0 zoom 1.5
    easeout .15 zoom .9 alpha 1.0
    easein .15 zoom 1.0

screen projector(display):
    showif annotation:
        add Solid("#000"):
            alpha 0.5
        frame at cd_transform:
            xalign 0.5 yalign 0.0 xpadding 100 ypadding 25
            hbox:
                add display:
                    zoom 0.55
    vbox:
        yoffset 15 xoffset 15
        #text "Toggle Annotations"
        style_prefix "radio"
        textbutton "Annotations" action [ToggleVariable("annotation", true_value=True, false_value=False)]
screen tort(verdict):
    hbox:
        xalign 0.5 yalign 0.5
        add verdict
        at stamp
label halloween2018:
    #blank screen. Tara chibi leans in from the side
stop music fadeout 1
scene black

show tara fierce avoid smirk:
    xoffset 1200 xalign 1.0 rotate 0 yanchor .05 xzoom -1
    easeout 1 xoffset 500 rotate -10

tara "It's Halloween!"

show tara shock grin raised:
    linear .2 yoffset -100 xoffset -500 rotate 360
    rotate 0
    linear .2 yoffset 5 xoffset -120 rotate 360
#make a huge hopping animation

tara "IT'S HALLOWEEN!!!"

show tara yell:
    zoom 2.0 xalign 0.5 yalign 0.5
    block:
        pause 0.1
        block:
            choice:
                xoffset 90
            choice:
                xoffset 110
            choice:
                xoffset 100
        block:
            choice:
                yoffset 100
            choice:
                yoffset 105
            choice:
                yoffset 95
        repeat

tara "{b}IT'S HALLOWEEN!!!!!!!!!!!!{/b}"

#maddie offscreen

maddie "Get back here."
$play_music(halloweensong)
#chibi tara pulls back. Normal maddie and tara
hide tara
scene taranormal
show tara front smile normal at left:
    yalign .5
show maddie at right:
    yalign .5

maddie closed open lower "Do you really have to be like this every single year?"
show maddie frown
voice "VA/halloween2018_e14915f7.ogg"
tara away smirk worry "Uh, yes? This is literally the best day of the year. I'm legally allowed to be as excited as I want."

show tara cat
maddie attaralow gape "I don't remember that being a law."

show maddie frown
voice "VA/halloween2018_54d6f852.ogg"
tara shockaway raised smirk "Well, it isn't a law {i}yet.{/i} But soon…"

tara direct grin normal "Soon…"
show tara smile
"" #Blank text box
show maddie sigh
maddie away "Well, okay then."
show maddie frown
tara shock yell fierce "ANYWAY! Welcome, everyone, to the Totally Terrifying Taranormal Halloween Special! Or at least the part of it we're going to include in this little bonus game."
show tara -yell
maddie front raised grin "These things tend to go on for {i}hours.{/i} Consider yourselves lucky."
show maddie attara smile

# tara closed grin raised "Before we start, I wanna point out this awesome Taranormal shirt I'm wearing. You can't buy it anywhere or anything, I just think it looks really cool."
# show tara cat
# maddie front grin "Thanks to {a=https://twitter.com/mgcoco_art}@mgcoco{/a} for the wonderful design. Be sure to keep an eye out for it in the main release!"
# show maddie smile attara normal
# voice "VA/redux tara 1.ogg"
# tara closed grin raised "Before we start, I wanna point out this awesome Taranormal shirt I'm wearing. You can buy your own copy on the Studio Élan webstore, whatever that means... Hey Mads, can you make sure to add a link to the webshop?"
# voice "VA/redux maddie 1.ogg"
# maddie attara open uneven "{a=https://vnstudioelan.com/store}A link to the what?{/a}"
# voice "VA/redux tara 2.ogg"
# show maddie frown
# tara shock yell raised "Perfect, thanks! Okay, moving on..."

tara front smirk normal "On that note, let's start the show by taking a look at some more awesome creations in this very special edition of..."
show fanart at top:
    yoffset 100
show maddie shock gape raised
show thunder behind tara:
    alpha 0.1
    linear 0.2 alpha 1.0
    linear 0.05 alpha 0.2
    linear 0.2 alpha 1.0
    pause 0.3
    linear 0.5 alpha 0.0
play audio [ scarytopic, "<silence .5>" ] fadein 1 fadeout 1
tara fierce shock yell "FRIGHTFUL FANART!"

hide fanart
hide thunder
with dissolve
show maddie attara normal smile
tara front grin normal "We've got a real treat for you this week. Our friend Kiri has put together some super awesome comics starring yours truly! And Mads, of course."
show tara shockaway pout
maddie worry open "I think the term is \"4koma.\""
show maddie -open -worry
tara raised smile "Oh yeah! That means you're supposed to read them in a different direction, right?"
maddie front grin normal"Don't worry, you won't get lost. The panels are numbered."
$ display = "pumpkinkoma"
#show screen annotations
show screen projector([display])
show tara:
    yoffset 250 xoffset 100
show maddie:
    yoffset 250 xoffset -100
with fade
$renpy.notify("View and Hide the image by toggling annotations at any time.")
tara closed furrow "I love this so much."
show maddie attara smile
maddie grin raised "It certainly does capture your essence, that's for sure. Except it's usually three in the morning rather than midnight."
show maddie -grin
tara avoid smirk fierce "I wonder if it's possible to actually verbalize emoji…"
show tara smile
maddie yell closed worry "I think I'm better off not knowing, thanks."
hide black
hide pumpkinkoma
maddie direct uneven gape "Also, who's Rachel?"
show maddie frown
tara direct grin furrow "Probably nobody important. Next!"
$display = "maddiekoma"
$annotation = True
show screen projector([display])
show maddie shockaway raised
tara front grin normal "Now isn't {i}this{/i} a blast from the past."

maddie shock grin "HAHAHA I DON'T KNOW WHAT YOU'RE TALKING ABOUT! I NEVER LOOKED LIKE THAT!"
show maddie frown
tara direct raised smirk "Then I suppose you won't mind if I show the audience a certain photo I just happen to have right here in my hand…"
show maddie:
    pause 0.1
    block:
        choice:
            xoffset -95
        choice:
            xoffset -105
        choice:
            xoffset -100
    block:
        choice:
            yoffset 250
        choice:
            yoffset 255
        choice:
            yoffset 245
    repeat
maddie shockaway "{b}DON'T YOU DARE.{/b}"
hide screen projector

show gothmaddie:
    zoom 0.8 xalign 0.5 yalign 0.1
    yoffset 900
    ease 5 yoffset 0
with dissolve
#goth maddie pic slowly slides on screen.

tara "I hate to admit it, but you rocked this look even better than I did. When are you gonna bring back the clip-on piercings?"
show gothmaddie behind maddie
show tara smile
show maddie:
    easeout 0.5 yoffset 0 xoffset 0 xpos .5
maddie yell shock raised "HA HA, VERY FUNNY! WHAT A SILLY PHOTO THAT DEFINITELY ISN'T ME! THANKS TARA! THAT'S ENOUGH OF THAT NOW!"
show maddie away frown worry:
    easein 1 xoffset -1500 yoffset 0
    pause 1
    ease 1 xoffset 0 xpos .95 yoffset 250
show gothmaddie:
    easein 1 xoffset -1500
#maddie and goth maddie photo both move off screen. Maddie comes back on and puts the comic back in place then goes back to the side

tara grin raised "Y'know Mads, I bet you could still pull it off. Maybe edgy goth vlogging was your true calling all along."

tara smirk closed normal "But know this."

#zoom on tara's face
show taranormal behind tara:
    zoom 1.25 yalign 0.75
show tara:
    zoom 1.25 yoffset 100 xoffset 150
hide maddie
with None
#show maddie:
    #ease 2 xoffset -600 zoom 0.5

tara direct furrow "If you do ever decide to challenge me…"
stop music
show taranormal:
    zoom 2.0
show tara:
    zoom 1.5 yoffset 0 xpos .5 xoffset 0
voice "VA/halloween2018_9a621009.ogg"
tara evil thin fierce "I will crush you. {w=0.008}Without hesitation. {w=0.008}Without mercy."
scene taranormal
show maddie shockaway yell raised at right
show tara at left
with None
#zoom out. Tara smiling, maddie looking shocked

tara front grin raised "Okay! Time for our last one!"

maddie shock "Y-yeah…"
$play_music(halloweensong)
$display = "tarakoma"
$annotation = True
show screen projector([display])
show tara smile shockaway normal:
    yoffset 100 xoffset 100
show maddie attara smile normal:
    yoffset 100 xoffset -100
with fade
maddie "This has definitely happened before."

tara fierce yell closed "You kidding me? This happens, like, once a week."

tara front grin normal "If I gotta sneeze, I'm gonna sneeze in style."
show tara smile
maddie open raised "Do you actually get more subs for dabbing?"

tara direct smirk raised "If we had a sprite of me dabbing, maybe we'd find out."

maddie front grin normal "Also, I will say that AbiGayIRL is a fantastic username."

tara closed smirk furrow "If I ever get to be friends with someone named Abigail, I'm gonna make them get that username on literally every website."

maddie attaralow uneven open "Where are you going to find someone named Abigail who has zero web presence?"
show maddie frown
tara avoid cat worry "I can dream, can't I?"

hide screen projector
show maddie attara normal smile
with dissolve
tara front grin raised "Last but not least, here's a couple pieces of art depicting yours truly in all her glory. You're all so good to me."

tara yell closed fierce "Let's start with a very sufficiently spooky submission from our good friend Adi!"

maddie direct uneven yell "Who?"
show maddie frown
tara direct smirk raised "I don't know, but doesn't the name seem familiar?"

#demon tara on screen
$display = "demon"
$annotation = True
show screen projector([display])
with fade
voice "VA/halloween2018_8a038ca2.ogg"
tara away grin "I'm just gonna say it. I'd hit that."

maddie attaralow worry open "Are you really thirsting over a drawing of yourself?"
voice "VA/halloween2018_0b53e362.ogg"
tara shockaway yell furrow "Look, I know hot when I see it. Demons are hot. I'm hot. Therefore, demon me is hot."

maddie yell raised "I see we're reaching levels of egoism previously thought impossible this evening."

maddie closed open "I'm moving on before you start making this {i}really{/i} weird."

hide screen projector
with dissolve
maddie direct grin normal "This final piece is from Lisa, another friend of ours. You may have seen it before somewhere else, but it was too good not to show here as well."

$display = "chibi"
show screen projector([display])
$ annotation= True
with dissolve
tara shockaway yell raised "CUUUUUTE! I love this!"

tara closed grin "I totally want that shirt. It'd be great for doing an episode on water-based cryptids. Or fishgirls."

maddie attara gape raised "That doesn't seem very on-brand."

tara worry cat avoid "Yeah, but fishgirls are cute. Squidgirls, too. Or jellyfishgirls."

maddie direct frown lower "We get it."

tara shock fierce pout "Y'know what I don't get? When fishgirls have breasts. They don't give birth to live young, right? Why do they need them?"

tara closed worry "I guess what I'm trying to say is...do fishgirls lacta-"

maddie shock yell raised "WOW, WHAT A GREAT PIECE OF ART! LET'S MOVE ON!"

#chibi fades
hide screen projector
hide maddie
hide tara
show maddie front smile at right:
    yalign .5
show tara at left:
    yalign .5
with fade
tara front grin normal "Now then! Onto our next event!"

tara furrow smirk "This one is a little something I like to call \"Trick or...Truth?\"."
show tort at top:
    yoffset 100
show thunder behind maddie:
    alpha 0.1
    linear 0.2 alpha 1.0
    linear 0.05 alpha 0.2
    linear 0.2 alpha 1.0
    pause 0.3
    linear 0.5 alpha 0.0
$play_sfx(scarytopic)
$renpy.pause(2.5)
#the words "Trick or Truth?" appear at the top of the screen
hide tort
hide thunder
tara raised grin closed "Back at the beginning of the month, we asked you wonderful people to send in your very finest photos of supernatural phenomena that you're {i}absolutely{/i} sure are real. I asked my lovely assistant-"

maddie attaralow lower gape "Don't call me that"
show maddie frown
tara front "-to pick out some of the best submissions for me to examine and give my expert opinion on! Remember: when in doubt, it's always best to rely on a real professional."

maddie closed open worry "What are you a professional of, exactly?"

tara closed fierce yell "Roll the first slide!"

#picture in the center of the screen in a frame. Tara and maddie on either side. First picture is the blurry creature in the woods with a circle around it
show mysterious out at truecenter:
    zoom 0.75
show tara
show maddie attara frown normal
tara front pout raised "Oh, this is good. This is very good. I'm loving this. Can we get a zoom on that?"

show mysterious pixels:
    zoom 1.0
with pixellate

tara fierce yell closed "Enhance! Enhance!"

show mysterious enhance
with pixellate

maddie attara grin raised "So what do you think that is, exactly?"
show maddie worry frown
tara front grin "Hell if I know, but it kicks ass. I love her."
show maddie direct
show screen tort("truth")
tara yell fierce shock "TRUTH!"

#truth stamp on the picture
hide screen tort
hide mysterious
show maddie attara normal
tara front grin normal "Next up, we've got…"

#silhouette of forest spirit cg
show shape at top:
    yoffset 50 xalign .5
voice "VA/halloween2018_bd19f279.ogg"
tara away raised pout "Now, see, this is all wrong. This is like the total opposite of that last one."
show tara thin
maddie uneven yell attara "Really? I think it looks a lot more convincing than the last one. Shadows aside, its definition is much clearer."
show maddie frown
tara closed pout worry "Mads, please. Trust the expert."
show maddie normal
voice "VA/halloween2018_76dd220d.ogg"
tara away "If you look closely, you can tell that this is {i}clearly{/i} a drawing. A really good drawing, but definitely a drawing. And there's no room in Taranormal for drawings!"

#maddie looks at the camera
show screen tort("trick")
show maddie direct frown lower
tara yell fierce shock "TRICK!"

#trick sticker
hide screen tort
hide shape
tara front raised grin "Next!"
show light at top:
    yoffset 50 zoom .8
#forest light from glimpse of abby cg
show maddie attaralow normal
tara pout fierce "Now this one is interesting. Minimalist, but in a good way. I feel like there's a lot you could take away from it."

maddie away uneven open "You know, something about this one looks oddly familiar…"
voice "VA/halloween2018_de7233c8.ogg"
tara shockaway worry grin "Have you seen a lot of weird floating lights around lately?"

maddie attara raised frown "No more than usual."

tara shockaway pout raised "Y'know, looking at it, I kinda get what you mean though. Something about it is definitely familiar."

tara closed worry yell "I'm gonna go ahead and give it a \"Trick\" because looking at it makes me feel weird and I'd like to move on."

show screen tort("trick")

tara yell fierce shock "Next!"

hide screen tort
hide light
show hb at top behind maddie:
    yoffset 50
show tara shockaway raised smile
maddie front open raised "According to the email this came with, Marina here was on a trip in the southwest with her girlfriend when the two of them spotted these strange lights above their motel."
show maddie attara frown
tara shock fierce yell "The only light I need to see here is the light of their LOVE. You two are SO CUTE."

tara closed "I know we've never met, but if I don't get to come to your wedding I'm going to be very disappointed."
voice "VA/halloween2018_4dd41a9e.ogg"
tara shockaway raised grin "Also, shout out to the world's largest thermometer behind them. I've been there and I can confirm it's as cool as it looks."

maddie attara uneven yell "When were you in Baker?"

tara closed raised cat "It was during one of my semi-annual Roswell trips. I figured maybe some aliens might have made it to California. You never know."

maddie away lower "Right…"
show maddie frown
tara smirk front normal "Anyway, I'm giving this one a \"Truth\" because those lights are obviously aliens and those two are way too cute for me to doubt them."

#truth sticker
show screen tort("truth")
tara front raised grin "Next!"
hide hb
hide screen tort
show hands at top behind maddie:
    yoffset 50 zoom .8
#silhouette of creature with hands and face pressed against window

maddie shock raised yell "That really gives me the creeps."
show maddie frown worry
tara direct smirk normal "Hey Mads, this looks like you every time you see that cute barista you have a crush on through the coffee shop window."
show tara cat
maddie shockaway raised yell "{b}TARA!{/b}"

tara grin "You're a real sucker for pink hair, huh? If you ever found someone with natural pink hair you'd be set for life."

maddie shock worry "June, if you're watching this, I swear she has no idea what she's talking about."

tara shockaway yell raised "Oh my god, you know her name? That's so cute."
show maddie away frown
tara grin closed fierce "Sounds like we've got our pick for this pic, then!"
show screen tort("maddiestamp")
#stamp appears on the pic that says MADDIE

tara front smirk "Next!"

maddie direct frown lower "I'm in hell."
hide screen tort
hide hands
 #slide disappears

tara smirk raised "So, this one comes with a little personal message from one Ms. \"MFisch.\" Like the city?"
show tara shockaway smile
maddie attara open normal "That's Memphis. I'm pretty sure \"MFisch\" is short for someone's name."
show maddie frown
tara yell closed normal "Let's get that up on screen."
show email at top:
    yoffset 50
#email from morgan appears on screen. I figure tara should read it so vision impaired people can know what's up
show maddie front
tara front grin raised "Hi Tara!! I'm a huge fan of your show and I just finished catching up with every single episode! You're my favorite vlogger and I can't wait to watch more!!! Keep being cute and awesome :)"
show tara smile
maddie raised grin "That's really sweet."
show maddie smile attara
voice "VA/halloween2018_ee30ea83.ogg"
tara closed grin "For sure. The best part about emails like this is that I can really feel the energy coming from her words. You just know someone like this is bursting with energy in real life, too. {size=30}A woman after my own heart…"

tara yell fierce "Thanks, MFisch! You keep being cute and awesome, too!"
show tara direct smirk normal
show maddie raised shockaway frown
extend " Also, DM me."
show maddie smile
show maddie yell shock

maddie "NEXT SLIDE."
hide email
show snowstep at truecenter:
    yoffset -50
#footprints in the snow pic
show maddie attara frown normal
voice "VA/halloween2018_911472b4.ogg"
tara worry shockaway pout "Okay, so, uh...we've got...a bunch of holes in the snow."
show tara front thin
maddie worry grin away "If I'm being honest, I just picked this one because of the fantastic shot composition. Wherever MFisch is from, they must have a great film school."
show maddie smile
tara shock pout raised "Oh shit. I got it."

tara closed fierce yell "They're FOOTPRINTS!"
show tara smile
maddie attara uneven gape "What's so paranormal about a few footprints?"
show maddie frown
voice "VA/halloween2018_d62f3adf.ogg"
tara away fierce smirk "That's just it, Mads! These aren't just any footprints! These are footprints of something strange. Something big… something {b}Taranormal{/b}…"
show tara smile
maddie away normal frown "Oh boy."

tara front yell "Sounds like a yeti to me, folks! Can't go wrong with a good old fashioned yeti. Which means, of course, this one is clearly…"
show screen tort("truth")
tara closed "Truth!"

#truth stamp
hide screen tort
hide snowstep
tara direct cat raised "And hey, MFisch...I'm serious about those DMs."

maddie shock yell raised "Next!"

#pants cg
show maddie smile attara normal
show pants at top behind maddie:
    yoffset 50 zoom .9
tara shockaway pout raised "Oh my god. Oh my god. Oh my god."

tara smirk "Is that…"

maddie attaralow grin "It sure is."
show maddie smile
#tara sprite bouncing

tara shock yell fierce "{b}THE FRESNO NIGHTCRAWLER!{/b}"

tara closed worry "I can't believe it! Real, indisputable photographic evidence!"

tara grin raised "Mads, this is amazing. Thank you."

maddie grin "Happy Halloween, Tara."
voice "VA/halloween2018_ff891edc.ogg"
show maddie smile
tara shockaway worry smile "You're really gonna make me cry on camera, huh?"

maddie closed "Keep it together, Ms. Professional. Let's hear that verdict."

tara closed smile furrow"I don't even have to say it. But you all know that hasn't stopped me yet."
show screen tort("truth")
show tara front grin raised
voice "VA/halloween2018_b6edc8d5.ogg"
maddie front grin raised "TRUTH!" (window_background = "gui/textbox_taramaddie.png",namebox_background="gui/name_taramaddie.png")
hide screen tort
hide pants
#truth stamp
hide tara
hide maddie
show tara front grin raised at left:
    yalign .5
show maddie front smile normal at right:
    yalign .5
with fade
tara "And that's gonna do it for this year's Trick or Truth! But don't worry, we aren't done yet."

tara normal closed yell "Looks like we've got a bit more time before our writer has to get back to doing something actually productive, so let's finish with one more section!"

tara direct smirk raised "One I like to call…"
show monologue movi at top:
    yoffset 15
show thunder behind tara:
    alpha 0.1
    linear 0.2 alpha 1.0
    linear 0.05 alpha 0.2
    linear 0.2 alpha 1.0
    pause 0.3
    linear 0.5 alpha 0.0
$play_sfx(scarytopic)
show maddie attaralow frown normal
tara shock raised yell "\"MADDIE'S MONSTROUS MOVIE MONOLOGUE!\""

#maddie's monstrous movie monologue appears at the top of the screen

tara front grin raised "Given that it's Halloween, Maddie's going to be talking about her favorite horror-"

maddie open "Film."
voice "VA/halloween2018_a5c74274.ogg"
tara shockaway "Huh?"
show monologue film
maddie closed lower yell "Not movie. Film. We already talked about this."
voice "VA/halloween2018_9e91270e.ogg"
tara away furrow smirk "Yeah, but...that messes up the title…"

maddie attaralow gape "You can't just do something with all F words instead?"

tara direct grin normal "I thought you wanted me to stop using so many F words."
show tara cat
maddie away open normal "Forget it."
show tara:
    easein 1 xoffset -800
#words at the top of the screen change so movie is crossed out and film is written in above it
show maddie at center:
    xanchor 0.5 yalign 0.7
with easeinleft
show monologue behind maddie
maddie closed open raised "*ahem*"
show maddie:
    zoom 1.1
#maddie moves to center screen and gets closer to camera
voice "VA/halloween2018_3a08b845.ogg"
maddie attara gape normal "{size=35}When it was first released in 1982, John Carpenter's horror masterpiece {i}The Thing{/i} was torn apart by critics. While criticism was aimed at a number of elements, one consistent point of critique was its relentlessly bleak tone."
show maddie:
    zoom 1.2
hide tara
voice "VA/halloween2018_9fc4d04a.ogg"
maddie closed uneven open "{size=35}All those critics are wrong, of course. {i}The Thing{/i} uses its environment, effects, music, and performances to create a tone that, while dark, is unparalleled in the world of horror in terms of sheer tension."

#for this next one, words go down to the bottom of the screen and beyond
play movie_mono "VA/halloween2018_7c38d106.ogg"
$ renpy.music.set_volume(1.0, channel="movie_mono")
show maddie:
    zoom 1.25
maddie front worry yell "{size=35}Given that {i}The Thing{/i} is technically a remake, Carpenter didn't have a choice when it came to the setting. It would have been easy to simply throw all the characters in a base and say they're cold, but John Carpenter isn't the type to take it easy!"
$ renpy.music.set_volume(0.35, channel="movie_mono")
show tara at center:
    yoffset 1200 zoom 1.5 xoffset 80
    ease 1 yoffset 200
#tara appears in front of maddie while she's still talking, closer to the camera

tara direct smirk "We might wanna call it quits here. She's gonna be like this for a while."

tara closed yell fierce "But thanks for taking the time to stop by! We hope you enjoyed getting this little treat from us. Or trick, depending on whether or not you were expecting us to actually take this seriously."

tara front grin raised "Happy Halloween! We'll see you all again real soon!"
scene black with fade
stop music fadeout 1
""

#fade to black. Silence.

#cardboard abby appears on screen
show abbycutout at center:
    subpixel True
    parallel:
        yoffset -1200
        linear 0.5 yoffset -100
        linear 0.025 yoffset -90
        linear 0.01 yoffset -100
    parallel:
        block:
            ease 2 xoffset 10
            ease 2 xoffset -10
            repeat
stop movie_mono fadeout 5
abby "{b}BOO!{/b}"

"Happy Halloween, everyone!"
return
