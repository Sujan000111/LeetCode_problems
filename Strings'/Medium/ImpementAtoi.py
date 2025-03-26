def Atoi(s):
  result=0
  sign=1
  if s[0]=='-':
    sign=-1
    s=s[1:]
  
  for i in s:

    n=ord(i)-ord('0')
    result=result*10+n
  if str(result)==s:
    print("valid")
  else:
    print("Invalid")
s=input()
Atoi(s)    