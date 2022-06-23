import wget,os
import datetime
from tkinter import messagebox

hlk_filter="https://docs.microsoft.com/en-us/windows-hardware/test/hlk/user/windows-hardware-lab-kit-filters"
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

wget.download(hlk_filter,"filter.cab")
wget.download(hlk_playlist,"playlist.zip")

messagebox.showinfo(title="Success",message="File download complete.")