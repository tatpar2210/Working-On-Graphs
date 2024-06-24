import matplotlib.pyplot as plt 

print("Graph Types Are: ")
print("1. Line --Line Graph")
print("2. Scatter --Scatter Graph")
print("3. Bar --Bar Graph")
print("4. HBar --Vertical Bar")
print("5. Pie --Pie chart")

graph = str(input("Enter the type of the Graph: "))
      

if graph == "Line":
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


elif graph == "Scatter":
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
        for h in range(-1, len(x)-1):
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
    legend_pos = str(input("Choices for position of label are:- best/upper left/upper right/lower left/lower right/right/center left/center right/lower center/upper center/center: "))
    plt.legend(legend_pos)
    plt.xlabel(graph_x)
    plt.ylabel(graph_y)
    plt.show()
    
elif graph == "Bar":
    graph_name = str(input("Give a name to the graph: "))
    graph_x = str(input("Give a name to the X-Coordinate: "))
    graph_y = str(input("Give a name to the Y-Coordinate: "))

    elements = int(input("Enter total no. elements: "))

    x = []
    for i in range(0, elements):
        x_ele = str(input("Give coordinates of X-axis: "))
        i += 1
        x.append(x_ele)
    print(x)

    y = []
    for t in range(-1, len(x)-1):
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
    for j in range(-1, len(x)-1):
        coor = "Give color of bar for X-axis value {}: "
        j += 1
        color = str(input(coor.format(x[j])))
        bar_color.append(color)
    print("\n")
    bar_width = []
    for s in range(-1, len(x)-1):
        coor = "Give width of bar for X-axis value {}: "
        s += 1
        width = float(input(coor.format(x[j])))
        bar_width.append(width)                    
    
    plt.bar(x, y, color=bar_color, width=bar_width)
    print("Graph is displayed in Plots!!")
    plt.title(graph_name)
    plt.xlabel(graph_x)
    plt.ylabel(graph_y)
    plt.show()

elif graph == "HBar":
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
    for t in range(-1, len(x)-1):
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
    for j in range(-1, len(x)-1):
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

elif graph == "Pie":
    graph_name = str(input("Give a name to the graph: "))
    
    elements = int(input("Enter no. of elements: "))
    
    x = []
    for i in range(0, elements):
        x_ele = int(input("Enter the values one-by-one: "))
        i += 1
        x.append(x_ele)
    y = []
    for t in range(-1, len(x)-1):
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
        for j in range(-1, len(x)-1):
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
            for s in range(-1, len(x)-1):
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
            for s in range(-1, len(x)-1):
                coor = "Give,amount to explode {} by: "
                s += 1
                expld = float(input(coor.format(y[s])))
                explode.append(expld)
            plt.title(graph_name)
            plt.pie(x, labels=y, explode=explode)
            plt.show()
        else:
            pass
    
else:
    print("INVALID INPUT!!")
    
save = str(input("Wanna save the figure(YES/NO): "))
if save == "YES":
    location = str(input("GIve the location to save the figure(Eg. /home/python/code): "))
    plt.savefig(location)
else:
    pass
