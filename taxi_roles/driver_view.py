import tkinter as tk


class DriverView:

    def __init__(self, frame=None):
        self._frame = frame
        self.create_widgets()

    def create_widgets(self):
        self._frame._clear_widgets()
        self.label = tk.Label(
            self._frame,
            text=
            f"Welcome to Taxi Booking App - Driver {self._frame._user['username']}"
        )
        self.label.grid(row=0, column=1)

        # View Assigned Bookings button
        self.btn_view_assigned_bookings = tk.Button(
            self._frame,
            text="View Assigned Bookings",
            command=self.view_assigned_bookings)
        self.btn_view_assigned_bookings.grid(row=1, column=1)

        # View Booking History button
        self.btn_view_history = tk.Button(self._frame,
                                          text="View Booking History",
                                          command=self.view_booking_history)
        self.btn_view_history.grid(row=2, column=1)

        # Confirm Booking button
        self.btn_confirm_booking = tk.Button(self._frame,
                                             text="Confirm Booking",
                                             command=self.confirm_booking)
        self.btn_confirm_booking.grid(row=3, column=1)

        # Cancel Booking button
        self.btn_cancel_booking = tk.Button(self._frame,
                                            text="Cancel Booking",
                                            command=self.cancel_booking)
        self.btn_cancel_booking.grid(row=4, column=1)

        # Availability Status button
        self.btn_availability_status = tk.Button(
            self._frame,
            text="Update Availability Status",
            command=self.update_availability_status)
        self.btn_availability_status.grid(row=5, column=1)

        # Logout button
        self.btn_logout = tk.Button(self._frame,
                                    text="Logout",
                                    command=self._frame.logout)
        self.btn_logout.grid(row=6, column=1)

    def view_assigned_bookings(self):
        # Access assigned bookings from the database

        self._frame._clear_widgets()
        self.label = tk.Label(
            self._frame,
            text=f"Assigned Trips - Driver {self._frame._user['username']}")
        self.label.grid(row=0, column=1)

        # Status messages
        self.text_var = tk.StringVar()
        self.status_text = tk.Label(self._frame,
                                    textvariable=self.text_var,
                                    width=50)
        self.status_text.grid(row=1, column=1)

        my_trips = filter(
            lambda x: x['driverid'] == self._frame._user['userid'],
            self._frame.db.trip_retrieve(tripstatus='driver_selected') + \
            self._frame.db.trip_retrieve(tripstatus='en_route') + \
            self._frame.db.trip_retrieve(tripstatus='started'),
        )
        self._booking_var = tk.IntVar(self._frame, -1)
        grid_location_trip = 5
        for curr_booking in my_trips:
            curr_booking_customer = self._frame.db.user_retrieve(
                userid=curr_booking['customerid'])
            curr_radio_button_1 = tk.Radiobutton(
                self._frame,
                text=
                f"{curr_booking_customer[0]['name']} from {curr_booking['pickupaddress']} to {curr_booking['destinationaddress']} - {curr_booking['tripstatus']}",
                variable=self._booking_var,
                value=curr_booking['tripid'],
                # command=group_1_select,
            )
            curr_radio_button_1.grid(row=grid_location_trip, column=1)
            grid_location_trip += 1

        # Back button to return to the main view
        back_button = tk.Button(self._frame,
                                text="Accept Trip",
                                command=self.accept_trip)
        back_button.grid(row=grid_location_trip + 1, column=1)

        # Back button to return to the main view
        back_button = tk.Button(self._frame,
                                text="Picked up Customer",
                                command=self.arrived_to_customer)
        back_button.grid(row=grid_location_trip + 2, column=1)

        # Back button to return to the main view
        back_button = tk.Button(self._frame,
                                text="Accept Payment",
                                command=self.accept_payment)
        back_button.grid(row=grid_location_trip + 3, column=1)

        # Back button to return to the main view
        back_button = tk.Button(self._frame,
                                text="Complete Trip",
                                command=self.complete_trip)
        back_button.grid(row=grid_location_trip + 4, column=1)

        # Back button to return to the main view
        back_button = tk.Button(self._frame,
                                text="Back",
                                command=self.create_widgets)
        back_button.grid(row=grid_location_trip + 5, column=1)

    def accept_trip(self):
        '''Accept a trip.
        '''
        trip_id = self._booking_var.get()
        trip_obj = self._frame.db.trip_retrieve(tripid=trip_id)[0]
        if trip_obj['tripstatus'] != 'pending':
            self.text_var.set("That trip is not pending for you to accept")
        self._frame.db.trip_update(tripid=trip_id, tripstatus='en_route')
        self.view_assigned_bookings()

    def arrived_to_customer(self):
        '''Arrived to customer pickup location.
        '''
        trip_id = self._booking_var.get()
        trip_obj = self._frame.db.trip_retrieve(tripid=trip_id)[0]
        if trip_obj['tripstatus'] != 'en_route':
            self.text_var.set("That trip is not one you have accepted yet")
        self._frame.db.trip_update(tripid=trip_id, tripstatus='started')
        self.view_assigned_bookings()

    def accept_payment(self):
        '''Accept Payment.
        '''
        self.text_var.set("Accept payment not implemented yet")

    def complete_trip(self):
        '''Arrived to customer pickup location.
        '''
        trip_id = self._booking_var.get()
        trip_obj = self._frame.db.trip_retrieve(tripid=trip_id)[0]
        if trip_obj['tripstatus'] != 'payment_completed':
            self.text_var.set("That trip has not been paid yet")
        self._frame.db.trip_update(tripid=trip_id, tripstatus='completed')
        self.view_assigned_bookings()

    def view_booking_history(self):
        # Access booking history from the database
        booking_history = self._frame.db.trip_retrieve(tripstatus='completed')
        self.display_list_in_frame("Booking History", booking_history)

    def confirm_booking(self):
        # Example: Display a confirmation message in the same frame
        self.display_message_in_frame("Booking Confirmed!")

    def cancel_booking(self):
        # Example: Display a cancellation message in the same frame
        self.display_message_in_frame("Booking Canceled!")

    def update_availability_status(self):
        # Example: Display an input form to update availability status in the same frame
        availability_status = tk.StringVar()
        availability_status.set("Available")  # Default value

        label = tk.Label(self._frame, text="Select Availability Status:")
        label.grid(row=7, column=0)

        dropdown = tk.OptionMenu(self._frame, availability_status, "Available",
                                 "Unavailable", "On trip")
        dropdown.grid(row=7, column=1)

        update_button = tk.Button(
            self._frame,
            text="Update Status",
            command=lambda: self.display_message_in_frame(
                f"Status Updated: {availability_status.get()}"))
        update_button.grid(row=7, column=2)

    def display_list_in_frame(self, title, data):
        # Clear existing widgets in the frame
        self._frame._clear_widgets()

        # Display list in the same frame
        listbox = tk.Listbox(self._frame)
        for item in data:
            listbox.insert(tk.END, self.format_listbox_item(item))

        listbox.grid(row=1, column=1)

        # Back button to return to the main view
        back_button = tk.Button(self._frame,
                                text="Back",
                                command=self.create_widgets)
        back_button.grid(row=2, column=1)

    def display_message_in_frame(self, message):
        # Clear existing widgets in the frame
        self._frame._clear_widgets()

        # Display a message in the same frame
        message_label = tk.Label(self._frame, text=message)
        message_label.grid(row=1, column=1)

        # Back button to return to the main view
        back_button = tk.Button(self._frame,
                                text="Back",
                                command=self.create_widgets)
        back_button.grid(row=2, column=1)

    @staticmethod
    def format_listbox_item(item):
        return f"Booking ID: {item['booking_id']}, Pick-Up: {item['pickup']}, Drop-Off: {item['dropoff']}, Customer: {item['customer_name']}"


# Example usage:
# driver_view = DriverView()  # Assuming the frame is initialized appropriately
# driver_view.view_assigned_bookings()  # or driver_view.view_booking_history(), etc.
