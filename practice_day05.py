class Employee:
    _tax=5
    __overtime_rate=0
    def __init__(self,Id,name,salary):
        self._ID=Id
        self._name=name
        self._salary=salary
        self._total_salary=salary 
        self.__extra_time=0
    @classmethod
    def overtime_rate(cls,rate):
        cls.__overtime_rate=rate
    def extra_time(self,time):
        self.__extra_time+=time 
    def set_total_salary(self):
        self._total_salary=self._salary+(self.__extra_time*Employee.__overtime_rate)-(self._salary*(Employee._tax/100))
    @classmethod
    def set_tax(cls,t):
        cls._tax=t
    @classmethod
    def get_tax(cls):
        return cls._tax
    def display(self):
        print("ID: ",self._ID)
        print("Name: ",self._name)
        print("Basic: ",self._salary)
        print("Total salary: ",self._total_salary)
        print("Extra time: ",self.__extra_time)
        print("Overtime rate: ",Employee.__overtime_rate)

class Manager(Employee):
    def __init__(self, Id, name, salary):
        super().__init__(Id, name, salary)
        self.__bonus=0
    def add_bonus(self,bonus):
        self.__bonus+=bonus
    def set_total_salary(self):
        self._total_salary=self._salary+self.__bonus-(self._salary*(Manager._tax/100))
    def display(self):
        super().display()
        print("bonus: ",self.__bonus)
e1=Employee(4398,"ALi",70000)
e2=Employee(3893,"Ans",72000)
m=Manager(10034,"Ahmad",120000)
Employee.overtime_rate(500)
Employee.set_tax(7)
e1.extra_time(16)
e1.extra_time(6)
e1.set_total_salary()
e2.extra_time(15)
e2.set_total_salary()
print("Employee 1 data: ")
e1.display()
print("Employee 2 data:\n")
e2.display()
Manager.set_tax(5)
m.add_bonus(22000)
m.set_total_salary()
print("Manager data: ")
m.display()
