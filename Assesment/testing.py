def listing(list1, list2):
    list3 = list1[:-1] + list2[1:]
    list3.append(list2[0])
    list3.append(list1[-1])
    print(list3)

#listing([70, 60, 50, 40, 30, 20, 10, 90], [80])

listing([10, 20, 30, 40, 50, 60, 70, 90], [80])

