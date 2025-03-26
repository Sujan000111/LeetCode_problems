def PS(a):
  n=len(a)
  pos=[]
  neg=[]
  for i in range(n):
    if a[i]>0:
      pos.append(a[i])
    else:
      neg.append(a[i]) 
  #(if n is not equal)for i in range(min(len(pos),len(neg))):
  for i in range(n//2):
    a[2*i]=pos[i]
    a[2*i+1]=neg[i]
  print(a)       

def input_format():
  a=list(map(int,input().strip("[]").split(",")))
  PS(a)
input_format()  

