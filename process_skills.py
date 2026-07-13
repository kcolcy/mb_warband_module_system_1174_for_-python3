from header_common import *
from module_info import *
from module_skills import *
from process_common import *

skill_name_pos = 1
skill_attribute_pos = 2
skill_max_level_pos= 3
skill_desc_pos = 4



def save_skills():
  ofile = open(export_dir + "skills.txt","w", encoding='utf-8')
  ofile.write("{0:d}\n".format(len(skills)))
  for i_skill in range(len(skills)):
    skill = skills[i_skill]
    ofile.write("skl_{0:s} {1:s} ".format(skill[0], replace_spaces(skill[1])))
    ofile.write("{0:d} {1:d} {2:s}\n".format(skill[skill_attribute_pos],skill[skill_max_level_pos],(skill[skill_desc_pos].replace(" ","_"))))
  ofile.close()

def save_python_header():
  ofile = open("./ID_skills.py","w")
  for i_skill in range(len(skills)):
    ofile.write("skl_{0:s} = {1:d}\n".format(skills[i_skill][0],i_skill))
  ofile.write("\n\n")
  ofile.close()

print("Exporting skills...")
save_python_header()
save_skills()
