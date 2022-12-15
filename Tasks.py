""" Задайте список из четных элементов """
# data = [x for x in range(10)]
# res = list(filter(lambda x: not x%2, data))
# print(res)

""" Задайте список из N элементов, заполненных числами из
промежутка [-N, N].
Найдите произведение элементов на указанных позициях. 
Позиции хранятся в файле file.txt в одной строке одно число. """
# num = int(input('Введите число '))
# lst = [i for i in range(-num, num+1)]
# sum = 1
# with open('text') as text:
#     index = list(map(int, text.readlines()))
# for i in range(len(index)):
#     sum *= lst[index[i]]
# print(lst)
# print(sum)


""" Задайте последовательность чисел. Напишите программу,
которая выведет список неповторяющихся элементов исходной последовательности. """
 
# import random 
# lst = []
# res = []

# lst = [random.randint(1,10) for i in range(random.randint(2, 10))]
# print(lst)

# for i in range(len(lst)):
#     if lst.count(lst[i]) == 1:
#         res.append(lst[i])
# print(res)





