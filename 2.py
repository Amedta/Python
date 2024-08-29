x = int(input("Enter integer:"))
if -100 <= x <= 100:
    if x >= 0:
        print(f"x = {x} \n{x} is a natural number")
    else:
        print(f"x = {x}")
else:
    print("The number is out of the allowed range (-100 to 100).")
