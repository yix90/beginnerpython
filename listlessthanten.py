a = list()
count = 0
while count < 10:
    try:
        b = int(input("Enter 10 integers in sequence: "))
    except:
        print ("Enter a number!")
        continue
    if b > 999:
        print ("The number you have entered is too large, please try again.")
        continue
    if b < 0:
        print ("Please enter a positive integer.")
        continue
    a.append(b)
    count = count + 1
print (a)
b = list ()
while True:
    try: test = int(input("Now enter a number: "))
    except:
        print ("Enter a number!")
        continue
    break
for num in a:
    if num > test:
        continue
    else:
        b.append(num)
print ("This series of numbers ", b, "is smaller than", test)
