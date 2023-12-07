
import tkinter as tk

class DriverView:
    def __init__(self, frame=None):
        self._frame = frame
        self.create_widgets()

    def create_widgets(self):
        self._frame._clear_widgets()
        self.label = tk.Label(self._frame, text="Welcome to Taxi Booking App - Driver")
        self.label.grid(row=0, column=1)

        

        # Logout button
        self.btn_login = tk.Button(self._frame,
                                   text="Logout",
                                   command=self._frame.logout)
        self.btn_login.grid(row=4, column=1)


    def view_assigned_bookings(self):
        '''A list of bookings a driver has been approved for, their locations, 
        times, and customer names will be displayed.
        '''
    
    def view_booking_history(self):
        '''Drivers can access their trip history with locations, dates, 
        and customer names included.
        '''
    
    def confirm_booking(self):
        '''Upon approval by admins, drivers will get notified of trips 
        they were chosen for and can choose whether to accept.
        '''
    
    def cancel_booking(self):
        '''Drivers can also deny trips they were chosen for.
        '''
    
    def availability_status(self):
        '''Drivers will state whether they are Available, Unavailable, or On trip.
        '''
    
