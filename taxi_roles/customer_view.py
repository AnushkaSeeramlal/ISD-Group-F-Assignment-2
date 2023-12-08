# System imports
import datetime
import random

import tkinter as tk


class CustomerView:

    def __init__(self, frame=None):
        self._frame = frame
        self.customer_index()

    def customer_index(self):
        self._frame._clear_widgets()
        self.header_label = tk.Label(
            self._frame,
            text=
            f"Welcome to Taxi Booking App - Customer {self._frame._user['username']}"
        )
        self.header_label.grid(row=0, column=1)

        # Book Taxi button
        self.btn_book_taxi = tk.Button(self._frame,
                                       text="Book Taxi",
                                       command=self.make_booking_window)
        self.btn_book_taxi.grid(row=1, column=1)

        # View Booking History button
        self.btn_view_history = tk.Button(
            self._frame,
            text="View Booking History",
            command=self.view_booking_history_window)
        self.btn_view_history.grid(row=2, column=1)

        # Logout button
        self.btn_logout = tk.Button(self._frame,
                                    text="Logout",
                                    command=self._frame.logout)
        self.btn_logout.grid(row=4, column=1)

    def make_booking_window(self):
        '''Make a trip booking.
        '''
        self._frame._clear_widgets()

        curr_time = datetime.datetime.now()

        self.header_label = tk.Label(
            self._frame, text=f"Book a trip - '{self._frame._user['name']}'")
        self.header_label.grid(row=1, column=1)

        # Pick-Up Address
        lbl_pickup = tk.Label(self._frame, text="Pick-Up Address: ")
        lbl_pickup.grid(row=3, column=0)
        self.entry_pickup = tk.Entry(self._frame)
        self.entry_pickup.grid(row=3, column=1)

        # Drop-Off Address
        lbl_dropoff = tk.Label(self._frame, text="Drop-Off Address:")
        lbl_dropoff.grid(row=4, column=0)
        self.entry_dropoff = tk.Entry(self._frame)
        self.entry_dropoff.grid(row=4, column=1)

        # Date
        self._entry_date = tk.StringVar()
        lbl_date = tk.Label(self._frame, text="Date:")
        lbl_date.grid(row=5, column=0)
        self.entry_date = tk.Entry(self._frame, textvariable=self._entry_date)
        self.entry_date.grid(row=5, column=1)
        self._entry_date.set(curr_time.strftime("%Y-%m-%d"))

        # Time
        self._entry_time = tk.StringVar()
        lbl_time = tk.Label(self._frame, text="Time:")
        lbl_time.grid(row=6, column=0)
        self.entry_time = tk.Entry(self._frame, textvariable=self._entry_time)
        self.entry_time.grid(row=6, column=1)
        self._entry_time.set(curr_time.strftime("%H:%M"))

        # Payment Method
        payment_types = [
            'cod',
        ]
        self.payment_type = tk.StringVar()
        self.lbl_payment = tk.Label(self._frame, text="Payment Method:")
        self.lbl_payment.grid(row=8, column=0)
        self.entry_payment_type = tk.OptionMenu(self._frame, self.payment_type,
                                                *payment_types)
        self.entry_payment_type.grid(row=8, column=1)

        # Price
        self.price_var = tk.StringVar()
        self.price_label = tk.Label(self._frame,
                                    text=f"Price: TBD",
                                    textvariable=self.price_var)
        self.price_label.grid(row=9, column=1)

        # Submit Button
        btn_submit = tk.Button(
            self._frame,
            text="Submit Booking",
            command=self.submit_booking,
        )
        btn_submit.grid(row=10, column=1)

        # Back to customer index
        self.btn_customer_index = tk.Button(self._frame,
                                            text="Back",
                                            command=self.customer_index)
        self.btn_customer_index.grid(row=11, column=1)

    def submit_booking(self):
        '''Create a trip booking.
        '''
        pickupaddress = self.entry_pickup.get()
        destinationaddress = self.entry_dropoff.get()
        requesttime = f"{self._entry_date.get()} {self._entry_time.get()}"
        paymentterms = self.payment_type.get()
        ridecost = random.randint(500, 1000) / 100
        self.price_var.set(f"Price: ${ridecost}")
        self._frame.db.trip_create(
            customerid=self._frame._user['userid'],
            requesttime=requesttime,
            ridecost=ridecost,
            pickupaddress=pickupaddress,
            destinationaddress=destinationaddress,
            paymentterms=paymentterms,
        )

    def view_booking_history_window(self):
        '''Booking history list.
        '''
        # Example: Display a new frame to show booking history
        self._frame._clear_widgets()

        # Header
        self.header_label = tk.Label(
            self._frame, text=f"Your trips - '{self._frame._user['name']}'")
        self.header_label.grid(row=1, column=1)

        # "Booking History",
        booking_history = self._frame.db.trip_retrieve(
            customerid=self._frame._user['userid'])
        self._booking_list = self.display_list_in_frame(
            booking_history, self.format_trip)
        self._booking_list.grid(row=5, column=1)

        # Back button to return to the main view
        back_button = tk.Button(self._frame,
                                text="Back",
                                command=self.customer_index)
        back_button.grid(row=10, column=1)

    def display_list_in_frame(self, data, formatter):
        '''Display the list in data in a listbox.
        '''
        # Display list in the same frame
        listbox = tk.Listbox(self._frame, width=100)
        for item in data:
            listbox.insert(tk.END, formatter(item))

        return listbox

    @staticmethod
    def fomat_dict(item):
        return str(item)

    @staticmethod
    def format_trip(item):
        print(f"Trip obj: {item}")
        trip_str = f"TripID: {item['tripid']} From: {item['pickupaddress']} To: {item['destinationaddress']} Date: {item['requesttime']} Cost: {item['ridecost']} State: {item['tripstatus']}"
        if item['driverid'] != 'None':
            trip_str += f" DriverID: {item['driverid']}"
        return trip_str


# Example usage:
# customer_view = CustomerView()  # Assuming the frame is initialized appropriately
# customer_view.view_booking_history_window()  # or customer_view.make_booking_window(), etc.
