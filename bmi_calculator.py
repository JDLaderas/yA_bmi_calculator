# 1st input: enter height in meters e.g: 1.65

height = input()
# 2nd input: enter weight in kilograms e.g: 72

weight = input()


height_str = int(height)
weight_str = int(weight)

calculation = weight_str / (height_str * height_str)

print(calculation)
