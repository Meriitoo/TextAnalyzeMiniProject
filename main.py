import tkinter as tk
from tkinter import messagebox


def analyze_text():
    user_text = text_entry.get("1.0", "end-1c")

    char_count = len(user_text)

    words = user_text.split()
    word_count = len(words)

    sentence_count = user_text.count('.') + user_text.count('!') + user_text.count('?')

    if word_count > 0:
        total_word_length = sum(len(word) for word in words)
        average_word_length = total_word_length / word_count
    else:
        average_word_length = 0

    analysis_result = f'Text analysis:\nNumber of characters: {char_count}\nNumber of words: {word_count}\nNumber of sentences: {sentence_count}\nAverage word length: {average_word_length:.2f}'

    messagebox.showinfo("Analysis Result", analysis_result)


def exit_program():
    root.destroy()


root = tk.Tk()
root.title('Text Analyzer')

instruction_label = tk.Label(root, text="Enter some text:")
instruction_label.pack()

text_entry = tk.Text(root, width=40, height=10)
text_entry.pack()

analyze_button = tk.Button(root, text="Analyze Text", command=analyze_text)
analyze_button.pack()

exit_button = tk.Button(root, text="Exit", command=exit_program)
exit_button.pack()

root.mainloop()
