def num_min(list1):
    v = int(list1[0])
    for j in list1:
        j = int(j)
        if j < v:
            v = j
    return v


def num_max(list1):
    v = int(list1[0])
    for j in list1:
        j = int(j)
        if j > v:
            v = j
    return v


def num_sum(list1):
    v = 0
    for j in list1:
        j = int(j)
        v += j
    return v


def num_multiply(list1):
    v = 1
    for j in list1:
        j = int(j)
        v *= j
    return v


def pro_on(name):
    with open(name, "r") as file:
        a = file.read().split()
        for i in range(len(a)):
            a[i] = a[i].strip(",")
        return num_sum(a), num_multiply(a), num_max(a), num_min(a), a
# В программе не может возникнуть ошибки переполнения, так как все числовые значения имеют тип int


# print(pro_on("file numbers.txt"))
