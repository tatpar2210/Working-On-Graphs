import matplotlib.pyplot as plt

graph_name = str(input("Give a name to the graph: "))
graph_x = str(input("Give a name to the X-Coordinate: "))
graph_y = str(input("Give a name to the Y-Coordinate: "))

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
        coor = "Give Y-axis coordinate for X-axis= {}: "
        h += 1
        y_ele = int(input(coor.format(x[h])))
        y.append(y_ele)
    print("\nThings You Can Edit: ")
    print("1. To change Line Colour")
    print("2. To change Line Type ")
    print("3. To change Marker Type ")
    print("4. To change Marker Color")
    print("5. To change Marker Size")
    print("6. To change Line width")
    print("7. Label The Graph")

    for j in range(1, 8):
        if j == 1:
            print("\nColor Codes available are listed below: ")
            print("Colour_Code    Colour")
            print("     b         Blue")
            print("     y         Yellow")
            print("     r         Red")
            print("     g         Green")
            print("     m         Magenta")
            print("     k         Black")
            print("     c         Cyan")
            print("     w         White")
            color = str(input("Enter the line color_code: "))
        elif j == 2:
            print("\nTypes of Line styles are:-(solid, dashed, dotted, dashdot)")
            line_style = str(input("Enter the Line_type: "))
        elif j == 3:
            print("""\nTypes of marker type available are listed below
                  Marker_Type    Marker""")
            marker_type = str(input("Enter Marker_type: "))
        elif j == 4:
            print("\nColor Codes available are listed below: ")
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
        elif j == 5:
            marker_size = float(input("\nEnter marker size: "))
        elif j == 6:
            line_width = float(input("\nEnter the width of the line: "))
        else:
            labels = str(input("\nLabel this Line: "))
    print("Data recorded.")
    print("\n")

    plt.plot(x, y, color, linestyle=line_style, marker=marker_type, markeredgecolor=marker_color,
             markersize=marker_size, linewidth=line_width, label=labels)

    g += 1
    axes.append(y)

print("X-axis coordinates: ", x)
print("Y-axis Coordinates: ", axes)

print("\nChoices for position of label are:- ")
print(" Label Position      Location Code")
print("     best                0")
print("     upper right         1")
print("     upper left          2")
print("     lower left          3")
print("     lower right         4")
print("     right               5")
print("     center left         6")
print("     center right        7")
print("     lower center        8")
print("     upper Center        9")
print("     center             10")
legend_pos = str(input())
plt.title(graph_name)
plt.xlabel(graph_x)
plt.ylabel(graph_y)
plt.legend(legend_pos)
plt.show()
