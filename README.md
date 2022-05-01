# SPbU python course
homework assignments for the Python programming course

### Задание №1

1. Реализовать функции для работы с векторами (скалярное произведение, вычисление длины, нахождение угла между ними)
   и матрицами (транспонирование, сложение, произведение).
2. Реализовать функции, имитирующие работу bash команд – wc, nl, head, tail.

### Задание №2

Частичное применение (каррирование, curry) - это превращение функции от нескольких параметров в функцию от одного
параметра, возвращающую функцию от остальных параметров. К ней существует обратная операция - uncarry. В Python
каррирование в таком виде затруднено из-за произвольной арности.

Напишите функцию curry_explicit(function, arity) и парную к ней uncurry_explicit(function, arity).

### Задание №3

1. Реализовать свой семафор через менеджеров контекстов. Применить его для чтения / записи в Dict однозначно обезопасив
   его для мультитретинга

    - https://github.com/google/styleguide/blob/91d6e367e384b0d8aaaf7ce95029514fcdf38651/pyguide.md#218-threading
2. Используя asyncio реализовать асинхронное скачивание картинок с сайта
   (для парсинга html взять bs4). Каждая картинка должна скачиваться в отдельной корутине. Число скачиваний — аргумент
   cli. 
    - https://www.thisfuckeduphomerdoesnotexist.com
    - https://github.com/google/styleguide/blob/91d6e367e384b0d8aaaf7ce95029514fcdf38651/pyguide.md#218-threading

### Задание №6

1. Table Analytics
2. Chart Visualization

- https://datalore.jetbrains.com/notebook/wdtBD26wbVkWRnpHbv69IN/KOwVEJ2dVahgy1dV5eRKvU
