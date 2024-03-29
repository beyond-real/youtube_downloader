import tkinter
import customtkinter
from pytube import YouTube


def startDownload():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        video = ytObject.streams.get_highest_resolution()

        title.configure(text=ytObject.title, text_color="yellow")
        finishLabel.configure(text="")
        video.download()
        finishLabel.configure(text="Downloaded!")
    except:
        finishLabel.configure(text="Download Error", text_color="red")


def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    per = str(int(percentage_of_completion))
    pPercentage.configure(text=per + "%")
    pPercentage.update()

    # update progress bar
    pBar.set(float(percentage_of_completion) / 100)


# system settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# app frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("YOUTUBE DOWNLOADER")

# ui elements
title = customtkinter.CTkLabel(app, text="Insert youtube link")
title.pack(padx=20, pady=10)

# link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=50, textvariable=url_var)
link.pack()

# finished downloading
finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()

# Progress percentage
pPercentage = customtkinter.CTkLabel(app, text="0%")
pPercentage.pack()

pBar = customtkinter.CTkProgressBar(app, width=500)
pBar.set(0)
pBar.pack(padx=10, pady=10)

# download button
download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx=10, pady=10)

# run app
app.mainloop()
