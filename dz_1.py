def largest_division(first_number, second_number):
    
    # Если первое или второе число = 0, то функция возращает наибольшее число из них
    
    if first_number == 0 or second_number == 0:
        return max(first_number, second_number)
    
    # Если первое число больше второго, то функция возращает разницу первого и второго числа 
    elif first_number > second_number:
        return largest_division(first_number - second_number, second_number)
    
    # Если первое число меньше второго, то функция возращает разницу второго и первого числа
    else:
        return largest_division(first_number, second_number - first_number)
    
    
number1 = int(input("Введите первое число >>>> "))
number2 = int(input("Введите второе число >>>> "))
print(largest_division(number1, number2))