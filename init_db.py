from database import get_connection

def create_books_table():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id SERIAL PRIMARY KEY,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            year INTEGER,
            available BOOLEAN DEFAULT TRUE
        );
    """)

    conn.commit()
    cur.close()
    conn.close()
    print("Books table created successfully.")

if __name__ == "__main__":
    create_books_table()