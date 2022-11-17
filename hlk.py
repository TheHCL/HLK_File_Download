import wget,os
import datetime
from tkinter import messagebox

hlk_filter="https://go.microsoft.com/fwlink/?linkid=875139"
hlk_playlist="https://aka.ms/HLKPlaylist"

now= datetime.datetime.now()
now= now.strftime("%Y%m%d")
files=["filter.cab","playlist.zip"]
if os.path.isdir(now):
	os.chdir(now)
	


else:
	os.mkdir(now)
	os.chdir(now)

for x in files:
		if os.path.isfile(x):
			os.remove(x)
t=os.getcwd()
wget.download(hlk_filter,"filter.cab")
wget.download(hlk_playlist,"playlist.zip")
os.system("Expand filter.cab -F:* "+t)
os.remove("filter.cab")
os.remove("Readme.txt")

messagebox.showinfo(title="Success",message="File download complete.")