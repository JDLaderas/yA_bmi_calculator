# 1st input: enter height in meters e.g: 1.65

height = input("What is your height in meter: ")
# 2nd input: enter weight in kilograms e.g: 72

weight = input("What is your height in kg: ")


height_float = float(height)
weight_float = float(weight)

calculation = weight_float / height_float ** 2

calc_round = round(calculation)

print("Your BMI is",calc_round)
