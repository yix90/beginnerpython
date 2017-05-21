import random
while True:
    try:
        n = int(input("How many numbers do you want in a list? "))
        r = int(input("Define the range. "))
    except:
        print ("Invalid input.")
        continue
    if n > 100 or r > 1000:
        print ("The number is too large.")
        continue
    break
a = []
b = []
count = 0
while count < n:
    a.append(random.randint(0,r))
    b.append(random.randint(0,r))
    count = count + 1
print (a, "\n", b)
u = raw_input("Press enter to continue.", )
ab = []
for aa in a:
    for bb in b:
        if (aa == bb and bb not in ab):
            ab.append(bb)
print (ab)           
