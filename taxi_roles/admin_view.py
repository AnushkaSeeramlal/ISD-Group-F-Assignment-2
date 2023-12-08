import tkinter as tk


class AdminView:

    def __init__(self, frame=None):
        self._frame = frame
        self.display_admin_index()

    def display_admin_index(self):
        '''Administrator index.
        '''
        self._frame._clear_widgets()
        self.header_label = tk.Label(self._frame,
                              text="Welcome to Taxi Booking App - Administrator")
        self.header_label.grid(row=0, column=1)

        # View Requested Bookings button
        self.btn_view_requested_bookings = tk.Button(
            self._frame,
            text="View & Assign Requested Bookings",
            command=self.view_requested_bookings_window)
        self.btn_view_requested_bookings.grid(row=1, column=1)

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
        '''Show requested bookings.
        '''
        self._frame._clear_widgets()

        # Headers
        self.header_label = tk.Label(self._frame,
                              text="Requested Trips to assign")
        self.header_label.grid(row=0, column=1)

        self.header_label_trips = tk.Label(self._frame,
                              text="Trips")
        self.header_label_trips.grid(row=2, column=0)

        self.header_label_drivers = tk.Label(self._frame,
                              text="Drivers")
        self.header_label_drivers.grid(row=2, column=2)

        # Trips
        requested_bookings = self._frame.db.trip_retrieve(tripstatus='pending')
        self._booking_var = tk.IntVar(self._frame, -1)
        grid_location_booking = 5
        for curr_booking in requested_bookings:
            curr_booking_customer = self._frame.db.user_retrieve(userid=curr_booking['customerid'])
            curr_radio_button_1 = tk.Radiobutton(
                self._frame,
                text=f"{curr_booking_customer[0]['name']} from {curr_booking['pickupaddress']} to {curr_booking['destinationaddress']}",
                variable=self._booking_var,
                value=curr_booking['tripid'],
                # command=group_1_select,
            )
            curr_radio_button_1.grid(row=grid_location_booking, column=0)
            grid_location_booking += 1

        available_drivers = filter(
            lambda x: x['driverstate'] == 1 and x['state'] == 1,
            self._frame.db.user_retrieve(role='driver'),
        )
        self._driver_var = tk.IntVar(self._frame, -1)
        grid_location_driver = 5
        for curr_driver in available_drivers:
            curr_radio_button_1 = tk.Radiobutton(
                self._frame,
                text=f"{curr_driver['name']}",
                variable=self._driver_var,
                value=curr_driver['userid'],
            )
            curr_radio_button_1.grid(row=grid_location_driver, column=2)
            grid_location_driver += 1

        if grid_location_booking > grid_location_driver:
            max_grid_select = grid_location_booking
        else:
            max_grid_select = grid_location_driver

        # Back button to return to the main view
        back_button = tk.Button(self._frame,
                                text="Assign Driver to Trip",
                                command=self.assign_driver_to_trip)
        back_button.grid(row=max_grid_select + 1, column=1)

        # Back button to return to the main view
        back_button = tk.Button(self._frame,
                                text="Back",
                                command=self.display_admin_index)
        back_button.grid(row=max_grid_select + 2, column=1)

    def assign_driver_to_trip(self):
        '''Assign a driver to the trip.
        '''
        trip_id = self._booking_var.get()
        driver_id = self._driver_var.get()
        print(f"Trip: {trip_id} ; Driver: {driver_id}")
        # Set the driver on the trip
        self._frame.db.trip_update(
            tripid=trip_id,
            driverid=driver_id,
            tripstatus='driver_selected'
        )
        # Set the driver as unavailable
        self._frame.db.user_update(userid=driver_id, driverstate=0)
        self.view_requested_bookings_window()

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
        self.header_label = tk.Label(self._frame,
                              text="Welcome to Taxi Booking App - List users")
        self.header_label.grid(row=0, column=1)

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

    def display_list(self, data, formatter, width=100):
        '''Display the list in data in a listbox.
        '''
        # Display list in the same frame
        listbox = tk.Listbox(self._frame, width=width)
        for item in data:
            listbox.insert(tk.END, formatter(item))

        return listbox

    @staticmethod
    def fomat_dict(item):
        return str(item)

    @staticmethod
    def format_trip(item):
        print(f"Trip obj: {item}")
        trip_str = f"TripID: {item['tripid']} From: {item['pickupaddress']} To: {item['destinationaddress']} Date: {item['requesttime']} Cost: {item['ridecost']}"
        if item['driverid'] != 'None':
            trip_str += f" DriverID: {item['driverid']}"
        return trip_str

