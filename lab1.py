def Grade(p):
    if isinstance(p, str) and p.lower() == "exit":
        return "EXIT SUCCESSFUL"
    
    try:
        a = int(p)
        if a >= 0 and a < 40:
            return "F"
        elif a >= 40 and a < 60:
            return "D"
        elif a >= 60 and a < 75:
            return "C"
        elif a >= 75 and a < 90:
            return "B"
        elif a >= 90 and a <= 100:
            return "A"
        else:
            return "INVALID INPUT!"
    except:
        return "INVALID INPUT!"
