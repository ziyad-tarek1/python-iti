
import mysql.connector
from mysql.connector import Error

# Function to establish a connection to the MySQL database
def connect_to_mysql():
    try:
        root_password = input("Enter MySQL root password: ")
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password=root_password,
            database="mysql"  # Connect to the default 'mysql' database
        )
        if connection.is_connected():
            print("Connected to MySQL database.")
            return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

# Function to show all tables in the current database
def show_tables(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()
        if tables:
            print("Tables in the database:")
            for table in tables:
                print(table[0])
        else:
            print("No tables found in the database.")
    except Error as e:
        print(f"Error showing tables: {e}")

# Function to create a new table
def create_table(connection):
    table_name = input("Enter the name of the table to create: ")
    columns = input("Enter column definitions (e.g., id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255)): ")
    try:
        cursor = connection.cursor()
        query = f"CREATE TABLE {table_name} ({columns})"
        cursor.execute(query)
        connection.commit()
        print(f"Table '{table_name}' created successfully.")
    except Error as e:
        print(f"Error creating table: {e}")

# Function to delete a table
def delete_table(connection):
    table_name = input("Enter the name of the table to delete: ")
    try:
        cursor = connection.cursor()
        query = f"DROP TABLE {table_name}"
        cursor.execute(query)
        connection.commit()
        print(f"Table '{table_name}' deleted successfully.")
    except Error as e:
        print(f"Error deleting table: {e}")

# Function to describe a table's structure
def describe_table(connection):
    table_name = input("Enter the name of the table to describe: ")
    try:
        cursor = connection.cursor()
        cursor.execute(f"DESCRIBE {table_name}")
        columns = cursor.fetchall()
        if columns:
            print(f"Structure of table '{table_name}':")
            for column in columns:
                print(column)
        else:
            print(f"Table '{table_name}' does not exist.")
    except Error as e:
        print(f"Error describing table: {e}")

# Function to insert data into a table
def insert_data(connection):
    table_name = input("Enter the name of the table to insert data into: ")
    columns = input("Enter column names (e.g., name, age): ")
    values = input(f"Enter values for columns ({columns}): ")
    try:
        cursor = connection.cursor()
        query = f"INSERT INTO {table_name} ({columns}) VALUES ({values})"
        cursor.execute(query)
        connection.commit()
        print("Data inserted successfully.")
    except Error as e:
        print(f"Error inserting data: {e}")

# Function to select data from a table
def select_data(connection):
    table_name = input("Enter the name of the table to select data from: ")
    try:
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()
        if rows:
            print(f"Data in table '{table_name}':")
            for row in rows:
                print(row)
        else:
            print(f"No data found in table '{table_name}'.")
    except Error as e:
        print(f"Error selecting data: {e}")

# Main menu
def main():
    connection = connect_to_mysql()
    if not connection:
        return

    while True:
        print("\nMySQL Administration Script")
        print("1. Show tables")
        print("2. Create a table")
        print("3. Delete a table")
        print("4. Describe a table")
        print("5. Insert data into a table")
        print("6. Select data from a table")
        print("7. Exit")
        choice = input("Select an option (1-7): ")

        if choice == "1":
            show_tables(connection)
        elif choice == "2":
            create_table(connection)
        elif choice == "3":
            delete_table(connection)
        elif choice == "4":
            describe_table(connection)
        elif choice == "5":
            insert_data(connection)
        elif choice == "6":
            select_data(connection)
        elif choice == "7":
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")

    if connection.is_connected():
        connection.close()
        print("MySQL connection closed.")

if __name__ == "__main__":
    main()
