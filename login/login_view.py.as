import tkinter as tk

window = tk.Tk()
window.title("Taxi Booking App")
window.geometry("420x300")

hello = tk.Label(text="Welcome to the Taxi Booking App !")
hello.pack(expand=True)

button = tk.Button(text="Click me!", fg= "Black", bg= "Green", font= ("Arial", 16) )
button.pack()

btn2 = tk.Button(text="Cancel", fg= "Black", bg= "red", font= ("Arial", 16))
btn2.pack()

tk.mainloop()