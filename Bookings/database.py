import sqlite3 as sq


class BookingDatabase:

    def __init__(self):
        '''
        Initializes the database connection.
        '''
        self.conn = sq.connect('bookings.db')
        self.cursor = self.conn.cursor()
        self.setup_tables()

    def setup_tables(self):
        '''
        Setup the database tables.
        '''

        sql_create_bookings_table = """
        CREATE TABLE IF NOT EXISTS BOOKINGS (
            Booking_ID INT PRIMARY KEY NOT NULL,
            Date DATETIME NOT NULL,
            Time DATETIME NOT NULL,
            Pickup_Address TEXT NOT NULL,
            Drop_off_Address TEXT NOT NULL, 
            Payment_Method INT NOT NULL
        );
        """
        response = self.conn.execute(sql_create_bookings_table)

    def fetch_payments(self, customer_id):
        '''Fetch all payments for a specific customer id.
        '''
        sql_fetch_payments = """
        SELECT * FROM PAYMENTS WHERE Customer_ID = ?
        """
        response = self.conn.execute(sql_fetch_payments, (customer_id,))
        return response.fetchall()

    def fetch_bookings(self, customer_id=None):
        '''Fetch all bookings for a specific customer id.
        '''
        sql_fetch_bookings = """
        SELECT * FROM BOOKINGS WHERE Customer_ID = ?
        """
        response = self.conn.execute(sql_fetch_bookings, (customer_id,))
        return response.fetchall()

    def fetch_all_bookings(self):
        '''Fetch all bookings.
        '''
        sql_fetch_all_bookings = """
        SELECT * FROM BOOKINGS
        """
        response = self.conn.execute(sql_fetch_all_bookings)
        return response.fetchall()