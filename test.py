from os import listdir
from os.path import isfile, join

playlist = [f for f in listdir("music") if isfile(join("music", f))]
for i in playlist:
    if i.endswith('.mp3' or '.wav'):
        print(i)

