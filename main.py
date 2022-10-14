
#1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# text = list('Напишите программуабв, удаляющую изабв текста всеабв слова, содеражщие "абв"'.split())
#
# print(list(filter(lambda i: 'абв' not in i, text)))

#2. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются забравшему последние конфеты.
# Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?

from random import *
#
# player1 = input('Введите имя Игрока 1: ')
# player2 = input('Введите имя Игрока 2: ')
# turn = bool(randint(0, 2))
# candies = 2021
#
# while candies > 0:
#     print('Осталось конфет:', candies)
#     if turn:
#         player_turn = int(input(f'Ход Игрока 1, {player1}: '))
#         if player_turn > 28:
#             print('Вы взяли больше 28 конфет, возьмите меньше')
#             continue
#         candies -= player_turn
#         turn = not turn
#     else:
#         if player_turn > 28:
#             print('Вы взяли больше 28 конфет, возьмите меньше')
#             continue
#         candies -= int(input(f'Ход Игрока 2, {player2}: '))
#         turn = not turn
# if turn:
#     print('Победил Игрок 2')
# else:
#     print('Победил Игрок 1')
#
# print('Игра закончена')

# a) Добавьте игру против бота

# from random import *
#
# player1 = input('Введите имя Игрока 1: ')
# print('Игрок 2 - БОТ')
# turn = bool(randint(0, 2))
# candies = 50
# bot_turn = 1
#
# while candies > 0:
#     print('Осталось конфет:', candies)
#     if turn:
#         player_turn = int(input(f'Ход Игрока 1, {player1}: '))
#         if player_turn > 28:
#             print('Вы взяли больше 28 конфет, возьмите меньше')
#             continue
#         candies -= player_turn
#         turn = not turn
#     else:
#         bot_turn = randint(1, 28)
#         print("Ход Бота: ", bot_turn)
#         candies -= bot_turn
#         turn = not turn
# if turn:
#     print('Победил Бот')
# else:
#     print('Победил Игрок 1')
#
# print('Игра закончена')

# b) Подумайте как наделить бота ""интеллектом""
# пыталась сделать бота, который всегда будет выигрывать через остаток от деления, но не получается

# player1 = input('Введите имя Игрока 1: ')
# print('Игрок 2 - БОТ')
# start_candies = int(input('Всего конфет в начале игры: '))
# max_candies_turn = int(input('Количество конфет, которые можно взять за 1 ход: '))
# turn = bool(randint(0, 2))
# candies = start_candies
# bot_turn = 1
#
# while candies > 0:
#     print('Осталось конфет:', candies)
#     if turn:
#         player_turn = int(input(f'Ход Игрока 1, {player1}: '))
#         if player_turn > 28:
#             print('Вы взяли больше 28 конфет, возьмите меньше')
#             continue
#         candies -= player_turn
#         turn = not turn
#     else:
#         bot_turn = start_candies % (max_candies_turn + 1)
#         print("Ход Бота: ", bot_turn)
#         candies -= bot_turn
#         turn = not turn
# if turn:
#     print('Победил Бот')
# else:
#     print('Победил Игрок 1')
#
# print('Игра закончена')

#3. Создайте программу для игры в ""Крестики-нолики"".
# Честно скажу, игра была взята на просторах интернета, эта версия мне показалась самой понятной
#
# # Инициализация карты
# maps = [1, 2, 3,
#         4, 5, 6,
#         7, 8, 9]
#
# # Инициализация победных линий
# victories = [[0, 1, 2],
#              [3, 4, 5],
#              [6, 7, 8],
#              [0, 3, 6],
#              [1, 4, 7],
#              [2, 5, 8],
#              [0, 4, 8],
#              [2, 4, 6]]
#
#
# # Вывод карты на экран
# def print_maps():
#     print(maps[0], end=" ")
#     print(maps[1], end=" ")
#     print(maps[2])
#
#     print(maps[3], end=" ")
#     print(maps[4], end=" ")
#     print(maps[5])
#
#     print(maps[6], end=" ")
#     print(maps[7], end=" ")
#     print(maps[8])
#
#
# # Сделать ход в ячейку
# def step_maps(step, symbol):
#     ind = maps.index(step)
#     maps[ind] = symbol
#
#
# # Получить текущий результат игры
# def get_result():
#     win = ""
#
#     for i in victories:
#         if maps[i[0]] == "X" and maps[i[1]] == "X" and maps[i[2]] == "X":
#             win = "X"
#         if maps[i[0]] == "O" and maps[i[1]] == "O" and maps[i[2]] == "O":
#             win = "O"
#
#     return win
#
# # Основная программа
# game_over = False
# player1 = True
#
# while game_over == False:
#
#     # 1. Показываем карту
#     print_maps()
#
#     # 2. Спросим у играющего куда делать ход
#     if player1 == True:
#         symbol = "X"
#         step = int(input("Человек 1, ваш ход: "))
#     else:
#         symbol = "O"
#         step = int(input("Человек 2, ваш ход: "))
#
#     step_maps(step, symbol)  # делаем ход в указанную ячейку
#     win = get_result()  # определим победителя
#     if win != "":
#         game_over = True
#     else:
#         game_over = False
#
#     player1 = not (player1)
#
# # Игра окончена. Покажем карту. Объявим победителя.
# print_maps()
# print("Победил", win)

#4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

with open('decoded.txt', 'r') as data:
    my_text = data.read()

def encode_rle(ss):
    str_code = ''
    prev_char = ''
    count = 1
    for char in ss:
        if char != prev_char:
            if prev_char:
                str_code += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    return str_code

str_code = encode_rle(my_text)
print('Изначальный текст:', my_text)
print('Закодированный текст:', str_code, '\n')

with open('encoded.txt', 'r') as data:
    my_text2 = data.read()

def decoding_rle(ss:str):
    count = ''
    str_decode = ''
    for char in ss:
        if char.isdigit():
            count += char
        else:
            str_decode += char * int(count)
            count = ''
    return str_decode

str_decode = decoding_rle(my_text2)
print('Изначальный текст:', my_text2)
print('Раскодированный текст:', str_decode)
