# BMI=体重/（身高**2）

user_weight = float(input("请输入您的体重(单位：千克):"))
user_height = float(input("请输入您的身高(单位：米):"))
user_BMI=user_weight/(user_height**2)
print("您的BMI值为："+str(user_BMI))
