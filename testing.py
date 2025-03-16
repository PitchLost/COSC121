def test_function():
    items = [0.0, 3.2, 7.6, 5.9, 1.4]
    for (i, num) in enumerate(items):
        items[i] = round(num)
    print(items)

test_function()