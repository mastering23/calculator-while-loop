
op=""
message = """ 
-----------------------------------------
    Calculator | Basic Math operations
-----------------------------------------
               < Menu 🛸>
| 1) add | 2)sub | 3)mult | 4)div | 00) exit |\n
Type Number :
"""
while op !=00:
  op = int(input(message))

  if (op == 00):
    print("Exit.......")
    break

  num1 = int(input("Enter first Number : "))
  num2 = int(input("Enter first Number : "))

  if(op == 1):
    print(f"{num1} + {num2} = {num1 + num2}")

  if (op == 2):
    print(f"{num1} - {num2} = {num1 - num2}")

  if (op == 3):
    print(f"{num1} x {num2} = {num1 * num2}")

  if (op == 4):
    print(f"{num1} / {num2} = {num1 / num2}")

