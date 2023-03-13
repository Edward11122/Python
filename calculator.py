def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

def modular(a, b):
    return a % b

print("1. add")
print("2. sub")
print("3. mul")
print("4. div")
print("5. modular")

select = input("Enter your choice (1/2/3/4/5): ")

num1 = float(input("input first number :"))
num2 = float(input("input second number :"))

if select == '1':
    print(add(num1, num2))
elif select == '2':
    print(sub(num1, num2))
elif select == '3':
    print(mul(num1, num2))
elif select == '4':
    print(div(num1, num2))
elif select == '5':
    print(modular(num1, num2))
else:
    print("error")