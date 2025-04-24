import psycopg2

def get_connection():
    """
    Create and return a connection to the PostgreSQL database.

    Update the parameters with your actual database credentials:
    - dbname: The name of your PostgreSQL database
    - user: Your PostgreSQL username
    - password: Your PostgreSQL password
    - host: Usually 'localhost' if running locally
    - port: Default PostgreSQL port is 5432

    :return: psycopg2 connection object
    """
    return psycopg2.connect(
        dbname="library_db",        # Change to your DB name if needed
        user="postgres",       # Replace with your PostgreSQL username
        password="nabilfekir",   # Replace with your PostgreSQL password
        host="localhost",
        port="5432"
    )
