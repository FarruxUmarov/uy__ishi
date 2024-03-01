try:
    file = open("file.txt")
except:
    print("Xatolik!!!")
else:

    comp = file.read()
    file.close()
    comp = comp.split("\n")

bolim1 = 0
bolim2 = 0
bolim3 = 0

for i in range(len(comp)):
    comp[i] = comp[i].split()
    comp[i][-2] = int(comp[i][-2])
    comp[i][-1] = comp[i][-1].split("-")
    comp[i][-1][0] = int(comp[i][-1][0])
  
    if comp[i][-1][0] == 1:
        bolim1 += 1
    elif comp[i][-1][0] == 2:
        bolim2 += 1
    elif comp[i][-1][0] == 3:
        bolim3 += 1
for name,position,monthly,bonus_monthly,section in comp:
    if bonus_monthly > 0:
        if bolim3 < bolim1 > bolim2:
            print("1-bo'lim")
            break
        elif bolim1 < bolim2 > bolim3:
            print("2-bo'lim")
            break
        elif bolim2 < bolim3 > bolim1:
            print("3-bo'lim")
            break

