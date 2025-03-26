def Armstrong(n):
  temp=n
  arm=0
  l=len(str(n))
  while temp!=0:
    rem=temp%10
    arm=arm+(rem**l)
    temp=temp//10
  if n==arm:
    print("Armstrong")
  else:
    print('Not an Armstrong')    

def input_format():
  n=int(input())
  Armstrong(n)
input_format()  