def ReverseWords(s):
  reverseWords=" ".join(s.split()[::-1])
  return reverseWords
s=input()
print(ReverseWords(s))