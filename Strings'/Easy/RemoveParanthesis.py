def RemoveParanthesis(str1):
  result=[]
  depth=0
  for i in str1:
    if i=="(":
      if depth>0:
        result.append(i)
      depth=depth+1
    elif i==")":
      depth=depth-1
      if depth>0:
        result.append(i)  
  return "".join(result)        
        

def input_format():
  str1=input()
  print(RemoveParanthesis(str1))
input_format()  

