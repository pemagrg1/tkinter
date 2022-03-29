"""A Palindrome number is a number which reverse is equal to the original number means number itself.
For example : 121, 111, 1223221, etc."""

# using the same logic from reversing a number,
n = int(input("please give a number : "))
temp = n
reverse = 0
while n != 0:
    reverse = reverse*10 + n % 10
    n = (n//10)

print(reverse)
if reverse == temp:
    print("It's a Palindrome")
else:
    print("The given number is not a Palindrome")
