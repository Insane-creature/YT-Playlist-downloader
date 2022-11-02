# This python program is used to download the whole playlist provided in the Youtube channel 
# Sometime we suffer downloading the whole playlist to our gallery in that case we can provide the playlist link and save the videos to the gallery

# Importing using pip install pytube

from pytube import Playlist

py = Playlist("https.......") #  here we have to provide the link of the playlist

print(f'Downloading: {py.title}') # this will indicate the title of the playlist

for video in py.videos:
    video.streams.first().download()


# Below program is to download single video feom YT

# from pytube import YouTube

# link = "https://youtu.be/A03oI0znAoc"
# youtube1 = YouTube(link)

# # print(youtube1.title)
# # print(youtube1.thumbnail_url)
# videos = youtube1.streams.all()
# vid = list(enumerate(videos))
# for i in vid:
#     print(i)

# strm = int(input("Enter: "))
# videos[strm].download()
# print("Succesfully")


