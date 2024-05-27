from Database_Connection import connect_database
import Author_Functions
import Book_Functions
import Genre_Functions
import User_Functions
menu_selection = ''
user_selection = ''
while True:
    print("\nHello welcome to the Library Management System with Database Intergration\n1. Book menu\n2. User menu\n3. Author menu\n4. Genre menu\n5. Quit")

    menu_selection = input("please select an option by number: ")

    book_selection = ''
    while True:
        conn = connect_database()
        if conn is not None:
            try:
                cursor = conn.cursor()
                # implement book class
                if menu_selection == '1':
                    print("\nBook Menu\n1. add book\n2. borrow book.\n3. return book.\n4. Search for a specific book\n5. view all books\n6. back to main menu")
                    book_selection = input("please select an option by number: ")
                    
                    if book_selection == '1':
                        add = Book_Functions.Book("title", "author_id", "genre_id", "isbn", "publication_date", "availablility")
                        add.add_book(cursor)
                    elif book_selection == '2':
                        check_out = Book_Functions.Book("title", "author_id", "genre_id", "isbn", "publication_date", "availablility")
                        check_out.check_out(cursor)
                    elif book_selection == '3':
                        return_book = Book_Functions.Book("title", "author_id", "genre_id", "isbn", "publication_date", "availablility")
                        return_book.return_book(cursor)
                    elif book_selection == '4':
                        search = Book_Functions.Book("title", "author_id", "genre_id", "isbn", "publication_date", "availablility")
                        search.search_book(cursor)
                    elif book_selection == '5':
                        view_all = Book_Functions.Book("title", "author_id", "genre_id", "isbn", "publication_date", "availablility")
                        view_all.view_all_books(cursor)
                    else:
                        break

                # implement user class
                elif menu_selection == '2':
                    print("\nUser Menu\n1.Add user\n2.Search user\n3.View all users\n4.back to main menu")
                    user_selection = input("Please select an option by number: ")

                    if user_selection == '1':
                        add = User_Functions.User("name", "library_id")
                        add.add_user(cursor)
                    elif user_selection == '2':
                        view = User_Functions.User("name", "library_id")
                        view.view_user(cursor)
                    elif user_selection == '3':
                        view_all = User_Functions.User("name", "library_id")
                        view_all.view_all_users(cursor)
                    elif user_selection == '4':
                        break
                
                # implement author class
                elif menu_selection == '3':
                    print("\nAuthor Menu\n1.Add author\n2.view author details\n3.View all authors\n4.back to main menu")
                    author_selection = input("Please select an option by number: ")
                    # import author methods
                    if author_selection == '1':
                        add = Author_Functions.Author("name", "biography")
                        add.add_Author(cursor)
                    elif author_selection == '2':
                        view = Author_Functions.Author("name", "biography")
                        view.view_author(cursor)
                    elif author_selection == '3':
                        view_all = Author_Functions.Author("name", "biography")
                        view_all.add_Author(cursor)
                    elif author_selection == '4':
                        break

                # implement genre methods
                elif menu_selection == '4':
                    # loads genre info
                    print("\nGenre Menu\n1.Add Genre\n2.Search Genre\n3.View all Genres\n4.back to main menu")
                    genre_selection = input("Please select an option by number: ")
                    if genre_selection == '1':
                        add = Genre_Functions.Genre("name", "description", "category")
                        add.add_genre(cursor)
                    elif genre_selection == '2':
                        view = Genre_Functions.Genre("name", "description", "category")
                        view.view_genre(cursor)
                    elif genre_selection == '3':
                        view_all = Genre_Functions.Genre("name", "description", "category")
                        view_all.add_genre(cursor)
                    elif genre_selection == '4':
                        break
                
                elif menu_selection == '5':
                    break
                
                conn.commit()
            
            
            finally:
                cursor.close()
                conn.close()
            