# -*- coding: utf-8 -*-
"""
Created on Tue May  7 13:01:55 2024

@author: USER
"""

name = "Adwait"

for letter in name:
    print(letter)
    
    

from tkinter import*
root=Tk()
root.title

root.geometry("400x400")
root.configure(background = 'snow')

enter_word = Entry(root)
enter_word.place(relx=0.5,rely=0.4,anchor=CENTER)

label = Label(root, text="Name in Ascii : ",bg="light yellow", fg="black")
label = ["text"] += ste(chr(encrypted))

def asciiConverter():
    input_word = enter_word.get()
    
    for letter in input_word:
        label["text"] += str(ord(letter)) +" "

btn=Button(root,text="Show name in Ascii",command=asciiConverter, bg='gold', fg = 'black')
btn.place(relx=0.4,rely=0.6,anchor=CENTER)

btn=Button(root,text="Show name in encryption",command=asciiConverter, bg='gold', fg = 'black')
btn.place(relx=0.5,rely=0.5,anchor=CENTER)

label.place(relx=0.5,rely=0.8,anchor=CENTER)

root.mainloop()