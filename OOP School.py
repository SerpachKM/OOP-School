# Эта функция принимает список чисел и возвращает их среднее значение, если список не пустой. Если список пустой, функция вернет 0.
# Функция проверяет, является ли список чисел списком или словарем, и использует разные подходы для вычисления среднего значения в зависимости от типа списка.
# Если список является списком, функция использует стандартную операцию сложения и деления на количество элементов списка, чтобы вычислить среднее значение.
# Если же список является словарем, функция перебирает все значения словаря и складывает их, затем делит сумму на количество значений, чтобы получить среднее значение.
def mean(numbers):
    if numbers:
        if isinstance(numbers, dict):
            res=[]
            for value in numbers.values():
                res += value
            return sum(res)/len(res)
        else:
            return sum(numbers)/len(numbers)
    else:
        return 0

# Данная функция принимает два аргумента: список студентов (persons) и название курса (course).
# Функция проходит по каждому студенту в списке и проверяет наличие курса в его оценках (person.grades).
# Если курс есть в оценках студента, то функция добавляет его оценку к общему среднему значению (res).
# Затем функция увеличивает счетчик количества оценок (lenth), которые были использованы при вычислении среднего значения.
# Если общее количество оценок не равно нулю, функция возвращает среднее значение оценок, деленное на общее количество оценок.
def courses_rating(persons, course):
    res = 0
    lenth = 0
    for person in persons:
        if course in person.grades:
            if person.grades[course]:
                res += mean(person.grades[course])
                lenth += 1
    if lenth != 0:
        return res/lenth

# Класс Student представляет собой абстрактный класс, который позволяет хранить информацию о студенте и его оценках по различным курсам.
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
# Данный код содержит проверку, является ли лектор объектом типа Lecturer, а также проверку на наличие курса, который нужно оценить.
# Если условия выполняются, то проверяется, является ли оценка целого типа в диапазоне от 0 до 10, и если это так, то она добавляется в список оценок лектора в соответствии с курсом.
# Если же условия не выполняются, выводится сообщение об ошибке и возвращается значение 'Ошибка'.
    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if isinstance(grade, int) and (0 <= grade <= 10) :
                if course in lecturer.grades:
                    lecturer.grades[course] += [grade]
                else:
                    lecturer.grades[course] = [grade]
            else:
                print("Оценка введена неверно")
        else:
            return 'Ошибка'
# В классе определены методы __str__(), __lt__() (меньше), __gt__() (больше), __le__() (меньше или равно) и __ge__() (больше или равно), которые используются для сравнения студентов друг с другом.
# Каждый из методов принимает на вход два объекта типа Student и сравнивает их среднюю оценку. Средняя оценка вычисляется по формуле: (сумма оценок всех курсов) / количество курсов.
# Методы __str__() и __lt__() возвращают строку с информацией о студенте, включая его имя, фамилию, среднюю оценку, список курсов в процессе обучения и список завершенных курсов.
# Методы __gt__() и __le__() возвращают True, если средняя оценка первого студента больше или меньше средней оценки второго студента соответственно, и False в противном случае.
# Аналогично, методы __ge__() возвращают True, если средняя оценка первого студента больше или равна средней оценке второго студента, и False в противном случае.
    def __str__(self):
        info = str(f"Имя: {self.name}\n"
                   f"Фамилия: {self.surname}\n"
                   f"Средняя оценка: {mean(self.grades)}\n"
                   f"Курсы в процессе обучения: {', '.join(self.courses_in_progress)}\n"
                   f"Завершенные курсы: {', '.join(self.finished_courses)}\n")
        return info
    def __lt__(self, other):
        return mean(self.grades) < mean(other.grades)
    def __gt__(self, other):
        return mean(self.grades) > mean(other.grades)
    def __le__(self, other):
        return mean(self.grades) <= mean(other.grades)
    def __ge__(self, other):
        return mean(self.grades) >= mean(other.grades)

# В классе определяются два атрибута:
# – self.name - имя ментора;
# – self.surname - фамилия ментора;
# а также метод __init__()(), который принимает на вход имя и фамилию ментора и инициализирует эти атрибуты.
# Кроме того, в классе определяется список self.courses_attached, который содержит список всех курсов, к которым прикреплен ментор.
# Этот список заполняется при создании экземпляра класса путем передачи ему списка курсов, к которым ментор прикреплен.
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

