# 9_6 Генераторы

def all_variants(text):
    yield text[0]
    yield text[1]
    yield text[2]
    yield text[:2]
    yield text[1:]
    yield text[:3]

a = all_variants("abc")
for i in a:
    print(i)