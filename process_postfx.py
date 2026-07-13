from header_common import *
from module_info import *
from module_postfx import *

def write_python_header(postfx_params_list):
  file = open("./ID_postfx_params.py","w")
  for i_postfx_param in range(len(postfx_params_list)):
    file.write("pfx_{0:s} = {1:d}\n".format(postfx_params_list[i_postfx_param][0],i_postfx_param))
  file.write("\n\n")
  file.close()

def write_postfx_params(postfx_params_list):
  ofile = open(export_dir + "postfx.txt","w", encoding='utf-8')
  ofile.write("postfx_paramsfile version 1\n")
  ofile.write("{0:d}\n".format(len(postfx_params_list)))
  for postfx_param in postfx_params_list:
    ofile.write("pfx_{0:s} {1:d} {2:d}".format(postfx_param[0], postfx_param[1],postfx_param[2]))
    params_list1 = postfx_param[3]
    params_list2 = postfx_param[4]
    params_list3 = postfx_param[5]
    ofile.write("  {0:f} {1:f} {2:f} {3:f}".format(params_list1[0], params_list1[1], params_list1[2], params_list1[3]))
    ofile.write("  {0:f} {1:f} {2:f} {3:f}".format(params_list2[0], params_list2[1], params_list2[2], params_list2[3]))
    ofile.write("  {0:f} {1:f} {2:f} {3:f}\n".format(params_list3[0], params_list3[1], params_list3[2], params_list3[3]))
  ofile.close()

print("Exporting postfx_params...")
write_postfx_params(postfx_params)
write_python_header(postfx_params)
