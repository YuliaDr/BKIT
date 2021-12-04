def field(items, *args):
    assert len(args) > 0
    if len(args) == 1:
        for i in items:
            a = i.get(args[0])
            if a != None:
                yield a
    else:
        for i in items:
            dic = {}
            for ar in args:
                a = i.get(ar)
                if a != None:
                    dic[ar] = a
            yield dic

# goods = [
#    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
#    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
# ]
# a = field(goods, 'title')
# b = field(goods, 'title', 'price')
# for i in a:
#     print(i, end=" ")
# print("\n-----------------------------------------")
# for i in b:
#     print(i, end=" ")