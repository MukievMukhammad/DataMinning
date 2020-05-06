import numpy

topology = [
    #A  B  C  D  E  F  G
    [0, 1, 0, 0, 0, 0, 0], #A
    [0, 0, 1, 1, 1, 0, 0], #B
    [0, 0, 0, 0, 1, 0, 0], #C
    [0, 0, 0, 0, 1, 0, 0], #D
    [0, 0, 0, 0, 0, 1, 0], #E
    [0, 0, 0, 0, 0, 0, 0], #F
    [0, 0, 0, 1, 0, 0, 0], #G
]



def multipe_matrix_to_vector(h, matrix):
    result = []
    for i in range(0, len(matrix)):
        row = matrix[i]
        sum = 0
        for j in range(0, len(h)):
            sum = sum + row[j] * h[j]
        result.append(sum)
    return result

def normalize(vector):
    result = []
    max = 0
    for i in vector:
        if i > max:
            max = i
    for i in vector:
        result.append(i/max)
    return result


def main():
    h = [1, 1, 1, 1, 1, 1, 1]
    transposed = numpy.transpose(topology)
    for i in range(20):
        Lh = multipe_matrix_to_vector(h.copy(), transposed.copy())
        a = normalize(Lh)
        La = multipe_matrix_to_vector(a.copy(), topology.copy())
        h = normalize(La.copy())

    h = normalize(h.copy())
    a = normalize(a.copy())
    print(h)
    pass


if __name__ == "__main__":
    main()