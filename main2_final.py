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
    stepeni = []
    for i in range(6):
        stepen = 0
        for j in range(6):
            print(matrix[i][j], end='')
            print(' ', end = '')
            if matrix[i][j] == 1:
                count += 1
                stepen += 1
        stepeni.append(stepen)
        print('')
    print('Кол-во единиц: ', count)
    print('Вероятность единицы: ', count/36)
    l = []
    for i in range(len(stepeni)):
        if stepeni[i] == max(stepeni):
            l.append(i + 1)
    print("Наибольшая степень: ", max(stepeni))
    print("Вершины наибольшей степени: ", end='')
    print(l)
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
    #-------------------------------------#
    #-----------------TEXT-----------------#
    tx1 = canvas.create_text(150, 50, width=25, font=("Arial", 35), text="1")
    tx2 = canvas.create_text(450, 50, width=25, font=("Arial", 35), text="2")
    tx3 = canvas.create_text(550, 250, width=25, font=("Arial", 35), text="3")
    tx4 = canvas.create_text(450, 450, width=25, font=("Arial", 35), text="4")
    tx5 = canvas.create_text(150, 450, width=25, font=("Arial", 35), text="5")
    tx6 = canvas.create_text(50, 250, width=25, font=("Arial", 35), text="6")
    #-----------------TEXT-----------------#
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