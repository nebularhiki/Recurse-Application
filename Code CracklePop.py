# Write a program that prints out the numbers 1 to 100 (inclusive).
# If the number is divisible by 3, print Crackle instead of the number.
# If it's divisible by 5, print Pop. If it's divisible by both 3 and 5, print CracklePop.

n = 1

while n <= 100:
    if (n % 3 == 0) and (n % 5 == 0):
        print("CracklePop")
        n += 1
    else:
        if n % 3 == 0:
            print("Crackle")
            n += 1
        else:
            if n % 5 == 0:
                print("Pop")
                n += 1
            else:
                print(n)
                n += 1
