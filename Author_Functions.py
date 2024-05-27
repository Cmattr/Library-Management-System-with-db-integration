from Database_Connection import connect_database

class Author:
    def __init__(self, name, biography):
        self.name = name
        self.biography = biography
    
    # Add author Function    
    def add_Author(self, cursor):
            self.name = input("Enter the Author: ")
            self.biography= input("Provide a brief Biography of the Author: ")
            try:
                query = "INSERT INTO authors (name, biography) VALUES (%s, %s)"
                cursor.execute(query, (self.name, self.biography))
                print(f"\n{self.name} has been added to the list of authors\n")
            except Exception as e:
                print(f"Error: {e}")

    # View all authors function
    def view_all_authors(self, cursor):
        try:
            query = "SELECT * FROM authors"
            cursor.execute(query)
            for row in cursor.fetchall():
                print(f"\n{row}\n")
        except Exception as e:
            print(f"Error: {e}")

    # Search for a specific author
    def view_author (self, cursor):
        self.name = input("Enter the Authors full name: ")
        try:
            query = "SELECT * FROM users WHERE name = %s "
            cursor.execute(query, (self.name))
            for row in cursor.fetchall():
                print(f"\n{row}\n")
        except Exception as e:
            print(f"Error: {e}")
                
