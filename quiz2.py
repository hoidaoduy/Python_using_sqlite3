import sqlite3
from contextlib import closing

if __name__ == '__main__':
    with closing(sqlite3.connect("customers.db")) as connection:
        with closing(connection.cursor()) as cursor:
            # SQL piece of code Executed
            try:
                cursor.execute("DROP TABLE customers")
            except sqlite3.OperationalError:
                print("Already exists the table")

            cursor.executescript("""
                    CREATE TABLE customers(name VARCHAR(255), address VARCHAR(255));
                    """)

            List = [('Dung', 'Binh Dinh'),
                    ('Tuan', 'Phu Yen'),
                    ('Royal', 'Vinh Phuc')]

            connection.executemany("""INSERT INTO customers(name, address)
                VALUES (?, ?)""", List)

            sql = """SELECT * FROM customers WHERE name = "Hoi";"""
            cursor.execute(sql)

            result = cursor.fetchall()
            for x in result:
                print(x)

            # Changes saved into database
            connection.commit()
