#TASK 2
#SIMPLE CALCULATOR


import tkinter as tk

def on_button_click(value):
    curr_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, curr_text + value)

def on_clear():
    entry.delete(0, tk.END)

def on_equal():
    try:
        output = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(output))
    except Exception as err:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "ERROR")

root = tk.Tk()
root.title("Calculator")
root.configure(bg='#000000')  

entry = tk.Entry(root, width=20, font=('Arial', 15), borderwidth=2, relief="solid", fg='#000000')
entry.grid(row=0, column=0, columnspan=4, pady=12)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_no = 1
col_no = 0

for button in buttons:
    if button.isdigit() or button == '.':
        color = '#404040'  
    elif button in ('+', '-', '*', '/'):
        color = '#ffffff'  
    elif button == '=':
        color = '#778899'  
    else:
        color = '#404040'

    button_command = lambda b=button: on_button_click(b) if b != '=' else on_equal()
    button_widget = tk.Button(root, text=button, width=5, height=2, bg=color, fg='#000000', command=button_command)
    button_widget.grid(row=row_no, column=col_no, padx=5, pady=5)
    col_no += 1
    if col_no > 3:
        col_no = 0
        row_no += 1

tk.Button(root, text='C', width=5, height=2, bg='#404040', fg='#ff9999', command=on_clear).grid(row=row_no, column=col_no, padx=5, pady=5)

root.mainloop()
