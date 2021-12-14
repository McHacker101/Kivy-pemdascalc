import math
operations = ["+", "-", '*', '/', '%']
def arithmetic(array, index):
    print(array[index])
    if array[index] == "+":
        new_num = int(array[index - 1]) + int(array[index + 1])
        array.insert(index - 1, new_num)
        del array[index:index+3]
        return array
    if array[index] == "-":
        new_num = int(array[index - 1]) - int(array[index + 1])
        array.insert(index - 1, new_num)
        del array[index:index+3] 
        return array
    if array[index] == "*":
        new_num = int(array[index - 1]) * int(array[index + 1])
        array.insert(index - 1, new_num)
        del array[index:index+3] 
        return array
    if array[index] == "/":
        new_num = int(array[index - 1]) / int(array[index + 1])
        array.insert(index - 1, new_num)
        del array[index:index+3] 
        return array

def solve_in_indices(array, indices):
    array_to_solve = array
    for i in indices:
        solution = arithmetic(array_to_solve, i)
    return solution


def solve(equation):
    eq = equation.split()
    op_indices = [ind for ind in range(len(eq)) if eq[ind] in operations]
    solution = solve_in_indices(eq, op_indices)
    return solution