from tkinter import *
from pygame import mixer
from tkinter import filedialog
import tkinter.messagebox
window = Tk()
window.title('Music player in python')
def browse_file():
    global filename
    filename = filedialog.askopenfilename()

window.geometry('300x300')
menubar = Menu(window)
submenu = Menu(menubar,tearoff=0)
window.config(menu=menubar)
menubar.add_cascade(label='File',menu=submenu)
menubar.add_cascade(label='About')
submenu.add_command(label='Open',command=browse_file)
submenu.add_command(label='Exit')

mixer.init()
textLabel = Label(window, text='The Play Button', font=('Agency Fb', 30))
textLabel.pack()
def play_music():
    try:
        mixer.music.load(filename)
        mixer.music.play()
    except:
        print("File not found or invalid file name")

def stop_music():
    mixer.music.stop()

def set_volume(value):
    volume = int(value)/100
    mixer.music.set_volume(volume)


photo = PhotoImage(file='play.png')
playButton = Button(window, image=photo,command=play_music)
playButton.pack()

stopPhoto = PhotoImage(file='stop.png')
stopButton = Button(window, image=stopPhoto, command=stop_music)
stopButton.pack()

scale = Scale(window,from_=0,to=100,orient=HORIZONTAL,command=set_volume)
scale.set(70)
scale.pack()




window.mainloop()
