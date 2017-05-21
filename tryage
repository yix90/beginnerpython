from datetime import date

thisyear = date.today().year

print ("What is your age?")
while True:
    in_age = input()
    if in_age.startswith('no'):
        print ("screwyouuu")
        continue
    try:
        age = int(in_age)
    except:
        print ("Invalid input, please type in an integer:")
        continue
    break
print ("Your age is", age)

print ("You will be 100 years old in the year", thisyear+(100-age))
