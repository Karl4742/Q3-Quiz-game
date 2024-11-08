

import sqlite3

# Define allowed course names to prevent SQL injection
ALLOWED_COURSES = {"Mathematics", "Astronomy", "History", "Geography", "Literature"}

def create_course_tables():
    with sqlite3.connect('Q3_quiz.db') as conn:
        cursor = conn.cursor()

        # Define the generic SQL command to create a course table
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS {} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT NOT NULL,
            option_a TEXT NOT NULL,
            option_b TEXT NOT NULL,
            option_c TEXT NOT NULL,
            option_d TEXT NOT NULL,
            correct_answer TEXT NOT NULL,
            feedback TEXT
        );
        """

        # Create each course table by safely formatting table names
        for course in ALLOWED_COURSES:
            cursor.execute(create_table_sql.format(course))

        conn.commit()
        print("All course tables created successfully.")

def add_question(course, question, options, correct_answer, feedback):
    if course not in ALLOWED_COURSES:
        raise ValueError("Invalid course name provided.")

    # Use parameterized queries to avoid SQL injection
    with sqlite3.connect('Q3_quiz.db') as conn:
        cursor = conn.cursor()
        cursor.execute(f"""
            INSERT INTO {course} (question, option_a, option_b, option_c, option_d, correct_answer, feedback)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (question, options['A'], options['B'], options['C'], options['D'], correct_answer, feedback))
        conn.commit()

def remove_question(course, question_id):
    if course not in ALLOWED_COURSES:
        raise ValueError("Invalid course name provided.")

    # Use parameterized queries to avoid SQL injection
    with sqlite3.connect('Q3_quiz.db') as conn:
        cursor = conn.cursor()
        cursor.execute(f"DELETE FROM {course} WHERE id=?", (question_id,))
        conn.commit()

def get_questions(course):
    if course not in ALLOWED_COURSES:
        raise ValueError("Invalid course name provided.")

    # Use parameterized queries to avoid SQL injection
    with sqlite3.connect('Q3_quiz.db') as conn:
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {course}")
        return cursor.fetchall()

create_course_tables()

