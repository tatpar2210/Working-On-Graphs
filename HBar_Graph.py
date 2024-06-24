import matplotlib.pyplot as plt

graph_name = str(input("Give a name to the graph: "))
graph_x = str(input("Give a name to the X-Coordinate: "))
graph_y = str(input("Give a name to the Y-Coordinate: "))

elements = int(input("Enter total no. elements: "))

x = []
for i in range(0, elements):
    x_ele = str(input("Give Name of bar on Y-axis: "))
    i += 1
    x.append(x_ele)
    print(x)

y = []
for t in range(-1, len(x ) -1):
    coor = "Give Y-axis coordinate for X-axis {}: "
    t += 1
    y_ele = int(input(coor.format(x[t])))
    y.append(y_ele)

print("\n")
print("Things You Can Edit: ")
print("1. To change Bar Colour")
print("2. To change Bar width")
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
bar_color = []
for j in range(-1, len(x ) -1):
    coor = "Give color of the bar for X-axis value {}: "
    j += 1
    color = str(input(coor.format(x[j])))
    bar_color.append(color)

plt.barh(x, y, color=bar_color)
print("Graph is displayed in Plots!!")
plt.title(graph_name)
plt.xlabel(graph_x)
plt.ylabel(graph_y)
plt.show()
