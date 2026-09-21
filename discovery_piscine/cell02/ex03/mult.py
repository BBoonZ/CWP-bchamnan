number_1 = int(input("Enter the first nubmer:\n"))
number_2 = int(input("Enter the second nubmer:\n"))

result = number_1 * number_2

print(f"{number_1} x {number_2} = {result}")

if result == 0:
    print("The result is positive and negative.")
elif result > 0:
    print("This result is positive.")
elif result < 0:
    print("The result is negative.")
