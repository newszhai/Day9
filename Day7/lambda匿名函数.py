def test_func(compute):
    result = compute(1,2)
    print(result)

# def compute(x,y):
#     return x+y
# test_func(compute)


test_func(lambda x,y:x+y)