# Класс Mentor определяет два атрибута - name и surname, а также метод __init__()().
# Этот метод принимает на вход аргументы name и surname и инициализирует соответствующие атрибуты.
# Также в классе определяется список courses_attached, содержащий список всех курсов, к которым привязан ментор.
# Класс Lecturer является наследником класса Mentor и наследует все его методы и атрибуты.
# Кроме того, класс Lecturer определяет свои собственные методы __init__()() и __str__()(), а также переопределяет методы __lt__(), __gt__(), __le__() и __ge__().
# Эти методы переопределяют методы класса Mentor для работы с оценками студентов и курсов.
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка: {mean(self.grades)}"
    def __lt__(self, other):
        return mean(self.grades) < mean(other.grades)
    def __gt__(self, other):
        return mean(self.grades) > mean(other.grades)
    def __le__(self, other):
        return mean(self.grades) <= mean(other.grades)
    def __ge__(self, other):
        return mean(self.grades) >= mean(other.grades)

# В классе определяются методы __str__()() и rate_hw().
# Метод rate_hw() принимает на вход объект типа Student, курс и оценку и выполняет следующие действия:
# 1. Проверяет, является ли студент объектом типа Student и имеет ли курс в списке своих курсов в процессе изучения.
# 2. Проверяет, есть ли курс в списке оценок студента и добавляет оценку в список оценок студента, если курс есть.
# 3. Возвращает 'Ошибка', если условия не выполнены.
class Reviewer(Mentor):
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

# Данный фрагмент описывает создание списка студентов, добавление курсов в их список курсов и добавление оценок в их список оценок.
# Затем он создает список менторов и добавляет курсы к их списку курсов. Наконец, он создает список рецензентов и добавляет курсы в их список.
Students = [Student('Олег', 'Резнов', 'Пол'),
            Student('Иван', 'Иванов', 'your_gender')]
Students[0].courses_in_progress += ['Python']
Students[0].courses_in_progress += ['Git']
Students[0].finished_courses += ['Introduction to the programming']
Students[1].courses_in_progress += ['Python']
Students[1].finished_courses += ['Paint']
Students[1].finished_courses += ['Calculator']

Lecturers = [Lecturer('Миша', 'Косолапов'),
             Lecturer('Лиза', 'Воронцова')]
Lecturers[0].courses_attached += ['Python']
Lecturers[0].courses_attached += ['Java']
Lecturers[1].courses_attached += ['JS']

Reviewers = [Reviewer('Юра', 'Лисинков'),
             Reviewer('Денис', 'Баскин')]
Reviewers[0].courses_attached += ['Python']
Reviewers[0].courses_attached += ['Git']
Reviewers[1].courses_attached += ['Python']
Reviewers[1].courses_attached += ['JS']

Reviewers[0].rate_hw(Students[0], 'Python', 8)
Reviewers[0].rate_hw(Students[0], 'Python', 9)
Reviewers[0].rate_hw(Students[0], 'Git', 10)
Reviewers[0].rate_hw(Students[1], 'Python', 10)
Reviewers[1].rate_hw(Students[1], 'Python', 6)

Students[0].rate_lecturer(Lecturers[0], 'Python', 10)
Students[0].rate_lecturer(Lecturers[0], 'Python', 9)
Students[1].rate_lecturer(Lecturers[0], 'Python', 8)
Students[1].rate_lecturer(Lecturers[1], 'JS', 7)

print(f"Reviewers[0]:\n{Reviewers[0]}\n")
print(f"Lecturers[0]:\n{Lecturers[0]}\n")
print(f"Lecturers[1]:\n{Lecturers[1]}\n")
print(f"Students[0]:\n{Students[0]}\n")
print(f"Students[1]:\n{Students[1]}\n")

print("Миша Косолапов < Лиза Воронцова ==>", Lecturers[0] > Lecturers[1])
print("Олег Резнов > Иван Иванов ==>", Students[0] > Students[1])

print(f"\nСредняя оценка домашних работ по Python: {courses_rating(Students, 'Python')}")
print(f"Средняя оценка лекторов по курсу Python: {courses_rating(Lecturers, 'Python')}")
