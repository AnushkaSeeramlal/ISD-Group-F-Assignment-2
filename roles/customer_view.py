import tkinter as tk

import Bookings


class CustomerView:

    def __init__(self, frame=None):
        self._frame = frame
        self.create_widgets()

    def create_widgets(self):
        self._frame._clear_widgets()
        self.label = tk.Label(
            self._frame,
            text=
            f"Welcome to Taxi Booking App - Customer {self._frame._user['username']}"
        )
        self.label.grid(row=0, column=1)

        # Payment button
        self.btn_login = tk.Button(self._frame,
                                   text="Make payment",
                                   command=self.make_payment)
        self.btn_login.grid(row=2, column=1)

        # Logout button
        self.btn_login = tk.Button(self._frame,
                                   text="Logout",
                                   command=self._frame.logout)
        self.btn_login.grid(row=4, column=1)

    def make_payment(self):
        self._frame._clear_widgets()
        self.label = tk.Label(
            self._frame,
            text=f"Make a payment - Customer {self._frame._user['username']}")
        self.label.grid(row=0, column=1)

        # Logout button
        self.btn_login = tk.Button(self._frame,
                                   text="Logout",
                                   command=self._frame.logout)
        self.btn_login.grid(row=4, column=1)
