import tkinter
#import numpy as np
import math
import time as t
#import sounddevice as sd
import turtle
from tkinter import *
import random

sps = 44100  # sound per second
duration = 5000
atten = 3.0  # volume

screen = turtle.Screen()
screen.title("Fret Board")
screen.setup(1000, 400)
screen.bgpic('1024x510.gif')
note = turtle.Turtle()
note.shape('circle')
note.color('')
note.shapesize(2)
note.penup()
FONT_SIZE = 25
FONT = ("Aarial", FONT_SIZE, "normal")
note.pensize(2)



def color1(x, y):
    note1 = turtle.Turtle()
    note1.shape('circle')
    note1.color('red')
    note1.shapesize(2)
    note1.penup()
    note1.goto(x, y)


def color2(x, y):
    note1 = turtle.Turtle()
    note1.shape('circle')
    note1.color('blue')
    note1.shapesize(2)
    note1.penup()
    note1.goto(x, y)


def color3(x, y):
    note1 = turtle.Turtle()
    note1.shape('circle')
    note1.color('orange')
    note1.shapesize(2)
    note1.penup()
    note1.goto(x, y)


def color4(x, y):
    note1 = turtle.Turtle()
    note1.shape('circle')
    note1.color('green')
    note1.shapesize(2)
    note1.penup()
    note1.goto(x, y)


def color5(x, y):
    note1 = turtle.Turtle()
    note1.shape('circle')
    note1.color('yellow')
    note1.shapesize(2)
    note1.penup()
    note1.goto(x, y)


def color6(x, y):
    note1 = turtle.Turtle()
    note1.shape('circle')
    note1.color('grey')
    note1.shapesize(2)
    note1.penup()
    note1.goto(x, y)


