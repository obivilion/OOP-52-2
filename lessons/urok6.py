# # Множественное наследование
# # BIG о нотация
# # MRO (Method Resolution Order)
#
# class Aminol:
#     def action(self):
#         return print("Some action")
#
# class Flyable(Aminol):
#     def fly(self):
#         return print("Fly")
#
# class Swimmble(Aminol):
#     def swim(self):
#         return print("Swim")
#
# class Duck(Flyable, Swimmble):
#     def make_sound(self):
#         return print("Krya krya")
#
# Donald_Macduck = Duck()
# Donald_Macduck.fly()
# Donald_Macduck.swim()
# Donald_Macduck.make_sound()
# Donald_Macduck.action()
# Donald_Macduck.action()
from doctest import run_docstring_examples


# BIG O нотация - это способ описания сложности алгоритмов. Она показывает ,
# как время выполнения или использования памяти увеличивается при росте размера входных данных

#  0(1) - Константная сложность

def get_element(list, index):
    return list[index]

list1=[1,2,3,4,5,6,7,8,9,10]
# print(get_element(list, 3))

#  0(n) - Линейная сложность

def find_element(lst, target):
    for i in lst:
        if i == target:
            return i

# print(find_element(list1, 4))

#  0(log n) - Логарифмическая сложность

def binary_search(lst, target):
    left , right = 0, len(lst) - 1

    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
print(binary_search(list1, 6))


#  0(n®) - Квадратичная сложность

def bubble_sort(lst):
    n = len(lst)

    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]

list2 = [9,2,5,32,66,11,77,334,12,99,221,33,99,12,33,455,]

bubble_sort(list2)
print(list2)

