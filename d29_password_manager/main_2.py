try:
    with open("data2.txt") as file:
        file.read()
except:
    open("data3.txt", "w")
