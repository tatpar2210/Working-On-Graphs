import matplotlib.pyplot as plt

graph_name = str(input("Give a name to the graph: "))

elements = int(input("Enter no. of elements: "))

x = []
for i in range(0, elements):
    x_ele = int(input("Enter the values one-by-one: "))
    i += 1
    x.append(x_ele)
y = []
for t in range(-1, len(x) - 1):
    coor = "Give Name to {}: "
    t += 1
    y_ele = str(input(coor.format(x[t])))
    y.append(y_ele)
plt.pie(x, labels=y)
plt.show()

col = str(input("Wanna change color (YES/NO): "))
if col == "YES":
    color = []
    print("|n")
    print("Color Codes available are listed below: ")
    print("Colour_Code    Colour")
    print("     b         Blue")
    print("     y         Yellow")
    print("     r         Red")
    print("     g         Green")
    print("     m         Magenta")
    print("     k         Black")
    print("     c         Cyan")
    print("     w         White")
    for j in range(-1, len(x) - 1):
        coor = "Give color to {}: "
        j += 1
        colour = str(input(coor.format(y[j])))
        color.append(colour)
    plt.title(graph_name)
    plt.pie(x, labels=y, colors=color)
    plt.show()

    exp = str(input("Wanna explode some parts(YES/NO): "))
    if exp == "YES":
        explode = []
        for s in range(-1, len(x) - 1):
            coor = "Give,amount to explode {} by: "
            s += 1
            expld = float(input(coor.format(y[s])))
            explode.append(expld)
        plt.title(graph_name)
        plt.pie(x, labels=y, colors=color, explode=explode)
        plt.show()
    else:
        pass
else:
    exp = str(input("Wanna explode some parts(YES/NO): "))
    if exp == "YES":
        explode = []
        for s in range(-1, len(x) - 1):
            coor = "Give,amount to explode {} by: "
            s += 1
            expld = float(input(coor.format(y[s])))
            explode.append(expld)
        plt.title(graph_name)
        plt.pie(x, labels=y, explode=explode)
        plt.show()
    else:
        pass
