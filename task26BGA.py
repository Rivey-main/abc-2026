def load_matrix(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    matrix = [[int(num) for num in line.split()] for line in lines if line.strip()]
    if not matrix:
        return False
    is_valid = len({len(row) for row in matrix}) == 1
    return matrix if is_valid else False


print("Результат загрузки правильной матрицы:")
print(load_matrix("matrix.txt")) 