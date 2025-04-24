from library_manager import LibraryManager

def print_menu():
    """
    Display the available options to the user.
    """
    print("\nLibrary Management System")
    print("1. Add a new book")
    print("2. View all books")
    print("3. Search for a book")
    print("4. Update availability (borrow/return)")
    print("5. Delete a book")
    print("6. Exit")

def main():
    manager = LibraryManager()

    while True:
        print_menu()
        choice = input("Select an option (1-6): ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter author: ")
            year = int(input("Enter publication year: "))
            manager.add_book(title, author, year)
            print("Book added successfully!")

        elif choice == '2':
            books = manager.list_books()
            for book in books:
                print(book)

        elif choice == '3':
            keyword = input("Enter keyword (title or author): ")
            results = manager.search_books(keyword)
            if results:
                for book in results:
                    print(book)
            else:
                print("No books found.")

        elif choice == '4':
            book_id = int(input("Enter book ID: "))
            status = input("Is the book available? (yes/no): ").lower()
            is_available = True if status == "yes" else False
            manager.update_availability(book_id, is_available)
            print("Book availability updated.")

        elif choice == '5':
            book_id = int(input("Enter book ID to delete: "))
            manager.delete_book(book_id)
            print("Book deleted.")

        elif choice == '6':
            manager.close()
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please choose from 1 to 6.")

if __name__ == "__main__":
    main()