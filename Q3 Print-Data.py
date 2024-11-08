import sqlite3

def print_all_questions(db_file):
    # Connect to the SQLite database
    with sqlite3.connect(db_file) as conn:
        cursor = conn.cursor()

        # Retrieve all table names in the database
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()

        # Loop through each table and print all questions
        for table in tables:
            table_name = table[0]
            print(f"\nQuestions in course: {table_name}\n" + "-" * 40)

            # Query all question data from the current table
            try:
                cursor.execute(f"SELECT question, option_a, option_b, option_c, option_d, correct_answer FROM {table_name};")
                questions_data = cursor.fetchall()

                # Print each question with its options and correct answer
                for index, (question, option_a, option_b, option_c, option_d, correct_answer) in enumerate(questions_data, start=1):
                    print(f"Question {index}: {question}")
                    print(f"    A: {option_a}")
                    print(f"    B: {option_b}")
                    print(f"    C: {option_c}")
                    print(f"    D: {option_d}")
                    print(f"    Correct Answer: {correct_answer}\n")

            except sqlite3.Error as e:
                print(f"Error reading questions from table '{table_name}': {e}")

# Specify the database file
db_file = 'Q3_quiz.db'
print_all_questions(db_file)
