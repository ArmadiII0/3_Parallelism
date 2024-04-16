from multiprocessing import Pool, Manager

def element(args):
    index, A, B, results_list = args
    i, j = index
    res = 0
    N = len(A[0]) or len(B)
    for k in range(N):
        res += A[i][k] * B[k][j]
    results_list.append(res)
    return res

if __name__ == "__main__":
    matrix1 = [[1, 2], [3, 4]]
    matrix2 = [[2, 0], [1, 2]]
    if len(matrix1[0]) != len(matrix2):
        print("Ошибка: Число столбцов первой матрицы должно быть равно числу строк второй матрицы.")
    else:
        with Manager() as manager:
            results_list = manager.list()
            rows = len(matrix1)
            cols = len(matrix2[0])
            with Pool() as pool:
                indices = [(i, j) for i in range(rows) for j in range(cols)]
                args = [(index, matrix1, matrix2, results_list) for index in indices]
                results = pool.map(element, args)
            result_matrix = [results_list[i * cols:(i + 1) * cols] for i in range(rows)]
            with open('result_matrix_temp.txt', 'w') as f:
                for row in result_matrix:
                    f.write(' '.join(map(str, row)) + '\n')
            print("Результаты успешно записаны в файл 'result_matrix_temp.txt'.")
            print("Результаты:")
            for row in result_matrix:
                print(row)
                