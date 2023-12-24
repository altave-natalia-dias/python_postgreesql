import psycopg2

def create_connection():
    try:
        # Establishing the connection
        conn = psycopg2.connect(
            database="postgres",
            user='postgres',
            password='password',
            host='localhost',
            port='5432'
        )
        return conn
    except psycopg2.Error as e:
        print(f"Error connecting to the database: {e}")
        raise

def fetch_and_print_records(cursor, sql):
    try:
        # Executing the query
        cursor.execute(sql)
        
        # Fetching and printing the results
        records = cursor.fetchall()
        print(records)
        
    except psycopg2.Error as e:
        print(f"Error executing query: {e}")
        raise

def search_records_by_state(cursor, state):
    # Feature 2: Search Records by State
    sql = f"SELECT * FROM employee WHERE state = '{state}';"
    fetch_and_print_records(cursor, sql)

def main():
    # Creating a connection and cursor
    conn = create_connection()
    cursor = conn.cursor()

    try:
        # Feature 2: Search Records by State
        user_state = input("Feature 2: Enter a state to search records: ")
        print(f"Searching records in state '{user_state}'")
        search_records_by_state(cursor, user_state)

    finally:
        # Closing the cursor and connection
        cursor.close()
        conn.close()

if __name__ == "__main__":
    main()
