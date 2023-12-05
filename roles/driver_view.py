
import tkinter as tk

class DriverView:
    def __init__(self, frame=None):
        self._frame = frame
        self.create_widgets()

    def create_widgets(self):
        self._frame._clear_widgets()
        self.label = tk.Label(self._frame, text="Welcome to Taxi Booking App - Driver")
        self.label.grid(row=0, column=1)

        self.button = tk.Button(self._frame, text="Book Taxi", command=self._frame._on_click_book_taxi)
        self.button.grid(row=1, column=1)