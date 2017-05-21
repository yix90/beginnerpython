def listends(a):
  b =[]
  b.append(a[0])
  b.append(a[-1])
  return b
  
userlist = []
print ("Enter a few numbers into a list. Type quit to finish.")
while True:
  inp = input()
  if inp == "quit":
    break
  try:
   int(inp)
  except:
    print ("Enter a number!")
    continue
  userlist.append(inp)

#Print the ends
print (listends(userlist))
