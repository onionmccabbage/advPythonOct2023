def demo():
    # generators are a part of python
    r = range(1, 99, 7) # start, stop-before, step
    o = (n for n in range(1, 99, 2))
    # we can always iterate over a generator
    for i in o:
        print(i, end=', ')
    # the benefit of generators is that at no time do the values all exist in memory
    # the values are generated on demand from a range or a generator object


if __name__ == '__main__':
    demo()