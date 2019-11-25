weight = int(input("please enter your weight"))
measure = input("enter P or K ")
if measure.upper() == "P":
    weight = weight*2
    print(f"you weight ${weight} pound")
elif measure.upper() == "K":
    weight = weight-2
    print(f"you weight {weight} kilograms")
