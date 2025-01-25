def calculator():
    print("Добро пожаловать в калькулятор!")
    print("Доступные операции: +, -, *, /")
    
    while True:
        try:
            num1 = float(input("Введите первое число: "))
            operator = input("Введите операцию (+, -, *, /): ")
            num2 = float(input("Введите второе число: "))

            if operator == "+":
                result = num1 + num2
            elif operator == "-":
                result = num1 - num2
            elif operator == "*":
                result = num1 * num2
            elif operator == "/":
                if num2 == 0:
                    print("Ошибка: деление на ноль!")
                    continue
                result = num1 / num2
            else:
                print("Неверный оператор! Попробуйте снова.")
                continue

            print(f"Результат: {num1} {operator} {num2} = {result}")
        except ValueError:
            print("Ошибка: введите числовые значения!")
        
        again = input("Хотите выполнить еще одну операцию? (да/нет): ").lower()
        if again != "да":
            print("Спасибо за использование калькулятора!")
            break

calculator()
