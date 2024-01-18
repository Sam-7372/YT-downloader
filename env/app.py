import customtkinter as ctk
import tkinter as ttk 
import tkinter.ttk as ttk
from pytube import YouTube
from tkinter.ttk import *
from pathlib import Path


def download_video():
    url = entry_url.get()
    resolution = resolution_var.get()
    

    progress_label.pack(pady=(10,5))
    progress_bar.pack(pady=(10,5))
    status_label.pack(pady=(10,5))


    try:
        yt = YouTube(url, on_progress_callback=on_progress)
        stream = yt.streams.filter(res=resolution).first()
        downloads_path = str(Path.home() / "Downloads")
      
        
        # downlaod the video into a specific dir
        #os.path.join("downloads",f"{yt.title}.mp4")
        stream.download(output_path=downloads_path)
        status_label.configure(text=f"Downloaded to {downloads_path}")#, text_colour= "white", fg_colour="green")
    except Exception as e: 
        status_label.configure(text=f"Error {str(e)}")#, text_colour= "white", fg_colour="red")

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_completed = (bytes_downloaded /total_size *100)
    progress_label.configure(text = str(int(percentage_completed))+"%") 
    progress_label.update()

    progress_bar.set(float(percentage_completed/100))
    



# create a root window 
root = ctk.CTk()
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

#title of window
root.title("YouTube Downloader")

# set max width and hight
root.geometry("720x480")
root.minsize(720, 480)
root.maxsize(1080, 720)

#create a frame to hold conent 
content_frame = ctk.CTkFrame(root)
content_frame.pack(fill = ctk.BOTH, expand=True, padx=10, pady = 10)

# create a label and the entry widget for the video url
url_label = ctk.CTkLabel(content_frame, text="Enter the youtube url here: ")
entry_url = ctk.CTkEntry(content_frame, width=400, height=40)
url_label.pack(pady=(10,5))
entry_url.pack(pady=(10,5))

#create download button
download_button = ctk.CTkButton(content_frame, text="Download", command=download_video)
download_button.pack(pady=(10,5))

# create a resolutiuon list box
resolutions = ["720p", "360p","240p"]
resolution_var = ctk.StringVar()
combobox_var = ctk.StringVar(value="option 2")
resolution_combobox = ctk.CTkComboBox(content_frame, values=resolutions,  variable=resolution_var)
#resolution_combobox = ctk.CTkComboBox(content_frame, values=resolutions, textvariable= resolution_var)
resolution_combobox.pack(pady=(10,5))
resolution_combobox.set("720p")

#create a label and the progress bar to display the download progress
progress_label = ctk.CTkLabel(content_frame, text="0%")
#progress_label.pack(pady=(10,5))

progress_bar = ctk.CTkProgressBar(content_frame, width=400)
progress_bar.set(0)
#progress_bar.pack(pady=(10,5))


# create the status label

status_label = ctk.CTkLabel(content_frame, text="")
#status_label.pack(pady=(10,5))

# to start the app
root.mainloop()