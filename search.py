import random # Импортируем библиотеку random

spisok = random.sample(range(0,1_000_000), 100) # Создадим список из уникальных элементов
spisok.sort()# Отсортируем список
print('Отсортированный список:', spisok)

target = int(input("Введите число: "))# Введем нужное нам число

# Линейный поиск
lin = -1     
linsravn = 0  

for index in range(len(spisok)):
    linsravn += 1
    if spisok[index] == target:
        lin = index
        break 

# Выведем результат линейного поиска
if lin != -1:             
    print(f"Элемент {target} найден на индексе {lin}.")
    print(f"Количество сравнений (линейный поиск): {linsravn}")
else:
    print(f"Элемент {target} не найден.")
    print(f"Количество сравнений (линейный поиск): {linsravn}")

# Бинарный поиск
bin = -1
binsravn = 0  
left, right = 0, len(spisok) - 1


while left <= right:
    binsravn += 1
    mid = left + (right - left) // 2

    if spisok[mid] == target:
        index_binary = mid
        break  
    elif spisok[mid] < target:
        left = mid + 1
    else:
        right = mid - 1

# Выведем результат бинарного поиска
if bin != -1:
    print(f"Элемент {target} найден на индексе {bin}.")
    print(f"Количество сравнений (бинарный поиск): {binsravn}")
else:
    print(f"Элемент {target} не найден.")
    print(f"Количество сравнений (бинарный поиск): {binsravn}")