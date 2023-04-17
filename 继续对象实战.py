class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id

    def print_info(self):
       print(f"员工名字：{self.name},工号:{self.id}")

class FullTimeEmployee(Employee):
    def __init__(self,name,id,monthly_salary):
        super().__init__(name,id)
        self.monthly_salary=monthly_salary

    def calculate_monthly_pay(self):
        return self.monthly_salary

class PartTimeEmployee(Employee):
    def __init__(self,name,id,daily_salary,work_days):
        super().__init__(name,id)
        self.daily_salary=daily_salary
        self.work_days=work_days

    def calculate_monthly_pay(self):
        return self.daily_salary*self.work_days

zhangsan=FullTimeEmployee("张三","1001",6000)
lisi=PartTimeEmployee("李四","1002",230,15)
zhangsan.print_info()
lisi.print_info()
print(zhangsan.calculate_monthly_pay())
print(lisi.calculate_monthly_pay())

