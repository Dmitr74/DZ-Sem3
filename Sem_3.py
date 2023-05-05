# Задача 16: 
# Требуется вычислить, сколько раз встречается некоторое число X в списке A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*
# 5
#     1 2 3 4 5
#     3
#     -> 1

'''
N = int(input('Введите длинну списка: '))

# from random import sample			            # вариант с рандомным НЕ повторяемым заполнением списка 
# list_A = sample(range(1,N+1), N)

# list_A = list(range(1,N+1))			        # вариант с заполнением списка по порядку


from random import randint			            
list_A = [randint(1,N+1) for i in range(N)]
print (list_A)

X = int(input('Введите искомое число Х: '))
count = 0
for i in range(0,len(list_A)):
    if X == list_A [i]: 
        count += 1
        
print ('Число Х встречается', count, 'раз.')
'''



# Задача 18: 
# Требуется найти в списке A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в списке. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5

N = int(input('Введите длинну списка: '))
X = int(input('Введите искомое число Х: '))

from random import randint			            
list_A = [randint(1,N+1) for i in range(N)]
print (list_A)

for i in range(0,len(list_A)):
    if X == list_A [i]: 
        print ('Число до X:', list_A [i-1], 'Число после X:',list_A [i+1])
        
        


# Задача 20: 
# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. 
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко; D, G – 2 очка; B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; 
# K – 5 очков; J, X – 8 очков; Q, Z – 10 очков. 
# А русские буквы оцениваются так: 
# А, В, Е, И, Н, О, Р, С, Т – 1 очко; Д, К, Л, М, П, У – 2 очка; Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; 
# Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков. 
# Напишите программу, которая вычисляет стоимость введенного пользователем слова. 
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

# *Пример:*
# ноутбук
#     12