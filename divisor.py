while True:
    try:
        num = int(input("Enter a number: "))
    except:
        continue
    if num > 1000000:
        print ("The number keyed is too large.")
        continue
    break
a = 1
mul = []
while a <= num:
    if num%a == 0:
        mul.append(a)
    a = a + 1
print ("The multiples of", num, "is", mul)
if len(mul) == 2:
    print (num, "is a prime number.")
