#import tkinter as tk

import customtkinter as ctk
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

#ctk.set_default_color_theme("./themes/yellow.json")

ctk.set_appearance_mode("System")  # Modes: system (default), light, dark
ctk.set_default_color_theme(
    "./themes/yellow.json")  # Themes: blue (default), dark-blue, green

def btn1_clicked():
  print("btn1 clicked")

#main window
window = ctk.CTk()
window.title("Taxi Booking App")
window.eval("tk::PlaceWindow . center")
window.geometry("500x350")

frame = ctk.CTkFrame(master=window)
frame.pack(pady=20, padx=20, fill="both", expand=True)

hello = ctk.CTkLabel(master=frame, text="""Welcome to the Taxi Booking App!
Please Login to Continue""")
#hello.pack(expand=True)
hello.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

#Username and Password Entry
user_id_entry = ctk.CTkEntry(master=frame, placeholder_text="Username", width=200, height = 30, border_width=2, corner_radius=10)
user_id_entry.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

password_entry = ctk.CTkEntry(master=frame, placeholder_text="Password", width=200, height = 30, border_width=2, corner_radius=10, show="*")
password_entry.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

#Buttons
btn1 = ctk.CTkButton(master=frame, text="Login", font=("Arial", 16), command=btn1_clicked)
#btn1.pack(pady=10, padx=10)
btn1.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

btn2 = ctk.CTkButton(master=frame, text="Register", font=("Arial", 16))
#btn2.pack(pady=10 , padx=10)
btn2.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

btn3 = ctk.CTkButton(master=frame, text="Exit", font=("Arial", 16))
#btn3.pack(pady=10 , padx=10)
btn3.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

btn4 = ctk.CTkButton(master=frame, text="Driver Login", font=("Arial", 16))
#btn4.pack(pady=10 , padx=10, anchor=ctk.SE)
btn4.place(relx=0.1, rely=0.8, anchor=tk.SW)


btn5 = ctk.CTkButton(master=frame, text="Admin Login", font=("Arial", 16))
#btn5.pack(pady=10 , padx=10, anchor=ctk.SW)
btn5.place(relx=0.8, rely=0.8, anchor=ctk.SE)

window.mainloop()
