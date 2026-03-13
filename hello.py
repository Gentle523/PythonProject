
score = int(input("Введіть кількість балів (0-100): "))

if score >= 90 and score <= 100:
    print("Відмінно")
elif score >= 70 and score <= 89:
    print("Добре")
elif score >= 50 and score <= 69:
    print("Задовільно")
elif score >= 0 and score <= 49:
    print("Незадовільно")
else:
    print("Помилка: введіть число від 0 до 100")