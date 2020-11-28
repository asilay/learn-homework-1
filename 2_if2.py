"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""


def strings_input(string1, string2):
    if string1.isdigit() or string2.isdigit():
        return 0
    elif string1 == string2:
        return 1
    elif string2.lower() == "learn":
        return 3
    elif len(string1) > len(string2):
        return 2


def main():
    a = strings_input(
        input("Put the first string: "),
        input("Fill with the second string: "),
    )
    print(a)


if __name__ == "__main__":
    main()
