#import tkinter as tk

import customtkinter as ctk

#ctk.set_default_color_theme("./themes/yellow.json")

ctk.set_appearance_mode("System")  # Modes: system (default), light, dark
ctk.set_default_color_theme("./themes/yellow.json")  # Themes: blue (default), dark-blue, green

window = ctk.CTk()
window.title("Taxi Booking App")
window.geometry("500x350")

frame = ctk.CTkFrame(master=window)
frame.pack(pady=20, padx=60, fill="both", expand=True)

hello = ctk.CTkLabel(master=frame, text="Welcome to the Taxi Booking App!")
hello.pack(expand=True)

button = ctk.CTkButton(master=frame, text="Click me!", font= ("Arial", 16))
button.pack()

btn2 = ctk.CTkButton(master=frame, text="Cancel", font= ("Arial", 16))
btn2.pack()

window.mainloop()