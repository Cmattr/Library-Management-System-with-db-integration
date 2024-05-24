from Database_Connection import connect_database


class Book:
    books = {}
    borrowed_books = {}
    # book methods
    def __init__(self, title, author, isbn, genre, publication_date, status):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.genre = genre
        self.publication_date = publication_date
        self.status = status
    
    def add_book(self):
        self.title = input("Input the book title: ")
        self.author = input("Input the name of the books author: ")
        self.isbn = input("Input the isbn of the book: ")
        self.genre = input("input the books genre: ")
        self.publication_date = input("Input the books publication date: ")
        self.status = "Available"
        self.books[self.title] = {"Author": self.author, "ISBN": self.isbn, "Genre": self.genre, "Date": self.publication_date,  "Status": self.status,}
        print(f"\nThe book {self.title} by {self.author} has been added to the library\n")

        conn = connect_database()
        if conn is not None:
            try:
                cursor = conn.cursor()
                #SQL query to create a new work out session
                query = "INSERT INTO Books (title, author_id, Genre_id, isbn, publication_date, availability) VALUES (%s, %s)"

                #implement the query
                cursor.execute(query, (self.__name, self.__library_id))
                conn.commit()
                print("Work out session successfully added to the calender")

            # close cursor and connection
            finally:
                cursor.close()
                conn.close()

    def borrow_book(self, title):
        title = input("input the name of the book you wish to borrow: ")
        if title in self.books:
            book_status = {"Status": "Borrowed"}
            Book.books[title].update(book_status)
            Book.borrowed_books[title] = Book.books[title].copy()
            print(f"\nyou have borrowed the book {title}.\n")
        else:
            print("\nthis book is not available\n")

    def return_book(self, title):
        title = input ("input the name of the book you wish to borrow: ")
        if title in self.borrowed_books:
            Book.books[title] = Book.borrowed_books[title].copy()
            Book.books[title]['Status'] = "Available"
            print(f"The book {title} has been returned to the library") 
            del Book.borrowed_books[title]
            print(f"\nThe book {self.title} by {self.author} has been returned to the library\n")
        else:
            print("\nthat book has not been borrowed from the library\n")

    def search(self, title):
        title = input("Please input the name of the book you wish to search: ")
        if title in Book.books:
            book_details = Book.books[title]
            print(f"\nTitle: {title}")
            for key, value in book_details.items():
                print(f"{key}: {value}")
        else: 
            print("\nThis book is not in the library\n")
    
    def view_books(self):
        if self.books:
            for title, details in self.books.items():
                print (f"\nTitle: {title}")
                print(', '.join(f"{key}: {value}" for key, value in details.items()))
        else:
            print("\nThe Library is empty\n")

    def view_borrowed_books(self):
        if self.borrowed_books:
            for title, details in self.borrowed_books.items():
                print (f"\nTitle: {title}")
                print(', '.join(f"{key}: {value}" for key, value in details.items()))
                print("")
        else:
            print("\nThe Library is empty\n")

    def save_book_info(self, saved_books):
        with open(saved_books, 'w') as file:
            for title, details in self.books.items():
                file.write(f"{title}, {details['Author']}, {details['ISBN']}, {details['Genre']}, {details['Date']}, {details['Status']}\n")
        print(f"Book information has been saved to {saved_books}")
    
    
    def load_books(cls):
        try:
            with open('Saved_books.txt', 'r') as file:
                for line in file:
                    title, author, isbn, genre, publication_date, status = line.strip().split(', ')
                    cls.books[title] = {
                        "Author": author,
                        "ISBN": isbn,
                        "Genre": genre,
                        "Date": publication_date,
                        "Status": status
                    }
        except FileNotFoundError:
            pass
        except Exception as e:
            print(f"\nAn error occurred: {e}\n")

class User:
    __users = {}
    # user methods
    def __init__(self, name, library_id):
        self.__name = name
        self.__library_id = library_id
        
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_library_id(self):
        return self.__library_id

    def set_library_id(self, library_id):
        self.__library_id = library_id

    def get_borrowed(self):
        return self.__borrowed

    def set_borrowed(self, borrowed):
        self.__borrowed = borrowed

    def add_user(self):
        self.__name = input("Input user name: ")
        self.__library_id = int(input("Input new Library ID: "))
        User.__users[self.__name] = {"Library ID": self.__library_id}
        print(f"\nThe User {self.__name}, ID: {self.__library_id} Has been added to the library\n")

        conn = connect_database()
        if conn is not None:
            try:
                cursor = conn.cursor()
                #SQL query to create a new work out session
                query = "INSERT INTO users (name, library_id) VALUES (%s, %s)"

                #implement the query
                cursor.execute(query, (self.__name, self.__library_id))
                conn.commit()
                print("Work out session successfully added to the calender")

            # close cursor and connection
            finally:
                cursor.close()
                conn.close()

    def view_user_details(self):
        name = input("Please enter the name of the user you wish to view: ")
        if name in User.__users:
            user_details = User.__users[name]
            print(f"\nTitle: {name}")
            for key, value in user_details.items():
                print(f"{key}: {value}\n")
        else:
            print("The input is not a valid user name, please try again")

    def view_all_users(self):
        if User.__users:
            for name, details in User.__users.items():
                print(f"\nName: {name}")
                print(', '.join(f"{key}: {value}" for key, value in details.items()))
                print("")
        else:
            print("\nThere are currently no users\n")
    
    def save_user_info(self, saved_user):
        with open(saved_user, 'w') as file:
            for name, details in self.__users.items():
                file.write(f"{name}, {details['Library ID']}\n")
        print(f"User information has been saved to {saved_user}")
    
    def load_users(self):
        try:
            with open('Saved_users.txt', 'r') as file:
                for line in file:
                    name, library_id = line.strip().split(', ')
                    self.__users[name] = {
                        "Library_id": library_id,
                    }
        except FileNotFoundError:
            pass
        except Exception as e:
            print(f"\nAn error occurred: {e}\n")

    def delete_user():
        name = input("Enter the name of the member you wish to delete: ")
        id = input("Enter the Library ID of the member you wish to delete: ")
        conn = connect_database()
        if conn is not None:
            try:
                cursor = conn.cursor()
                #SQL query to create a new work out session
                query = "DELETE FROM users WHERE                                                                                                                                                                     "

                #implement the query
                cursor.execute(query, (name, id))
                conn.commit()
                print("Work out session successfully added to the calender")

            # close cursor and connection
            finally:
                cursor.close()
                conn.close()



