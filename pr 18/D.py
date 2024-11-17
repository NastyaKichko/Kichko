def A(s):
    a = []
    l = []
    i = 0
    while i < len(s):
        if s[i].isdigit():
            num = 0
            while i < len(s) and s[i].isdigit():
                num = num * 10 + int(s[i])
                i += 1
            a.append(num)
        elif s[i] == '(':
            l.append(s[i])
            i += 1
        elif s[i] == ')':
            while l[-1] != '(':
                num2 = a.pop()
                num1 = a.pop()
                op = l.pop()
                if op == '+':
                    a.append(num1 + num2)
                elif op == '-':
                    a.append(num1 - num2)
                elif op == '*':
                    a.append(num1 * num2)
                elif op == '/':
                    a.append(num1 // num2)
            l.pop()
            i += 1
        elif s[i] in ['+', '-', '*', '/']:
            while l and l[-1] in ['*', '/'] and s[i] in ['+', '-']:
                num2 = a.pop()
                num1 = a.pop()
                op = l.pop()
                if op == '*':
                    a.append(num1 * num2)
                elif op == '/':
                    a.append(num1 // num2)
            l.append(s[i])
            i += 1
    while l:
        num2 = a.pop()
        num1 = a.pop()
        op = l.pop()
        if op == '+':
            a.append(num1 + num2)
        elif op == '-':
            a.append(num1 - num2)
        elif op == '*':
            a.append(num1 * num2)
        elif op == '/':
            a.append(num1 // num2)
    return a[0]
s = input("Введите выражение: ")
result = A(s)
print("Ответ:", result)
