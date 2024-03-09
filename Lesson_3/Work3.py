'''
                    1. ФУНКЦИИ И МОДУЛИ
    Н-р, у нас имеется прграммный код, в котором некоторые строки повторяюся несколько раз.
    Чтобы каждый раз не прописывать их заново, можно вынести их в отдельный фрагмент кода, т.е. создать функцию
В C# перед названием функции мы указывали ее тип данных, н-р int или void.
В Python нет такого понятия, как функция разных типов или процедура,
все они объединяются в одну функцию с типом def.
    Конструкция функции внутри Python:
def function_name(x):
    # body line 1
        # ...
    # body line n
    # optional return
'''
                        # Задача 1: 
# Необходимо создать функцию sumNumbers(n), которая будет считать
# сумму всех элементов от 1 до n
                        # Решение 1:
'''
    ВАЖНО!!!, сколько аргументов мы передаем, столько и
принимаем. Или наоборот сколько аргументов мы принимаем, столько и передаем.
В нашем случае функция sumNumbers принимает 1 аргумент(n).
'''
    # 1. Необходимо создать функцию:
def sumNumbers(n):

    # 2. Реализовать решение задачи внутри функции
    summa = 0
    for i in range(1, n + 1):   # вызываем функцию range, от 1 до n + 1, 
                                # так как range не включает последний элемент, поэтому указываем n + 1.
        summa += i
    print(summa)

    # 3. Спросим у пользователя число
n = int(input()) # 5
sumNumbers(n) # 15
print()

                        # Решение 2 (используя return):
'''
    return выполняет следующие действия:
- Завершает работу функции
- Возвращает значение
'''
    # 1. Необходимо создать функцию:
def sumNumbers(num):

    # 2. Реализовать решение задачи внутри функции
    summa = 0
    for i in range(1, num + 1):   # вызываем функцию range, от 1 до n + 1, 
                                # так как range не включает последний элемент, поэтому указываем n + 1.
        summa += i
    return summa

    # 3. Спросим у пользователя число
num = int(input()) # 5
print(sumNumbers(num)) # 15


'''
                        2. МОДУЛЬНОСТЬ
    Как работает функция .append?
Это же точно такая же функция, как и sumNumbers(n), но мы ее нигде не создаем,
все дело в том что, это функция автоматически срабатывает и чтобы ей
пользоваться ничего дополнительно писать не надо.
'''
    # 1. Создаем в VSC файл function_file.py (Новый Python файл, в котором находятся функция f(x))
# Код из файла:
    # def fan(x):
    #     if x == 1:
    #         return 'Целое'
    #     elif x == 2.3:
    #         return 23
    #     return # выход из функции

    # 2. В рабочем файле VSC Work3.py
'''
    Чтобы начать взаимодействовать с функцией в файле function_file.py необходимо
добавить эту возможность к себе в программный код. Сначала мы обращаемся к
файлу(без расширения)
    С помощью import мы можем вызвать эту функцию в другом скрипте и дальше
использовать её в новом файле. Можно сократить название функции в рабочем
файле с помощью команды: Alias (псевдоним)
'''
# Код для импорта кода из файла function_file.py:
import function_file
print(function_file.fan(1)) # Целое
print(function_file.fan(2.3)) # 23
print(function_file.fan(28)) # None

# Запись: from function_file import * - означает, 
# что из файла function_file мы хотим импортировать все имеющиеся в нем функции

# Не хотим писать все время длинное название файла,
# воспользуемся командой: Alias (псевдоним), на время работы программы, тогда запись будет следующей:
import function_file as ff
print(ff.fan(1)) # Целое
print(ff.fan(2.3)) # 23
print(ff.fan(28)) # None

'''
                2.1 Значения по умолчанию для функции
P.S. В Python можно перемножать строку на число.
'''
#1.
def new_string(symbol, count):
# В данной функции есть два аргумента: symbol (символ или число) и count (число, на
# которое умножается первый аргумент).
    return symbol * count
print(new_string('!', 5)) # !!!!! - Введены оба аргумента, функция работает без ошибок.
print(new_string('!')) # TypeError missing 1 required ... - Функция выдала ошибку, т.к. мы введи только 1 символ

#2. 
# Можно указать значение переменной count по умолчанию. Например, если
# значение явно не указано (нет второго аргумента), по умолчанию значение
# переменной count равно трем.
def new_string(symbol, count=3): # Указать значение переменной count по умолчанию
    return symbol * count
print(new_string('!', 5)) # !!!!!
print(new_string('!')) # !!!
print(new_string(4)) # 12

'''
        2.2 Возможность передачи неограниченного количества аргументов
● Можно указать любое количество значений аргумента функции.
● Перед аргументом надо поставить *.
'''
#     В примере ниже функция работает СО СТРОКОЙ, поэтому при введении чисел
# программа выдаёт ошибку:
def concatenation(*params):
    res = ""
    for item in params:
        res += item
    return res

