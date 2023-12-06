import tkinter as tk

class AdminView:
    def __init__(self, frame=None):
        # Main frame
        self._frame = frame
        self.create_widgets()

    def create_widgets(self):
        self._frame._clear_widgets()
        self.label = tk.Label(self._frame, text="Welcome to Taxi Booking App - Admin role")
        self.label.grid(row=0, column=1)

        # Logout button
        self.btn_login = tk.Button(self._frame,
                                   text="Logout",
                                   command=self._frame.logout)
        self.btn_login.grid(row=4, column=1)

    def view_requested_bookings(self):
        '''All booking requests will be shown in a list.
        '''

    def assign_driver_to_booking(self):
        '''Driver will be assigned to a booking request.
        '''


    def confirm_booking(self):
        """Admins will be able to deny requests for bookings also.
        """

    def cancel_booking(self):
        '''Booking request will be cancelled.
        '''

    def manage_current_drivers(self):
        """A list of current drivers, their information, 
        and their status will be available for viewing.
        """

    def manage_current_customers(self):
        """A list of current users, their information, 
        and trips made can be seen from another list.
        """
