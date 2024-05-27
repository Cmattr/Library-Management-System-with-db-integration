from Database_Connection import connect_database

class User:
    def __init__(self, name, library_id):
        self.name = name
        self.library_id = library_id
    
    # Add user function
    def add_user(self, cursor):
        try:
            self.name = input("Enter the users full name: ")
            self.library_id= input("Enter Library ID: ")
            query = "INSERT INTO users (name, library_id) VALUES (%s, %s)"
            cursor.execute(query, (self.name, self.library_id))
            (f"\nUser: {self.name} has been added to the library\n")
        except Exception as e:
            print(f"Error: {e}")

    # view all users function
    def view_all_users(self, cursor):
        try:    
            query = "SELECT * FROM users"
            cursor.execute(query)
            for row in cursor.fetchall():
                print(f"\n{row}\n")
        except Exception as e:
            print(f"Error: {e}")

    # Search a specific user funciton        
    def view_user (self, cursor):
        self.name = input("Enter the users full name: ")
        self.library_id = input("Enter the users library_id: ")
        try:
            query = "SELECT * FROM users WHERE name = %s AND library_id = %s"
            cursor.execute(query, (self.name, self.library_id))
            for row in cursor.fetchall():
                print(f"\n{row}\n")
        except Exception as e:
            print(f"Error: {e}")