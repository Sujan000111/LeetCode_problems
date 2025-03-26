def Armstrong(n):
  temp=n
  p=len(str(n))
  result=0
  while temp!=0:
    rem=temp%10
    result=result+(rem**p)
    temp=temp//10
  return result
n=int(input())
if(Armstrong(n)==n):
  print("yes")
elif(Armstrong(n)!=n):
  print('No')    

