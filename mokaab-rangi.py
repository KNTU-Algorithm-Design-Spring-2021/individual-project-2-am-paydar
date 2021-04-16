class Color:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    # negative compare
    def __eq__(self, other):
        if isinstance(other, Color):
            return self.r == 255-other.r and self.g == 255-other.g and self.b == 255-other.b


class Cube:
    self.above_face=0
    # Length: طول , width:عرض  ,height:ارتفاع
    # c is array of length 6 for storing each face color
    def __init__(self, l, w, h, weight, colors):
        self.l = l
        self.w = w
        self.h = h
        self.weight = weight
        self.colors = colors

    def __str__():
        print(weight)


def color_compare(color_list1, color_list2):
    result = []
    for i in color_list1:
        for j in color_list1:
            if i == j:
                result.append((i, j))
    return result


def color_compare(color_list1, color_list2):
    result = []
    for i in range(6):
        for j in range(6):
            if color_list1[i] == color_list2[j]:
                result.append((i, j))
    return result


def get_height(cube, x):
    if x == 1 or x == 6:
        return cube.h
    elif x == 2 or x == 3:
        return cube.l
    else:
        return cube.w


def cube_staying(cube1, cube2, negative_face):
    x = float('inf')
    tempi = -1
    tempj = -1

    for i in negative_face:
        temp = get_height(cube1, i[0])+get_height(cube2, i[1])
        tempi = i[0]
        tempj = i[1]

        if x > temp:
            x = temp
    return tempi, tempj


n = int(input())  # number of cubes
cubes = []
for i in range(n):
    l, w, h = input().split()
    l = int(l)
    w = int(w)
    h = int(h)
    weight = int(input())
    colors = []
    for j in range(6):
        r, g, b = input().split()
        r = int(r)
        g = int(g)
        b = int(b)
        new_color = Color(r, g, b)
        colors.append(new_color)
    new_cube = Cube(l, w, h, weight, colors)
    cubes.append(new_cube)

lis = [0]*n

sorted(cubes, key=lambda x: x.weight, reverse=True)

for j in range(1, n):
    for i in range(j):
        negative_face = color_compare(cubes[i].colors, cubes[j].colors)
        state1, state2 = cube_staying(cubes[i], cubes[j], negative_face)
        if lis[j]<lis[i]+state2:
            lis[j]+=lis[i]+state2

        # for cube in cubes:
        #     print(cube.weight)
        # for i in range(n):
        #     for j in range(n):
