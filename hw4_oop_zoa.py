# hw4_oop_zoa
# 1 task
class Student:
    def __init__(self, name, age):
        self.name = name
        self._age = age
    
    def get_info(self):
        return print(f'Студент {self.name}, возраст {self._age}')
    
    def __str__(self):
        return f'{self.name}, {self._age} лет'
    
print('1.task:')
student1 = Student("Анна", 20)
print(student1.get_info())

# 2 task
class GraduateStudent(Student):
    def __init__(self, name, age, research_topic):
        super().__init__(name, age)
        self._research_topic = research_topic
        self.__publications = 0
    
    def add_publication(self):
        if self.__validate_publication():
            self.__publications +=1
    
    def __validate_publication(self):
        return True
    
    def get_info(self):
        #return super().get_info()
        print(f'Студент {self.name}, возраст {self._age}, тема {self._research_topic}')

print('2.task:')
grad_student = GraduateStudent("Петр", 25, "Искусственный интеллект")
print(grad_student.get_info())
grad_student.add_publication()
grad_student.add_publication()

# 3 task
class StudentManager():
    def __init__(self):
        self._student_list = list()
    
    def add_student(self, obj):
        self._student_list.append(obj) 
    
    def __str__(self):
        return super().__str__()
    
    def __len__(self):
        return len(self._student_list)
    
    def __getitem__(self, index):
        return self._student_list[index]
    
    def __repr__(self):
        return f'Сырые данные: {super().__repr__()}'
    
    def print_all_info(self):
        for student in self._student_list:
            if hasattr(student,'_research_topic'):
                print(f'Имя: {student.name}, возраст {student._age}, тема {student._research_topic} ')
            else:
                print(f'Имя: {student.name}, возраст {student._age}')

print('3.task:')
manager = StudentManager()
student1 = Student("Света", 20)
student2 = GraduateStudent("Роман", 25, "AI")
manager.add_student(student1)
manager.add_student(student2)
print(len(manager))
print(manager[0])
print(repr(manager[0]))

manager.print_all_info()
