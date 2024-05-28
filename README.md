Hello and welcome to the Library Management System with Database Intergration appliction. This code is seperated into seperate files each holding their own class for a specific function.
The file labled Main.py is where you will run the code. The terminal will then promt you with various options such as book menu, author menu, user menu, genre menu and Quit. you will be asked to select a menu by number.
once selecting you will once again be prompted with several options. From here you can select an action and enter new information into the database or retrieve data to view. at 

Book Menu: When selecting an option from the book menu the Book_Functions.py folder will be accessed and the relevant function will be ran to make changes or pull data from the Library Management Database.
1. Add book - By selecting this action you will be asked to provide the book title, author id, genre id, ISBN and a publication date.
  The information will then be added to the Library Management database in the books table. The availability of the book will automatically be set to a boolean value of true.
2. borrow book - By selecting this action you will be asked to provide the book title. The information will then be altered and the boolean value of the availabilty will then be set to false showing the book has been checked out.
   Lastly you will be presented with a due date for the book. 2 weeks from when you checked it out.
3. Return book - By selecting this action you will be asked to provide the book title. The information will then be altered in the Library Management database for this book and will change the boolean value of availability back to true.
   The function will then provide you with any late fees that may have occured.
4. Search for a specific book -  By selecting this action you will be asked to provide the book title. The information for the book will then be pulled from the library management database and displayed
5. View all books -  By selecting this action, all the columns in the Book table will be pulled from the database and will be displayed.
6. Back to Main Menu -  This action will return you to the previous Main Menu

User Menu: When selecing an option from this menu the User_Functions.py folder will be accessed and the relevant function will be ran to make changes or pull data from the Library Management Database. 
1. Add User -  By selecting this action you will be asked to provide a Username and New Library id. the information will then be added to the Library Management database in the Users table.
2. Search for a specific user -  By selecting this action you will be asked to provide the User name. The information for the book will then be pulled from the library management database and displayed
3. View all users -  By selecting this action, all the columns in the users table will be pulled from the database and will be displayed.
4. Back to Main Menu -  This action will return you to the previous Main Menu

Author Menu: When selecing an option from this menu the Author_Functions.py folder will be accessed and the relevant function will be ran to make changes or pull data from the Library Management Database. 
1. Add Author -  By selecting this action you will be asked to provide the authors name and a brief biography of the author. the information will then be added to the Library Management database in the Authors table.
2. Search for a specific Author -  By selecting this action you will be asked to provide the Auhtors name. The information for the book will then be pulled from the library management database and displayed
3. View all Authors -  By selecting this action, all the columns in the authors table will be pulled from the database and will be displayed.
4. Back to Main Menu -  This action will return you to the previous Main Menu

Genre Menu: When selecing an option from this menu the Genres_Functions.py folder will be accessed and the relevant function will be ran to make changes or pull data from the Library Management Database. 
1. Add Genre -  By selecting this action you will be asked to provide a Genre name, a brief discription and a category (Fiction or Non-Fiction). the information will then be added to the Library Management database in the genre table.
2. Search for a specific Genre -  By selecting this action you will be asked to provide the genre name. The information for the book will then be pulled from the library management database and displayed
3. View all Genre -  By selecting this action, all the columns in the users table will be pulled from the database and will be displayed.
4. Back to Main Menu -  This action will return you to the previous Main Menu

Quit: by selecting Quit you will exit the program.
