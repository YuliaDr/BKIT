from gen_random import gen_random

class Unique(object):
    def __init__(self, items, **kwargs):
        self.data = items
        self.index = 0
        self.res_data = set()
        if kwargs.get('ignore_case') == None:
            self.ignore_case = False
        else:
            self.ignore_case = kwargs['ignore_case']


    def __next__(self):
        while True:
            if self.index >= len(self.data):
                raise StopIteration
            else:
                current = self.data[self.index]
                self.index = self.index + 1
                if self.ignore_case == False:
                    if current not in self.res_data:
                        self.res_data.add(current)
                        return current
                else:
                    low_data = [i.lower() for i in self.res_data]
                    if current.lower() not in low_data:
                        self.res_data.add(current)
                        return current

    def __iter__(self):

        return self

# data = [1, 4, 1, 8]
# for i in Unique(data):
#     print(i, end=" ")