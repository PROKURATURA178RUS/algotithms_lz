import random # Добавим библиотеку random

print('Сортировка пузырьком:') # Создадим список для сортировки пузырьком
bubble = [random.randint(0, 1_000_000) for _ in range(100)]
bubble_n = bubble.copy()
bubblesravnenie = 0
n = len(bubble)
print('Исходный список:',bubble)


for i in range(n):          # Цикл для сортировки пузырьком
    for j in range(0, n-i-1):
        bubblesravnenie += 1
        if bubble_n[j] < bubble_n[j+1]:  
            bubble_n[j], bubble_n[j+1] = bubble_n[j+1], bubble_n[j]
    print(f"Шаг {i + 1}: {bubble_n}")


print("Отсортированный список (пузырьком):", bubble_n) # Вывод данных
print("Количество сравнений (пузырьком):", bubblesravnenie)


print('Сортировка выбором:') # Создадим список для сортировки выбором
choose = [random.randint(0, 1_000_000) for _ in range(100)]
choose_n = choose.copy()
choosesravnenie = 0
n = len(choose)
print('Исходный список:',choose)


for i in range(n):     # Цикл для сортировки выбором
    max_index = i
    for j in range(i + 1, n):
        choosesravnenie += 1
        if choose_n[j] > choose_n[max_index]:  
            max_index = j
    choose_n[i], choose_n[max_index] = choose_n[max_index], choose_n[i]
    print(f"Шаг {i + 1}: {choose_n}")


print("Отсортированный список (выбором):", choose_n) # Вывод данных
print("Количество сравнений (выбором):", choosesravnenie)