height = int(input("Enter the height of the triangle: "))

for i in range(height):
    for j in range(height - i - 1):
        print(" ", end="")
    for j in range(2 * i + 1):
        print("*", end="")
    print()
