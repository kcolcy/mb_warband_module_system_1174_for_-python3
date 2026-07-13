from module_info import *
from module_scene_props import *

from process_common import *
from process_operations import *

def save_scene_props(variable_list,variable_uses,tag_uses,quick_strings):
  ofile = open(export_dir + "scene_props.txt","w", encoding='utf-8')
  ofile.write("scene_propsfile version 1\n")
  ofile.write(" {0:d}\n".format(len(scene_props)))
  for scene_prop in scene_props:
    ofile.write("spr_{0:s} {1:d} {2:d} {3:s} {4:s} ".format(scene_prop[0], scene_prop[1], get_spr_hit_points(scene_prop[1]), scene_prop[2], str(scene_prop[3])))
    save_simple_triggers(ofile,scene_prop[4]  , variable_list,variable_uses,tag_uses,quick_strings)
    ofile.write("\n")
  ofile.close()


def save_python_header():
  file = open("./ID_scene_props.py","w")
  for i_scene_prop in range(len(scene_props)):
    file.write("spr_{0:s} = {1:d}\n".format(scene_props[i_scene_prop][0],i_scene_prop))
  file.close()

print("Exporting scene props...")
save_python_header()
variable_uses = []
variables = load_variables(export_dir,variable_uses)
tag_uses = load_tag_uses(export_dir)
quick_strings = load_quick_strings(export_dir)
save_scene_props(variables,variable_uses,tag_uses,quick_strings)
save_variables(export_dir,variables,variable_uses)
save_tag_uses(export_dir,tag_uses)
save_quick_strings(export_dir,quick_strings)
