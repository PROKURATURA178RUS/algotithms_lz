import random as ran

unsorted_list_1 = [ran.randint(0, 1000000) for t in range(100)] #случайные элементы из указанного диапазона
print(unsorted_list_1)
list_2 = unsorted_list_1.copy()
list_1 = unsorted_list_1.copy()

#сортировка пузырьком
score1 = 0 #начинаем подсчет с 0 количество сравнений
stop_flag = True # стоп флаг если он имеет значение true запускает цикл
while stop_flag:
    stop_flag = False # меняем значение true, если программа не сделает изменене она завершиться 
    print(list_1) #промежуточный
    for i in range(len(list_1) - 1): # -1 потому что в дальнейшем мы сравниваем с i + 1 
        score1 += 1 #прибавляем каждый цикл +1
        if list_1[i] < list_1[i + 1]: 
            ap = list_1[i] 
            list_1[i] = list_1[i + 1] #меняем местами
            list_1[i + 1] = ap #меняем местами
            stop_flag = True

#сортировка выбором
score = 0
for a in range(0 ,len(list_2)):
    min = a
    print(list_2) #промежуточный
    for j in range(a + 1,len(list_2)):
        score += 1
        if list_2[j] > list_2[min]:
            min = j
    b = list_2[a]
    list_2[a] = list_2[min]
    list_2[min] = b
print(f"НЕ СОРТИРОВАННЫЙ СПИСОК:{unsorted_list_1}")
print(f"СОРТИРОВАННЫЙ СПИСОК ПУЗЫРЬКОМ:{list_1}")
print(f"СОРТИРОВАННЫЙ СПИСОК ВЫБОРОМ:{list_2}")
print(f'количество сравнений в сортировке пузырьком:{score1}')
print(f'количество сравнений в сортировке выборкой:{score}')