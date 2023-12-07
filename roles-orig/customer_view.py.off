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


        self.button = tk.Button(self._frame, 
                                text="Book Taxi", 
                                command=self._frame._on_click_book_taxi)
        self.button.grid(row=1, column=1)

        # Logout button
        self.btn_login = tk.Button(self._frame,
                                   text="Logout",
                                   command=self._frame.logout)
        self.btn_login.grid(row=4, column=1)


    def make_booking(self):
        '''Users will enter the Pick-Up Address, Drop-Off Address, 
        Date, time, and payment method.
        '''
    
    def view_booking(self):
        '''Users will be able to see their Pick-Up Address, 
        Drop-Off Address, and time for their trip.
        '''
    
    def edit_booking(self):
        '''The client should be able to edit the information 
        entered when booking a trip.
        '''
    
    def cancel_booking(self):
        '''After a trip is booked clients can cancel their trip.
        '''
    
    def view_booking_history(self):
        '''This list shows all previous trips booked, their pick-up 
        and drop-off locations, dates, and prices.
        '''
    
    def select_payment_method(self):
        '''Once locations for the trip are selected a price will be given 
        and the user will get different payment options.
        '''
    
    def make_payment(self):
        '''Payments can be made by entering card information.
        '''
    
    def cancel_payment(self):
        '''Cancellation of payment can be done
        '''
    
    def view_driver_information(self):
        '''This will be a display of the Driver’s name and License Plate 
        for easy identification on the driver’s arrival.
        '''