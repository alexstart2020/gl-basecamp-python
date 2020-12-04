def count_holes(value):
    value = [int(x) for x in str(value)]
    a = value.count(4)
    b = value.count(6)
    c = value.count(8)
    d = value.count(9)
    e = value.count(0)
    return c*2 + a + b + d + e

while True:
    value = input("Введите целое число: ")
    try:
        value = int(value)
        print("Количество отверстий: ", count_holes(value))
    except:
        print("Введенное значение не соответствует формату!!!")
