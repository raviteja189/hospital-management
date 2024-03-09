# -*- coding: utf-8 -*-

from tkinter import *
import tkinter
from tkinter import filedialog
import numpy as np
from tkinter.filedialog import askopenfilename
import pandas as pd 
from tkinter import simpledialog
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense, LSTM, Bidirectional
from sklearn.preprocessing import OneHotEncoder
from keras.layers import Dropout
from sklearn.metrics import mean_squared_error
from tensorflow.keras.optimizers import Adam
import keras
import seaborn as sns
plt.switch_backend('TkAgg')

from PIL import ImageTk, Image  

main = tkinter.Tk()
main.title("Data Visualization") #designing main screen
main.geometry("1000x650")

#img =Image.open('bgimg.jpg')
#bg = ImageTk.PhotoImage(img, master=main, width=10, height=10)

# Add image
#label = Label(main, image=bg)
#label.place(x = 0,y = 10)

global filename
global train_df

 
def upload():
    global filename
    filename = filedialog.askopenfilename(initialdir = "dataset")
    text.delete('1.0', END)
    text.insert(END,filename+' Loaded')

def visualize():
    global train_df
    train_df = pd.read_csv("static\csvFiles\haemoglobin.csv")
    x= train_df.Year
    y = train_df.hm_Result
    plt.figure(figsize=(10,6))
    plt.grid(True)
    plt.xlabel('Year')
    plt.ylabel('Hemoglobin')
    plt.plot(x,y)
    plt.title('Haemoglobin')
    plt.show()

def visualize1():
    global train_df
    train_df = pd.read_csv("static\csvFiles\Eosinophil.csv")
    x= train_df.Year
    y = train_df.es_Result
    plt.figure(figsize=(10,6))
    plt.grid(True)
    plt.xlabel('Year')
    plt.ylabel('Eosinophils')
    plt.plot(x,y)
    plt.title('Eosinophils')
    plt.show()

def visualize2():
    global train_df
    train_df = pd.read_csv("static\csvFiles\platelets.csv")
    x= train_df.Year
    y = train_df.plt_Result
    plt.figure(figsize=(10,6))
    plt.grid(True)
    plt.xlabel('Year')
    plt.ylabel('Platelets')
    plt.plot(x,y)
    plt.title('Platelets')
    plt.show()

def visualize3():
    global train_df
    train_df = pd.read_csv("static\csvFiles\RBC.csv")
    x= train_df.Year
    y = train_df.rbc_Result
    plt.figure(figsize=(10,6))
    plt.grid(True)
    plt.xlabel('Year')
    plt.ylabel('RBC')
    plt.plot(x,y)
    plt.title('RBC')
    plt.show()

def visualize4():
    global train_df
    train_df = pd.read_csv("static\csvFiles\WBC.csv")
    x= train_df.Year
    y = train_df.wbc_Result
    plt.figure(figsize=(10,6))
    plt.grid(True)
    plt.xlabel('Year')
    plt.ylabel('WBC')
    plt.plot(x,y)
    plt.title('WBC')
    plt.show()

def graph():
  height = [nn_rmse,lstm_rmse, bilstm_rmse]
  bars = ('NN RMSE','LSTM RMSE', 'BiLSTM RMSE')
  y_pos = np.arange(len(bars))
  plt.bar(y_pos, height)
  plt.xticks(y_pos, bars)
  plt.title("Comparison of 3 models")
  plt.show()

def close():
  main.destroy()
   
font = ('times', 16, 'bold')
title = Label(main, text='Year Wise Health Reports Analysis', justify=LEFT)
title.config(bg='magenta', fg='black')  
title.config(font=font)           
title.config(height=3, width=120)       
title.place(x=100,y=5)
title.pack()

font1 = ('times', 14, 'bold')
# uploadButton = Button(main, text="Upload Health Reports", command=upload)
# uploadButton.place(x=10,y=100)
# uploadButton.config(font=font1)  

visualizeButton = Button(main, text="Hemoglobin plot ", command=visualize)
visualizeButton.place(x=10,y=100)
visualizeButton.config(font=font1)

visualizeButton = Button(main, text="Eosinophils plot ", command=visualize1)
visualizeButton.place(x=230,y=100)
visualizeButton.config(font=font1)

visualizeButton = Button(main, text="Platelets plot ", command=visualize2)
visualizeButton.place(x=400,y=100)
visualizeButton.config(font=font1)

visualizeButton = Button(main, text="RBC plot ", command=visualize3)
visualizeButton.place(x=600,y=100)
visualizeButton.config(font=font1)

visualizeButton = Button(main, text="WBC plot ", command=visualize4)
visualizeButton.place(x=750,y=100)
visualizeButton.config(font=font1)


closeButton = Button(main, text="Close App", command=close)
closeButton.place(x=500,y=200)
closeButton.config(font=font1)

font1 = ('times', 12, 'bold')
text=Text(main,height=20,width=160)
scroll=Scrollbar(text)
text.configure(yscrollcommand=scroll.set)
text.place(x=10,y=250)
text.config(font=font1) 

main.config(bg='magenta')
main.mainloop()
