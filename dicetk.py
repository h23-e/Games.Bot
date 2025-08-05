from tkinter import*
import random

root=Tk()
root.geometry("400x400")
root.title("Roll Dice Simulator")

label = Label(root,text='',font=("Helvetica",400,"bold"),bg='skyblue')

def roll_dice():
    dice=['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
    label.configure(text=f'{random.choice(dice)}')
    label.pack()

button=Button(root,text='Roll Dice',foreground='yellow',command=roll_dice,bg='indigo',font=("Arial",20))
button.pack()
root.mainloop()
