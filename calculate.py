more = '1'
print("Для возведения в степень нажмите 'z'>>")
while more == '1':
    x_num = int(input("Введите первое число>>"))
    act = input("Введите операцию>>")
    y_num = int(input("Введите второе число"))
    if act == '+':
            print (x_num + y_num)
    elif act == '-':
            print (x_num - y_num)
    elif act == '-':
            print (x_num - y_num)
    elif act == '*':
            print (x_num * y_num)
    elif act == '/':
            print (x_num / y_num)
    elif act == '%':
            print (x_num * y_num /100)
    elif act == 'z':
            print (x_num ** y_num)    
    else:
            print ("Некорректная операция")
more = input("Для продолжения использования нажмите '1'>>")
