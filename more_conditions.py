# BMI=体重/（身高**2）
user_weight = float(input("请输入您的体重(单位：千克):"))
user_height = float(input("请输入您的身高(单位：米):"))
gender = input("请输入您的称呼（先生/女士）：")
user_BMI = user_weight/(user_height**2)
print("您的BMI值为："+str(user_BMI))

# 偏瘦：user_BMI<=18.5
# 正常：18.5<user_BMI<=25
# 偏胖: 25<user_BMI<=30
# 肥胖: user_BMI>30

if user_BMI <= 18.5:
    print(gender+"您好，此BMI属于偏瘦范围。")
elif 18.5 < user_BMI <= 25:
    print(gender+"您好，此BMI属于正常范围。")
elif 25 < user_BMI <= 30:
    print(gender+"您好，此BMI属于偏胖范围。")
else:
    print(gender+"您好，此BMI属于肥胖范围。")


