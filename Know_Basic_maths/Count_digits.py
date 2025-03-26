def Count_digits(str1):
  count=0
  for s in str1:
    if s.isdigit():
      count=count+1
  print(count)    

def input_format():
  str1=input()
  Count_digits(str1)
input_format()  

#2
n=7789
count=0
while n!=0:
  rem=n%10
  count=count+1
  print(rem)
  n=n//10
print(count)  

#3
import math
n=7789094855949484588
count=math.log10(n)
print(int(count+1))

#Time Complexity : O(log10(N))