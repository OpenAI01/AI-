# f=open("./libai.txt","r",encoding="utf-8"
# with open("./libai.txt","r",encoding="utf-8")as f:
    # content=f.read()
    # print(content)
# f.close()
with open("./libai.txt", "r", encoding="utf-8") as f:
    lines=f.readlines()
    for line in lines:
        print(line)