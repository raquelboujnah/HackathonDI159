
class Book:
    def __init__(self, id, title, author, year, available=True):
        """
        Initialize a Book object.

        :param id: Unique ID of the book (from the database)
        :param title: Title of the book
        :param author: Author of the book
        :param year: Year of publication
        :param available: Availability status (True if the book is available)
        """
        self.id = id
        self.title = title
        self.author = author
        self.year = year
        self.available = available

    def __str__(self):
        """
        Return a string representation of the book object.
        """
        status = "Available" if self.available else "Not available"
        return f"{self.id} - {self.title} by {self.author} ({self.year}) [{status}]"