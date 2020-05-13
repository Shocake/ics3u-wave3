n = int(input("Enter an integer >= 2"))

if n < 2:
    print("ERROR: Please enter an integer >= 2")

factor = 2
print("The prime factors of", n, "are:")
while factor <= n:
    if n % factor == 0:
        print(factor)
        n = n // factor
    else:
        factor = factor + 1