print(concatenation('a', 's', 'd', 'w')) # asdw
print(concatenation('a', '1')) # a1
# print(concatenatio(1, 2, 3, 4)) # TypeError: ...


'''
                        3. РЕКУРСИЯ
    Рекурсия в Python аналогична рекурсии в C#.
'''

                        # Задача 2: 
# Пользователь вводит число n. Необходимо вывести n - первых
# членов последовательности Фибоначчи.
                        # Решение:
'''
    При описании рекурсии важно указать, когда функции надо
остановиться и перестать вызывать саму себя. По-другому говоря, необходимо
указать базис рекурсии.
'''
def fib(n): # Внутри функции fib(n), мы сначала задаем (базис) условие для прекращения рукурсии
    if n in [1, 2]: # если число n равно 1 или 2, это означает, 
                    # что первое число и второе число последовательности равны 1.
        return 1    # возвращаем 1
    return fib(n - 1) + fib(n - 2) # складываем 2 предыдущих числа друг с другом и получаем 3-е число.

list_1 = [] # список, в который будем записывать найденные числа
for i in range(1, 10): # Последовательность Ф. выведем из 9 чисел
    list_1.append(fib(i))
print(list_1) # [1, 1, 2, 3, 5, 8, 13, 21, 34]

'''
                        4. АЛГОРИТМЫ
    Алгоритм - набор инструкций для выполнения некоторой задачи.
Рассмотрим 2 самых интересных алгоритмы сортировок:
    ● Быстрая сортировка
    ● Сортировка слиянием
                    4.1  Быстрая сортировка
P.S. “Программирование это разбиение чего-то большого и невозможного на что-то
маленькое и вполне реальное”.

Например, Два друга решили поиграть в игру: один загадывает число от 1 до 100, другой
должен отгадать. Должны весь отрезок поделить пополам, 
получившийся - снова делим на 2 и так до конца.
    Иван загадал число 77.
    Петр: Число больше 50? Иван: Да.
    Петр: Число больше 75? Иван: Да.
    Петр: Число больше 87? Иван: Нет.
    Петр: Число больше 81? Иван: Нет.
    Петр: Число больше 78? Иван: Нет.
    Петр: Число больше 76? Иван: Да
Число оказалось в диапазоне 76 < x < 78, значит это число 77. Задача решена. На
самом деле мы сейчас познакомились с алгоритмом бинарного поиска.
'''
def quicksort(array):  # в качестве параметра функции quicksort передаем массив array
    if len(array) < 2:
        return array
    else:
        pivot = array[0]  # первое значение
    less = [i for i in array[1:] if i <= pivot]  # элементы меньше по размеру
    greater = [i for i in array[1:] if i > pivot]  # элементы больше по размеру
    return quicksort(less) + [pivot] + quicksort(greater) # преобразовали число: pivot в список: [pivot], иначе будет ошибка
print(quicksort([10, 5, 2, 3]))

'''
● 1-е повторение рекурсии:
    ○ array = [10, 5, 2, 3]
    ○ pivot = 10
    ○ less = [5, 2, 3]
    ○ greater = []
    ○ return quicksort([5, 2, 3]) + [10] + quicksort([])
● 2-е повторение рекурсии:
    ○ array = [5, 2, 3]
    ○ pivot = 5
    ○ less = [2, 3]
    ○ greater = []
    ○ return quicksort([2, 3]) + [5] + quicksort([]) # Важно! Не забывайте, что
здесь помимо вызова рекурсии добавляется список [10]
● 3-е повторение рекурсии:
    ○ array = [2, 3]
    ○ return [2, 3] # Сработал базовый случай рекурсии
На этом работа рекурсии завершилась и итоговый список будет выглядеть таким
образом: [2, 3] + [5] + [10] = [2, 3, 5, 10]
Значение [2]просто записывается без рекурсии, т.к. дано для этого условие: (if len(array) < 2)!!!
'''
'''
                    4.2  Сортировка слиянием
'''
def merge_sort(nums):
    if len(nums) > 1:
#делим весь список на 2, до тех пор, пака не останется по 1 элементу
        mid = len(nums) // 2
        left = nums[:mid] # левая часть = i
        right = nums[mid:] # правая часть = j
        # k - конечный список
        merge_sort(left) # рекурсия для левой часть
        merge_sort(right) # рекурсия для правой часть
# Упорядочеваем наш список сравнением элементов из левой и правой части
        i = j = k = 0 # множественное присвоивание
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1
# если в каком-то списке left либо right остались значения, 
# мы добавляем их в конец всего списка:
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1
list = [38, 27, 43, 3, 9, 82, 10]
merge_sort(list)
print(list) # [3, 9, 10, 27, 38, 43, 82]