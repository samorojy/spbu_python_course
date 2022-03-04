# SPbU python course

### Задание №1

1. Реализовать функции для работы с векторами (скалярное произведение, вычисление длины, нахождение угла между ними)
   и матрицами (транспонирование, сложение, произведение).
2. Реализовать функции, имитирующие работу bash команд – wc, nl, head, tail.

### Задание №2

Частичное применение (каррирование, curry) - это превращение функции от нескольких параметров в функцию от одного
параметра, возвращающую функцию от остальных параметров. К ней существует обратная операция - uncarry. В Python
каррирование в таком виде затруднено из-за произвольной арности.

Напишите функцию curry_explicit(function, arity) и парную к ней uncurry_explicit(function, arity).
