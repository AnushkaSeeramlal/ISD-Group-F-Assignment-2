import tkinter as tk

class CustomerView:
    def __init__(self, frame=None):
        self._frame = frame
        self.create_widgets()

    def create_widgets(self):
        self._frame._clear_widgets()
        self.label = tk.Label(
            self._frame,
            text=f"Welcome to Taxi Booking App - Customer {self._frame._user['username']}"
        )
        self.label.grid(row=0, column=1)

        # Book Taxi button
        self.btn_book_taxi = tk.Button(self._frame, 
                                       text="Book Taxi", 
                                       command=self.make_booking_window)
        self.btn_book_taxi.grid(row=1, column=1)

        # View Booking History button
        self.btn_view_history = tk.Button(self._frame, 
                                          text="View Booking History", 
                                          command=self.view_booking_history_window)
        self.btn_view_history.grid(row=2, column=1)

        # Logout button
        self.btn_logout = tk.Button(self._frame,
                                    text="Logout",
                                    command=self._frame.logout)
        self.btn_logout.grid(row=4, column=1)

    def make_booking_window(self):
        # Example: Display a window to enter booking details in the same frame
        new_frame = tk.Frame(self._frame)
        new_frame.grid(row=5, column=1)

        # Pick-Up Address
        lbl_pickup = tk.Label(new_frame, text="Pick-Up Address:")
        lbl_pickup.grid(row=0, column=0)
        entry_pickup = tk.Entry(new_frame)
        entry_pickup.grid(row=0, column=1)

        # Drop-Off Address
        lbl_dropoff = tk.Label(new_frame, text="Drop-Off Address:")
        lbl_dropoff.grid(row=1, column=0)
        entry_dropoff = tk.Entry(new_frame)
        entry_dropoff.grid(row=1, column=1)

        # Date
        lbl_date = tk.Label(new_frame, text="Date:")
        lbl_date.grid(row=2, column=0)
        entry_date = tk.Entry(new_frame)
        entry_date.grid(row=2, column=1)

        # Time
        lbl_time = tk.Label(new_frame, text="Time:")
        lbl_time.grid(row=3, column=0)
        entry_time = tk.Entry(new_frame)
        entry_time.grid(row=3, column=1)

        # Payment Method
        lbl_payment = tk.Label(new_frame, text="Payment Method:")
        lbl_payment.grid(row=4, column=0)
        entry_payment = tk.Entry(new_frame)
        entry_payment.grid(row=4, column=1)

        # Submit Button
        btn_submit = tk.Button(new_frame, text="Submit Booking", command=lambda: self.submit_booking(entry_pickup.get(),
                                                                                                     entry_dropoff.get(),
                                                                                                     entry_date.get(),
                                                                                                     entry_time.get(),
                                                                                                     entry_payment.get()))
        btn_submit.grid(row=5, column=1)

    def submit_booking(self, pickup, dropoff, date, time, payment_method):
        # Example: Handle the submitted booking details
        # You should implement the actual logic to handle bookings based on your requirements
        print(f"Booking Details: Pick-Up={pickup}, Drop-Off={dropoff}, Date={date}, Time={time}, Payment Method={payment_method}")

    def view_booking_history_window(self):
        # Example: Display a new frame to show booking history
        booking_history = [{"booking_id": 1, "pickup": "Location A", "dropoff": "Location B", "date": "2023-01-01"},
                           {"booking_id": 2, "pickup": "Location C", "dropoff": "Location D", "date": "2023-02-01"}]
        self.display_list_in_frame("Booking History", booking_history)

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

    @staticmethod
    def format_listbox_item(item):
        return f"Booking ID: {item['booking_id']}, Pick-Up: {item['pickup']}, Drop-Off: {item['dropoff']}, Date: {item['date']}"

# Example usage:
# customer_view = CustomerView()  # Assuming the frame is initialized appropriately
# customer_view.view_booking_history_window()  # or customer_view.make_booking_window(), etc.
