import tkinter as tk

def get_values():
    number1 = int(number1_entry.get())
    number2 = int(number2_entry.get())
    return number1, number2

def insert_values(value):
    answer_entry.delete(0, 'end')
    answer_entry.insert(0, value)

def add():
    number1, number2 = get_values()
    res = number1 + number2
    insert_values(res)

def sub():
    number1, number2 = get_values()
    res = number1 - number2
    insert_values(res)

def mul():
    number1, number2 = get_values()
    res = number1 * number2
    insert_values(res)

def div():
    number1, number2 = get_values()
    res = number1 / number2
    insert_values(res)

window = tk.Tk()
window.title('Calculator')
window.geometry("350x350")
window.resizable(False, False)

number1_entry = tk.Entry(window, width=24)
number1_entry.place(x=100, y=50 )
number2_entry = tk.Entry(window, width=24)
number2_entry.place(x=100, y=100)
answer_entry = tk.Entry(window, width=24)
answer_entry.place(x=100, y=150)


number1 = tk.Label(window, text='Enter number1')
number1.place(x=100,y=25)
number2 = tk.Label(window, text='Enter number2')
number2.place(x=100,y=75)
answer = tk.Label(window, text='The answer is: ')
answer.place(x=100,y=125)

button_add = tk.Button(window, text="+", width=2, height=2, command=add)
button_add.place(x=100, y=200)
button_sub = tk.Button(window, text="-", width=2, height=2, command=sub)
button_sub.place(x=150, y=200)
button_mul = tk.Button(window, text="*", width=2, height=2, command=mul)
button_mul.place(x=200, y=200)
button_div = tk.Button(window, text="/", width=2, height=2, command=div)
button_div.place(x=250, y=200)

window.mainloop()