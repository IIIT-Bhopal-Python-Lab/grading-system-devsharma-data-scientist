p = input()
if p.lower() == "exit":
    print("EXIT SUCCESSFUL")
    break
    
try:
    a = int(p)    #input ko integer me convert karne ki koshish kro
    if a >= 0 and a < 40:
        print("F")   #Fail
    elif a >= 40 and a < 60:
        print("D")   #Below avg
    elif a >= 60 and a < 75:
        print("C")   #avg
    elif a >= 75 and a < 90:
        print("B")   #good
    elif a >= 90 and a <= 100:
        print("A")   #Excellent
    else:
        print("INVALID INPUT!")   # agr no. 0-100 ke bahar ho
except:
    # agr input no. nahi hai,toh error!
     print("INVALID INPUT!")
