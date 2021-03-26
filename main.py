from tkinter import *

window = Tk()
window.minsize(width=250, height=150)
window.title("Program")
window.config(padx=20, pady=20)

def button_clicked():
    miles = float(input.get())
    result = str(miles * 1.609)
    result_label.config(text=result)


miles_label = Label(text="Miles", font=("Arial", 12, "bold"))
miles_label.config(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to", font=("Arial", 12, "bold"))
is_equal_label.config(text="is equal to")
is_equal_label.grid(column=0, row=1)

km_label = Label(text="Km", font=("Arial", 12, "bold"))
km_label.config(text="Km")
km_label.grid(column=2, row=1)

result_label = Label(text="0", font=("Arial", 12, "bold"))
result_label.config(text="0")
result_label.grid(column=1, row=1)

calc_button = Button(text="Calculate", command=button_clicked)
calc_button.grid(column=1, row=2)

input = Entry(width=7)
input.grid(column=1, row=0)













window.mainloop()
