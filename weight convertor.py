weight = int(input("weight:"))
weight_unit =input("(L)bs or (K)g:")
if weight_unit.lower() == "k":
    weightconverted = 2 * weight
    print(f"your weight is {weightconverted} lbs. ")
elif weight_unit.upper() == "L":
    weightconverted = 0.45 * weight
    print(f"your weight is {weightconverted} Kgs.")
else:
    print("invalid input")