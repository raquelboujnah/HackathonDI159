from library_manager import LibraryManager

def seed_books():
    manager = LibraryManager()

    books = [
        ("1984", "George Orwell", 1949),
        ("To Kill a Mockingbird", "Harper Lee", 1960),
        ("The Great Gatsby", "F. Scott Fitzgerald", 1925),
        ("Brave New World", "Aldous Huxley", 1932),
        ("The Catcher in the Rye", "J.D. Salinger", 1951),
        ("Moby-Dick", "Herman Melville", 1851),
        ("Pride and Prejudice", "Jane Austen", 1813),
        ("Jane Eyre", "Charlotte Brontë", 1847),
        ("Wuthering Heights", "Emily Brontë", 1847),
        ("The Hobbit", "J.R.R. Tolkien", 1937),
        ("Fahrenheit 451", "Ray Bradbury", 1953),
        ("The Lord of the Rings", "J.R.R. Tolkien", 1954),
        ("The Chronicles of Narnia", "C.S. Lewis", 1950),
        ("Animal Farm", "George Orwell", 1945),
        ("A Tale of Two Cities", "Charles Dickens", 1859),
        ("The Picture of Dorian Gray", "Oscar Wilde", 1890),
        ("Crime and Punishment", "Fyodor Dostoevsky", 1866),
        ("War and Peace", "Leo Tolstoy", 1869),
        ("The Brothers Karamazov", "Fyodor Dostoevsky", 1880),
        ("Dracula", "Bram Stoker", 1897),
        ("The Alchemist", "Paulo Coelho", 1988),
        ("The Little Prince", "Antoine de Saint-Exupéry", 1943),
        ("Les Misérables", "Victor Hugo", 1862),
        ("Don Quixote", "Miguel de Cervantes", 1605),
        ("The Divine Comedy", "Dante Alighieri", 1320),
        ("Frankenstein", "Mary Shelley", 1818),
        ("Slaughterhouse-Five", "Kurt Vonnegut", 1969),
        ("The Old Man and the Sea", "Ernest Hemingway", 1952),
        ("Of Mice and Men", "John Steinbeck", 1937),
        ("Beloved", "Toni Morrison", 1987)
    ]

    for title, author, year in books:
        manager.add_book(title, author, year)

    manager.close()
    print("30 sample books inserted into the database.")

if __name__ == "__main__":
    seed_books()