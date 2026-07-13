from header_common import *
from module_info import *
from module_music import *
from process_common import *

def save_python_header():
  ofile = open("./ID_music.py","w")
  for i_track in range(len(tracks)):
    ofile.write("track_{0:s} = {1:d}\n".format(tracks[i_track][0],i_track))
  ofile.write("\n\n")
  ofile.close()

def save_tracks():
  file = open(export_dir + "music.txt","w", encoding='utf-8')
  file.write("{0:d}\n".format(len(tracks)))
  for track in tracks:
    file.write("{0:s} {1:d} {2:d}\n".format(track[1], track[2], (track[2] | track[3])))
  file.close()

print("Exporting tracks...")
save_python_header()
save_tracks()
