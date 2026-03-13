print("--- Калькулятор CASIO 430 ---")
num1 = float(input("Перше число: "))
op = input("Дія (+, -, *, /): ")
num2 = float(input("Друге число: "))

if op == "+":
    print(f"Результат: {num1 + num2}")
elif op == "-":
    print(f"Результат: {num1 - num2}")
elif op == "*":
    print(f"Результат: {num1 * num2}")
elif op == "/":
    if num2 != 0:
        print(f"Результат: {num1 / num2}")
    else:
        print("Помилка: Ділення на нуль!")
else:
    print("Невідома операція")