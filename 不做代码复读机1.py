# def calculate_sector(central_angle,radius):
#     sector_area=central_angle/360*3.14*radius**2
#     print(f"此扇形的面积为：{sector_area}")
# calculate_sector(160,30)
# calculate_sector(60,15)
# calculate_sector(30,16)

def calculate_BMI(weight,height):
    BMI=weight/height**2
    if BMI<=18.5:
        category="偏瘦"
    elif BMI<=25:
        category="正常"
    elif BMI<=30:
        category="偏胖"
    else:
        category="肥胖"
    print(f"您的BMI分类为：{category}")
    return BMI
result=calculate_BMI(70,1.8)
print(result)
