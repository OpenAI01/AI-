# contacts=["老余","老林","老陈","老曾","老李","老张"]
# for name in contacts:
#     message_content=name+":岁月之乐，点翠花柳喜开颜.\
# 云开雾散，良辰美景共团圆。祝福"+name+\
#         "及家人新年快乐，平安顺遂，虎年大吉！"
#     send_message(name, message_content)


gpa_dict={"小明":3.251,"小花":3.869,"小李":2.683,"小张":3.685}
for name,gpa in gpa_dict.items():
  print("{0}你好，你当前的绩点为:{1:.2f}".format(name,gpa))
  # print(name+"你好，你当前的绩点为："+str(gpa))
