try:
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
except ValueError:
    print("Ошибка: введите корректные числа.")
    exit()

a_int = int(a)
b_int = int(b)

print("1. + Сложение")
print("2. - Вычитание")
print("3. * Умножение")
print("4. / Деление")
print("5. // Целочисленное деление")
print("6. % Остаток от деления")
print("7. ** Возведение в степень")
print("8. == Равно")
print("9. != Не равно")
print("10. > Больше")
print("11. < Меньше")
print("12. >= Больше или равно")
print("13. <= Меньше или равно")
print("14. and Логическое И")
print("15. or Логическое ИЛИ")
print("16. not Логическое НЕ")
print("17. & Побитовое И")
print("18. | Побитовое ИЛИ")
print("19. ^ Побитовое ИСКЛЮЧАЮЩЕЕ ИЛИ")
print("20. ~ Побитовое НЕ")
print("21. << Сдвиг влево")
print("22. >> Сдвиг вправо")

choice = input("Введите номер операции: ")

if choice == '1':
    result = a + b
    print(result)
elif choice == '2':
    result = a - b
    print(result)
elif choice == '3':
    result = a * b
    print(result)
elif choice == '4':
    if b == 0:
        print("Ошибка")
    else:
        result = a / b
        print(result)
elif choice == '5':
    if b == 0:
        print("Ошибка")
    else:
        result = a // b
        print(result)
elif choice == '6':
    if b == 0:
        print("Ошибка")
    else:
        result = a % b
        print(result)
elif choice == '7':
    result = a ** b
    print(result)
elif choice == '8':
    result = a == b
    print(result)
elif choice == '9':
    result = a != b
    print(result)
elif choice == '10':
    result = a > b
    print(result)
elif choice == '11':
    result = a < b
    print(result)
elif choice == '12':
    result = a >= b
    print(result)
elif choice == '13':
    result = a <= b
    print(result)
elif choice == '14':
    result=a > 0 ,b > 0
    print ((a>0), " " , (b>0))
elif choice == '15':
    result = (a > 0) or (b > 0)
    print ((a>0), " " , (b>0))
elif choice == '16':
    result = not (a > 0)
    print(result)
elif choice == '17':
    result = a_int & b_int
    print(result)
elif choice == '18':
    result = a_int | b_int
    print(result)
elif choice == '19':
    result = a_int ^ b_int
    print(result)
elif choice == '20':
    result = ~a_int
    print(result)
elif choice == '21':
    result = a_int << b_int
    print(result)
elif choice == '22':
    result = a_int >> b_int
    print(result)
else:
    print("Ошибка: неверный выбор операции.")