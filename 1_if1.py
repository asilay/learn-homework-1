"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить 
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: 
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат 
  работы функции в переменную
* Вывести содержимое переменной на экран

"""


def edication(a):
    if a < 8:
        return "You should go to kindergrden"
    elif a < 19:
        return "You should study at school"
    elif a < 25:
        return "You'd better study at university"
    else:
        return "You've already studied enough, now go to work"


def main():
    age = int(input("Please fill your age here: "))
    result = edication(age)
    print(result)


if __name__ == "__main__":
    main()
