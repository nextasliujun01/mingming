import os
from pytube import YouTube
from tkinter import *
location = []
def download(youtube_link, download_folder):
    YouTube(youtube_link).streams.get_highest_resolution().download(download_folder)
    #yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution')[-1].download()
    #yt = YouTube('http://youtube.com/watch?v=9bZkp7q19f0')
    #print(yt.streams)
    return True

def clicked():

    #lbl.configure(text="Button was clicked !!")
    res =  txt.get()
    lbl_1.configure(text = "Please wait")
    #lbl.configure(text= res)
    r = download(res, location)
    if r is True:
        lbl_1.configure(text = "done")
    else:
        return False

############## Get user home.
home = os.path.expanduser('~')
print(home)
location = os.path.join(home, 'Downloads')

### Start GUI. 
window = Tk()

window.title("Download App")

window.geometry('1000x100')
lbl_0a = Label(window, text = "Download YouTube file", font=("Arial Bold", 10))
lbl_0a.grid(column=0, row= 0)
lbl_0b = Label(window, text = "Use Ctrl-C to copy link and Ctrl_V to paste", font=("Arial Bold", 10))
lbl_0b.grid(column=1, row= 0)


lbl = Label(window, text="Copy and Paste YouTube link:",   bg='white')

lbl.grid(column=0, row=1)

txt = Entry(window,width=100, text='Put link here')

txt.grid(column=1, row=1)

###btn = Button(window, text="Click Me")
btn = Button(window, text='Download',command=clicked)

btn.grid(column=1, row=2)
### Just show wait/done 
lbl_1 = Label(window, text = "Wait")
lbl_1.grid(column=1, row = 3)

window.mainloop()


