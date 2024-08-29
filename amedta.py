def factoral(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    fact = 1
    for i in range(1, int(n) + 1):
        fact *= i
    return fact

# Example usage:
num = int(input("Enter your number: "))
print("Factorial of", num, ":", end=" ")
print(factoral(num))
