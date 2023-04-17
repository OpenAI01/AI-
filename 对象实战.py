class Student:
    def __init__(self,name,student_id):
        self.name=name
        self.student_id=student_id
        self.grades={"语文":0,"数学":0,"英语":0}

    def setting_grade(self,course,grade):
        if course in self.grades:
            self.grades[course]=grade

    def print_grades(self):
        print(f"学生{self.name}（学号:{self.student_id}）的成绩为：")
        for course in self.grades:
            print(f"{course}:{self.grades[course]}分")

# zeng= Student("小曾","100002")
# print(chen.name)
# zeng.setting_grade("数学",95)
# print(zeng.grades)
chen= Student("小陈","100001")
chen.setting_grade("语文",92)
chen.setting_grade("数学",94)
chen.print_grades()

