from module_info import *
from module_quests import *

from process_common import *

def save_quests():
  ofile = open(export_dir + "quests.txt","w", encoding='utf-8')
  ofile.write("questsfile version 1\n")
  ofile.write("{0:d}\n".format(len(quests)))
  for i_quest in range(len(quests)):
    quest = quests[i_quest]
    ofile.write("qst_{0:s} {1:s} {2:d} ".format(quest[0],(quest[1].replace(" ","_")),quest[2]))
    ofile.write("{0:s} ".format(quest[3].replace(" ","_")))
    ofile.write("\n")
  ofile.close()

def save_python_header():
  ofile = open("./ID_quests.py","w")
  for i_quest in range(len(quests)):
    ofile.write("qst_{0:s} = {1:d}\n".format(quests[i_quest][0],i_quest))
  for i_quest in range(len(quests)):
    ofile.write("qsttag_{0:s} = {1:d}\n".format(quests[i_quest][0],opmask_quest_index|i_quest))
  ofile.write("\n\n")
  ofile.close()


print("Exporting quest data...")
save_quests()
save_python_header()
  
