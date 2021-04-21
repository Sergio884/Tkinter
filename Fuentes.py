import tkinter as tk
from tkinter import *
from tkinter import font

ventana = Tk()

ventana.geometry("1355x755+0+0")
ventana.resizable(width=False, height=False)

lbFuente = Label(ventana, text="Harlow Solid Italic : Así se ve esta fuente aeiou AEIOU ñ?¿!",
                     font=("Harlow Solid Italic", 30)).place(x=0, y=0)
lbFuente = Label(ventana, text="Goudy Old Style : Así se ve esta fuente aeiou AEIOU ñ?¿!",
                     font=("Goudy Old Style", 30)).place(x=0, y=55)
lbFuente = Label(ventana, text="DejaVu Serif : Así se ve esta fuente aeiou AEIOU ñ?¿!",
                         font=("DejaVu Serif", 30)).place(x=0, y=110)
lbFuente = Label(ventana, text="AR DELANEY : Así se ve esta fuente aeiou AEIOU ñ?¿!",
                     font=("AR DELANEY", 30)).place(x=0, y=165)
lbFuente = Label(ventana, text="AR CARTER : Así se ve esta fuente aeiou AEIOU ñ?¿!",
                     font=("AR CARTER", 30)).place(x=0, y=220)

lbFuente = Label(ventana, text="AR DARLING : Así se ve esta fuente aeiou AEIOU ñ?¿!",
                     font=("AR DARLING", 30)).place(x=0, y=275)
lbFuente = Label(ventana, text="Freestyle Script : Así se ve esta fuente aeiou AEIOU ñ?¿!",
                     font=("Freestyle Script", 30)).place(x=0, y=330)
lbFuente = Label(ventana, text="Papyrus : Así se ve esta fuente aeiou AEIOU ñ?¿!",
                     font=("Papyrus", 30)).place(x=0, y=385)
lbFuente = Label(ventana, text="Matura MT Script Capitals : Así se ve esta fuente aeiou AEIOU ñ?¿!",
                     font=("Matura MT Script Capitals", 25)).place(x=0, y=445)
lbFuente = Label(ventana, text="Parchment : Así se ve esta fuente aeiou AEIOU ñ?¿!",
                     font=("Parchment", 60)).place(x=0, y=500)
lbFuente = Label(ventana, text="Script MT Bold : Así se ve esta fuente aeiou AEIOU ñ?¿!",
                     font=("Script MT Bold", 30)).place(x=0, y=585)
lbFuente = Label(ventana, text="Segoe Print : Así se ve esta fuente aeiou AEIOU ñ?¿!",
                     font=("Segoe Print", 30)).place(x=0, y=640)
ventana.mainloop()

root = tk.Tk()
#for font in font.families():
 #   if "pyru" in font:
  #      print(font)
