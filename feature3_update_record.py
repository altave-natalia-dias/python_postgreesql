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

def update_record_state(cursor, record_id, new_state):
    # Feature 3: Update Record
    try:
        # Updating the state of a specific record
        update_sql = "UPDATE employee SET state = %s WHERE id = %s;"
        cursor.execute(update_sql, (new_state, record_id))
        print("Record updated successfully...")
        
    except psycopg2.Error as e:
        print(f"Error updating record: {e}")
        raise

def main():
    # Creating a connection and cursor
    conn = create_connection()
    cursor = conn.cursor()

    try:
        # Feature 3: Update Record
        user_record_id = input("Feature 3: Enter the ID of the record to update: ")
        user_new_state = input("Enter the new state for the record: ")
        update_record_state(cursor, user_record_id, user_new_state)

        # Committing changes to the database
        conn.commit()

    finally:
        # Closing the cursor and connection
        cursor.close()
        conn.close()

if __name__ == "__main__":
    main()
