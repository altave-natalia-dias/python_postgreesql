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

def sort_records_by_name(cursor):
    # Feature 1: Sort Records by Name
    sql = 'SELECT * FROM employee ORDER BY name;'
    fetch_and_print_records(cursor, sql)

def main():
    # Creating a connection and cursor
    conn = create_connection()
    cursor = conn.cursor()

    try:
        # Feature 1: Sort Records by Name
        print("Feature 1: Sorting records by name")
        sort_records_by_name(cursor)

    finally:
        # Closing the cursor and connection
        cursor.close()
        conn.close()

if __name__ == "__main__":
    main()
