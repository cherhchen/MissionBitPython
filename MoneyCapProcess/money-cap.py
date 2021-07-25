from tkinter import *
import tkinter as tk
from tkinter import font
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)


def buttonClicked(date_entry, item_entry, category_entry, expense_entry):
    print("Button is clicked!", date_entry, item_entry, category_entry, expense_entry)

root = tk.Tk()
root.title('Money Cap')

HEIGHT = 700
WIDTH = 1000

canvas = tk.Canvas(root, height = HEIGHT, width= WIDTH)
canvas.pack()

title_frame = tk.Frame(root, bg='#C6FFBD')
title_frame.place(relwidth=1, relheight=0.1)
title_img = tk.PhotoImage(file='MoneyCapBanner.gif')
title_label = tk.Label(title_frame, image=title_img)
title_label.place(relx=0, rely=0, relwidth=0.65, relheight=1)

frame = tk.Frame(root, bg='#05FF70', bd=10)
frame.place(relx=0.05, rely=0.15, relwidth=0.6, relheight=0.65)

lower_frame = tk.Frame(root, bg='#C6FFBD', bd=5)
lower_frame.place(relx=0.05, rely=0.85, relwidth=0.6, relheight=0.1)

date = tk.Entry(lower_frame)
date.place(relx=0.025, rely=0.4, relwidth=0.2, relheight=0.5)
date_label = tk.Label(lower_frame, text="Date:", font=('Courier'), bg='#C6FFBD')
date_label.place(relx=-0.03, rely=0.1, relwidth=0.2, relheight=0.2)

item = tk.Entry(lower_frame)
item.place(relx=0.25, rely =0.4, relwidth=0.2, relheight=0.5)
item_label = tk.Label(lower_frame, text="Item Name:", font=('Courier'), bg='#C6FFBD')
item_label.place(relx=0.22, rely=0.1, relwidth=0.2, relheight=0.2)

category = StringVar()
dropdown_options = ["Housing", "Transportation", "Food", "Utilities", "Entertainment", "Medical", "Clothing", "Insurance", "Charity", "Savings", "Other"]
#dropdown.set(dropdown_options[0])
category_dropdown = OptionMenu(lower_frame, category, *dropdown_options)
category_dropdown.place(relx=0.48, rely=0.4, relwidth=0.22, relheight=0.5)
category_label = tk.Label(lower_frame, text="Category:", font=('Courier'), bg='#C6FFBD')
category_label.place(relx=0.45, rely=0.1, relwidth=0.2, relheight=0.2)

expense = tk.Entry(lower_frame)
expense.place(relx=0.73, rely=0.4, relwidth=0.125, relheight=0.5)
expense_label = tk.Label(lower_frame, text="Expense($):", font=('Courier'), bg='#C6FFBD')
expense_label.place(relx=0.70, rely=0.1, relwidth=0.2, relheight=0.2)

button = tk.Button(lower_frame, text="+", highlightbackground='#C6FFBD', command=lambda: buttonClicked(date.get(), item.get(), category.get(), expense.get()))
button.place(relx=0.95, rely=0.2, relwidth=0.08, relheight=0.8, anchor='n')

root.mainloop()
