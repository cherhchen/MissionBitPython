#https://www.youtube.com/watch?v=8exB6Ly3nx0

from tkinter import *
import numpy as np
import matplotlib.pyplot as plt

root = Tk()
root.geometry("400x200")

def graph():
    house_prices = np.random.normal(200000, 250000, 5000)
    plt.hist(house_prices, 50)
    plt.show()

my_button = Button(root, text="Graph It!", command=graph)
my_button.pack()

root.mainloop()
