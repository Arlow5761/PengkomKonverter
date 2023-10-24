from pytube import YouTube

def Download():    # Input URL YouTube dan Folder Destination
    url = input("Enter the YouTube URL: ")
    uri = input("Folder Destination: ")

    yt = YouTube(url)
    
    print("Title:", yt.title)
    print("Views:", yt.views)

    # Get the highest resolution stream
    yd = yt.streams.get_highest_resolution()
    
    # Download the video to the folder destination
    yd.download()
    
    print("Download complete.")
