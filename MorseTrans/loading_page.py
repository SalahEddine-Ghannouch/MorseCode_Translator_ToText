from tkinter import *
from tkinter.ttk import Progressbar
import tkinter as tk
from tkinter import ttk

w=Tk()


width_of_window = 427
height_of_window = 250
screen_width = w.winfo_screenwidth()
screen_height = w.winfo_screenheight()
x_coordinate = (screen_width/2)-(width_of_window/2)
y_coordinate = (screen_height/2)-(height_of_window/2)
w.geometry("%dx%d+%d+%d" %(width_of_window,height_of_window,x_coordinate,y_coordinate))
w.overrideredirect(1)


s = ttk.Style()
s.theme_use('clam')
s.configure("red.Horizontal.TProgressbar", foreground='red', background='#4f4f4f')
progress=Progressbar(w,style="red.Horizontal.TProgressbar",orient=HORIZONTAL,length=500,mode='determinate',)

#############   progressbar  -----------------------

def new_win():
    import login_page


def bar():
    l4=Label(w,text='Loading...',fg='white',bg=a)
    lst4=('Calibri (Body)',11)
    l4.config(font=lst4)
    l4.place(x=18,y=210)
    
    import time
    r=0
    for i in range(100):
        progress['value']=r
        w.update_idletasks()
        time.sleep(0.03)
        r=r+1
    
    w.destroy()
    new_win()
        
progress.place(x=-10,y=235)



#############
#   frame 3   #
###########

'''
def rgb(r):
    return "#%02x%02x%02x" % r
#Frame(w,width=432,height=241,bg=rgb((100,100,100))).
'''

a='#0052cc'
Frame(w,width=427,height=241,bg=a).place(x=0,y=0)  #249794
b1=Button(w,width=10,height=1,text='Get Started',command=bar,border=0,fg=a,bg='white')
b1.place(x=170,y=200)


######## Label  ########

l1=Label(w,text='Welcome to',fg='white',bg=a)
lst1=('Calibri (Body)',18,'bold')
l1.config(font=lst1)
l1.place(x=50,y=80)

l2=Label(w,text='Morse Code',fg='white',bg=a)
lst2=('Calibri (Body)',18)
l2.config(font=lst2)
l2.place(x=190,y=82)

l3=Label(w,text='Translator App',fg='white',bg=a)
lst3=('Calibri (Body)',13)
l3.config(font=lst3)
l3.place(x=50,y=110)

w.mainloop()


