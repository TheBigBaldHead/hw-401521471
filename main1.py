def tak(n):
    if len(str(n)) == 1:
        return n
    else:
        n = str(n)
        numbers = list()
        for number in range(len(n)):
            numbers.append(int(n[number]))
        return tak(sum(numbers))

def draw():
    number = input()
    intnum = int(number)
    output = tak(intnum)
    print(output)

draw()
