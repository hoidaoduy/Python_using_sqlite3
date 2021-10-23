3import sqlite3
from contextlib import closing


def create_table(name_of_database, name_of_table):
    """
    :param name_of_database: name of data query
    :param name_of_table: name of table query
    """
    with closing(sqlite3.connect(name_of_database)) as connection:
        with closing(connection.cursor()) as cursor:
            # SQL piece of code Executed
            try:
                execute = "DROP TABLE {}".format(name_of_table)
                cursor.execute(execute)
            except sqlite3.OperationalError:
                print("Already exists the table")

            execute = "CREATE TABLE {} (name VARCHAR(255), address VARCHAR(255))".format(name_of_table)
            cursor.execute(execute)
            # Changes saved into database
            connection.commit()


def input_data(name_of_database, name_table, list_data):
    """
    :param name_of_database: name of data query
    :param name_table: name of table query
    :param list_data: list have data
    """
    with closing(sqlite3.connect(name_of_database)) as connection:
        with closing(connection.cursor()) as cursor:
            execute = "INSERT INTO {} (name, address) VALUES (?, ?)".format(name_table)
            connection.executemany(execute, list_data)
            # Changes saved into database
            connection.commit()


def view_data(name_of_database, name_of_table):
    """
    :param name_of_database: name of data
    :param name_of_table: name of table query
    :return: view data from table
    """
    with closing(sqlite3.connect(name_of_database)) as connection:
        with closing(connection.cursor()) as cursor:
            execute = "SELECT * FROM {}".format(name_of_table)
            cursor.execute(execute)
            result = cursor.fetchall()
            for x in result:
                print(x)


if __name__ == '__main__':
    create_table("database.db", "customers")
    List = [('Hoi', 'Binh Dinh'),
            ('Tuan', 'Phu Yen'),
            ('Anh', 'Vinh Phuc')]
    input_data("database.db", "customers", List)
    view_data("database.db", "customers")

    print("Finish")
