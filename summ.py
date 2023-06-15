def calculate_average(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return average

# Запрос чисел у пользователя
input_numbers = input("Введите числа, разделенные пробелом: ")
numbers_list = input_numbers.split()

# Преобразование строковых значений в числа
numbers = [float(num) for num in numbers_list]

# Вычисление среднего значения
average = calculate_average(numbers)

# Вывод результата
print("Среднее значение:", average)
