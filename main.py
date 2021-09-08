# importing all the modules
from tkinter import *
import time

# tkinter essential
root = Tk()

canvas_time = Canvas(root)
canvas_time.pack()

canvas_stopwatch = Canvas(root)
canvas_stopwatch.pack()

canvas_timer = Canvas(root)
canvas_timer.pack()


# --------------------------------------------
# this section of code will handle the labels of the main clock part
# the time will contain time in the form of 07:47:09
# aka in hours:minutes:secoonds
# this paragraph of code will contain the hours: part
label_time_hr = Label(canvas_time, text = '')
label_time_hr.grid(row = 1, column = 1)
label_time_hr_dot = Label(label_time_hr, text = ':')
label_time_hr_dot.grid(row = 1, column = 2)

# this paragraph of code will contain the minutes: part
label_time_min = Label(canvas_time, text = '')
label_time_min.grid(row = 1, column = 3)
label_time_min_dot = Label(label_time_min, text = ':')
label_time_min_dot.grid(row = 1, column = 4)

# this paragraph of code will contain the seconds part
label_time_sec = Label(canvas_time, text = '')
label_time_sec.grid(row = 1, column = 5)
# ----------------------------------------------

# tkinter essential
root.mainloop()