def Reverse(n):
  reverse=0
  while n!=0:
    rem=n%10
    reverse=reverse*10+rem
    n=n//10
  print(reverse)  

def input_format():
  n=int(input())
  Reverse(n)
input_format()  
