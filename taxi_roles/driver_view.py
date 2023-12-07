import tkinter as tk

class DriverView:
    def __init__(self, frame=None):
        self._frame = frame
        self.create_widgets()

    def create_widgets(self):
        self._frame._clear_widgets()
        self.label = tk.Label(
            self._frame, 
            text=f"Welcome to Taxi Booking App - Driver {self._frame._user['username']}"
        )
        self.label.grid(row=0, column=1)

        # View Assigned Bookings button
        self.btn_view_assigned_bookings = tk.Button(self._frame,
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
        self.btn_availability_status = tk.Button(self._frame,
                                                text="Update Availability Status",
                                                command=self.update_availability_status)
        self.btn_availability_status.grid(row=5, column=1)

        # Logout button
        self.btn_logout = tk.Button(self._frame,
                                    text="Logout",
                                    command=self._frame.logout)
        self.btn_logout.grid(row=6, column=1)

    def view_assigned_bookings(self):
        # Example: Display assigned bookings in the same frame
        assigned_bookings = [{"booking_id": 1, "pickup": "Location A", "dropoff": "Location B", "customer_name": "John Doe"},
                             {"booking_id": 2, "pickup": "Location C", "dropoff": "Location D", "customer_name": "Jane Smith"}]
        self.display_list_in_frame("Assigned Bookings", assigned_bookings)

    def view_booking_history(self):
        # Example: Display booking history in the same frame
        booking_history = [{"booking_id": 1, "pickup": "Location A", "dropoff": "Location B", "date": "2023-01-01"},
                           {"booking_id": 2, "pickup": "Location C", "dropoff": "Location D", "date": "2023-02-01"}]
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

        dropdown = tk.OptionMenu(self._frame, availability_status, "Available", "Unavailable", "On trip")
        dropdown.grid(row=7, column=1)

        update_button = tk.Button(self._frame, text="Update Status", command=lambda: self.display_message_in_frame(f"Status Updated: {availability_status.get()}"))
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
        back_button = tk.Button(self._frame, text="Back", command=self.create_widgets)
        back_button.grid(row=2, column=1)

    def display_message_in_frame(self, message):
        # Clear existing widgets in the frame
        self._frame._clear_widgets()

        # Display a message in the same frame
        message_label = tk.Label(self._frame, text=message)
        message_label.grid(row=1, column=1)

        # Back button to return to the main view
        back_button = tk.Button(self._frame, text="Back", command=self.create_widgets)
        back_button.grid(row=2, column=1)

    @staticmethod
    def format_listbox_item(item):
        return f"Booking ID: {item['booking_id']}, Pick-Up: {item['pickup']}, Drop-Off: {item['dropoff']}, Customer: {item['customer_name']}"

# Example usage:
# driver_view = DriverView()  # Assuming the frame is initialized appropriately
# driver_view.view_assigned_bookings()  # or driver_view.view_booking_history(), etc.
