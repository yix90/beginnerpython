import random

x = ""
n = int(input("Enter the number of characters:"))
while len(x) < n:
  y = random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-=`~!@#$%^&*()_+[];,./<>?:"{}')
  x = x + y

print (x)
