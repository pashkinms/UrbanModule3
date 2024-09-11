import tkinter as tk

window = tk.Tk()
window.title('Calculator')
window.geometry("350x350")
window.resizable(False, False)
button_add = tk.Button(window, text="+", width=2, height=2)
button_add.place(x=100, y=200)
button_sub = tk.Button(window, text="-", width=2, height=2)
button_sub.place(x=150, y=200)
button_mul = tk.Button(window, text="*", width=2, height=2)
button_mul.place(x=200, y=200)
button_div = tk.Button(window, text="/", width=2, height=2)
button_div.place(x=250, y=200)

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


window.mainloop()