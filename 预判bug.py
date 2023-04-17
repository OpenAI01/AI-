try:
    user_weight = float(input("请输入您的体重(单位：千克):"))
    user_height = float(input("请输入您的身高(单位：米):"))
    user_BMI=user_weight/(user_height**2)
except ValueError:
    print("输入内容非合理数字，请重新运行程序，并输入合理数字。")
except ZeroDivisionError:
    print("身高不能为零，请重新运行程序，并输入正确数字。")
except:
    print("发生了未知错误，请重新运行程序。")
else:
    print("您的BMI值为："+str(user_BMI))
finally:
    print("程序结束运行。")