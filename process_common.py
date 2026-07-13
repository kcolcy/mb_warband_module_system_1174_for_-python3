
def convert_to_identifier(s0):
  s1 = s0.replace(" ","_")
  s2 = s1.replace("'","_")
  s3 = s2.replace("`","_")
  s4 = s3.replace("(","_")
  s5 = s4.replace(")","_")
  s6 = s5.replace("-","_")
  s7 = s6.replace(",","")
  s8 = s7.replace("|","")
  s9 = s8.replace("\t","_") #Tab
  s10 = s9.lower()
  return s10

def convert_to_identifier_with_no_lowercase(s0):
  s1 = s0.replace(" ","_")
  s2 = s1.replace("'","_")
  s3 = s2.replace("`","_")
  s4 = s3.replace("(","_")
  s5 = s4.replace(")","_")
  s6 = s5.replace("-","_")
  s7 = s6.replace(",","")
  s8 = s7.replace("|","")
  s9 = s8.replace("\t","_") #Tab
  return s9

def replace_spaces(s0):
  return s0.replace("\t","_").replace(" ","_")
