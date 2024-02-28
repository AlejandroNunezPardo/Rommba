import tkinter as tk
from tkinter import Frame
import alimpiar
import lista
import script
import tupla

window = tk.Tk()
window.title("Actividad Roomba")
window.geometry("500x300")

hello = tk.Label(text="Welcome to the Seven Heaven")
hello.pack()
button = tk.Button(text="Pusla")
button.pack()

tk.mainloop()