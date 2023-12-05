'''Login View
'''
# System imports
import tkinter as tk

class LoginView:

    accounts = {
        'admin': {
            'password': 'adminpassword',
            'role': 'admin',
        },
        'david': {
            'password': 'customerpassword',
            'role': 'customer',
        },
        'joel': {
            'password': 'customerpassword',
            'role': 'customer',
        },
        'driver': {
            'password': 'driverpassword',
            'role': 'driver',
        },
        'crazy': {
            'password': 'crazypassword',
            'role': 'crazy',
        }

    }

    def __init__(self, frame=None):
        self._frame = frame
        self.create_widgets()

    def create_widgets(self):
        self._frame._clear_widgets()
        # Main Label
        self.label = tk.Label(self._frame, text="Login to Taxi Booking App")
        self.label.grid(row=0, column=1)
        # Status messages
        self.text_var = tk.StringVar()
        self.status_text = tk.Label(self._frame, textvariable=self.text_var, width=50)
        self.status_text.grid(row=1, column=1)
        # Username
        self.lbl_user_id = tk.Label(self._frame, text="Username: ")
        self.lbl_user_id.grid(row=2,column=0)
        self.entry_username = tk.Entry(self._frame, width=20)
        self.entry_username.grid(row=2,column=1)
        # Password
        self.lbl_password = tk.Label(self._frame, text="Password: ")
        self.lbl_password.grid(row=3,column=0)
        self.entry_password = tk.Entry(self._frame, width=20, show="*")
        self.entry_password.grid(row=3,column=1)
        # Login button
        self.btn_login = tk.Button(self._frame,text="Login",command=self._btn_login_click)
        self.btn_login.grid(row=4,column=1)

    def _btn_login_click(self):
        '''Login to account and if successful redirect to appropriate view.
        '''
        username = self.entry_username.get()
        if username not in self.accounts:
            self.text_var.set("User does not exist")
            return

        if self.entry_password.get() != self.accounts[username]['password']:
            self.text_var.set("Login Failed. Check password")
            return

        self.text_var.set("Login Successful")
        self._frame._user = self.accounts[username]
        self._frame._user['username'] = username
        match self.accounts[username]['role']:
            case 'admin':
                # Load admin view
                self._frame.display_admin()
            case 'customer':
                # Load customer view
                self._frame.display_customer()
            case 'driver':
                # Load driver view
                self._frame.display_driver()
            case _:
                # Unknown role - display login
                self.text_var.set("Unknown user role")

