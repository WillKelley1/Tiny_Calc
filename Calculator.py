# Python Calculator 
# Obviously There are things you could improve on this
# - More Appealing GUI 
# - Have the answer displayed at the top like a normal calculator
# - Give it like a waiting animation like googles dinosaur


import tkinter as tk

def evaluate(event):
    try:
        result.set(eval(entry.get()))
    except Exception as e:
        result.set("Error")

app = tk.Tk()
app.title("Calculator")

# Entry for numbers and result
entry = tk.Entry(app, width=20, font=('Arial', 16))
entry.bind('<Return>', evaluate)
entry.grid(row=0, column=0, columnspan=4, sticky="nsew")  # Note the sticky parameter

buttons = [
    '7', '8', '9', '+',
    '4', '5', '6', '-',
    '1', '2', '3', '*',
    'C', '0', '=', '/'
]

row_val = 1
col_val = 0

for button in buttons:
    if button == 'C':
        b = tk.Button(app, text=button, command=lambda: entry.delete(0, tk.END))
    elif button == '=':
        b = tk.Button(app, text=button, command=lambda: evaluate(None))
    else:
        b = tk.Button(app, text=button, command=lambda b=button: entry.insert(tk.END, b))
    
    b.grid(row=row_val, column=col_val, sticky="nsew")
    
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

result = tk.StringVar(app)
result_label = tk.Label(app, textvariable=result, font=('Arial', 14))
result_label.grid(row=5, column=0, columnspan=4, sticky="nsew")

# Adjust the column and row weights so they expand proportionally with resizing
for i in range(4):
    app.grid_columnconfigure(i, weight=1)
for i in range(6):
    app.grid_rowconfigure(i, weight=1)

app.mainloop()
