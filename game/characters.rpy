

image the_ctc:
    "gui/ctc.png"
    ctc_transform
    block:
        alpha 0.0
        .25
        easeout_circ .25 alpha 1.0
        1
        easeout_circ .25 alpha 0.0
        .5
        repeat
transform ctc_transform:
    pos(1395,960)
screen ctc(arg="last"):
    add "the_ctc" at ctc_transform
screen ctc(arg="last"):
    variant "small"
    add "the_ctc":
        pos(1495,960)



define tara = Character("Tara", image="tara", voice_tag="tara",callback = tara_beep,namebox_background = "gui/name_tara.png", window_background=Frame("gui/textbox_tara.png",10,10))
define maddie = Character("Maddie", image="maddie",voice_tag="maddie",callback= maddie_beep, namebox_background = "gui/name_maddie.png", window_background=Frame("gui/textbox_maddie.png",10,10))
define abby = Character("Abigail", image="abby",voice_tag="abby",callback = abby_beep, namebox_background = "gui/name_abigail.png", window_background=Frame("gui/textbox_abby.png",10,10))
define morgan = Character("Morgan", image="morgan",voice_tag="morgan", callback=morgan_beep,namebox_background = "gui/name_morgan.png", window_background=Frame("gui/textbox_morgan.png",10,10))
define taramorgan = Character("Tara & Morgan", image="taramorgan",voice_tag="taramorgan", callback=taramorgan_beep,namebox_background="gui/name_taramorgan.png", window_background=Frame("gui/textbox_taramorgan.png",10,10))

image ityslogo = "gui/logo small.png"
image white = Solid("#fff")
image bg roomblur = im.Blur("images/bg room.png", 1.5)

image loveyhearts:
    "hearts"
    1
    "hearts1"
    1
    repeat
image loveyheartsrev:
    "hearts1"
    1
    "hearts"
    1
    repeat

layeredimage tara:
    group base auto:
        attribute fistup default
    group eyes auto:
        attribute default default
        attribute front:
            "tara_eyes_default"
        attribute direct:
            "tara_eyes_sly"
        attribute avoid:
            "tara_eyes_sly"
    group mouth auto:
        attribute smile default
        attribute thin:
            "tara_mouth_dot"
    group brows auto:
        attribute neutral default
        attribute angled:
            "tara_brows_fierce"
    group extra auto
    xanchor .5

layeredimage morgan:
    group base auto:
        attribute standing default
    group eyes auto:
        attribute default default
    group mouth auto:
        attribute smile default
    group brows auto:
        attribute neutral default
    group extra auto
    xanchor .5

layeredimage maddie:
    group base:
        attribute standing default
        attribute guard:
            "maddie_base_guard"
    group extra auto multiple:
        attribute heart:
            "loveyhearts"
    group eyes auto:
        attribute default default
        attribute gentle:
            "maddie_eyes_narrow"
        attribute attara:
            "maddie_eyes_away"
        attribute front:
            "maddie_eyes_default"
        attribute attaralow:
            "maddie_eyes_away"
        attribute direct:
            "maddie_eyes_sly"
    group mouth auto:
        attribute smile default
        attribute grin:
            "maddie_mouth_laugh"
        attribute gape:
            "maddie_mouth_sigh"
    group brows auto:
        attribute neutral default
        attribute normal:
            "maddie_brows_neutral"
        attribute lower:
            "maddie_brows_worry"
    xanchor .5

layeredimage abby:
    group base:
        attribute standing default
        attribute oho:
            "abby_base_oho"
    group extra auto multiple:
        attribute heart:
            "loveyheartsrev"
    group eyes auto:
        attribute default default
    group mouth auto:
        attribute smile default
    group brows auto:
        attribute neutral default
    xanchor .5

image abby_window = "gui/textbox_abby.png"
image maddie_annoy_os = AlphaMask("maddie away uneven sigh", "offscreen_mad",xalign=.5)
image maddie_annoy2_os = AlphaMask("maddie away uneven small", "offscreen_mad",xalign=.5)
image maddie_agree_os = AlphaMask("maddie closed worry laugh", "offscreen_mad",xalign=.5)
image maddie_sigh_os = AlphaMask("maddie closed worry sigh", "offscreen_mad",xalign=.5)
image maddie_asking_os = AlphaMask("maddie away open", "offscreen_mad",xalign=.5)
image maddie_nervous_os = AlphaMask("maddie narrow worry sigh", "offscreen_mad",xalign=.5)
image maddie_happy_os = AlphaMask("maddie closed neutral laugh", "offscreen_mad",xalign=.5)
image maddie_fear_os = AlphaMask("maddie shock raised yell", "offscreen_mad",xalign=.5)
image maddie_lovey_os = AlphaMask("maddie narrow neutral laugh blush", "offscreen_mad",xalign=.5)
image maddie_films1_os = AlphaMask("maddie narrow angry yell", "offscreen_mad",xalign=.5)
image maddie_films2_os = AlphaMask("maddie closed uneven sigh", "offscreen_mad",xalign=.5)
image abby_lovey_os = AlphaMask("abby blush narrow open", "offscreen_abby",xalign=.5,xzoom=-1)
image abby_loveyu_os = AlphaMask("abby oho blush uclosed open", "offscreen_abby",xalign=.5,xzoom=-1)
image abby_laugh_os = AlphaMask("abby oho uclosed laugh", "offscreen_abby",xalign=.5,xzoom=-1)
image abby_excited_os = AlphaMask("abby raised default laugh", "offscreen_abby",xalign=.5,xzoom=-1)
image abby_gasp_os = AlphaMask("abby oho horror yell raised", "offscreen_abby",xalign=.5,xzoom=-1)
image abby_unsure_os = AlphaMask("abby worry sigh", "offscreen_abby",xalign=.5,xzoom=-1)
