import tkinter as tk


class AdminView:

    def __init__(self, frame=None):
        self._frame = frame
        self.display_admin_index()

    def display_admin_index(self):
        self._frame._clear_widgets()
        self.label = tk.Label(self._frame,
                              text="Welcome to Taxi Booking App - Admin role")
        self.label.grid(row=0, column=1)

        # View Requested Bookings button
        self.btn_view_requested_bookings = tk.Button(
            self._frame,
            text="View Requested Bookings",
            command=self.view_requested_bookings_window)
        self.btn_view_requested_bookings.grid(row=1, column=1)

        # Assign Driver to Booking button
        self.btn_assign_driver = tk.Button(
            self._frame,
            text="Assign Driver to Booking",
            command=self.assign_driver_to_booking_window)
        self.btn_assign_driver.grid(row=2, column=1)

        # Confirm Booking button
        self.btn_confirm_booking = tk.Button(
            self._frame,
            text="Confirm Booking",
            command=self.confirm_booking_window)
        self.btn_confirm_booking.grid(row=3, column=1)

        # Cancel Booking button
        self.btn_cancel_booking = tk.Button(self._frame,
                                            text="Cancel Booking",
                                            command=self.cancel_booking_window)
        self.btn_cancel_booking.grid(row=4, column=1)

        # Manage Current Drivers button
        self.btn_manage_drivers = tk.Button(
            self._frame,
            text="Manage Current Drivers",
            command=self.manage_current_drivers_window)
        self.btn_manage_drivers.grid(row=5, column=1)

        # Manage Current Customers button
        self.btn_manage_customers = tk.Button(
            self._frame,
            text="Manage Current Customers",
            command=self.manage_current_customers_window)
        self.btn_manage_customers.grid(row=6, column=1)

        # List registered users
        self.btn_list_registered_users = tk.Button(
            self._frame,
            text="List Registered Users",
            command=self.list_registered_users_window)
        self.btn_list_registered_users.grid(row=9, column=1)

        # Logout button
        self.btn_logout = tk.Button(self._frame,
                                    text="Logout",
                                    command=self._frame.logout)
        self.btn_logout.grid(row=10, column=1)

    def view_requested_bookings_window(self):
        # Example: Display a new frame to show requested bookings
        requested_bookings = [{
            "booking_id": 1,
            "pickup": "Location A",
            "dropoff": "Location B",
            "customer_name": "John Doe"
        }, {
            "booking_id": 2,
            "pickup": "Location C",
            "dropoff": "Location D",
            "customer_name": "Jane Smith"
        }]
        self.display_list_in_frame("Requested Bookings", requested_bookings)

    def assign_driver_to_booking_window(self):
        # Example: Display a new frame to assign a driver to a booking
        self.display_message_in_frame("Driver Assigned!")

    def confirm_booking_window(self):
        # Example: Display a new frame to confirm a booking
        self.display_message_in_frame("Booking Confirmed!")

    def cancel_booking_window(self):
        # Example: Display a new frame to cancel a booking
        self.display_message_in_frame("Booking Canceled!")

    def manage_current_drivers_window(self):
        # Example: Display a new frame to manage current drivers
        current_drivers = [{
            "driver_id": 1,
            "name": "Driver A",
            "status": "Available"
        }, {
            "driver_id": 2,
            "name": "Driver B",
            "status": "Unavailable"
        }]
        self.display_list_in_frame("Current Drivers", current_drivers)

    def manage_current_customers_window(self):
        # Example: Display a new frame to manage current customers
        current_customers = [{
            "customer_id": 1,
            "name": "Customer A",
            "trips_made": 5
        }, {
            "customer_id": 2,
            "name": "Customer B",
            "trips_made": 3
        }]
        self.display_list_in_frame("Current Customers", current_customers)

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
                                command=self.display_admin_index)
        back_button.grid(row=10, column=1)

    def display_message_in_frame(self, message):
        # Clear existing widgets in the frame
        self._frame._clear_widgets()

        # Display a message in the same frame
        message_label = tk.Label(self._frame, text=message)
        message_label.grid(row=1, column=1)

        # Back button to return to the main view
        back_button = tk.Button(self._frame,
                                text="Back",
                                command=self.display_admin_index)
        back_button.grid(row=10, column=1)

    #@staticmethod

    # class AdminView:
    # ... (other methods)

    #@staticmethod
    def format_listbox_item(self, item):
        if 'name' in item and 'driver_id' in item and 'status' in item:
            return f"{item['name']} (ID: {item['driver_id']}) - Status: {item['status']}"
        else:
            return "Invalid item format"

    def list_registered_users_window(self):
        '''List the registered users.
            '''
        self._frame._clear_widgets()
        self.label = tk.Label(self._frame,
                              text="Welcome to Taxi Booking App - List users")
        self.label.grid(row=0, column=1)

        # create listbox object
        self.user_listbox = tk.Listbox(self._frame,
                                       height=10,
                                       width=50,
                                       bg="grey",
                                       activestyle='dotbox',
                                       font="Helvetica",
                                       fg="yellow")

        # inserting listbox list
        for curr_user in self._frame.db.user_retrieve():
            curr_user = dict(curr_user)
        print(f"User Row: {curr_user}")
        self.user_listbox.insert(
            tk.END, f"ID: {curr_user['userid']} # " +
            f"Name: {curr_user['username']} # " +
            f"Password: {curr_user['password']} # " +
            f"Role: {curr_user['role']}" + f"State: {curr_user['state']}")
        self.user_listbox.grid(row=3, column=1)

        # Back button to return to the main view
        back_button = tk.Button(self._frame,
                                text="Back",
                                command=self.display_admin_index)
        back_button.grid(row=5, column=1)


# Example usage:
# admin_view = AdminView()  # Assuming the frame is initialized appropriately
# admin_view.view_requested_bookings_window()  # or admin_view.manage_current_drivers_window(), etc.
