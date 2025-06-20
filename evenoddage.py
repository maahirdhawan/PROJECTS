try:
    age = int(input("Enter your age: "))
    if (age%2) == 0:
        print("even number")
    else:
        print("Odd number")
    print(aege)
except ValueError as ex:
    print("Please enter an interger as this is an ",ex)
except NameError as ey:
    print(ey)
    
    

