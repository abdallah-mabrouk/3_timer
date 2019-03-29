#################################import part################################
############################################################################

from tkinter import Tk,IntVar , PhotoImage,ttk,Label
import playsound
#################################window part################################
############################################################################

r=1
def start_timer():
    global r
    if r ==0:
        pass
    else:
        if second.get()==0 and minute.get()==0 and hour.get() ==0:
            stop_()
            playsound.playsound('We Are the Brave, Lenka Sings for Honor.mp3')
        else:
            if second.get() > 0:
                second.set(second.get()-1)
            elif second.get()==0:
                second.set(59)
                if minute.get() > 0:
                    minute.set(minute.get()-1)
                elif minute.get() == 0:
                    minute.set(59)
                    hour.set(hour.get()-1)
            s_spin.after(1000,start_timer)

def start_():
    global r
    if second.get() == 0 and minute.get() == 0 and hour.get() == 0:
        pass
    else:
        r = 1
        h_spin.place_forget()
        m_spin.place_forget()
        s_spin.place_forget()
        start.place_forget()
        h_Label.place(x=95,y=70)
        m_Label.place(x=135,y=70)
        s_Label.place(x=175,y=70)
        m1.place(x=120, y=70)
        m2.place(x=160, y=70)
        pause.place(x=60,y=100)
        stop.place(x=135,y=100)
        start_timer()
def stop_():
    global r
    r=0
    start.place(x=100,y=100)
    pause.place_forget()
    continue_.place_forget()
    stop.place_forget()
    h_Label.place_forget()
    m_Label.place_forget()
    s_Label.place_forget()
    h_spin.place(x=55, y=70)
    m_spin.place(x=110, y=70)
    s_spin.place(x=165, y=70)
    m1.place_forget()
    m2.place_forget()
def continue__():
    global r
    r = 1
    start_timer()
    continue_.place_forget()
    pause.place(x=60,y=100)
def pause_():
    global r
    r = 0
    pause.place_forget()
    continue_.place(x=60,y=100)


timer = Tk()
timer.geometry("280x250+500+130")
timer.resizable(False, False)
timer.maxsize(280, 200)
timer.minsize(280, 200)
timer.iconbitmap('icon.ico')
bg = PhotoImage(file='Untitled-2.png')
timer.title("timer")


hour = IntVar()
minute = IntVar()
second = IntVar()


bg_label = Label(timer,image=bg,relief='flat' ,bd=0)
bg_label.place(x=0,y=0)
h_spin = ttk.Spinbox(timer,from_=00,to=23,width=5,textvariable= hour)
h_spin.place(x=55,y=70)
m_spin = ttk.Spinbox(timer,from_=00,to=59,width=5,textvariable= minute)
m_spin.place(x=110,y=70)
s_spin = ttk.Spinbox(timer,from_=00,to=59,width=5,textvariable= second)
s_spin.place(x=165,y=70)
start = ttk.Button(timer,text='start',command=start_)
start.place(x=100,y=100)
stop = ttk.Button(timer,text='stop',command=stop_)#135

pause = ttk.Button(timer,text='pause',command=pause_)#60

continue_ = ttk.Button(timer,text='continue',command=continue__)
h_Label = ttk.Label(timer,textvariable= hour)
m_Label = ttk.Label(timer,textvariable= minute)
s_Label = ttk.Label(timer,textvariable= second)

m1 = ttk.Label(timer,text=':')
m2 = ttk.Label(timer,text=':')



timer.mainloop()