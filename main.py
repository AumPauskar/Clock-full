# importing all the modules
from tkinter import *
import time
import controller as co
import json

with open('settings.json', 'r') as val:
	data = json.load(val)
	hours_timer = int(data['timer_hrs']); minutes_timer = int(data['timer_min']); seconds_timer = int(data['timer_sec'])
timer = co.Convert(hours_timer, minutes_timer, seconds_timer)

# would get the data from settings.json and controller.py
geometry_size = co.GiveLayout()
font_clock_main = co.GiveMainClockFont()
font_clock_timer = co.GiveTimerClockFont()

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
    hour_clock = time.strftime('%H')
    minute_clock = time.strftime('%M')
    second_clock = time.strftime('%S')
    label_time_hr.config(text = hour_clock)
    label_time_min.config(text = minute_clock)
    label_time_sec.config(text = second_clock)
    root.after(1000, RunClock)

def RunTimer():
    global hours_timer, minutes_timer, seconds_timer
    if hours_timer == minutes_timer == seconds_timer == 0:
        minutes_timer = 'Time'; seconds_timer = 'up'
        label_timer_hr.grid_forget()
        label_timer_hr_dot.grid_forget()
        label_timer_min_dot.grid_forget()
    elif minutes_timer == seconds_timer == 0:
        hours_timer -=1 
        minutes_timer = seconds_timer = 59
        root.after(1000, RunTimer)
    elif seconds_timer == 0:
        minutes_timer -= 1
        seconds_timer == 59
        root.after(1000, RunTimer)
    else:
        seconds_timer -= 1
        root.after(1000, RunTimer)

    if len(str(seconds_timer)) == 1:
        temp_timer_sec = '0' + str(seconds_timer)
    else:
        temp_timer_sec = str(seconds_timer)
    if len(str(minutes_timer)) == 1:
        temp_timer_min = '0' + str(minutes_timer)
    else:
        temp_timer_min = str(minutes_timer)
    label_timer_hr.config(text = hours_timer)
    label_timer_min.config(text = minutes_timer)
    label_timer_sec.config(text =seconds_timer)
    
# --------------------
# this section of code will handle the labels of the main clock part
# the time will contain time in the form of 07:47:09
# aka in hours:minutes:secoonds
# this paragraph of code will contain the hours: part
label_time_hr = Label(canvas_time, text = '', font = font_clock_main)
label_time_hr.grid(row = 1, column = 1)
label_time_hr_dot = Label(canvas_time, text = ':', font = font_clock_main)
label_time_hr_dot.grid(row = 1, column = 2)

# this paragraph of code will contain the minutes: part
label_time_min = Label(canvas_time, text = '', font = font_clock_main)
label_time_min.grid(row = 1, column = 3)
label_time_min_dot = Label(canvas_time, text = ':', font = font_clock_main)
label_time_min_dot.grid(row = 1, column = 4)

# this paragraph of code will contain the seconds part
label_time_sec = Label(canvas_time, text = '', font = font_clock_main)
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
label_timer_hr = Label(canvas_timer, text ='', font = font_clock_timer)
label_timer_hr.grid(row = 1, column = 1)
label_timer_hr_dot = Label(canvas_timer, text = ':', font = font_clock_timer)
label_timer_hr_dot.grid(row = 1, column = 2)

# this paragraph of code will contain the minutes part
label_timer_min = Label(canvas_timer, text ='', font = font_clock_timer)
label_timer_min.grid(row = 1, column = 3)
label_timer_min_dot = Label(canvas_timer, text = ':', font = font_clock_timer)
label_timer_min_dot.grid(row = 1, column = 4)

# this paragraph of code will contain the seconds part
label_timer_sec = Label(canvas_timer, text = '', font = font_clock_timer)
label_timer_sec.grid(row = 1, column = 5)
# --------------------

RunTimer()
RunClock()
# tkinter essential
root.mainloop()