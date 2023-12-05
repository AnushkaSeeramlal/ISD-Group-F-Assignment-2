#from PIL import Image, ImageTk
#from tkinter import ttk
#from tkinter.filedialog import askopenfilename
#from tkinter.messagebox import showinfo
#from tkinter.scrolledtext import ScrolledText
#from tkinter.ttk import Combobox
#import customtkinter as ctk
#from login import LoginView 
#from Bookings import DatabaseHelpers

'''Main entry for application
'''
#Following the pep8 formatting standard

# System imports
import tkinter as tk

# External imports

# Local imports
import Bookings
from login import LoginView
from roles import AdminView, CustomerView, DriverView

class MainFrame(tk.Frame):
    '''Main frame for application

    This is the main window that we display at the user.
    Every view wipes and re-uses this frame.
    '''

    def __init__(self, master=None):
        super().__init__(master)
        self._window = master
        self.pack()
        self.create_default_widgets()

        self.db = Bookings.BookingDatabase()
        self._user = None


    def create_default_widgets(self):
        self.label = tk.Label(self, text="Welcome to Taxi Booking App")
        self.label.pack()
        self._login_button = tk.Button(self, text="Login",command=self.display_login)
        self._login_button.pack(pady=50)


    def _clear_widgets(self):
        '''Clear all widgets on the frame.
        '''
        for widget in self.winfo_children():
            widget.destroy()

    def logout(self):
        if self._user is not None:
            self._user = None
            self._clear_widgets()
            self.display_login()

    def display_login(self, ):
        '''Display login screen.
        '''
        LoginView(self)

    def display_admin(self):
        '''
        '''
        AdminView(self)

    def display_customer(self):
        '''
        '''
        CustomerView(self)

    def display_driver(self):
        '''
        '''
        DriverView(self)


def main():
    window = tk.Tk()
    window.title("Taxi Booking App")
    window.resizable(width=False, height=False)
    window.eval("tk::PlaceWindow . center")
    window.geometry("600x400")
    main_frame = MainFrame(window)
    window.mainloop()



main()
