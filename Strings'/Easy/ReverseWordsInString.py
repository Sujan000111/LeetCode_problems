def ReverseWords(str1):
  return " ".join(str1.split()[::-1])
str1=input()
print(ReverseWords(str1))