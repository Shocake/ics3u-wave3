def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, n):
        if not n % i:
            return False
            
    return True

number = int(input("Test if your number is prime:"))
if is_prime(number):
    print("Prime")
else:
    print("Composite")