from pytube import YouTube
from tkinter import *
import os

main_window = Tk()
main_window.minsize(width=200, height=100)
main_window.resizable(width=False, height=False)
main_window.title('YouTube downloader')

link_label = Label(main_window, text='Link URL').grid(row=0, column=0)
link = Entry(main_window, width=35, borderwidth=5, )
link.grid(row=0, column=1, columnspan=3, padx=30)

path_label = Label(main_window, text='Download path').grid(row=1, column=0)
path = Entry(main_window, width=35, borderwidth=5, )
path.grid(row=1, column=1, columnspan=3, padx=30)


def on_click_audio():
    yt = YouTube(link.get())
    user_path = path.get()
    print("Title:", yt.title)
    print("View:", yt.views)
    music = yt.streams.filter(only_audio=True).first()
    downloaded_file = music.download(user_path)
    base, ext = os.path.splitext(downloaded_file)
    new_file = base + '.mp3'
    os.rename(downloaded_file, new_file)
    Label(main_window, text="Download complete").grid(row=3, column=1)


def on_click_video():
    yt = YouTube(link.get())
    user_path = path.get()
    print("Title:", yt.title)
    print("View:", yt.views)
    video = yt.streams.get_highest_resolution()
    video.download(user_path)
    Label(main_window, text="Download complete").grid(row=3, column=1)


Button(main_window, text="AUDIO (MP3)", command=on_click_audio).grid(row=0, column=4)
Button(main_window, text="VIDEO MP4)", command=on_click_video).grid(row=0, column=5)
main_window.mainloop()
