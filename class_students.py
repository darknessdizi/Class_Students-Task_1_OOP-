class Student:

    '''Создаем класс для студентов'''

    def __init__(self, name, surname, gender):

        '''Конструктор класса Student.
        Добавляет студента в класс и определяет его атрибуты'''

        self.name = name
        self.surname = surname
        self.gender = gender