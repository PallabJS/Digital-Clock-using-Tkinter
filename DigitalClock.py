import tkinter as tk
import datetime

timelist = []
drawn = False
def formatTime():
    pass
def mytimeUpdate():
    global timelist
    h = int((datetime.datetime.now().hour))
    if h>12:
        h = h-12
    m = int((datetime.datetime.now().minute))
    s = int((datetime.datetime.now().second))
    daytime = ((datetime.datetime.now().strftime("%p")))
    timelist.append(str(h))
    timelist.append(":")
    timelist.append(str(m))
    timelist.append(":")
    timelist.append(str(s))
    timelist.append(daytime)
    timestring = ' '.join(timelist)
    # print(timestring)

def mainfn():
    global timelist
    window1.config(text = timelist)
    timelist = []
    window1.after(1000, mainfn)
    mytimeUpdate()
main = tk.Tk()

main.title("Digital Clock")
#window creation
window1 = tk.Label(main, text = str(timelist) , padx = 60, pady = 60, font = "1000")

#Window Binding to main
window1.pack()

mainfn()
main.mainloop()
