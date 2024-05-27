from Database_Connection import connect_database
import datetime
class Book:
    def __init__(self, title, author_id, genre_id, isbn, publication_date, availability):
        self.title = title
        self.author_id = author_id
        self.genre_id = genre_id
        self.isbn = isbn
        self.publiction_date = publication_date
        self.availability = availability
        
    #adding book function
    def add_book(self, cursor):
        self.title = input("Enter the book title: ")
        self.author_id = input("Enter the author ID: ")
        self.genre_id = input("Enter the genre ID: ")
        self.isbn = input("Enter an ISBN for the book: ")
        self.publiction_date = input("Enter the publication date (YYYY-MM-DD): ")
        try:
            query = "INSERT INTO books (title, author_id, genre_id, isbn, publication_date) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(query, (self.title, self.author_id, self.genre_id, self.isbn, self.publiction_date))
            print(f"\n The book: {self.title} has been added to the library.\n")
        except Exception as e:
            print(f"Error: {e}")

    #Search for a specific book function
    def search_book (self, cursor):
        self.title = input("Enter the book title: ")
        try:
            query = "SELECT * FROM books WHERE title = %s"
            cursor.execute(query, (self.title, ))
            for row in cursor.fetchall():
                print(f"\n{row}\n")
        except Exception as e:
            print(f"Error: {e}")
    
    # View all books function
    def view_all_books(self, cursor):
        try:
            query = "SELECT * FROM books"
            cursor.execute(query)
            for row in cursor.fetchall():
                print(f"\n{row}\n")
        except Exception as e:
            print(f"Error: {e}")

    # Check out books function
    def check_out(self, cursor):
        self.title = input ("Enter the name of the book you wish to borrow: ")
        try:
            query =  "UPDATE books SET availability = 0 WHERE title = %s"
            cursor.execute(query, (self.title, ))
            print(f"\nYou have checked out the book: {self.title}")
            # Give a due date for the book
            due_date = datetime.date.today() + datetime.timedelta(weeks=2)
            print(f"The due date for the book '{self.title}' is: {due_date}\n")
        
        except Exception as e:
            print(f"Error: {e}")

    #Return book function
    def return_book(self, cursor):
        self.title = input ("Enter the name of the book you wish to return: ")
        try: 
            query =  "UPDATE books SET availability = 1 WHERE title = %s"
            cursor.execute(query, (self.title, ))
            print(f"\nYou have returned the book: {self.title}")
             # Check if book is overdue
            if datetime.date.today() > self.due_date:
                # Calculate fine as $1 per day overdue
                self.fines += (datetime.date.today() - self.due_date).days
                print(f"You have a fine of ${self.fines}.\n")
        except Exception as e:
            print(f"Error: {e}")

