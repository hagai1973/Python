# weight = 86
# height = 1.71
weight = float(input("Type your weight: "))
height = float(input("Type your height (x.xx): "))

bmi = round((weight/(height**2)),2)
print(f"Your BMI is: {bmi}")

if bmi<18.5:
 print("You are underweight")
elif bmi >=18.5 and bmi < 25:
 print("You are in Normal range")
elif bmi>=25 and bmi<30:
  print("You are in overweight range")
elif bmi>=30 and bmi<35:
  print("You are in obes range")
else:
  print("You are in clinically obes range")

