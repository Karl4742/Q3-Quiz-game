import tkinter as tk
from tkinter import messagebox
import sqlite3
import random

# Function to center the window on the screen
def center_window(window, width, height):
    # Get the screen width and height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Calculate the position of the window
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)

    # Set the window size and position
    window.geometry(f"{width}x{height}+{x}+{y}")

# Question class for displaying questions and handling feedback
class Question:
    def __init__(self, question_text, options, correct_answer, feedback):
        self.question_text = question_text
        self.options = options
        self.correct_answer = correct_answer
        self.feedback = feedback
        self.selected_option = tk.StringVar(value="")  # Initialize with no selection

    def display(self, parent_frame):
        # Clear the previous question
        for widget in parent_frame.winfo_children():
            widget.destroy()

        # Display question text
        question_label = tk.Label(parent_frame, text=self.question_text, font=("Arial", 14))
        question_label.pack(pady=10)

        # Reset the selected option for each new question
        self.selected_option.set("")

        # Display options as radio buttons
        for option_key, option_text in self.options.items():
            option_button = tk.Radiobutton(
                parent_frame,
                text=option_text,
                variable=self.selected_option,
                value=option_key,
                font=("Arial", 12)
            )
            option_button.pack(anchor="w", padx=20, pady=5)

    def get_feedback(self):
        if self.selected_option.get() == self.correct_answer:
            return f"Correct! {self.feedback}", True
        else:
            return f"Incorrect. {self.feedback}", False


# Function to load questions from the database
def load_questions(course):
    with sqlite3.connect("Q3_quiz.db") as conn:
        cursor = conn.cursor()
        cursor.execute(f"SELECT question, option_a, option_b, option_c, option_d, correct_answer, feedback FROM {course}")
        questions_data = cursor.fetchall()
    
    # Convert each question data row to a Question object
    questions = []
    for question_text, option_a, option_b, option_c, option_d, correct_answer, feedback in questions_data:
        options = {"A": option_a, "B": option_b, "C": option_c, "D": option_d}
        question = Question(question_text, options, correct_answer, feedback)
        questions.append(question)
    
    # Shuffle questions and take the first 10
    random.shuffle(questions)
    return questions[:10]


# Function to start the quiz
def start_quiz(course):
    global questions, submit_button, next_button, current_question_index, correct_answers, incorrect_answers, feedback_label, quiz_window, progress_label

    # Load questions from the database
    questions = load_questions(course)
    if not questions:
        messagebox.showinfo("Error", "No questions available in this category.")
        return

    # Declare quiz_window as a global variable to access it in other functions
    quiz_window = tk.Toplevel(root)
    quiz_window.title("Quiz")

    # Center the quiz window on the screen
    center_window(quiz_window,1000, 600)  # Set the desired size for the quiz window

    question_frame = tk.Frame(quiz_window)
    question_frame.pack(pady=20)

    feedback_label = tk.Label(quiz_window, font=("Arial", 12))
    feedback_label.pack(pady=10)

    # Initialize counters
    correct_answers = [0]
    incorrect_answers = [0]
    current_question_index = [0]

    # Add a label for progress (e.g., "1 out of 10")
    progress_label = tk.Label(quiz_window, font=("Arial", 12))
    progress_label.pack(pady=5)

    def show_question():
        question = questions[current_question_index[0]]
        question.display(question_frame)
        
        # Update the progress label
        progress_label.config(text=f"Question {current_question_index[0] + 1} out of {len(questions)}")
        
        feedback_label.config(text="")  # Clear feedback

    def submit_answer():
        question = questions[current_question_index[0]]
        
        # Check if an option has been selected
        if question.selected_option.get() == "":
            # Use quiz_window as the parent to avoid the app moving to the front
            messagebox.showwarning("No Answer Selected", "Please select an answer before submitting.", parent=quiz_window)
            return

        # Get feedback based on the selected answer
        feedback, is_correct = question.get_feedback()
        
        if is_correct:
            correct_answers[0] += 1
        else:
            incorrect_answers[0] += 1

        feedback_label.config(text=feedback)
        submit_button.config(state="disabled")  # Disable submit after answering

        # Determine if it's the last question to show "Finish" instead of "Next"
        if current_question_index[0] < len(questions) - 1:
            next_button.config(text="Next Question", command=next_question)
        else:
            next_button.config(text="Finish", command=finish_quiz)

        next_button.pack(pady=10)  # Show the Next/Finish button

    def next_question():
        current_question_index[0] += 1
        show_question()
        next_button.pack_forget()
        submit_button.config(state="normal")

    def finish_quiz():
        # Use global quiz_window to ensure it's accessible here
        global quiz_window
        score_summary = f"Quiz completed!\nCorrect answers: {correct_answers[0]}\nIncorrect answers: {incorrect_answers[0]}"
        feedback_label.config(text=score_summary)
        submit_button.config(state="disabled")
        next_button.config(state="disabled")
        
        # Close quiz window and return to main menu after a short delay
        quiz_window.after(2000, lambda: (quiz_window.destroy(), show_main_menu()))

    submit_button = tk.Button(quiz_window, text="Submit Answer", command=submit_answer)
    submit_button.pack(pady=10)

    next_button = tk.Button(quiz_window)
    next_button.pack_forget()

    show_question()


# Function to select category and start quiz
def select_category():
    course = course_var.get()
    if course and course != "Select a course":
        start_quiz(course)
        category_window.destroy()
    else:
        messagebox.showwarning("Warning", "Please select a valid category.")


# Function to display the main menu with a dropdown for course selection
def show_main_menu():
    global category_window
    category_window = tk.Frame(root)
    category_window.pack(pady=20)

    # Category selection label
    tk.Label(category_window, text="Select a Quiz Category", font=("Arial", 14)).pack(pady=10)
    
    # Available courses as options (update based on actual courses in your database)
    courses = ["Mathematics", "Astronomy", "History", "Geography", "Literature"]
    
    # Dropdown for selecting course
    global course_var
    course_var = tk.StringVar(value="Select a course")
    dropdown = tk.OptionMenu(category_window, course_var, *courses)
    dropdown.config(font=("Arial", 12))
    dropdown.pack(pady=10)

    # Start button to begin the quiz
    start_button = tk.Button(category_window, text="Start Quiz Now", command=select_category)
    start_button.pack(pady=10)


# Main application window
root = tk.Tk()
root.title("Quiz App")

# Center the main window on the screen
center_window(root, 600, 500)  # Set your desired window size here

show_main_menu()  # Show the main menu initially

root.mainloop()