def animmation():
    openstrg = [-474.0, -142.0], [-474.0, -86.0], [-472.0, -32.0], [-472.0, 27.0], [-472.0, 86.0], [-472.0, 144.0]
    note_list_E = [-432.0, -141.0], [-354.0, -142.0], [-285.0, -142.0], [-216.0, -145.0] \
        , [-153.0, -145.0], [-93.0, -145.0], [-9.0, -142.0], [58.0, -143.0], [120.0, -143.0], [191.0, -143.0], [260.0,
                                                                                                                -141.0] \
        , [322.0, -141.0]
    note_list_A = [-435.0, -86.0], [-365.0, -85.0], [-285.0, -85.0], [-209.0, -85.0], [-142.0, -84.0], [-80.0, -84.0], \
                  [-8.0, -84.0], [48.0, -84.0], [105.0, -84.0], [186.0, -83.0], [259.0, -84.0], [322.0, -85.0]
    note_list_D = [-434.0, -27.0], [-362.0, -30.0], [-284.0, -29.0], [-209.0, -29.0], [-144.0, -30.0], \
                  [-79.0, -28.0], [-5.0, -28.0], [53.0, -30.0], [108.0, -30.0], [180.0, -29.0], [248.0, -29.0], [319.0,
                                                                                                                 -29.0]
    note_list_G = [-428.0, 28.0], [-358.0, 28.0], [-285.0, 30.0], [-212.0, 31.0], [-145.0, 31.0], \
                  [-78.0, 29.0], [-4.0, 30.0], [54.0, 30.0], [112.0, 30.0], [182.0, 31.0], [254.0, 30.0], [320.0, 31.0]
    note_list_B = [-435.0, 87.0], [-354.0, 87.0], [-302.0, 87.0], [-214.0, 87.0], [-142.0, 86.0], [-71.0, 87.0], \
                  [-13.0, 86.0], [56.0, 87.0], [128.0, 88.0], [187.0, 86.0], [254.0, 86.0], [322.0, 87.0]
    note_list_e1 = [-435.0, 143.0], [-358.0, 144.0], [-293.0, 142.0], [-235.0, 142.0], \
                   [-170.0, 140.0], [-73.0, 144.0], [-22.0, 141.0], [55.0, 141.0], \
                   [117.0, 141.0], [180.0, 141.0], [247.0, 141.0], [315.0, 140.0]

    #################open notes########################
    E = [-474.0, -142.0]
    A = [-474.0, -86.0]
    D = [-472.0, -32.0]
    G = [-472.0, 27.0]
    B = [-472.0, 86.0]
    e1 = [-472.0, 144.0]
    note.color('blue')
    note.goto(E)
    note.write('E', font=FONT), note.color('red')
    note.goto(A)
    note.write('A', font=FONT), note.color('black')
    note.color('orange')
    note.goto(D)
    note.write('D', font=FONT)
    note.color('green')
    note.goto(G)
    note.write('G', font=FONT)
    note.color('grey')
    note.goto(B)
    note.write('B', font=FONT)
    note.color('yellow')
    note.goto(e1)
    note.write('e1', font=FONT)
    note.hideturtle()

    for x, y in openstrg:
        note.goto(x, y)
        break
    #############################################################
    ########################E_string_notes#####################################
    S = '#'
    F = [-432.0, -141.0]
    FS = [-374.0, -142.0]
    G = [-295.0, -142.0]
    Ab = [-240.0, -145.0]
    A = [-153.0, -145.0]
    Bb = [-100.0, -145.0]
    B = [-9.0, -142.0]
    C = [48.0, -143.0]
    CS = [120.0, -143.0]
    D = [191.0, -143.0]
    Eb = [260.0, -141.0]
    E = [322.0, -141.0]
    for x, y in note_list_E:
        note.color('blue')
        note.goto(F)
        note.write('F', font=FONT)
        note.goto(FS)
        note.write('F#', font=FONT)
        note.goto(G)
        note.write('G', font=FONT)
        note.goto(Ab)
        note.write('Ab', font=FONT)
        note.goto(A)
        note.write('A', font=FONT)
        note.goto(Bb)
        note.write('Bb', font=FONT)
        note.goto(B)
        note.write('B', font=FONT)
        note.goto(C)
        note.write('C', font=FONT)
        note.goto(CS)
        note.write('C#', font=FONT)
        note.goto(D)
        note.write('D', font=FONT)
        note.goto(Eb)
        note.write('Eb', font=FONT)
        note.goto(E)
        note.write('E', font=FONT)
        break
    ####################################################################
    ##########################A_string##################################

    for x, y in note_list_A:
        note.color('red')
        Bb = [-435.0, -86.0]
        B = [-365.0, -85.0]
        C = [-295.0, -85.0]
        CS = [-240.0, -85.0]
        D = [-152.0, -84.0]
        Eb = [-100.0, -84.0]
        E = [-8.0, -84.0]
        F = [48.0, -84.0]
        FS = [105.0, -84.0]
        G = [186.0, -83.0]
        Ab = [249.0, -84.0]
        A = [322.0, -85.0]

        note.goto(Bb)
        note.write('Bb', font=FONT)
        note.goto(B)
        note.write('B', font=FONT)
        note.goto(C)
        note.write('C', font=FONT)
        note.goto(CS)
        note.write('C#', font=FONT)
        note.goto(D)
        note.write('D', font=FONT)
        note.goto(Eb)
        note.write('Eb', font=FONT)
        note.goto(E)
        note.write('E', font=FONT)
        note.goto(F)
        note.write('F', font=FONT)
        note.goto(FS)
        note.write('F#', font=FONT)
        note.goto(G)
        note.write('G', font=FONT)
        note.goto(Ab)
        note.write('Ab', font=FONT)
        note.goto(A)
        note.write('A', font=FONT)
        break
    ##############################################################################
    #############################D_string#################################################
    Eb = [-434.0, -27.0]
    E = [-362.0, -30.0]
    F = [-284.0, -29.0]
    FS = [-240.0, -29.0]
    G = [-158.0, -30.0]
    Ab = [-89.0, -28.0]
    A = [-11.0, -28.0]
    Bb = [53.0, -30.0]
    B = [108.0, -30.0]
    C = [180.0, -29.0]
    CS = [248.0, -29.0]
    D = [319.0, -29.0]
    for x, y in note_list_D:
        note.color('orange')
        note.goto(Eb)
        note.write('Eb', font=FONT)
        note.goto(E)
        note.write('E', font=FONT)
        note.goto(F)
        note.write('F', font=FONT)
        note.goto(FS)
        note.write('F#', font=FONT)
        note.goto(G)
        note.write('G', font=FONT)
        note.goto(Ab)
        note.write('Ab', font=FONT)
        note.goto(A)
        note.write('A', font=FONT)
        note.goto(Bb)
        note.write('F', font=FONT)
        note.goto(B)
        note.write('B', font=FONT)
        note.goto(C)
        note.write('C', font=FONT)
        note.goto(CS)
        note.write('C#', font=FONT)
        note.goto(A)
        note.write('A', font=FONT)
        note.goto(D)
        note.write('D', font=FONT)
        break
    ###################################################################################
    ##################################G_string#################################################
    Ab = [-438.0, 28.0]
    A = [-358.0, 28.0]
    Bb = [-295.0, 30.0]
    B = [-222.0, 31.0]
    C = [-155.0, 31.0]
    CS = [-98.0, 29.0]
    D = [-15.0, 30.0]
    Eb = [44.0, 30.0]
    E = [112.0, 30.0]
    F = [182.0, 31.0]
    FS = [254.0, 30.0]
    G = [320.0, 31.0]
    note.color('green')
    for x, y in note_list_G:
        note.goto(Ab)
        note.write('Ab', font=FONT)
        note.goto(A)
        note.write('A', font=FONT)
        note.goto(Bb)
        note.write('Bb', font=FONT)
        note.goto(B)
        note.write('B', font=FONT)
        note.goto(C)
        note.write('C', font=FONT)
        note.goto(CS)
        note.write('C#', font=FONT)
        note.goto(D)
        note.write('D', font=FONT)
        note.goto(Eb)
        note.write('Eb', font=FONT)
        note.goto(E)
        note.write('E', font=FONT)
        note.goto(F)
        note.write('F', font=FONT)
        note.goto(FS)
        note.write('F#', font=FONT)
        note.goto(G)
        note.write('G', font=FONT)
        break
    #######################################################################################
    #####################################B_String##########################################

    C = [-435.0, 87.0]
    CS = [-374.0, 87.0]
    D = [-302.0, 87.0]
    Eb = [-234.0, 87.0]
    E = [-150.0, 86.0]
    F = [-91.0, 87.0]
    FS = [-33.0, 86.0]
    G = [56.0, 87.0]
    Ab = [120.0, 88.0]
    A = [187.0, 86.0]
    Bb = [254.0, 86.0]
    B = [322.0, 87.0]
    note.color('grey')
    for x, y in note_list_B:
        note.goto(C)
        note.write('C', font=FONT)
        note.goto(CS)
        note.write('C#', font=FONT)
        note.goto(D)
        note.write('D', font=FONT)
        note.goto(Eb)
        note.write('Eb', font=FONT)
        note.goto(E)
        note.write('E', font=FONT)
        note.goto(F)
        note.write('F', font=FONT)
        note.goto(FS)
        note.write('F#', font=FONT)
        note.goto(G)
        note.write('G', font=FONT)
        note.goto(Ab)
        note.write('Ab', font=FONT)
        note.goto(A)
        note.write('A', font=FONT)
        note.goto(Bb)
        note.write('Bb', font=FONT)
        note.goto(B)
        note.write('B', font=FONT)
        break
    #######################################################################################
    #################################e_string##############################################
    F = [-435.0, 143.0]
    FS = [-368.0, 144.0]
    G = [-293.0, 142.0]
    Ab = [-235.0, 142.0]
    A = [-170.0, 140.0]
    Bb = [-103.0, 144.0]
    B = [-22.0, 141.0]
    C = [55.0, 141.0]
    CS = [110.0, 141.0]
    D = [180.0, 141.0]
    Eb = [247.0, 141.0]
    E = [315.0, 140.0]
    note.color('yellow')
    for x, y in note_list_e1:
        note.goto(F)
        note.write('F', font=FONT)
        note.goto(FS)
        note.write('F#', font=FONT)
        note.goto(G)
        note.write('G', font=FONT)
        note.goto(Ab)
        note.write('Ab', font=FONT)
        note.goto(A)
        note.write('A', font=FONT)
        note.goto(Bb)
        note.write('Bb', font=FONT)
        note.goto(B)
        note.write('B', font=FONT)
        note.goto(C)
        note.write('C', font=FONT)
        note.goto(CS)
        note.write('C#', font=FONT)
        note.goto(D)
        note.write('D', font=FONT)
        note.goto(Eb)
        note.write('Eb', font=FONT)
        note.goto(E)
        note.write('E', font=FONT)
        break



