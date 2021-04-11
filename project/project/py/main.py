from tkinter import *
import matplotlib.pyplot as plt
import numpy as np

root = Tk()
root.title('Построение графика функции')
root.geometry('1020x620')

canvas = Canvas(root, width=1020, height=620, bg='#26252d')

#линии сетки по вертикали
for y in range(21):
    k = 50 * y
    canvas.create_line(10+k, 610, 10+k, 10, width=1, fill='#1d1018')
    
#линии сетки по горизонтали
for x in range(13):
    k = 50 * x
    canvas.create_line(10, 10+k, 1010, 10+k, width=1, fill='#1d1018')

#линии координат Х и У
canvas.create_line(510, 10, 510, 610, width=1, arrow=FIRST, fill='white')#ось У
canvas.create_line(0, 310, 1010, 310, width=1, arrow=LAST, fill='white')# ось Х
    
canvas.pack()
root.mainloop()
