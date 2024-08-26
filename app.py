from pytubefix import YouTube
from sys import argv


vid = input("Enter the link of the video you want to download: ")
yt = YouTube(vid)

print("Title: ", yt.title)
print("Views: ", yt.views)

dload = yt.streams.get_highest_resolution()
dload.download()