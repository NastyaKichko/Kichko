def calculate(expression):
    expression = expression.replace(" ", "")

    num = ""
    result = 0
    operator = None

    for char in expression:
        if char.isdigit():
            num += char
        else:
            if num:
                num = int(num)
                if operator == '+':
                    result += num
                elif operator == '-':
                    result -= num
                elif operator == '*':
                    result *= num
                elif operator == '/':
                    result //= num
                else:
                    result = num
                num = ""
            operator = char


    if num:
        num = int(num)
        if operator == '+':
            result += num
        elif operator == '-':
            result -= num
        elif operator == '*':
            result *= num
        elif operator == '/':
            result //= num
        else:
            result = num

    return result

expression = input("Введите выражение: ")

result = calculate(expression)
print("Ответ:", result)
