class Human:
    # TODO: name, surname, str(Human) -> Name Surname
    def __init__(self,name,surname):
        self.name=name
        self.surname=surname
    def str(self):
        return f"{self.name}  {self.surname}"


class Employee(Human):
    #TODO: salary, get_paid -> sum of money to be paid
    def __init__(self, name, surname, salary):
        super(Employee, self).__init__(name, surname)
        self.salary=salary
        self.paid=0
    def __str__(self):
        return f"{self.name}  {self.surname} {self.salary}"

    def get_paid(self):
        self.paid += self.salary
        return self.paid
class Programmer(Employee):
    # TODO: programming language, bonus
    def __init__(self,name,surname,salary,language,bonus):
        super(Programmer, self).__init__(name,surname,salary)
        self.language=language
        self.bonus=bonus
    def __str__(self):
        return f"{self.name}  {self.surname} {self.salary} {self.language}  {self.bonus}"

    def get_paid(self):
        self.paid +=self.salary + self.bonus
        return self.paid


class Manager(Employee):
    # TODO: title, multiplication_k
    def __init__(self,name,surname,salary,title,multiplication_k):
        super(Manager, self).__init__(name,surname,salary)
        self.title=title
        self.multiplication_k=multiplication_k
    def __str__(self):
        return f"{self.name}  {self.surname} {self.salary} {self.title}  {self.multiplication_k}"

    def get_paid(self):
        self.paid += self.salary * self.multiplication_k
        return self.paid


employees = [Programmer('Anton', 'Martynov', 1000, 'python', 100),
             Manager('Kyrylo', 'Kozhemyaka',2000,'LoL', 1.2),
             Employee('Sam', 'Smith', 800)]

for e in employees:
    print(f"{e} have to be paid: {e.get_paid()}")