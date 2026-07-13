from module_info import *
from module_presentations import *
from ID_meshes import *

from process_common import *
from process_operations import *

def save_presentations(variable_list,variable_uses,tag_uses,quick_strings):
  ofile = open(export_dir + "presentations.txt","w", encoding='utf-8')
  ofile.write("presentationsfile version 1\n")
  ofile.write(" {0:d}\n".format(len(presentations)))
  for presentation in presentations:
    ofile.write("prsnt_{0:s} {1:d} {2:d} ".format(presentation[0], presentation[1], presentation[2]))
    save_simple_triggers(ofile,presentation[3], variable_list,variable_uses,tag_uses,quick_strings)
    ofile.write("\n")
  ofile.close()


def save_python_header():
  file = open("./ID_presentations.py","w")
  for i_presentation in range(len(presentations)):
    file.write("prsnt_{0:s} = {1:d}\n".format(presentations[i_presentation][0],i_presentation))
  file.close()

print("Exporting presentations...")
save_python_header()
variable_uses = []
variables = load_variables(export_dir,variable_uses)
tag_uses = load_tag_uses(export_dir)
quick_strings = load_quick_strings(export_dir)
save_presentations(variables,variable_uses,tag_uses,quick_strings)
save_variables(export_dir,variables,variable_uses)
save_tag_uses(export_dir,tag_uses)
save_quick_strings(export_dir,quick_strings)
