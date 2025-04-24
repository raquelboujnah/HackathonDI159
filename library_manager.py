from database import get_connection
from book import Book

class LibraryManager:
    def __init__(self):
        """
        Initialize the database connection and cursor.
        """
        self.conn = get_connection()
        self.cur = self.conn.cursor()

    def add_book(self, title, author, year):
        """
        Add a new book to the database.
        :param title: Book title
        :param author: Book author
        :param year: Year of publication
        """
        self.cur.execute(
            "INSERT INTO books (title, author, year) VALUES (%s, %s, %s)",
            (title, author, year)
        )
        self.conn.commit()

    def list_books(self):
        """
        Retrieve all books from the database.
        :return: List of Book objects
        """
        self.cur.execute("SELECT * FROM books ORDER BY id")
        rows = self.cur.fetchall()
        return [Book(*row) for row in rows]

    def search_books(self, keyword):
        """
        Search for books by title or author.
        :param keyword: String to search in title or author
        :return: List of Book objects matching the keyword
        """
        self.cur.execute(
            "SELECT * FROM books WHERE title ILIKE %s OR author ILIKE %s",
            (f"%{keyword}%", f"%{keyword}%")
        )
        rows = self.cur.fetchall()
        return [Book(*row) for row in rows]

    def update_availability(self, book_id, is_available):
        """
        Update the availability status of a book.
        :param book_id: ID of the book
        :param is_available: Boolean status
        """
        self.cur.execute(
            "UPDATE books SET available = %s WHERE id = %s",
            (is_available, book_id)
        )
        self.conn.commit()

    def delete_book(self, book_id):
        """
        Delete a book from the database by its ID.
        :param book_id: ID of the book to delete
        """
        self.cur.execute("DELETE FROM books WHERE id = %s", (book_id,))
        self.conn.commit()

    def close(self):
        """
        Properly close the database connection and cursor.
        """
        self.cur.close()
        self.conn.close()