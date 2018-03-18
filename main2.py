import random
from tkinter import *
from tkinter import Canvas
canvas = Canvas(width = 600, height = 600, bg = 'white')
canvas.pack()
def callback(event):
    canvas.delete("all")
    matrix = [[0 for i in range(6)] for j in range(6)]
    count = 0
    point = 50
    while count < 14:
        i = random.randint(0, 5)
        j = random.randint(0, 5)
        k = random.random()
        if k >= 0.6:
            if i != j:
                if matrix[i][j] != 1:
                    matrix[i][j] = 1
                    matrix[j][i] = 1
                    count += 2
                else:
                    continue
    count = 0
    for i in range(6):
        for j in range(6):
            print(matrix[i][j], end='')
            print(' ', end = '')
            if matrix[i][j] == 1:
                count += 1
        print('')
    print('Кол-во единиц: ', count)
    print('Вероятность единицы: ', count/36)
    canvas.bind("<Button-1>", callback)
    #---------------CIRCLES---------------#
    oval1 = canvas.create_oval(3*point, point, 5*point, 3*point,
                               outline="black", fill="blue", width=0)
    oval2 = canvas.create_oval(7*point, point, 9*point, 3*point,
                               outline="black", fill="blue", width=0)
    oval3 = canvas.create_oval(9*point, 5*point, 11*point, 7*point,
                               outline="black", fill="blue", width=0)
    oval4 = canvas.create_oval(7*point, 9*point, 9*point, 11*point,
                               outline="black", fill="blue", width=0)
    oval5 = canvas.create_oval(3*point, 9*point, 5*point, 11*point,
                               outline="black", fill="blue", width=0)
    oval6 = canvas.create_oval(point, 5*point, 3*point, 7*point,
                               outline="black", fill="blue", width=0)
    # -------------------------------------#
    centers = [[200, 100], [400,100], [500, 300], [400, 500], [200, 500], [100, 300]]
    l = 0
    for i in range(6):
        for j in range(6):
            if matrix[i][j] == 1:
                line = canvas.create_line(centers[i][0], centers[i][1],
                                          centers[j][0], centers[j][1],
                                          width = 3, fill="red")
canvas.bind("<Button-1>", callback)
mainloop()


