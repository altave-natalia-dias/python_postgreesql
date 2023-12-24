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

def create_table(cursor):
    try:
        # Creating a table
        sql = '''
            CREATE TABLE IF NOT EXISTS employee(
                id SERIAL PRIMARY KEY,
                name VARCHAR(20) NOT NULL,
                state VARCHAR(20) NOT NULL
            )
        '''
        cursor.execute(sql)
        print("Table 'employee' created successfully...")
    except psycopg2.Error as e:
        print(f"Error creating table: {e}")
        raise

def insert_records(cursor, data):
    try:
        # Inserting records into the employee table
        for record in data:
            cursor.execute("INSERT INTO employee(name, state) VALUES (%s, %s)", record)
        print("Records have been inserted into the 'employee' table successfully...")
    except psycopg2.Error as e:
        print(f"Error inserting records: {e}")
        raise

def main():
    # Creating a connection and cursor
    conn = create_connection()
    cursor = conn.cursor()

    try:
        # Creating table if not exists
        create_table(cursor)

        # List containing records to be inserted into the table
        data = [('Babita', 'Bihar'), ('Anushka', 'Hyderabad'), 
                ('Anamika', 'Bangalore'), ('Sanaya', 'Pune'),
                ('Radha', 'Chandigarh')]

        # Inserting records into the table
        insert_records(cursor, data)

        # Committing changes to the database
        conn.commit()

    finally:
        # Closing the cursor and connection
        cursor.close()
        conn.close()

if __name__ == "__main__":
    main()
