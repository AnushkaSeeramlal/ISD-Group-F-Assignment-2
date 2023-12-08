'''Login View
'''
# System imports
import tkinter as tk


class LoginView:

    def __init__(self, frame=None):
        self._frame = frame
        self.login_view()

    def login_view(self):
        '''Main login view.
        '''
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
        # Register button
        self.btn_register = tk.Button(self._frame,text="Register",command=self.register_view)
        self.btn_register.grid(row=5,column=1)

    def register_view(self):
        '''Allow someone to register.
        '''
        self._frame._clear_widgets()

        # Main Label
        self.label = tk.Label(self._frame, text="Register to Taxi Booking App")
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

        # Name
        self.lbl_name = tk.Label(self._frame, text="Name: ")
        self.lbl_name.grid(row=4,column=0)
        self.entry_name = tk.Entry(self._frame, width=20)
        self.entry_name.grid(row=4,column=1)

        # address
        self.lbl_address = tk.Label(self._frame, text="Address: ")
        self.lbl_address.grid(row=5,column=0)
        self.entry_address = tk.Entry(self._frame, width=20)
        self.entry_address.grid(row=5,column=1)

        # phone
        self.lbl_phone = tk.Label(self._frame, text="Phone: ")
        self.lbl_phone.grid(row=6,column=0)
        self.entry_phone = tk.Entry(self._frame, width=20)
        self.entry_phone.grid(row=6,column=1)

        # email
        self.lbl_email = tk.Label(self._frame, text="Email: ")
        self.lbl_email.grid(row=7,column=0)
        self.entry_email = tk.Entry(self._frame, width=20)
        self.entry_email.grid(row=7,column=1)

        # license_plate
        self.lbl_license_plate = tk.Label(self._frame, text="License Plate (Drivers Only): ")
        self.lbl_license_plate.grid(row=9,column=0)
        self.entry_license_plate = tk.Entry(self._frame, width=20)
        self.entry_license_plate.grid(row=9,column=1)

        # Role
        role_options = [
            # 'admin', # Future use
            'customer',
            'driver',
        ]
        self.role_var = tk.StringVar()
        self.lbl_role = tk.Label(self._frame, text="Role: ")
        self.lbl_role.grid(row=10,column=0)
        self.entry_role = tk.OptionMenu(self._frame, self.role_var, *role_options)
        self.entry_role.grid(row=10,column=1)

        # Register button
        self.btn_register = tk.Button(self._frame,text="Register Account",command=self._create_account)
        self.btn_register.grid(row=11,column=1)

        # Go back to login button
        # Register button
        self.btn_login = tk.Button(self._frame,text="Back to Login",command=self.login_view)
        self.btn_login.grid(row=12,column=1)

    def _create_account(self):
        '''Create a user account from the register page.

        TODO: Error handling (e.g. duplicate account names)
        '''

        account_role = self.role_var.get()
        if account_role == 'driver':
            account_state = 1 # Don't need to approve drivers.
        else:
            account_state = 1

        self._frame.db.user_create(
            username=self.entry_username.get().strip(),
            password=self.entry_password.get(),
            name=self.entry_name.get(),
            address=self.entry_address.get(),
            phone=self.entry_phone.get(),
            email=self.entry_email.get(),
            license_plate=self.entry_license_plate.get(),
            role=self.role_var.get(),
            state=account_state,
        )
        if False:
            self.text_var.set("Created account. An admin needs to approve your account.")
        else:
            self.text_var.set("Created account. Please login.")

    def _btn_login_click(self):
        '''Login to account and if successful redirect to appropriate view.
        '''
        username = self.entry_username.get()
        print(f"Login by user: {username}")
        db_result = self._frame.db.user_retrieve(username=username)
        if not db_result:
            self.text_var.set("User does not exist")
            return

        user_db_record = db_result[0]
        print(f"Login user object: {user_db_record}")

        if self.entry_password.get() != user_db_record['password']:
            self.text_var.set("Login Failed. Check password")
            return

        if user_db_record['state'] == 2:
            self.text_var.set("Account not approved. Please contact admin")
            return

        self.text_var.set("Login Successful")
        self._frame._user = user_db_record
        match user_db_record['role']:
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

