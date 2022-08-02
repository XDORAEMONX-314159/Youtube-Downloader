import tkinter as tk
import tkinter.messagebox
from pytube import YouTube

def download():
    my_video = YouTube(str(url_entry.get()))
    for stream in my_video.streams:
        print(stream)
    my_video = my_video.streams.get_highest_resolution()
    my_video.download(output_path=str(output_entry.get()))    
    
    tkinter.messagebox.showinfo(title= 'Download complete', message = "Download complete")
    
window = tk.Tk()
window.title("Youtube Downloader")
window.geometry("300x160+420+150")

label_1 = tk.Label(window, text= 'Thanks for using Youtube Downloader')
label_1.pack()

label_URL = tk.Label(window, text= 'Please enter the URL down')
label_URL.pack()

url_entry = tk.Entry(window, width=40)
url_entry.pack()

label_path = tk.Label(window, text="Please enter the output_path down")
label_path.pack()

output_entry = tk.Entry(window, width=40)
output_entry.pack()
    
button = tk.Button(window, text="Download Now", command=download)
button.pack()

window.mainloop()
