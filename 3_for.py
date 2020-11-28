"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""


def main():
    for i in marks:
        class_perf = sum(i["marks"]) / len(i["marks"])
        print(f"The {i['class']}'th class average mark is {class_perf}")
        sum_marks += sum(i["marks"])
        sum_stud += len(i["marks"])
    print(f"The school average mark is {sum_marks/sum_stud}")


marks = [
    {"class": "4", "marks": [3, 4, 4, 5, 2]},
    {"class": "5", "marks": [3, 4, 2, 5, 3]},
]
sum_marks = 0
sum_stud = 0

if __name__ == "__main__":
    main()
