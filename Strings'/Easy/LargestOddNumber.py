def LargestOdd(str1):
  n=int(str1)
  if n%2==0:
    temp=n
    max=0
    while temp>0:
      rem=temp%10
      temp=temp//10
      if rem%2!=0 :
        if rem>max:
          max=rem
    return max 
  else:
    return n

str1=input()
if LargestOdd(str1) ==0:
  print('""')
else:
  print(f"{str(LargestOdd(str1))}")  
        
#or
def largest_odd_substring(num: str) -> str:
    # Traverse the string from right to left to find the last odd digit
    for i in range(len(num) - 1, -1, -1):
        if int(num[i]) % 2 == 1:  # Check if the digit is odd
            return num[:i+1]  # Return substring from start to this odd digit
    return ""  
num=input()
print(largest_odd_substring(num))        