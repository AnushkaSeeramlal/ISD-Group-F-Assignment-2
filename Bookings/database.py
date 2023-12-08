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

    def _result_to_dict(self, result):
        '''
        '''
        return list(map(dict, result))

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
            userid         INTEGER PRIMARY KEY AUTOINCREMENT,
            name           TEXT NOT NULL,
            username       TEXT NOT NULL UNIQUE,
            password       TEXT NOT NULL,
            role           TEXT NOT NULL,
            address        TEXT NULL,
            phone          TEXT NULL,
            email          TEXT NULL,
            licenceplate   TEXT NULL,
            driverstate    INT  NOT NULL DEFAULT 0,   /* 0: Unavailable, 1: Available */
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
            tripid             INTEGER PRIMARY KEY AUTOINCREMENT,
            customerid         INT NOT NULL,               /* Customer requesting ride */
            ridecost           INT NOT NULL,               /* Multiplied by 100 */
            paymentterms       TEXT NOT NULL,              /* 'cod' */
            requesttime        DATETIME NOT NULL,          /* When the customer requested the ride */
            pickupaddress      TEXT NOT NULL,
            destinationaddress TEXT NOT NULL,
            driverid           INT NULL,                   /* Driver accepting the booking */
            tripstatus         TEXT NOT NULL               /* 'pending', 'driver_selected', 'en_route', 'started', 'payment_completed', 'completed' */
        );
        """
        # Future fields
        # driveracceptTime   DATETIME NULL,             /* When did the driver accept the booking */
        #PickupTime         DATETIME NULL,              /* Time the user was picked up */
        #DropoffTime        DATETIME NULL               /* Time the user was dropped off */
        self.conn.execute(sql_create_trip_table)

        sql_create_payment_table = """
        CREATE TABLE IF NOT EXISTS PAYMENT (
            paymentid           INTEGER PRIMARY KEY AUTOINCREMENT,
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
                username,
                password,
                role,
                state,
                name,
                address,
                phone,
                email,
                licenceplate,
                driverstate
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

    def user_retrieve(self, userid=None, username=None, role=None):
        '''Fetch a user from the database.
        '''
        if userid is not None:
            where_clause = f"WHERE userid={userid}"
        elif username is not None:
            where_clause = f"WHERE username='{username}'"
        elif role is not None:
            where_clause = f"WHERE role='{role}'"
        else:
            where_clause = ''

        full_sql = "SELECT * FROM USERS " + where_clause
        print(f"SQL: {full_sql}")

        self.cursor.execute(full_sql)
        return self._result_to_dict(self.cursor.fetchall())

    def user_update(self,
                    userid,
                    username=None,
                    password=None,
                    role=None,
                    state=None,
                    driverstate=None):
        '''Update a user.

        id is mandatory.
        Then specify any values you want to update
        '''
        update_list = []
        if username is not None:
            update_list.append(f"username='{username}'")
        if password is not None:
            update_list.append(f"password='{password}'")
        if role is not None:
            update_list.append(f"role='{role}'")
        if state is not None:
            update_list.append(f"state={state}")
        if driverstate is not None:
            update_list.append(f"driverstate={driverstate}")

        updates = ",".join(update_list)

        update_sql = f"UPDATE USERS SET {updates} WHERE userid={userid}"
        self.cursor.execute(update_sql)
        self.conn.commit()

    def trip_create(
        self,
        customerid,
        ridecost,
        requesttime,
        pickupaddress,
        destinationaddress,
        driverid=None,
        tripstatus='pending',
        paymentterms='cod',
    ):
        '''Trip create.
        '''
        self.cursor.execute(f"""
            INSERT INTO TRIP (
                customerid,
                ridecost,
                paymentterms,
                requesttime,
                pickupaddress,
                destinationaddress,
                driverid,
                tripstatus
            ) VALUES (
                '{customerid}',
                '{ridecost}',
                '{paymentterms}',
                '{requesttime}',
                '{pickupaddress}',
                '{destinationaddress}',
                '{driverid}',
                '{tripstatus}'
            )
        """)
        self.conn.commit()

    def trip_retrieve(self,
                      tripid=None,
                      customerid=None,
                      driverid=None,
                      tripstatus=None):
        '''Fetch a trip
        '''
        if tripid is not None:
            where_clause = f"WHERE tripid={tripid}"
        elif customerid is not None:
            where_clause = f"WHERE customerid='{customerid}'"
        elif driverid is not None:
            where_clause = f"WHERE driverid='{driverid}'"
        elif tripstatus is not None:
            where_clause = f"WHERE tripstatus='{tripstatus}'"
        else:
            where_clause = ''

        self.cursor.execute("SELECT * FROM TRIP " + where_clause)
        return self._result_to_dict(self.cursor.fetchall())

    def trip_update(self, tripid, **kwargs):
        '''Update a trip.
        '''
        print(kwargs)
        update_list = []
        for k, v in kwargs.items():
            update_list.append(f"{k}='{v}'")

        print(update_list)

        updates = ",".join(update_list)

        update_sql = f"UPDATE TRIP SET {updates} WHERE tripid={tripid}"
        print(f"trip_update SQL: {update_sql}")
        self.cursor.execute(update_sql)
        self.conn.commit()

    def payment_create(self, tripid, paymentamount, paymentmethod,
                       paymenttime):
        '''Payment create.
        '''
        self.cursor.execute(f"""
            INSERT INTO PAYMENT (
                tripid,
                paymentamount,
                paymentmethod,
                paymenttime
            ) VALUES (
                '{tripid}',
                '{paymentamount}',
                '{paymentmethod}',
                '{paymenttime}'
            )
        """)
        self.conn.commit()

    def payment_retrieve(self, paymentid=None, tripid=None):
        '''Fetch a payment.
        '''
        if paymentid is not None:
            where_clause = f"WHERE paymentid={paymentid}"
        elif tripid is not None:
            where_clause = f"WHERE tripid='{tripid}'"
        else:
            where_clause = ''

        self.cursor.execute("SELECT * FROM PAYMENT " + where_clause)
        return self._result_to_dict(self.cursor.fetchall())

    def payment_update(self, paymentid, **kwargs):
        '''Update a payment.
        '''
        update_list = []
        for k, v in kwargs.items():
            update_list.append(f"{k}='{v}'")

        updates = ",".join(update_list)

        update_sql = f"UPDATE PAYMENT SET {updates} WHERE paymentid={paymentid}"
        self.cursor.execute(update_sql)
        self.conn.commit()
