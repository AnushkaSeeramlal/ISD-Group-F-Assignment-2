import sqlite3 as sq


class BookingDatabase:
    '''
    1. Customer wants to schedule a trip.
        a. Actioned by Customer.
        b. Enters desired pickup time, pickup address, drop off address.
        c. Trip state is now pending.
    2. Admin is shown a list of pending trips and available drivers, and matches up a trip to a driver.
        a. Actioned by Admin.
        b. Selects driver for a trip.
        c. Trip state is now driver_selected
    3. Driver is notified of trip.
        a. Actioned by Driver.
        b. Driver accepts trip whose state is now en_route
        c. Driver declines trip returning the Trip to pending (goto step #2).
        d. Driver state goes to unavailable.
        e. Driver proceeds to pickup the passenger.
    4. Driver arrives at the pickup location.
        a. Passenger is notified of arrival and boards vehicle.
        b. Trip state goes to started.
    5. Driver collects payment upon arrival at destination.
        a. Actioned by Driver.
        b. Payment details entered.
        c. Passenger disembarks vehicle.
        d. Trip status is marked as completed.
        e. Driver state is changed to available.
    '''

    def __init__(self):
        '''
        Initializes the database connection.
        '''
        self.conn = sq.connect('bookings.db')
        self.conn.row_factory = sq.Row
        self.cursor = self.conn.cursor()
        self.setup_tables()

    def setup_tables(self):
        '''
        Setup the database tables.
        '''
        # state:
        #   0 : Inactive
        #   1 : Active
        #   2 : Pending Approval
        sql_create_user_table = """
        CREATE TABLE IF NOT EXISTS USERS (
            userid         INTEGER PRIMARY KEY,
            name           TEXT NOT NULL,
            username       TEXT NOT NULL UNIQUE,
            password       TEXT NOT NULL,
            role           TEXT NOT NULL,
            address        TEXT NULL,
            phone          TEXT NULL,
            email          TEXT NULL,
            LicencePlate   TEXT NULL,
            DriverState    INT  NOT NULL DEFAULT 0,   /* 0: Unavailable, 1: Available */
            state          INT  NOT NULL              /* 0: Inactive, 1: Active, 2: Pending Approval */
        );
        """
        self.cursor.execute(sql_create_user_table)

        usercount = self.cursor.execute(
            "SELECT COUNT() FROM USERS").fetchone()[0]
        if usercount == 0:
            print("Creating default user")
            # The table is empty, fill in a single admin
            self.cursor.execute("""
                INSERT INTO USERS (
                    username,  name,             password,        role,   state
                ) VALUES (
                    'admin',   'Administrator', 'adminpassword','admin', 1
                );
                """)
            self.conn.commit()

        # Bookings table
        sql_create_trip_table = """
        CREATE TABLE IF NOT EXISTS TRIP (
            tripid             INT PRIMARY KEY NOT NULL,
            customerid         INT NOT NULL,               /* Customer requesting ride */
            ridecost           INT NOT NULL,               /* Multiplied by 100 */
            paymentterms       TEXT NOT NULL,              /* 'cod' */
            requesttime        DATETIME NOT NULL,          /* When the customer requested the ride */
            PickupAddress      TEXT NOT NULL,
            DestinationAddress TEXT NOT NULL,
            driverid           INT NULL,                   /* Driver accepting the booking */
            tripstatus         TEXT NOT NULL               /* 'pending', 'driver_selected', 'en_route', 'started', 'completed' */
        );
        """
        # Future fields
        # driveracceptTime   DATETIME NULL,             /* When did the driver accept the booking */
        #PickupTime         DATETIME NULL,              /* Time the user was picked up */
        #DropoffTime        DATETIME NULL               /* Time the user was dropped off */
        self.conn.execute(sql_create_trip_table)

        sql_create_payment_table = """
        CREATE TABLE IF NOT EXISTS PAYMENT (
            paymentid           INT PRIMARY KEY NOT NULL,
            tripid              INT NOT NULL,
            paymentamount       INT NOT NULL,               /* Multiplied by 100 */
            paymentmethod       TEXT NOT NULL,              /* 'cod' */
            paymenttime         DATETIME NOT NULL           /* When the payment was made */
        );
        """
        self.conn.execute(sql_create_payment_table)

    def user_create(
        self,
        username,
        password,
        role,
        state,
        name=None,
        address=None,
        phone=None,
        email=None,
        license_plate=None,
    ):
        '''Create a user in the database.
       
        '''
        if role == 'driver':
            driverstate = 1
        else:
            driverstate = 0
        self.cursor.execute(f"""
            INSERT INTO USERS (
                username, password, role, state, name, address,
                phone, email, LicencePlate, DriverState
            ) VALUES (
                '{username}',
                '{password}',
                '{role}',
                {state},
                '{name}',
                '{address}',
                '{phone}',
                '{email}',
                '{license_plate}',
                {driverstate}
            )
        """)
        self.conn.commit()

    def user_retrieve(self, id=None, username=None):
        '''Fetch a user from the database.
        '''
        if id is not None:
            where_clause = f"WHERE userid={id}"
        elif username is not None:
            where_clause = f"WHERE username='{username}'"
        else:
            where_clause = ''

        self.cursor.execute("SELECT * FROM USERS " + where_clause)
        return self.cursor.fetchall()

    def user_update(self,
                    userid,
                    username=None,
                    password=None,
                    role=None,
                    state=None):
        '''Update a user.

        id is mandatory.
        Then specify any values you want to update
        '''
        update_list = []
        if username is not None:
            update_list += f"username='{username}'"
        if password is not None:
            update_list += f"password='{password}'"
        if role is not None:
            update_list += f"role='{role}'"
        if state is not None:
            update_list += f"state={state}"

        updates = ",".join(update_list)

        update_sql = f"UPDATE USERS SET {updates} WHERE userid={userid}"
        self.cursor.execute(update_sql)

    def fetch_payments(self, customer_id):
        '''Fetch all payments for a specific customer id.
        '''
        sql_fetch_payments = """
        SELECT * FROM PAYMENT WHERE Customer_ID = ?
        """
        response = self.conn.execute(sql_fetch_payments, (customer_id, ))
        return response.fetchall()

    def fetch_bookings(self, customer_id=None):
        '''Fetch all bookings for a specific customer id.
        '''
        sql_fetch_bookings = """
        SELECT * FROM TRIP WHERE Customer_ID = ?
        """
        response = self.conn.execute(sql_fetch_bookings, (customer_id, ))
        return response.fetchall()

    def fetch_all_bookings(self):
        '''Fetch all bookings.
        '''
        sql_fetch_all_bookings = """
        SELECT * FROM TRIP
        """
        response = self.conn.execute(sql_fetch_all_bookings)
        return response.fetchall()

    def booking_create(self, customer_id, date, time, pickup_address,
                       drop_off_address, payment_method):
        '''Create a booking in the database.
        '''
