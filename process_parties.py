from header_game_menus import *
from module_info import *
from module_game_menus import *
from module_parties import *
from process_operations import *

from process_common import *


def save_parties(parties):
  file = open(export_dir + "parties.txt","w", encoding='utf-8')
  file.write("partiesfile version 1\n")
  file.write("{0:d} {1:d}\n".format(len(parties), len(parties)))
  for i_party in range(len(parties)):
    party = parties[i_party]
    if (party[5] >= 0):
      add_tag_use(tag_uses,tag_faction,party[5])

    file.write(" 1 {0:d} {1:d} ".format(i_party, i_party))
#    file.write(" 1 {0:d} ".format(i_party))
    file.write("p_{0:s} {1:s} {2:d} ".format(convert_to_identifier(party[0]),replace_spaces(party[1]),party[2]))
    menu_no = 0
    menu_param = party[3]
    if (type(menu_param) is type("hehe")):
      menu_no = find_object(game_menus,menu_param)
      if (menu_no < 0):
        print("Error: Unable to find menu-id :" + menu_param)
    else:
      menu_no = menu_param
    file.write("{0:d} ".format(menu_no))
    
    file.write("{0:d} {1:d} {2:d} {3:d} {4:d} ".format(party[4], party[5], party[6], party[6],party[7]))
    ai_behavior_object = 0
    ai_param = party[8]
    if (type(ai_param) is type("hehe")):
      ai_behavior_object = find_object(parties,ai_param)
      if (ai_behavior_object < 0):
        print("Error: Unable to find party-id :" + ai_param)
    else:
      ai_behavior_object = ai_param
    file.write("{0:d} {1:d} ".format(ai_behavior_object,ai_behavior_object))
    position = party[9]
    default_behavior_location = position
    file.write("{0:f} {1:f} ".format(default_behavior_location[0],default_behavior_location[1]))
    file.write("{0:f} {1:f} ".format(default_behavior_location[0],default_behavior_location[1]))
    file.write("{0[0]:f} {0[1]:f} 0.0 ".format(position))
    member_list = party[10]
    file.write("{0:d} ".format(len(member_list)))
    for member in member_list:
      add_tag_use(tag_uses,tag_troop,member[0])
      file.write("{0:d} {1:d} 0 {2:d} ".format(member[0],member[1],member[2]))
    bearing = 0.0
    if (len(party) > 11):
      bearing = (3.1415926 / 180.0) * party[11]
    file.write("\n{0:f}\n".format(bearing))
  file.close()

def save_python_header(parties):
  file = open("./ID_parties.py","w")
  for i_party in range(len(parties)):
    file.write("p_{0:s} = {1:d}\n".format(convert_to_identifier(parties[i_party][0]),i_party))
  file.close()


print("Exporting parties")
tag_uses = load_tag_uses(export_dir)
save_python_header(parties)
save_parties(parties)
save_tag_uses(export_dir, tag_uses)
#print "Generating C header..."
#save_c_header()
#print "Generating Python header..."
#print "Finished."
