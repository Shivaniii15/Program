import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("MCQ Quiz")

        self.questions = [
            "What is the capital of France?",
            "Which planet is known as the 'Red Planet'?",
            "What is 2 + 2?"
        ]

        self.options = [
            ["Paris", "London", "Berlin", "Madrid"],
            ["Mars", "Venus", "Jupiter", "Saturn"],
            ["3", "5", "4", "7"]
        ]

        self.correct_answers = [0, 0, 2]  # Index of correct option for each question

        self.current_question = 0
        self.score = 0

        self.question_label = tk.Label(root, text=self.questions[self.current_question])
        self.question_label.pack()

        self.option_buttons = []
        for i in range(4):
            button = tk.Button(root, text=self.options[self.current_question][i], command=lambda i=i: self.check_answer(i))
            button.pack()
            self.option_buttons.append(button)

    def check_answer(self, selected_option):
        if selected_option == self.correct_answers[self.current_question]:
            self.score += 1

        self.current_question += 1

        if self.current_question < len(self.questions):
            self.question_label.config(text=self.questions[self.current_question])
            for i in range(4):
                self.option_buttons[i].config(text=self.options[self.current_question][i])
        else:
            self.show_result()

    def show_result(self):
        messagebox.showinfo("Quiz Result", f"You scored {self.score} out of {len(self.questions)}!")
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
