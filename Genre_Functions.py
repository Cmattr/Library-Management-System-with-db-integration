from Database_Connection import connect_database

class Genre:
    def __init__(self, name, description, category):
        self.name = name
        self.description = description
        self.category = category
    
    # Add genre function
    def add_genre(self, cursor):
            self.name = input("Enter the genre: ")
            self.description = input("Provide a brief discription of the gerne: ")
            self.category = input("Enter a category for the genre (fiction/ non-fiction) ")
            try:
                query = "INSERT INTO genres (name, description, category) VALUES (%s, %s, %s)"        
                cursor.execute(query, (self.name, self.description, self.category))
                print(f"{self.name} has been added to the list of Genres")
            except Exception as e:
                print(f"Error: {e}")

    # View all genres function
    def view_all_genres(self, cursor):
        try:
            query = "SELECT * FROM genres"
            cursor.execute(query)
            for row in cursor.fetchall():
                print(f"\n{row}\n")
        except Exception as e:
            print(f"Error: {e}")

    # Search a specific genre function
    def view_genre (self, cursor):
        try:
            self.name = input("Enter the book Title: ")
            query = "SELECT * FROM genre WHERE name = %s"
            cursor.execute(query, (self.name))
            for row in cursor.fetchall():
                print(f"\n{row}\n")
        except Exception as e:
            print(f"Error: {e}")   
