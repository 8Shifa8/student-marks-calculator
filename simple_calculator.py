expr = input("Enter expression (eg: 5+3*2):").strip()
allowed_charas = "0123456789+-*/()"

if all(i in allowed_charas for i in expr):
    print(eval(expr))

else:
    print("Invalid Syntax")
