# System imports
import tkinter as tk

# External imports
# Local imports
import Bookings
from taxi_login.login_view import LoginView
from taxi_roles.admin_view import AdminView
from taxi_roles.customer_view import CustomerView
from taxi_roles.driver_view import DriverView


class MainFrame(tk.Frame):
    '''Main frame for application

    This is the main window that we display to the user.
    Every view wipes and re-uses this frame.
    '''

    def __init__(self, master=None):
        super().__init__(master)
        self._window = master
        self.pack()

        self.db = Bookings.BookingDatabase()
        self._user = None

        self.create_default_widgets()

    # Method to create default widgets
    def create_default_widgets(self):
        self.label = tk.Label(self, text="Welcome to Taxi Booking App")
        self.label.pack()
        self._login_button = tk.Button(self,
                                       text="Login",
                                       command=self.display_login)
        self._login_button.pack(pady=50)

        if self._user is None:
            self.display_login()

    # Method to clear all widgets on the frame
    def _clear_widgets(self):
        '''Clear all widgets on the frame.
        '''
        for widget in self.winfo_children():
            widget.destroy()

    # Method to log out the user
    def logout(self):
        if self._user is not None:
            self._user = None
            self._clear_widgets()
            self.display_login()

    # Method to display the login screen
    def display_login(self, ):
        '''Display login screen.
        '''
        LoginView(self)

    # Method to display the admin view
    def display_admin(self):
        AdminView(self)

    # Method to display the customer view
    def display_customer(self):
        CustomerView(self)

    # Method to display the driver view
    def display_driver(self):
        DriverView(self)


# Main method to create the window and start the application loop
def main():
    window = tk.Tk()
    window.title("Taxi Booking App")
    window.resizable(width=False, height=False)
    window.eval("tk::PlaceWindow . center")
    window.geometry("600x400")
    MainFrame(window)
    window.mainloop()


main()