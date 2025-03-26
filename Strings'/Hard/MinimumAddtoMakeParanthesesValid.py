def minAddToMakeValid(s):
  balance=0
  moves=0
  for char in s:
    if char=="(":
      balance=balance+1
    else:
      if balance>0:
        balance=balance-1 
      else:
        moves=moves+1
  return moves+balance
s=input()
print(minAddToMakeValid(s))         