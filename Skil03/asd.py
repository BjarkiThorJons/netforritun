with open("ord.txt", "r", encoding="ISO-8859-1") as f:
    skra = f.read()
    skra = skra.split("\n")


for x in skra:
    print(x)


