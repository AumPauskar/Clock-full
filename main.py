# importing all the modules
from tkinter import *
import time
import controller as co

geometry_size = co.GiveLayout()

# tkinter essential
root = Tk()
root.title('Clock')
root.geometry(geometry_size)

canvas_time = Canvas(root)
canvas_time.pack()

canvas_stopwatch = Canvas(root)
canvas_stopwatch.pack()

canvas_timer = Canvas(root)
canvas_timer.pack()

def RunClock():
    hour = time.strftime('%H')
    minute = time.strftime('%M')
    second = time.strftime('%S')
    label_time_hr.config(text = hour)
    label_time_min.config(text = minute)
    label_time_sec.config(text = second)
    root.after(1000, RunClock)
# --------------------
# this section of code will handle the labels of the main clock part
# the time will contain time in the form of 07:47:09
# aka in hours:minutes:secoonds
# this paragraph of code will contain the hours: part
label_time_hr = Label(canvas_time, text = '')
label_time_hr.grid(row = 1, column = 1)
label_time_hr_dot = Label(canvas_time, text = ':')
label_time_hr_dot.grid(row = 1, column = 2)

# this paragraph of code will contain the minutes: part
label_time_min = Label(canvas_time, text = '')
label_time_min.grid(row = 1, column = 3)
label_time_min_dot = Label(canvas_time, text = ':')
label_time_min_dot.grid(row = 1, column = 4)

# this paragraph of code will contain the seconds part
label_time_sec = Label(canvas_time, text = '')
label_time_sec.grid(row = 1, column = 5)
# --------------------


# --------------------
# this part will contain the script for the stopwatch part
# the time will be displayed in a hour:minute:second fashion
# this paragraph will contain the hours part
label_stopwatch_hr = Label(canvas_stopwatch, text = '')
label_stopwatch_hr.grid(row = 1, column = 1)
label_stopwatch_hr_dot = Label(canvas_stopwatch, text = ':')
label_stopwatch_hr_dot.grid(row = 1, column = 2)

# this part will contain the minutes part
label_stopwatch_min = Label(canvas_stopwatch, text = '')
label_stopwatch_min.grid(row = 1, column = 3)
label_stopwatch_min_dot = Label(canvas_stopwatch, text = ':')
label_stopwatch_min_dot.grid(row = 1, column = 4)

# this part will contain the seconds part
label_stopwatch_sec = Label(canvas_stopwatch, text ='')
label_stopwatch_sec.grid(row = 1, column = 5)
# --------------------

# --------------------
# this part will contain the countdown-timer part
# the time will be displayed in a hour:minute:second fashion
# this paragraph of code will contain the hours part
label_timer_hr = Label(canvas_timer, text ='')
label_timer_hr.grid(row = 1, column = 1)
label_timer_hr_dot = Label(canvas_timer, text = ':')
label_timer_hr_dot.grid(row = 1, column = 2)

# this paragraph of code will contain the minutes part
label_timer_min = Label(canvas_timer, text ='')
label_timer_min.grid(row = 1, column = 3)
label_timer_min_dot = Label(canvas_timer, text = ':')
label_timer_min_dot.grid(row = 1, column = 4)

# this paragraph of code will contain the seconds part
label_timer_sec = Label(canvas_timer, text = '')
label_timer_sec.grid(row = 1, column = 5)
# --------------------


RunClock()
# tkinter essential
root.mainloop()