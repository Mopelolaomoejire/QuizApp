import tkinter as tk
import json

class Quiz:
    def __init__(self, quiz_data):
        self.quiz_data = quiz_data
        self.score = 0
        self.current_question = 0
        self.total_questions = len(self.quiz_data)

    def display_question(self):
        question_label.config(text=self.quiz_data[self.current_question]['question'])
        self.display_options()

   
    def display_options(self):
        options = self.quiz_data[self.current_question]['options']
        for i, option in enumerate(options):
            radio_buttons[i].config(text=option, value=option)

    def check_answer(self, selected_option):
        answer = self.quiz_data[self.current_question]['answer']
        if selected_option == answer:
            self.score += 1

    def next_question(self):
        self.current_question += 1
        if self.current_question < self.total_questions:
            self.display_question()
        else:
            show_result()

def load_quiz_from_json(file_name):
    with open(file_name, 'r') as file:
        quiz_data = json.load(file)
    return quiz_data

def show_result():
    result_label.config(text=f"Your Score: {quiz.score}/{quiz.total_questions}")

def option_selected():
    selected = selected_option.get()
    quiz.check_answer(selected)
    quiz.next_question()

quiz_data = load_quiz_from_json(r'C:\Users\USER\Desktop\Quiz_data.json')  # Replace 'quiz_data.json' with your JSON file

quiz = Quiz(quiz_data)

root = tk.Tk()
root.title("Quiz App")

question_label = tk.Label(root, text="", wraplength=300)
question_label.pack()

selected_option = tk.StringVar()

radio_buttons = []
for _ in range(4):
    button = tk.Radiobutton(root, text="", variable=selected_option, value="")
    button.pack()
    radio_buttons.append(button)

submit_button = tk.Button(root, text="Submit", command=option_selected)
submit_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

quiz.display_question()

root.mainloop()
