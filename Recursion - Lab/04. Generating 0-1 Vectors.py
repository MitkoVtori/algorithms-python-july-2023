def gen01(index, vector):
    if index >= len(vector):
        print(''.join([str(x) for x in vector]))
        return
    for number in range(2):
        vector[index] = number
        gen01(index + 1, vector)


n = int(input())
vector = [0] * n
gen01(0, vector)