class Author:
    authors = {} 
    # author methods
    def __init__(self, name, biography):
        self.name = name
        self.biography = biography

    def add_author(self):
            self.name = input("Enter the authors name: ")
            self.biography = input("Provide a small biography of the author: ")
            self.authors[self.name] = {"Biography": self.biography}
            print(f"\nAuthor: {self.name}\nBiography: {self.biography}\n")

            conn = connect_database()
            if conn is not None:
                try:
                    cursor = conn.cursor()
                    #SQL query to create a new work out session
                    query = "INSERT INTO authors (name, biography) VALUES (%s, %s)"

                    #implement the query
                    cursor.execute(query, (self.name, self.biography))
                    conn.commit()
                    print("Work out session successfully added to the calender")

                # close cursor and connection
                finally:
                    cursor.close()
                    conn.close()

    def view_authors_details(self,name):
        name = input("Please enter the name of the author you wish to view: ")
        if name in Author.authors:
            author_details = Author.authors[name]
            print(f"\nTitle: {name}")
            for key, value in author_details.items():
                print(f"{key}: {value}\n")
        else:
            print("this author is not recognized please try again.")

    def view_all_authors(self):    
        if self.authors:
            for name, details in self.authors.items():
                print (f"\nName: {name}")
                print(', '.join(f"{key}: {value}" for key, value in details.items()))
                print("")       
        else:
            print("\nThere are currently no authors\n")

    def save_author_info(self, saved_authors):
        with open(saved_authors, 'w') as file:
            for name, details in self.authors.items():
                file.write(f"{name}, {details['Biography']}\n")
        print(f"Author information has been saved to {saved_authors}")

    def load_authors(self):
        try:
            with open('Saved_Author.txt', 'r') as file:
                for line in file:
                    name, biography = line.strip().split(', ')
                    self.authors[name] = {
                        "Biography": biography,
                    }
        except FileNotFoundError:
            pass
        except Exception as e:
            print(f"\nAn error occurred: {e}\n")

class Genre:
    genres = {} 
    # genre methods
    def __init__(self, name, description, category):
        self.name = name
        self.description = description
        self.category = category

    def add_genre(self):
            self.name = input("Enter the genre: ")
            self.description = input("Provide a brief discription of the gerne: ")
            self.category = input("Enter a category for the genre (fiction/ non-fiction) ")
            self.genres[self.name] = {"Category": self.category, "Description": self.description}
            print(f"\nAuthor: {self.name}\ncategory: {self.category}\ndescription:: {self.description}")

            conn = connect_database()
            if conn is not None:
                try:
                    cursor = conn.cursor()
                    #SQL query to create a new work out session
                    query = "INSERT INTO genres (name, description, category) VALUES (%s, %s, %s)"

                    #implement the query
                    cursor.execute(query, (self.name, self.description, self.category))
                    conn.commit()
                    print("Work out session successfully added to the calender")

                # close cursor and connection
                finally:
                    cursor.close()
                    conn.close()

    def view_genre_details(self,name):
        name = input("Please enter the name of the genre you wish to view: ")
        if name in Genre.genres:
            genre_details = Genre.genres[name]
            print(f"\nGenre: {name}")
            for key, value in genre_details.items():
                print(f"{key}: {value}")
        else:
            print("this genre is not recognized please try again.")

    def view_all_genres(self):    
        if self.genres:
            for name, details in self.genres.items():
                print (f"\ngenre: {name}")
                print(', '.join(f"{key}: {value}" for key, value in details.items()))
                print("")       
        else:
            print("\nThere are currently no genres\n")

    def save_genres_info(self, saved_genres):
        with open(saved_genres, 'w') as file:
            for name, details in self.genres.items():
                file.write(f"{name}, {details['Description']}, {details['Category']} \n")
        print(f"Genre information has been saved to {saved_genres}")

    def load_genres(self):
        try:
            with open('Saved_genre.txt', 'r') as file:
                for line in file:
                    name, description, category = line.strip().split(', ')
                    self.genres[name] = {
                        "Description": description,
                        "Category": category,
                    }
        except FileNotFoundError:
            pass
        except Exception as e:
            print(f"\nAn error occurred: {e}\n") 