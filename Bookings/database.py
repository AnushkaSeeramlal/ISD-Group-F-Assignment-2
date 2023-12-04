import sqlite3 as sq 

class DatabaseHelpers:
  def database_connection(self):
connection = sq.connect(database="sample.db")
connection.cursor()

sql_task = """
CREATE TABLE BOOKINGS
(Booking_ID INT PRIMARY KEY NOT NULL,
Date DATETIME NOT NULL, 
Time DATETIME NOT NULL, 
Pickup_Address TEXT NOT NULL,
Drop_off_Address TEXT NOT NULL, 
Payment_Method INT NOT NULL);
"""

DatabaseHelpers.database_connection()

response = connection.execute(sql_task)

print(response.fetchall())

response.fetchall()
