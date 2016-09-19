#count from 1 to n
#if number is divisible by 3, print "fizz"
#if number is divisible by 5, print "buzz"
#if number is divisible by 3 and 5, print "fizz buzz"

for n in range(1,101):
    if n % 15 == 0:
        print ("fizzbuzz")
    elif n % 5 == 0:
        print ("buzz")
    elif n % 3 == 0:
        print ("fizz")
    else:
        print (n, "Fizzbuzz counting up to 100")
