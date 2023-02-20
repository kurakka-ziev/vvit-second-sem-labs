groupmates = [
    {
        "name": "Александр",
        "surname": "Иванов",
        "exams": ["Информатика", "ЭЭиС", "Web"],
        "marks": [4, 3, 5]
    },
    {
        "name": "Иван",
        "surname": "Петров",
        "exams": ["История", "АиГ", "КТП"],
        "marks": [4, 4, 4]
    },
    {
        "name": "Кирилл",
        "surname": "Смирнов",
        "exams": ["Философия", "ИС", "КТП"],
        "marks": [5, 5, 5]
    },
    {
        "name": "Вася",
        "surname": "Пупкин",
        "exams": ["Философия", "КГ", "АиГ"],
        "marks": [2, 2, 3]
    },
    {
        "name": "Гений",
        "surname": "Мысли",
        "exams": ["Философия", "КГ", "АиГ"],
        "marks": [2, 1, 1]
    }
]


def sorting(students):
    c = 0
    while True:
        try:
            mark = int(input("Input the mark(>0): "))
            break
        except:
            print("bro it needs a number")
    if mark > 0:
        print(u"Имя".ljust(15), u"Фамилия".ljust(10), u"Экзамены".ljust(35), u"Оценки".ljust(15), u"Средняя оценка".ljust(10))
        for student in students:
            av_mark = sum(student["marks"])/len(student["marks"])
            if av_mark > mark:
                print(student["name"].ljust(15), student["surname"].ljust(10), str(student["exams"]).ljust(35), str(student["marks"]).ljust(15), str(av_mark)[0:3].ljust(5))
                c += 1
        if c == 0:
                print("STUDENTS NOT FOUND")
    else:
        print("please insert number bigger and not equal to 0")
        sorting(groupmates)

sorting(groupmates)
