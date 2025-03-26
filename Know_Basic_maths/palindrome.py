def Palindrome(n):
  temp=n
  reverse=0
  while temp!=0:
    rem=temp%10
    reverse=reverse*10+rem
    temp=temp//10
  if(reverse==n):
    print("Palindrome")
  else:
    print("Not a plaindrome")  
def input_format():
  n=int(input())
  Palindrome(n)
input_format()  
