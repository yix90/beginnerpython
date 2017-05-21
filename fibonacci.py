def fibogen(n):
  a = 0
  b = 1
  fibolist = []
  count = 0
  while count < n:
    c = a + b
    fibolist.append(c)
    a = b
    b = c
    count = count + 1
  return fibolist
  
def checkint(help_text):
  while True:
    try:
      return int(input(help_text))
    except:
      print("Invalid input!")
      continue

n = checkint("How many numbers do you want to generate?")
print (fibogen(n))
