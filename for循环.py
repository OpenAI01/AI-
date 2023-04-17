temperature_dict={"111":36.4,"112":36.6,"113":36.2,"114":38.1,"115":38.9}
for stuff_id,temperature in temperature_dict.items():
    if temperature >= 38:
        print(stuff_id+"号员工体温为"+str(temperature)+"度，超过38度。")


total=0
for i in range(1,101):
    total=total+i
print(total)