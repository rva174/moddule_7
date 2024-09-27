def add_everything_up(a, b):
    try:
        return a + b
    except TypeError:
        a = str(a)
        b = str(b)
        return a + b
    else:
        return a + b

# print(add_everything_up('a', 'b'))
# print(add_everything_up(6.3, 7.7))

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))