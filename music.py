from tkinter import *
from PIL import ImageTk, Image
import os
from pygame import mixer

col1 = '#ffffff'
col2 = '#3C1DC6'
col3 = '#333333'
col4 = '#CFC7F8'

window = Tk()
window.title("Music Player")
window.geometry('352x255')
window.configure(background=col1)
window.resizable(width=FALSE, height=FALSE)

def play_music():
    running = listbox.get(ACTIVE)
    running_song['text'] = running
    mixer.music.load(running)
    mixer.music.play()

def pause_music():
    mixer.music.pause()

def continue_music():
    mixer.music.unpause()

def stop_music():
    mixer.music.stop()

def next_music():
    playing = running_song['text']
    index = songs.index(playing)
    new_index = index + 1
    playing = songs[new_index]
    mixer.music.load(playing)
    mixer.music.play()

    listbox.delete(0, END)

    show()

    listbox.select_set(new_index)
    running_song['text'] = playing

def prev_music():
    playing = running_song['text']
    index = songs.index(playing)
    new_index = index - 1
    playing = songs[new_index]
    mixer.music.load(playing)
    mixer.music.play()

    listbox.delete(0, END)

    show()

    listbox.select_set(new_index)
    running_song['text'] = playing

left_frame = Frame(window, width=150, height=150, bg=col1)
left_frame.grid(row=0,column=0, padx=1,pady=1)

right_frame = Frame(window, width=250, height=150, bg=col3)
right_frame.grid(row=0,column=1, padx=0)

down_frame = Frame(window, width=400, height=150, bg=col4)
down_frame.grid(row=1,column=0,columnspan=3,padx=0,pady=1)

listbox = Listbox(right_frame, selectmode=SINGLE, font=('Arial 9 bold'), width=22, bg=col3, fg=col1)
listbox.grid(row=0,column=0)

w = Scrollbar(right_frame)
w.grid(row=0, column=1)

listbox.config(yscrollcommand=w.set)
w.config(command=listbox.yview)

image_1 = Image.open('icons/1.png')
image_1 = image_1.resize((130,130))
image_1 = ImageTk.PhotoImage(image_1)
app_image = Label(left_frame, height=130, image=image_1, padx=10, bg=col1)
app_image.place(x=10, y=15) 

image_2 = Image.open('icons/2.png')
image_2 = image_2.resize((55,55))
image_2 = ImageTk.PhotoImage(image_2)
play_button= Button(down_frame, width=40, height=40, image=image_2, padx=10, bg=col1, font=('Ivy 10'), command=play_music)
play_button.place(x=56+28, y=35) 

image_5 = Image.open('icons/5.png')
image_5 = image_5.resize((30,30))
image_5 = ImageTk.PhotoImage(image_5)
prev_button= Button(down_frame, width=40, height=40, image=image_5, padx=10, bg=col1, font=('Ivy 10'), command=prev_music)
prev_button.place(x=10+28, y=35) 

image_4 = Image.open('icons/4.png')
image_4 = image_4.resize((30,30))
image_4 = ImageTk.PhotoImage(image_4)
next_button= Button(down_frame, width=40, height=40, image=image_4, padx=10, bg=col1, font=('Ivy 10'), command=next_music)
next_button.place(x=102+28, y=35) 

image_3 = Image.open('icons/3.png')
image_3 = image_3.resize((55,55))
image_3 = ImageTk.PhotoImage(image_3)
pause_button= Button(down_frame, width=40, height=40, image=image_3, padx=10, bg=col1, font=('Ivy 10'), command=pause_music)
pause_button.place(x=148+28, y=35) 

image_7 = Image.open('icons/7.png')
image_7 = image_7.resize((70,70))
image_7 = ImageTk.PhotoImage(image_7)
continue_button= Button(down_frame, width=40, height=40, image=image_7, padx=10, bg=col1, font=('Ivy 10'), command=continue_music)
continue_button.place(x=194+28, y=35) 

image_6 = Image.open('icons/6.png')
image_6 = image_6.resize((30,30))
image_6 = ImageTk.PhotoImage(image_6)
stop_button= Button(down_frame, width=40, height=40, image=image_6, padx=10, bg=col1, font=('Ivy 10'), command=stop_music)
stop_button.place(x=240+28, y=35) 

line = Label(left_frame, width=200, height=1, padx=10, bg=col3)
line.place(x=0, y=1)

line = Label(left_frame, width=200, height=1, padx=10, bg=col1)
line.place(x=0, y=3)

running_song = Label(down_frame,text='Choose a song',font=('Ivy 10'), width=44, height=1, padx=10, bg=col1, fg=col3, anchor=NW)
running_song.place(x=0,y=1)



os.chdir(r'C:\Users\meetp\Python\music\music')
songs = os.listdir()

def show():
    for i in songs:
        listbox.insert(END, i)


show()

mixer.init()
music_state = StringVar()
music_state.set("Choose one!")

window.mainloop() 