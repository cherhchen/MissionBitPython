from tkinter import *
import tkinter as tk

top = Tk()

class Item():
    def __init__(self, word, num):
        self.word = word
        self.num = num

    def getWord(self):
        return self.word

    def getNum(self):
        return self.num

    def displayLabel(self):
        label = tk.Label(top, text=self.word, bg='red')
        #label.pack(pady=10)

python = Item("Python", 1)
perl = Item("Perl", 2)
c = Item("C", 3)
php = Item("PHP", 4)
jsp = Item("JSP", 5)
ruby = Item("Ruby", 6)

scrollbar = Scrollbar(top)
scrollbar.pack(side=RIGHT, fill=Y)

Lb1 = Listbox(top, yscrollcommand=scrollbar.set)
Lb1.insert(1, python.getWord() + ' ' +str(python.getNum()))
Lb1.insert(2, perl.getWord(), perl.getNum())
Lb1.insert(3, c.getWord(), c.getNum())
Lb1.insert(4, php.getWord(), php.getNum())
Lb1.insert(5, jsp.getWord(), jsp.getNum())
Lb1.insert(6, ruby.getWord(), ruby.getNum())

Lb1.pack(side=LEFT, fill=BOTH)

scrollbar.config(command=Lb1.yview)
top.mainloop()