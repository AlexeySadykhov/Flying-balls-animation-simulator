import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
import time
import random
import playsound


def sound():
    if sound_box.get() == 'On':
        state = True
    else:
        state = False
    if state:
        playsound.playsound('hit_sample.wav',
                            block=False)
    else:
        pass


def choose_color():
    return "#%06x" % random.randint(0, 16777215)


def create_objects(count, min_s, max_s, min_r, max_r):
    arr = []
    for i in range(count):
        x = random.randint(100, win_w - 100)
        y = random.randint(100, win_h - 100)
        r = random.randint(min_r, max_r)
        speed_x = random.randint(min_s, max_s)
        speed_y = random.randint(min_s, max_s)
        ball = canvas.create_oval(x - r,
                                  y - r,
                                  x + r,
                                  y + r,
                                  fill=choose_color(),
                                  outline=choose_color(),
                                  width=3)
        config = {'obj': ball,
                  'speed_x': speed_x,
                  'speed_y': speed_y}
        arr.append(config)
    return arr


def start():
    canvas.delete('all')
    global running
    running = True
    num_of_obj = 1
    min_speed = 1
    max_speed = 10
    min_size = 5
    max_size = 50
    try:
        num_of_obj = int(num_of_balls_box.get())
        if num_of_obj <= 0:
            mb.showerror('Error',
                         'Number of balls must be positive number.')
        min_speed = int(min_speed_box.get())
        max_speed = int(max_speed_box.get())
        if max_speed < min_speed:
            mb.showerror('Error',
                         'Min speed must be lower then max speed.')
        min_size = int(min_size_box.get())
        max_size = int(max_size_box.get())
        if max_size < min_size:
            mb.showerror('Error',
                         'Min size must be less then max size.')
    except ValueError:
        mb.showerror('Error',
                     'Arguments must be integers.')

    objects = create_objects(num_of_obj,
                             min_speed,
                             max_speed,
                             min_size,
                             max_size)
    while running:
        for conf in objects:
            canvas.move(conf['obj'], conf['speed_x'], conf['speed_y'])
            coordinates = canvas.coords(conf['obj'])
            if coordinates[0] < 0 or coordinates[2] > win_w:
                canvas.itemconfig(conf['obj'],
                                  fill=choose_color(),
                                  outline=choose_color())
                sound()
                conf['speed_x'] = -conf['speed_x']
            if coordinates[1] < 0 or coordinates[3] > win_h:
                canvas.itemconfig(conf['obj'],
                                  fill=choose_color(),
                                  outline=choose_color())
                sound()
                conf['speed_y'] = -conf['speed_y']
        window.update()
        time.sleep(0.01)


def stop():
    global running
    running = False
    canvas.delete('all')


window = tk.Tk()
window.title('Flying balls animation simulator')
win_h = 650
win_w = 1200
window.config(width=win_w,
              height=win_h+50)
window.resizable(width=False,
                 height=False)

canvas = tk.Canvas(master=window,
                   background='black',
                   width=win_w,
                   height=win_h)
start_button = tk.Button(master=window,
                         text='Start',
                         command=start)
stop_button = tk.Button(master=window,
                        text='Stop',
                        command=stop)
num_of_balls_label = tk.Label(master=window,
                              text='Number of balls:')
num_of_balls_box = tk.Spinbox(master=window,
                              from_=1,
                              to=100,
                              width=5)
sound_label = tk.Label(master=window,
                       text='Sound:')
sound_box = ttk.Combobox(master=window,
                         state='readonly',
                         values=['On', 'Off'])
sound_box.current(0)
min_speed_label = tk.Label(master=window,
                           text='Min speed:')
min_speed_box = tk.Spinbox(master=window,
                           from_=1,
                           to=100,
                           width=5)
max_speed_label = tk.Label(master=window,
                           text='Max speed:')
max_speed_box = tk.Spinbox(master=window,
                           from_=1,
                           to=100,
                           width=5)
min_size_label = tk.Label(master=window,
                          text='Min size:')
min_size_box = tk.Spinbox(master=window,
                          from_=1,
                          to=50,
                          width=5)
max_size_label = tk.Label(master=window,
                          text='Max size:')
max_size_box = tk.Spinbox(master=window,
                          from_=1,
                          to=50,
                          width=5)

canvas.pack(side='top', fill='both')
start_button.pack(side='left')
stop_button.pack(side='left')
num_of_balls_label.pack(side='left')
num_of_balls_box.pack(side='left')
min_speed_label.pack(side='left')
min_speed_box.pack(side='left')
max_speed_label.pack(side='left')
max_speed_box.pack(side='left')
min_size_label.pack(side='left')
min_size_box.pack(side='left')
max_size_label.pack(side='left')
max_size_box.pack(side='left')
sound_box.pack(side='right')
sound_label.pack(side='right')

running = False
window.mainloop()
