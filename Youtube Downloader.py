import tkinter as tk
import tkinter.messagebox
from pytube import YouTube

def download():
    my_video = YouTube(str(url_entry.get()))
    for stream in my_video.streams:
        print(stream)
    my_video = my_video.streams.get_highest_resolution()
    my_video.download(output_path="write the path here")    
    
    tkinter.messagebox.showinfo(title= 'Download complete', message = "Download complete")
    
window = tk.Tk()
window.title("Youtube Downloader")
window.geometry("600x600+420+150")
window.iconphoto(True, tk.PhotoImage(file='E:\python\youtube icon.png'))

label = tk.Label(window, text= 'Thanks for using Youtube Downloader')
label.pack()

label = tk.Label(window, text= 'Please enter the URL down')
label.pack()

url_entry = tk.Entry(window, width=40)
url_entry.pack()
    
button = tk.Button(window, text="Download Now", command=download)
button.pack()

window.mainloop()
