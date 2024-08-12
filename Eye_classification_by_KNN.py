import numpy

R = "Right"
L = "Left"

All_values = {
    (119, 182): R,
    (114, 183): R,
    (450, 469): R,
    (451, 381): R,
    (70, 112): R,
    (73, 99): R,
    (69, 77): R,
    (67, 119): R,
    (83, 105): R,
    (88, 115): R,
    (66, 126): R,
    (86, 94): R,
    (99, 70): R,
    (93, 81): R,
    (90, 96): R,

    (205, 180): L,
    (203, 181): L,
    (652, 455): L,
    (633, 365): L,
    (127, 110): L,
    (133, 99): L,
    (114, 78): L,
    (131, 122): L,
    (140, 105): L,
    (141, 116): L,
    (141, 125): L,
    (124, 89): L,
    (163, 71): L,
    (141, 80): L,
    (136, 96): L,
}

values = list(All_values.keys())  # all input data

X, Y = map(list, zip(*values))

x = int(input('Enter x value: '))  # enter x
y = int(input('Enter y value: '))  # enter y


def Eclidian_Distance(x_value, y_value):
    list_disAll = []
    for i in range(len(X)):
        dis_r = numpy.sqrt(((x_value - X[i]) ** 2) + ((y_value - Y[i]) ** 2))
        list_disAll.append(float(dis_r))
    return list_disAll


K = 7


def KNN(k_value):
    # list of all distance between x,y lists that we get from Eclidian_Distance function
    List_Dis = Eclidian_Distance(x, y)

    list_min = []  # list have the number K of minimum distances
    List_val_x = []  # list of x at the position of mini val
    List_val_y = []  # list of y at the position of mini val
    for i in range(k_value):
        mini = min(List_Dis)  # choose small value of list of distance

        list_min.append(mini)  # add minimum value in list_min

        idx = List_Dis.index(mini)  # return index or position of small item in the list

        List_Dis.remove(mini)  # remove the min val we get

        List_val_x.append(X[idx])
        X.remove(X[idx])  # remove the x at the same location of min val
        List_val_y.append(Y[idx])
        Y.remove(Y[idx])  # remove the y at the same location of min val

    List_of_tuples = [(List_val_x[i], List_val_y[i]) for i in range(0, len(List_val_x))]  # make list have (x, y) tuples
    list_of_theValues_of_Each_Key = []
    for i in List_of_tuples:
        if i not in All_values:
            pass
        else:
            list_of_theValues_of_Each_Key.append(All_values[i])

    Ri = list_of_theValues_of_Each_Key.count(R)
    Li = list_of_theValues_of_Each_Key.count(L)
    if Ri > Li:
        print(f"Your given eye location is detected as Right eye: ({x}, {y})")
    else:
        print(f"Your given eye location is detected as Left eye: ({x}, {y})")


KNN(K)
