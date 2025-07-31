def Grade():
    while True:
        p = input("Enter Your Marks and to Exit write EXIT: ")

        if p.lower() == "exit":
            print("EXIT SUCCESSFUL")
            break

        if not p.isdigit():
            print("INVALID INPUT!")
            continue

        a = int(p)
        if a >= 0 and a < 40:
            print("F")
        elif a >= 40 and a < 60:
            print("D")
        elif a >= 60 and a < 75:
            print("C")
        elif a >= 75 and a < 90:
            print("B")
        elif a >= 90 and a <= 100:
            print("A")
        else:
            print("INVALID INPUT!")

Grade()
