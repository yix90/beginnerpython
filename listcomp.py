a = []
while len(a) < 10:
  try:
    inp= int(input("Enter 10 numbers into a list:"))
  except:
    print ("Enter an integer!")
    continue
  a.append(inp)

b = [num for num in a if num%2 == 0]
print (a, b)
