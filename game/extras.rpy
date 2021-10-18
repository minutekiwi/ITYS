init:
    $ style.hyperlink_text.color = gui.accent_color # inherits from the default dialog look, so it'll look like the rest of the dialogue, and we'll just have to change the look of the link hovered
    #$ style.hyperlink_text.idle_color=gui.accent_color
init python:
    def MaxScale(img, minwidth=config.screen_width, minheight=config.screen_height):
     currwidth, currheight = renpy.image_size(img)
     xscale = float(minwidth) / currwidth
     yscale = float(minheight) / currheight

     if xscale > yscale:
        maxscale = xscale
     else:
        maxscale = yscale

     return im.FactorScale(img, maxscale, maxscale)

    def MinScale(img, maxwidth=config.screen_width, maxheight=config.screen_height):
     currwidth, currheight = renpy.image_size(img)
     xscale = float(maxwidth) / currwidth
     yscale = float(maxheight) / currheight

     if xscale < yscale:
         minscale = xscale
     else:
         minscale = yscale

     return im.FactorScale(img, minscale, minscale)

    maxnumx = 4
    maxnumy = 1
    maxthumbx = config.screen_width / (maxnumx + 1)
    maxthumby = config.screen_height / (maxnumy + 1)
    maxperpage = maxnumx * maxnumy
    gallery_page = 0
    closeup_page = 0

    class MusicItem:
     def __init__(self, name, file, length, composer):
         self.name = name
         self.file = file
         self.length = length
         self.composer = composer
         self.refresh_audio()

     def refresh_audio(self):
         if not renpy.seen_audio(self.file):
             self.is_locked = True
         else:
             self.is_locked = False

    class GalleryItem:
     def __init__(self, images, thumb, cgnumber, cgtitle, always_unlocked=True, locked="lockedthumb"):
         self.images = images
         self.thumb = thumb
         self.cgnumber = cgnumber
         self.cgtitle = cgtitle
         self.locked = locked
         self.always_unlocked = always_unlocked
         self.refresh_lock()

     def num_images(self):
         return len(self.images)

     def refresh_lock(self):
         self.num_unlocked = 0
         lockme = False
         for img in self.images:

             if not renpy.seen_image(img):
                 if self.always_unlocked:
                     lockme = False
                 else:
                     lockme = True
             else:
                 self.num_unlocked += 1
         self.is_locked = lockme


    gallery_items = []
    gallery_items.append(GalleryItem(["pumpkinkoma","tarakoma","maddiekoma"], "pumpkinkoma thumb", "4Komas", "by {a=https://twitter.com/pentagonfruit}Kiri{/a}"))
    #gallery_items.append(GalleryItem(["tarakoma"], "tarakoma thumb", "CG #1", "Train to Another World"))
    gallery_items.append(GalleryItem(["gothmaddiegallery"], "gothmaddie thumb", "Goth Maddie", "by {a=https://twitter.com/minutekiwi}minute{/a}"))
    gallery_items.append(GalleryItem(["demon"], "demon thumb", "Demon Tara", "by {a=https://twitter.com/adirosette}Adirosa{/a}"))
    gallery_items.append(GalleryItem(["chibi"], "chibi thumb", "Water Cryptid Tara", "by {a=https://twitter.com/llullabye}Lisa{/a}"))
    chibitheme = "<loop 7.578 to 98.585>ost/A widdle song of people plumb.ogg" #
    taratheme = "<loop 9.600 to 182.465>ost/Episode One.ogg" #Less or no fade-in
    taraspoopy = "<loop 9.600 to 182.465>ost/Episode One (Ultra rare spoopy mix).ogg" #Less or no fade-in
    halloweensong = "<loop 9.6>ost/halloweensong.ogg"

    scarytopic = "<from 1 to 4.35>ost/sfx/Train Brakes.ogg"

    music_items = []
    music_items.append(MusicItem("Episode One", taratheme, "2:58", "Kris \"Astartus\" Flacke"))
    music_items.append(MusicItem("Episode One (Ultra rare spoopy mix)", taraspoopy, "2:58", "Kris \"Astartus\" Flacke"))
    music_items.append(MusicItem("Chibi Theme", chibitheme, "1:39", "Kris \"Astartus\" Flacke"))
    music_items.append(MusicItem("Stay Spooky Everyone!", halloweensong, "2:36", "Kris \"Astartus\" Flacke"))


    sfx_displaylist = {
        scarytopic : "(Spooky noise)"
    }
default persistent.audio_cues = True

init python:
    renpy.music.register_channel("ambient", "sfx", True)
    def play_sfx(soundfx,fade=1):
            renpy.sound.play(soundfx,fadein=fade,fadeout=fade)
            if persistent.audio_cues:
                renpy.notify("SFX: {i}" + sfx_displaylist[renpy.sound.get_playing('sound')] + "{/i}")
    def play_music(song,fade=5):
        if song in [taratheme,taraspoopy]:
            renpy.music.play(song,fadein=3)
        else:
            renpy.music.play(song, fadein=fade)
        if persistent.audio_cues:
            for i in music_items:
                if i.file == renpy.music.get_playing('music'):
                    renpy.notify("Now playing: " + i.name)
    def play_amb(ambience):
        renpy.music.play(ambience,channel='ambient',fadein=10)
        if persistent.audio_cues:
            renpy.notify("Ambience: {i}" + sfx_displaylist[renpy.music.get_playing('ambient')] + "{/i}")
