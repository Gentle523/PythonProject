import random
secret_number = random.randint(1, 10)
guess = 0
print("Я думаю о цифрі від одного до десятого")
while guess != secret_number:
    guess = int(input("ведідь ваше число: "))
    if guess < secret_number:
        print("Більше!")
    elif guess > secret_number:
        print("Менше!")
    else:
        print("Ти виграв!")