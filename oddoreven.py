while True:
    try:
        num = int(input("Enter a number: "))
    except:
        print ("Please enter an integer.")
        continue
    break
test = num%2
if test == 1:
    print ("You have entered an odd number.")
elif num%4 == 0:
    print ("You have entered a multiple of 4.")
else:
    print ("You have entered an even number.")
