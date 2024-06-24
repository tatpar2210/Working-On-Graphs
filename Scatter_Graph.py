import matplotlib.pyplot as plt

graph_name = str(input("Give a name to the graph: "))
graph_x = str(input("Give a name to the X-Coordinate: "))
graph_y = str(input("Give a name to the Y-coordinate: "))

data = int(input("Enter no. of graph to be studied: "))
elements = int(input("Enter total no. of elements: "))

# Entry of X-Axis Coordinates
x = []
for i in range(0, elements):
    x_ele = int(input("Give X-axis Coordinates: "))
    i += 1
    x.append(x_ele)
print(x)

# Entry of other Axes Coordinates
axes = []
for g in range(0, data):
    y = []
    for h in range(-1, len(x) - 1):
        coor = "Give Y-axis coordinate for X-axis {}: "
        h += 1
        y_ele = int(input(coor.format(x[h])))
        y.append(y_ele)
    print("\n")
    print("Things You Can Edit: ")
    print("1. To change Marker Type ")
    print("2. To change Marker Color")
    print("3. To change Marker Size")

    for j in range(1, 5):
        if j == 1:
            print("\n")
            print("Types of marker type available are listed below")
            print("Marker_Type    Marker")
            marker_type = str(input("Enter Marker_type: "))
        elif j == 2:
            print("\n")
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
            marker_color = str(input("Enter the marker color_code: "))
        elif j == 3:
            marker_size = float(input("Enter marker size: "))
        else:
            labels = str(input("Label your graph: "))
    plt.scatter(x, y, marker=marker_type, c=marker_color, s=marker_size, label=labels)
    g += 1
    axes.append(y)

print("X-axis coordinates: ", x)
print("Y-axis Coordinates: ", axes)
plt.title(graph_name)
legend_pos = str(input(
    "Choices for position of label are:- best/upper left/upper right/lower left/lower right/right/center left/center right/lower center/upper center/center: "))
plt.legend(legend_pos)
plt.xlabel(graph_x)
plt.ylabel(graph_y)
plt.show()
