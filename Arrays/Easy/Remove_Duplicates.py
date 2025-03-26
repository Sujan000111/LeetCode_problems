def remove_duplicates(a):
  a=set(a)
  print(list(a))
  print(len(a))    

def input_format():
  a=list(map(int,input().strip('[]').split(",")))
  remove_duplicates(a)
input_format()  