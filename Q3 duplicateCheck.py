import sqlite3

def print_table_schema(cursor):
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    
    print("Table schemas:")
    for table in tables:
        table_name = table[0]
        if table_name == "sqlite_sequence":
            continue  # Skip sqlite_sequence table

        print(f"\nSchema for table: {table_name}")
        cursor.execute(f"PRAGMA table_info({table_name});")
        columns = cursor.fetchall()
        for column in columns:
            print(f"- Column: {column[1]}, Type: {column[2]}")

def has_question_column(cursor, table_name):
    cursor.execute(f"PRAGMA table_info({table_name});")
    columns = cursor.fetchall()
    return any(column[1] == 'question' for column in columns)

def check_for_duplicates_and_remove(db_file):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    print_table_schema(cursor)

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    question_tracker = {}

    for table in tables:
        table_name = table[0]
        
        # Skip the sqlite_sequence table
        if table_name == "sqlite_sequence":
            print(f"Skipping internal table '{table_name}'.")
            continue

        if has_question_column(cursor, table_name):
            cursor.execute(f"SELECT rowid, question FROM {table_name};")
            rows = cursor.fetchall()

            for row in rows:
                row_id, question_text = row
                if question_text in question_tracker:
                    question_tracker[question_text].append((table_name, row_id))
                else:
                    question_tracker[question_text] = [(table_name, row_id)]
        else:
            print(f"Skipping table '{table_name}' - no 'question' column found.")

    for question, occurrences in question_tracker.items():
        for table_name, row_id in occurrences[1:]:
            print(f"Deleting duplicate question in table '{table_name}': {question}")
            cursor.execute(f"DELETE FROM {table_name} WHERE rowid = ?", (row_id,))

    conn.commit()
    conn.close()
    print("\nDuplicate questions removed (if any).")

# Specify the database file
db_file = 'Q3_quiz.db'
check_for_duplicates_and_remove(db_file)