def animmation2():
    openstrg = [-474.0, -142.0], [-474.0, -86.0], [-472.0, -32.0], [-472.0, 27.0], [-472.0, 86.0], [-472.0, 144.0]
    note_list_E = [-432.0, -141.0], [-354.0, -142.0], [-285.0, -142.0], [-216.0, -145.0] \
        , [-153.0, -145.0], [-93.0, -145.0], [-9.0, -142.0], [58.0, -143.0], [120.0, -143.0], [191.0, -143.0], [260.0,
                                                                                                                -141.0] \
        , [322.0, -141.0]
    note_list_A = [-435.0, -86.0], [-365.0, -85.0], [-285.0, -85.0], [-209.0, -85.0], [-142.0, -84.0], [-80.0, -84.0], \
                  [-8.0, -84.0], [48.0, -84.0], [105.0, -84.0], [186.0, -83.0], [259.0, -84.0], [322.0, -85.0]
    note_list_D = [-434.0, -27.0], [-362.0, -30.0], [-284.0, -29.0], [-209.0, -29.0], [-144.0, -30.0], \
                  [-79.0, -28.0], [-5.0, -28.0], [53.0, -30.0], [108.0, -30.0], [180.0, -29.0], [248.0, -29.0], [319.0,
                                                                                                                 -29.0]
    note_list_G = [-428.0, 28.0], [-358.0, 28.0], [-285.0, 30.0], [-212.0, 31.0], [-145.0, 31.0], \
                  [-78.0, 29.0], [-4.0, 30.0], [54.0, 30.0], [112.0, 30.0], [182.0, 31.0], [254.0, 30.0], [320.0, 31.0]
    note_list_B = [-435.0, 87.0], [-354.0, 87.0], [-302.0, 87.0], [-214.0, 87.0], [-142.0, 86.0], [-71.0, 87.0], \
                  [-13.0, 86.0], [56.0, 87.0], [128.0, 88.0], [187.0, 86.0], [254.0, 86.0], [322.0, 87.0]
    note_list_e1 = [-435.0, 143.0], [-358.0, 144.0], [-293.0, 142.0], [-235.0, 142.0], \
                   [-170.0, 140.0], [-73.0, 144.0], [-22.0, 141.0], [55.0, 141.0], \
                   [117.0, 141.0], [180.0, 141.0], [247.0, 141.0], [315.0, 140.0]

    for x, y in note_list_E:
        color2(x, y)
    for x, y in note_list_A:
        color1(x, y)
    for x, y in note_list_D:
        color3(x, y)
    for x, y in note_list_G:
        color4(x, y)
    for x, y in note_list_B:
        color6(x, y)
    for x, y in note_list_e1:
        color5(x, y)


root = tkinter.Tk()
root.config(background='black')
root.title("Menu")
root.minsize(1000, 400)
root.maxsize(1000, 400)
label1 = Label(root, text="option 1 : DISPLAY notes position")
label2 = Label(root, text="option 2 : DISPLAY Guitar notes")
label1.config(font=('Helvatical bold', 20), background='black', foreground='red')
label2.config(font=('Helvatical bold', 20), background='black', foreground='red')
e = Entry(root)

def fade():
    root.destroy()
def user_in():
    if int(e.get()) < 2:
        print(e,fade(),animmation2())
    elif e != 2:
        print(e,fade(),animmation())




button1 = Button(root, text='click', width=50, bg='red',command=user_in)
e.config(bg='black', fg='red', font=('Helvatical bold', 20))
label1.pack()
label2.pack()
e.pack()
button1.bind('<Button-1>')
e.get()
button1.pack()

root.mainloop()
screen.mainloop()
