def occurance(s):
  repeated=[]
  non_repeated=[]
  for i in s:
    if s.count(i)>1:
      repeated.append(i)
    else:
      non_repeated.append(i)
  print("repeated",repeated)
  print("non repeated",non_repeated)    
s=input()
occurance(s)    

