# Python program to check given number is even or odd

# taking input from the user
num = int(input("Enter a number to check if it's even/odd "))

# if number is divisible by 2
if num % 2 == 0:
    print("%d is even number" % num)
else:
    print("%d is odd number" % num)
