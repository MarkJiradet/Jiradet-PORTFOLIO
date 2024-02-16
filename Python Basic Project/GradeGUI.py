import tkinter as tk
from tkinter import filedialog

# Default grading criteria
grading_criteria = {
    'A': 80,
    'B': 70,
    'C': 60,
    'D': 50,
    'F': 0
}

def load_file():
    filename = filedialog.askopenfilename(filetypes=[('Text files', '*.txt')])
    if filename:
        input_file.delete(0, tk.END)
        input_file.insert(0, filename)

def save_file():
    filename = filedialog.asksaveasfilename(defaultextension='.txt')
    if filename:
        output_file.delete(0, tk.END)
        output_file.insert(0, filename)

def update_criteria():
    grading_criteria['A'] = int(a_grade.get())
    grading_criteria['B'] = int(b_grade.get())
    grading_criteria['C'] = int(c_grade.get())
    grading_criteria['D'] = int(d_grade.get())
    grading_criteria['F'] = int(f_grade.get())

def process_grades():
    input_filename = input_file.get()
    output_filename = output_file.get()
    if not input_filename or not output_filename:
        return

    # Load grades from input file
    with open(input_filename, 'r') as file:
        header = file.readline().strip().split(',')
        subjects = header[1:]
        grades = {}
        for line in file:
            data = line.strip().split(',')
            name = data[0]
            grades[name] = [int(x) for x in data[1:]]

    # Compute letter grades
    def letter_grade(score):
        for grade, cutoff in grading_criteria.items():
            if score >= cutoff:
                return grade
        return 'F'

    with open(output_filename, 'w') as file:
        file.write('Name,' + ','.join(subjects) + '\n')
        for name, scores in grades.items():
            processed = [letter_grade(score) for score in scores]
            file.write(name + ',' + ','.join(processed) + '\n')

# Create the main window
root = tk.Tk()
root.title('Grade Processor')

# Input file
input_frame = tk.Frame(root)
input_frame.pack(padx=10, pady=10)

input_label = tk.Label(input_frame, text='Input File:')
input_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

input_file = tk.Entry(input_frame)
input_file.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)

input_button = tk.Button(input_frame, text='Browse...', command=load_file)
input_button.grid(row=0, column=2, padx=5, pady=5)

# Output file
output_frame = tk.Frame(root)
output_frame.pack(padx=10, pady=10)

output_label = tk.Label(output_frame, text='Output File:')
output_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

output_file = tk.Entry(output_frame)
output_file.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)

output_button = tk.Button(output_frame, text='Save As...', command=save_file)
output_button.grid(row=0, column=2, padx=5, pady=5)

# Grading criteria
grading_frame = tk.Frame(root)
grading_frame.pack(padx=10, pady=10)

a_label = tk.Label(grading_frame, text='A:')
a_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

a_grade = tk.Entry(grading_frame, width=5)
a_grade.grid(row=0, column=1, padx=5, pady=5)
a_grade.insert(0, grading_criteria['A'])

b_label = tk.Label(grading_frame, text='B:')
b_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)

b_grade = tk.Entry(grading_frame, width=5)
b_grade.grid(row=1, column=1, padx=5, pady=5)
b_grade.insert(0, grading_criteria['B'])

c_label = tk.Label(grading_frame, text='C:')
c_label.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)

c_grade = tk.Entry(grading_frame, width=5)
c_grade.grid(row=2, column=1, padx=5, pady=5)
c_grade.insert(0, grading_criteria['C'])

d_label = tk.Label(grading_frame, text='D:')
d_label.grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)

d_grade = tk.Entry(grading_frame, width=5)
d_grade.grid(row=3, column=1, padx=5, pady=5)
d_grade.insert(0, grading_criteria['D'])

f_label = tk.Label(grading_frame, text='F:')
f_label.grid(row=4, column=0, padx=5, pady=5, sticky=tk.W)

f_grade = tk.Entry(grading_frame, width=5)
f_grade.grid(row=4, column=1, padx=5, pady=5)
f_grade.insert(0, grading_criteria['F'])

update_button = tk.Button(grading_frame, text='Update', command=update_criteria)
update_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

#Process grades
process_button = tk.Button(root, text='Process Grades', command=process_grades)
process_button.pack(padx=10, pady=10)

root.mainloop()
