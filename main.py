from tkinter import *
from math import *


t = 0
statute = 'start'
vitesse = 8

def deplacement():
    global t, statute,vitesse
    if canvasSchema.coords(lune)[0] <= 296:
        canvasTerre.move(lune2, -canvasTerre.coords(lune2)[0]-800, 0)

    # if 200 >= canvasTerre.coords(lune2)[0] >= 120 and canvasTerre.coords(ombreTerre)[0] < 0:
    #     canvasTerre.move(ombreTerre, 2050, 0)
    #     canvasTerre.move(ombreTerre, 0, 0)
    #
    # if canvasTerre.coords(lune2)[0] >= 700 and canvasTerre.coords(ombreTerre)[0] > 0:
    #     canvasTerre.move(ombreTerre, canvasTerre.coords(ombreTerre)[0]-2000, 0)
    #     canvasTerre.move(ombreTerre, 0, 0)


    if statute == 'start':
        dt = 0.01
        om = pi / vitesse * dt
        r = 170
        dx = r * om * sin(om * t)
        dy = r * om * cos(om * t)
        canvasSchema.move(lune, dx, dy)
        canvasTerre.move(lune2, r*om*10*0.5, 0)
        t += 1
        fenetre.after((int)(1000*dt), deplacement)
    else:
        canvasSchema.move(lune, 0, 0)
        canvasSchema.move(lune2, 0, 0)


def pause():
    global statute
    if statute == 'start':
        statute = 'pause'
    else:
        statute = 'start'
    deplacement()

# def accelerer():
#     global vitesse
#     vitesse -= 1
#
# def freiner():
#     global vitesse
#     vitesse += 1

fenetre = Tk()
fenetre.attributes('-fullscreen', True)

fenetre.config(bg='black')
canvasSchema = Canvas(fenetre, width='960', height='1080', bg='black', highlightthickness=0)
canvasTerre = Canvas(fenetre, width='960', height='1080', bg='black', highlightthickness=0)
canvasTerre.place(x=960,y=0)

canvasSchema.pack(fill='both', expand=1)
soleil = canvasSchema.create_oval(380, 50, 580, 250, outline='yellow', fill='yellow')
terre = canvasSchema.create_oval(430, 800, 530, 900, outline='blue', fill='blue')
lune = canvasSchema.create_oval(295, 835, 325, 865, outline='white', fill='white')
lune2 = canvasTerre.create_oval(-800, 400, -600, 600, outline='white', fill='white')
ombreTerre = canvasTerre.create_oval(400, 350, 600, 550, outline='black', fill='black')

canvasSchema.create_line(960, 0, 960, 1080, fill='white')
canvasSchema.create_line(380, 150, 447, 1080, fill='grey')

canvasSchema.create_line(580, 150, 515, 1080, fill='grey')

canvasSchema.create_text(50, 540, text='Schéma', fill='white', font=10)
canvasTerre.create_text(500, 50, text='Vue de la Terre', fill='white', font=10)
canvasTerre.create_text(500, 1000, text='Cette simulation est à but instructif, les couleurs, les distances et le temps ne sont donc pas à echelle réelle', fill='white', font=10)


bouton_quitter = Button(canvasSchema, text='Quitter', command=fenetre.destroy)
# bouton_accelerer = Button(canvasSchema, text='Accelerer', command=accelerer)
# bouton_freiner = Button(canvasSchema, text='Freiner', command=freiner)
bouton_pause = Button(canvasSchema, text='Pause', command=pause)

# bouton_accelerer.pack()
# bouton_freiner.pack()
bouton_quitter.place(x=10, y=35)
bouton_pause.place(x=10, y=0)

deplacement()
fenetre.mainloop()

