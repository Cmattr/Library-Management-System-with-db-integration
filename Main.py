import Library

menu_selection = ''
user_selection = ''
while True:
    print("\nHello welcome to the Library Management System with Database Intergration\n1. Book menu\n2. User menu\n3. Author menu\n4. Genre menu\n5. Quit")

    menu_selection = input("please select an option by number: ")

    book_selection = ''
    while True:

        # implement book class
        if menu_selection == '1':
            # load book info
            load = Library.Book("title", "author", "isbn", "genre", "date", "status")
            load.load_books()
            print("\nBook Menu\n1. add book\n2. borrow book.\n3. return book.\n4. Search for a specific book\n5. view all books\n6. view borrowed books\n7. Save to txt file\n8. back to main menu")
            book_selection = input("please select an option by number: ")
            # import book methods
            if book_selection == '1':
                add = Library.Book("title", "author", "isbn", "genre", "date", "status" )
                add.add_book()
            elif book_selection == '2':
                borrow = Library.Book("title", "author", "isbn", "genre", "date", "status" )
                borrow.borrow_book("title")
            elif book_selection == '3':
                returned = Library.Book("title", "author", "isbn", "genre", "date", "status" )
                returned.return_book("title")
            elif book_selection == '4':
                Look_up = Library.Book("title", "author", "isbn", "genre", "date", "status" )
                Look_up.search("title")
            elif book_selection == '5':
                view = Library.Book("title", "author", "isbn", "genre", "date", "status" )
                view.view_books()
            elif book_selection == '6':
                view_borrowed = Library.Book("title", "author", "isbn", "genre", "date", "status" )
                view_borrowed.view_borrowed_books()
            elif book_selection == '7':
                save = Library.Book("title", "author", "isbn", "genre", "date", "status")
                save.save_book_info("Saved_books.txt")
            elif book_selection == '8':
                break

        # implement user class
        elif menu_selection == '2':
            # load user info
            load = Library.User("name", "library_id")
            load.load_users()
            print("\nUser Menu\n1.Add user\n2.Search user\n3.View all users\n4.save to txt file\n5.back to main menu")
            user_selection = input("Please select an option by number: ")
            # import user methods
            if user_selection == '1':
                add = Library.User("name", "library_id")
                add.add_user()
            elif user_selection == '2':
                view = Library.User("name", "library_id")
                view.view_user_details()
            elif user_selection == '3':
                view_all = Library.User("name", "library_id")
                view_all.view_all_users()
            elif user_selection == '4':
                save = Library.User("name", "library_id")
                save.save_user_info("saved_users.txt")
            elif user_selection == '5':
                break
        
        # implement author class
        elif menu_selection == '3':
            # load author info
            load = Library.Author("author_id", "biography")
            load.load_authors()
            print("\nAuthor Menu\n1.Add author\n2.Search author\n3.View all authors\n4.save to txt file\n5.back to main menu")
            author_selection = input("Please select an option by number: ")
            # import author methods
            if author_selection == '1':
                add = Library.Author("author_id", "biography")
                add.add_author()
            elif author_selection == '2':
                view = Library.Author("author_id", "biography")
                view.view_authors_details('name')
            elif author_selection == '3':
                view_all = Library.Author("author_id", "biography")
                view_all.view_all_authors()
            elif author_selection == '4':
                save = Library.Author("name", "Biography")
                save.save_author_info("Saved_Author.txt")
            elif author_selection == '5':
                break

        # implement genre methods
        elif menu_selection == '4':
            # loads genre info
            load = Library.Genre('name', 'description', 'category')
            load.load_genres()
            print("\nGenre Menu\n1.Add Genre\n2.Search Genre\n3.View all Genres\n4.save to txt file\n5.back to main menu")
            genre_selection = input("Please select an option by number: ")
            # import genre methods
            if genre_selection == '1':
                add = Library.Genre("name", "description", "category")
                add.add_genre()
            elif genre_selection == '2':
                view = Library.Genre("name", "description", "category")
                view.view_genre_details('name')
            elif genre_selection == '3':
                view_all = Library.Genre("name", "description", "category")
                view_all.view_all_genres()
            elif genre_selection == '4':
                save = Library.Genre("name", "description", "category")
                save.save_genres_info("Saved_genre.txt")
            elif genre_selection == '5':
                break
        
        elif menu_selection == '5':
            break
        