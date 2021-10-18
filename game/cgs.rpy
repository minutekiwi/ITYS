##Characters and their images
image emoji1 = SnowBlossom("rainbow.png", count=18, xspeed=(300,600), yspeed=(0), start=-5, horizontal=True)
image emoji2 = SnowBlossom("love.png", count=18, xspeed=(300,600), yspeed=(0), start=-5, horizontal=True)
image emoji3 = SnowBlossom("cry.png", count=18, xspeed=(300,600), yspeed=(0), start=-45, horizontal=True)

transform flip:
    xzoom -1
transform unflip:
    xzoom 1
