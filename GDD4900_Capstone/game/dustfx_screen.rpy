# define screen to overlay gameplay with dust particle effect
screen dustFX:
    add Snow(im.Scale("gui/smoke3.png", 10, 10), max_particles=400, speed=15, wind=0, gravity=10,\
                  xborder=(0, 1920), yborder=(0, 1080), start=400)