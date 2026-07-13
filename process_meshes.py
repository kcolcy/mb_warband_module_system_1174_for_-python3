from header_common import *
from module_info import *
from module_meshes import *

from process_common import *

def save_meshes():
  ofile = open(export_dir + "meshes.txt","w", encoding='utf-8')
  ofile.write("{0:d}\n".format(len(meshes)))
  for i_mesh in range(len(meshes)):
    mesh = meshes[i_mesh]
    ofile.write("mesh_{0} {1} {2} {3:.6f} {4:.6f} {5:.6f} {6:.6f} {7:.6f} {8:.6f} {9:.6f} {10:.6f} {11:.6f}\n".format(mesh[0],mesh[1],replace_spaces(mesh[2]),mesh[3],mesh[4],mesh[5],mesh[6],mesh[7],mesh[8],mesh[9],mesh[10],mesh[11]))
  ofile.close()

def save_python_header():
  ofile = open("./ID_meshes.py","w")
  for i_mesh in range(len(meshes)):
    ofile.write("mesh_{0:s} = {1:d}\n".format(meshes[i_mesh][0],i_mesh))
  ofile.write("\n\n")
  ofile.close()

print("Exporting meshes...")
save_python_header()
save_meshes()
