# задача 2. Напишите программу для. проверки истинности 
# утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для 
# всех значений предикат.
    
x = input('Введите значение X = ')
y = input('Введите значение Y = ')
z = input('Введите значение Z = ')
first = not (x or y or z)
second = (not x) and (not y) and (not z)
print(first == second)