# Add questions to each course (ensuring tables exist beforehand)
try:
    #course 1 == math course
    add_question(
        course="Mathematics",
        question="What is 5 + 7?",
        options={"A": "10", "B": "12", "C": "15", "D": "11"},
        correct_answer="B",
        feedback="Adding 5 and 7 gives 12."
    )#1

    add_question(
        course="Mathematics",
        question="What is 5 * 5?",
        options={"A": "10", "B": "15", "C": "20", "D": "25"},
        correct_answer="D",
        feedback="5 multiplied by 5 is 25."
    )#2

    add_question(
        course="Mathematics",
        question="What is 4 / 2?",
        options={"A": "2", "B": "4.5", "C": "4", "D": "-4"},
        correct_answer="A",
        feedback="4 divided by 2 is equal to 2."
    )#3

    add_question(
        course="Mathematics",
        question="What is 2^2 or 2 squared?",
        options={"A": "2", "B": "3", "C": "4", "D": "400"},
        correct_answer="C",
        feedback="2 times itself is 4."
    )#4

    add_question(
        course="Mathematics",
        question="What is 4^2 or 4 squared?",
        options={"A": "2", "B": "4", "C": "8", "D": "16"},
        correct_answer="D",
        feedback="4 times itself is 16."
    )#5

    add_question(
        course="Mathematics",
        question="What is 3^3 or 3 cubed?",
        options={"A": "3", "B": "9", "C": "27", "D": "81"},
        correct_answer="C",
        feedback="3 * 3 * 3 is 27."
    )#6

    add_question(
        course="Mathematics",
        question="What is 5^3 or 5 cubed?",
        options={"A": "125", "B": "120", "C": "200", "D": "15"},
        correct_answer="A",
        feedback="5 * 5 * 5 is 125."
    )#7

    add_question(
        course="Mathematics",
        question="What is 10^3 or 10 cubed?",
        options={"A": "10", "B": "30", "C": "500", "D": "1000"},
        correct_answer="D",
        feedback="10 * 10 * 10 is 1000."
    )#8

    add_question(
        course="Mathematics",
        question="What is the squareroot of 25?",
        options={"A": "0", "B": "5", "C": "20", "D": "1"},
        correct_answer="B",
        feedback="5 times itself is 25 so when you reverse it you get the squareroot."
    )#9

    add_question(
        course="Mathematics",
        question="what is MOD(| 0 + 6 |)?",
        options={"A": "0", "B": "3", "C": "6", "D": "12"},
        correct_answer="C",
        feedback="Modulo we are taking the remainder when doing math."
    )#10


    #Course 2 == Astronomy 
    add_question(
        course="Astronomy",
        question="What planet is known as the Red Planet?",
        options={"A": "Earth", "B": "Mars", "C": "Jupiter", "D": "Saturn"},
        correct_answer="B",
        feedback="Mars is known as the Red Planet."
    )#1

    add_question(
        course="Astronomy",
        question="What is the hottest planet in the solar system",
        options={"A": "Mercury", "B": "Earth", "C": "Venus", "D": "Mars"},
        correct_answer="C",
        feedback="Venus is a average of 870°F (465°C)"
    )#2

    add_question(
        course="Astronomy",
        question="What type of galaxy is the milky way?",
        options={"A": "Seyfert galaxy", "B": "Irregular galaxy", "C": "Elliptical galaxy", "D": "Spiral galaxy"},
        correct_answer="D",
        feedback="The milky way is a large barred spiral galaxy."
    )#3

    add_question(
        course="Astronomy",
        question="Which dwarf planet is the furthest from the sun",
        options={"A": "Pluto", "B": "Eris", "C": "Ceres", "D": "Makemake"},
        correct_answer="B",
        feedback="Eris is a staggering 68 AU or 6.3 billion miles from the sun"
    )#4

    add_question(
        course="Astronomy",
        question="Where are stars born?",
        options={"A": "Nebulae", "B": "Black holes", "C": "Pulsars", "D": "Stars are never made they just exist"},
        correct_answer="A",
        feedback="Nebulae are giant clouds of closely packed matter that over time can coalesce into a star"
    )#5

    add_question(
        course="Astronomy",
        question="What does dark energy do?",
        options={"A": "Pulls every thing together", "B": "makes things dark", "C": "Pushes matter apart", "D": "nothing, you made up dark energy"},
        correct_answer="C",
        feedback="Dark energy is the invisible force that is thought to expand at an accelerating rate essentially pushing things apart"
    )#6

    add_question(
        course="Astronomy",
        question="Which planet in the solar system has the largest mountain?",
        options={"A": "Mercury", "B": "Venus", "C": "Earth", "D": "Mars"},
        correct_answer="D",
        feedback="Olympus Mons on Mars is 16 miles high which is 3 times higher than Mt. Everest."
    )#7

    add_question(
        course="Astronomy",
        question="As a star ages if fuses denser and denser elements, what element do stars stop at?",
        options={"A": "hydrogen", "B": "Lithium", "C": "Iron", "D": "Uranium"},
        correct_answer="C",
        feedback="Stars stop at iron fusion since it endothermic meaning requires more energy than it releases."
    )#8

    add_question(
        course="Astronomy",
        question="What is the brightest things is the universe?",
        options={"A": "Super massive stars", "B": "Quasars", "C": "Neutron stars", "D": "Pulsars"},
        correct_answer="B",
        feedback="Quasars are fueled by supermassive black holes and produce light brighter than galaxies."
    )#9

    add_question(
        course="Astronomy",
        question="What is the next closest star to Earth?",
        options={"A": "Proxima Centauri", "B": "Barnard's Star", "C": "Ross 128", "D": "Earendel"},
        correct_answer="A",
        feedback="Proxima Centauri is 4.2 light years away from us, or in miles 25,300,000,000,000 miles away."
    )#10


    #course 3 == History
    add_question(
        course="History",
        question="Who was the first president of the United States?",
        options={"A": "Thomas Jefferson", "B": "Abraham Lincoln", "C": "George Washington", "D": "John Adams"},
        correct_answer="C",
        feedback="George Washington was the first U.S. president."
    )#1

    add_question(
    course="History",
    question="In what year did World War II end?",
    options={"A": "1945", "B": "1939", "C": "1950", "D": "1940"},
    correct_answer="A",
    feedback="World War II ended in 1945."
    )#2

    add_question(
        course="History",
        question="Who wrote the Declaration of Independence?",
        options={"A": "Benjamin Franklin", "B": "Thomas Jefferson", "C": "George Washington", "D": "John Adams"},
        correct_answer="B",
        feedback="Thomas Jefferson is credited with writing the Declaration of Independence."
    )#3

    add_question(
        course="History",
        question="Which country was the first to land a man on the moon?",
        options={"A": "USA", "B": "Russia", "C": "China", "D": "Germany"},
        correct_answer="A",
        feedback="The United States was the first to land a man on the moon in 1969 during the Apollo 11 mission."
    )#4

    add_question(
        course="History",
        question="Who was the leader of Nazi Germany during World War II?",
        options={"A": "Adolf Hitler", "B": "Joseph Stalin", "C": "Winston Churchill", "D": "Benito Mussolini"},
        correct_answer="A",
        feedback="Adolf Hitler was the leader of Nazi Germany during World War II."
    )#5

    add_question(
        course="History",
        question="What ancient civilization built the pyramids?",
        options={"A": "Romans", "B": "Greeks", "C": "Egyptians", "D": "Mayans"},
        correct_answer="C",
        feedback="The ancient Egyptians are known for building the pyramids."
    )#6

    add_question(
        course="History",
        question="Which event triggered the start of World War I?",
        options={"A": "The bombing of Pearl Harbor", "B": "The assassination of Archduke Franz Ferdinand", "C": "The signing of the Treaty of Versailles", "D": "The D-Day invasion"},
        correct_answer="B",
        feedback="The assassination of Archduke Franz Ferdinand in 1914 triggered World War I."
    )#7

    add_question(
        course="History",
        question="Who was the first female prime minister of the United Kingdom?",
        options={"A": "Margaret Thatcher", "B": "Queen Elizabeth II", "C": "Theresa May", "D": "Eleanor Roosevelt"},
        correct_answer="A",
        feedback="Margaret Thatcher was the first female prime minister of the United Kingdom."
    )#8

    add_question(
        course="History",
        question="What was the name of the ship that carried the Pilgrims to America in 1620?",
        options={"A": "Mayflower", "B": "Santa Maria", "C": "The Endeavour", "D": "The Beagle"},
        correct_answer="A",
        feedback="The Mayflower was the ship that carried the Pilgrims to America in 1620."
    )#9

    add_question(
        course="History",
        question="Which U.S. president delivered the Gettysburg Address?",
        options={"A": "Abraham Lincoln", "B": "George Washington", "C": "Thomas Jefferson", "D": "Franklin D. Roosevelt"},
        correct_answer="A",
        feedback="Abraham Lincoln delivered the Gettysburg Address on November 19, 1863."
    )#10


    add_question(   #geography
        course="Geography",
        question="What is the largest continent?",
        options={"A": "Africa", "B": "Asia", "C": "Europe", "D": "Antarctica"},
        correct_answer="B",
        feedback="Asia is the largest continent by land area."
    )#1

    add_question(  #geography
    course="Geography",
    question="Which country has the most population in the world?",
    options={"A": "India", "B": "China", "C": "United States", "D": "Indonesia"},
    correct_answer="B",
    feedback="China has the largest population in the world."
    )#2

    add_question(  #geography
        course="Geography",
        question="Which river is the longest in the world?",
        options={"A": "Amazon River", "B": "Nile River", "C": "Yangtze River", "D": "Mississippi River"},
        correct_answer="B",
        feedback="The Nile River is traditionally considered the longest river in the world."
    )#3

    add_question(  #geography
        course="Geography",
        question="Which ocean is the largest by area?",
        options={"A": "Atlantic Ocean", "B": "Indian Ocean", "C": "Southern Ocean", "D": "Pacific Ocean"},
        correct_answer="D",
        feedback="The Pacific Ocean is the largest ocean by area."
    )#4

    add_question(  #geography
        course="Geography",
        question="Which country is known as the Land of the Rising Sun?",
        options={"A": "China", "B": "South Korea", "C": "Japan", "D": "India"},
        correct_answer="C",
        feedback="Japan is known as the Land of the Rising Sun."
    )#5

    add_question(  #geography
        course="Geography",
        question="What is the capital of Australia?",
        options={"A": "Sydney", "B": "Melbourne", "C": "Canberra", "D": "Brisbane"},
        correct_answer="C",
        feedback="The capital of Australia is Canberra."
    )#6

    add_question(  #geography
        course="Geography",
        question="Which desert is the largest in the world?",
        options={"A": "Sahara Desert", "B": "Gobi Desert", "C": "Kalahari Desert", "D": "Antarctic Desert"},
        correct_answer="D",
        feedback="The Antarctic Desert is the largest desert in the world."
    )#7

    add_question(  #geography
        course="Geography",
        question="What is the smallest country in the world?",
        options={"A": "Monaco", "B": "Vatican City", "C": "San Marino", "D": "Liechtenstein"},
        correct_answer="B",
        feedback="Vatican City is the smallest country in the world."
    )#8

    add_question(  #geography
        course="Geography",
        question="Which continent is entirely located in the Southern Hemisphere?",
        options={"A": "Africa", "B": "South America", "C": "Australia", "D": "Antarctica"},
        correct_answer="D",
        feedback="Antarctica is the only continent entirely located in the Southern Hemisphere."
    )#9

    add_question(  #geography
        course="Geography",
        question="Which mountain range is the highest in the world?",
        options={"A": "Andes", "B": "Himalayas", "C": "Rockies", "D": "Alps"},
        correct_answer="B",
        feedback="The Himalayas contain the highest mountains in the world, including Mount Everest."
    )#10


    add_question(   #Literature
        course="Literature",
        question="Who wrote 'Romeo and Juliet'?",
        options={"A": "Charles Dickens", "B": "J.K. Rowling", "C": "William Shakespeare", "D": "Mark Twain"},
        correct_answer="C",
        feedback="Shakespeare wrote 'Romeo and Juliet'."
    )#1

    add_question(  #Literature
    course="Literature",
    question="Who is the author of 'Pride and Prejudice'?",
    options={"A": "Charlotte Brontë", "B": "Jane Austen", "C": "Virginia Woolf", "D": "Emily Dickinson"},
    correct_answer="B",
    feedback="Jane Austen is the author of 'Pride and Prejudice'."
    )#2

    add_question(  #Literature
        course="Literature",
        question="What is the title of George Orwell's novel about a dystopian future where Big Brother watches everything?",
        options={"A": "Animal Farm", "B": "1984", "C": "Brave New World", "D": "Fahrenheit 451"},
        correct_answer="B",
        feedback="George Orwell wrote '1984', a novel about a totalitarian regime."
    )#3

    add_question(  #Literature
        course="Literature",
        question="Which novel begins with the line 'Call me Ishmael'?",
        options={"A": "Moby-Dick", "B": "The Great Gatsby", "C": "To Kill a Mockingbird", "D": "Pride and Prejudice"},
        correct_answer="A",
        feedback="'Moby-Dick' begins with the famous line 'Call me Ishmael.'"
    )#4

    add_question(  #Literature
        course="Literature",
        question="Who wrote 'The Catcher in the Rye'?",
        options={"A": "F. Scott Fitzgerald", "B": "J.D. Salinger", "C": "Mark Twain", "D": "John Steinbeck"},
        correct_answer="B",
        feedback="J.D. Salinger wrote 'The Catcher in the Rye'."
    )#5

    add_question(  #Literature
        course="Literature",
        question="In which novel would you find the character 'Atticus Finch'?",
        options={"A": "The Grapes of Wrath", "B": "To Kill a Mockingbird", "C": "1984", "D": "Of Mice and Men"},
        correct_answer="B",
        feedback="Atticus Finch is a key character in 'To Kill a Mockingbird' by Harper Lee."
    )#6

    add_question(  #Literature
        course="Literature",
        question="Who wrote 'The Great Gatsby'?",
        options={"A": "Ernest Hemingway", "B": "F. Scott Fitzgerald", "C": "John Steinbeck", "D": "William Faulkner"},
        correct_answer="B",
        feedback="'The Great Gatsby' was written by F. Scott Fitzgerald."
    )#7

    add_question(  #Literature
        course="Literature",
        question="Which character is the protagonist in 'Harry Potter and the Sorcerer's Stone'?",
        options={"A": "Hermione Granger", "B": "Ron Weasley", "C": "Harry Potter", "D": "Albus Dumbledore"},
        correct_answer="C",
        feedback="The protagonist of 'Harry Potter and the Sorcerer's Stone' is Harry Potter."
    )#8

    add_question(  #Literature
        course="Literature",
        question="Which novel is set in a dystopian future and focuses on the themes of surveillance and totalitarianism?",
        options={"A": "Fahrenheit 451", "B": "1984", "C": "Brave New World", "D": "The Hunger Games"},
        correct_answer="B",
        feedback="'1984' by George Orwell is set in a dystopian future where surveillance is rampant."
    )#9

    add_question(  #Literature
        course="Literature",
        question="Who wrote 'Frankenstein'?",
        options={"A": "Mary Shelley", "B": "Bram Stoker", "C": "Edgar Allan Poe", "D": "H.G. Wells"},
        correct_answer="A",
        feedback="'Frankenstein' was written by Mary Shelley."
    )#10

except sqlite3.OperationalError as e:
    print("Database or table error:", e)
except Exception as e:
    print("An error occurred:", e)
