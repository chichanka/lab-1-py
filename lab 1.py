# Завдання 1: Створення чотирьох змінних та присвоєння їм значень
a = float(input("Введіть перше число: "))
b = float(input("Введіть друге число: "))
c = float(input("Введіть третє число: "))
d = float(input("Введіть четверте число: "))

# Завдання 2: Виконання арифметичних операцій
addition = a + b
subtraction = c - d
multiplication = a * c
division = b / d
exponentiation = a ** b
integer_division = c // a
modulus = d % b

# Заносимо результати в список
results = [addition, subtraction, multiplication, division, exponentiation, integer_division, modulus]

# Завдання 3: Визначення кількості елементів у списку та виведення парних елементів
num_elements = len(results)
print("Кількість елементів у списку:", num_elements)
print("Парні елементи списку:")
for item in results:
    if isinstance(item, int) and item % 2 == 0:
        print(item)

# Завдання 4: Заміна місцями другого і п'ятого елементів списку
results[1], results[4] = results[4], results[1]
print("Список після заміни другого і п'ятого елементів:", results)

# Завдання 5: Введення імені та прізвища, виведення повідомлення
name = input("Введіть ваше прізвище та ім'я: ")
print("Виконавець даної лабораторної роботи:", name)
print("Висновки по роботі:")
print("1. Навчилися працювати зі змінними та функцією input.")
print("2. Ознайомилися з основними арифметичними операціями в Python.")
print("3. Навчилися працювати зі списками та їх елементами.")
print("4. Розглянули методи виведення інформації на екран.")
