from tkinter import *
import random

# -------------------
# variables globales
# -------------------
BASE = 660
ALTURA = 330


def mover_carros():
    pass

# -------------------
# ventana principal
# -------------------
ventana_principal = Tk()
ventana_principal.title("UIS Cars")
ventana_principal.resizable(False, False)
ventana_principal.geometry("700x500")
ventana_principal.config(bg="white")

# -------------------
# frame de graficacion
# -------------------
frame_graficacion = Frame(ventana_principal)
frame_graficacion.config(bg="green", width=680, height=350)
frame_graficacion.place(x=10,y=10)

# creacion canvas
c = Canvas(frame_graficacion, width=BASE, height=ALTURA)
c.config(bg="black")
c.place(x=10,y=10)


# -------------------
# frame de controles
# -------------------
frame_controles = Frame(ventana_principal)
frame_controles.config(bg="green", width=680, height=120)
frame_controles.place(x=10,y=370)

# desplegar ventana
ventana_principal.mainloop()