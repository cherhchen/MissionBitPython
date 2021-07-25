import tkinter as tk

root = tk.Tk()

def testing():
  print("This is a test.")

button = tk.Button(root, text="hello", command=testing)
button.pack()

root.mainloop()