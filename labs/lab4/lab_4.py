print("Task_1")
def air_conditioner():
    try:
        temperature = float(input("Введите температуру в помещении: "))

        if temperature >= 20:
            print("Кондиционер выключается")
        else:
            print("Кондиционер включается")

    except ValueError:
        print("Ошибка: Введите числовое значение температуры")


air_conditioner()


print("Task_2")
def season_detector():
    try:
        month = int(input("Введите номер месяца (1-12): "))

        if month < 1 or month > 12:
            print("Ошибка: Введите число от 1 до 12")
        elif month in [12, 1, 2]:
            print("Зима")
        elif month in [3, 4, 5]:
            print("Весна")
        elif month in [6, 7, 8]:
            print("Лето")
        else:
            print("Осень")

    except ValueError:
        print("Ошибка: Введите целое число")


season_detector()

print("Task_3")
def dog_to_human_age():
    print("=== Перевод собачьего возраста в человеческий ===")

    try:
        dog_age = float(input("Введите возраст собаки: "))


        if dog_age < 1:
            print("Ошибка: Возраст собаки не может быть меньше 1 года")
            return


        if dog_age > 22:
            print("Ошибка: Слишком большой возраст для собаки (максимум 22 года)")
            return


        if dog_age <= 2:
            human_age = dog_age * 10.5
        else:
            human_age = 2 * 10.5 + (dog_age - 2) * 4

        print(f"Собачий возраст: {dog_age} лет")
        print(f"Эквивалентный человеческий возраст: {human_age} лет")

    except ValueError:
        print("Ошибка: Введите числовое значение возраста")


dog_to_human_age()

print("Task_4")
def check_divisible_by_6():
    print("=== Проверка делимости числа на 6 ===")

    try:
        number = int(input("Введите целое число: "))


        last_digit = abs(number) % 10
        digit_sum = sum(int(digit) for digit in str(abs(number)))

        is_even_last_digit = (last_digit % 2 == 0)
        is_sum_divisible_by_3 = (digit_sum % 3 == 0)

        print(f"Число: {number}")
        print(f"Последняя цифра: {last_digit} ({'чётная' if is_even_last_digit else 'нечётная'})")
        print(f"Сумма цифр: {digit_sum} ({'делится на 3' if is_sum_divisible_by_3 else 'не делится на 3'})")

        if is_even_last_digit and is_sum_divisible_by_3:
            print(f"Результат: Число {number} ДЕЛИТСЯ на 6")
        else:
            print(f"Результат: Число {number} НЕ ДЕЛИТСЯ на 6")

    except ValueError:
        print("Ошибка: Введите целое число")


check_divisible_by_6()

print("Task_5")
def check_password_strength():
    print("\n=== Проверка надежности пароля ===")

    password = input("Введите пароль для проверки: ")


    conditions = {
        "Длина не менее 8 символов": len(password) >= 8,
        "Содержит заглавные буквы латиницы": any(c.isupper() for c in password),
        "Содержит строчные буквы латиницы": any(c.islower() for c in password),
        "Содержит цифры": any(c.isdigit() for c in password),
        "Содержит специальные знаки": any(not c.isalnum() for c in password)
    }

    print("\nРезультат проверки:")

    all_conditions_met = True
    for condition, met in conditions.items():
        status = "+ Выполнено" if met else "- Не выполнено"
        print(f"{status}: {condition}")

        if not met:
            all_conditions_met = False

    print(f"\nОбщий результат: {'+ Пароль надежный' if all_conditions_met else '- Пароль ненадежный'}")


check_password_strength()