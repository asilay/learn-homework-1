"""

Домашнее задание №1

Цикл while: ask_user со словарём

* Создайте словарь типа "вопрос": "ответ", например:
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
* Напишите функцию ask_user() которая с помощью функции input()
  просит пользователя ввести вопрос, а затем, если вопрос есть
  в словаре, программа давала ему соотвествующий ответ. Например:

    Пользователь: Что делаешь?
    Программа: Программирую
    
"""

phrase_dict = {"Как дела?": "Хорошо!", "Что делаешь?": "Программирую"}

def ask_user(dict):
    while True:
        ask = input()
        if dict.get(ask):
            print(dict[ask])
            break


if __name__ == "__main__":
    ask_user(phrase_dict))
