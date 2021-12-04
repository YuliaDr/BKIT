import operator

data = [4, -30, 100, -100, 123, 1, 0, -1, -4]

if __name__ == '__main__':
    result = list(map(operator.itemgetter(0), sorted([(x, abs(x))  for x in data], key = operator.itemgetter(1), reverse = True)))
    print(result)

    result_with_lambda = sorted(data, key=lambda x: abs(x), reverse=True)
    print(result_with_lambda)
