# 1) за заданими значеннями ймовірності появи символів 
# обчислити ентропію та надлишковість дискретного джерела інформації

# 2) задано матрицю сумісних імовірностей p(x, y) прояви двох символів 
# на виходах джерел x та y. Обчислити ентропію обʼєднання двох джерел, 
# загальні умовні енропії, середню взаємну кількість інформації
# визначити, яке з цих двох джерел має більшу надлишковість 
# та чи є джерела статистично незалежними

# 3) Для двох дискретних джерел задано числові значення однієї
# безумовної та однієї умовної ймовірності появи символів.
# знайти все, що вказано в пункті 2
import math
import numpy as np

def entropy(probabilities):
    entr = 0
    for p in probabilities:
        if p != 0:
            entr += p * np.log2(p)
    return -entr

def statistical_redundancy(probabilities):
    return 1 - (entropy(probabilities) / np.log2(len(probabilities)))

def conditional_probability_matrix(matrix):
    return np.array([matrix[i] / np.sum(matrix, axis=1)[i] for i in range(len(matrix))])

def general_entropy_x_y(matrix):
    entr = 0
    for i in range(len(matrix)):
        entr += entropy(matrix[i])
    return entr

def x_entropy(matrix):
    return entropy(np.sum(matrix, axis=1))

def y_entropy(matrix):
    return entropy(np.sum(matrix, axis=0))

def mutual_information(matrix):
    return general_entropy_x_y(matrix) - x_entropy(matrix) - y_entropy(matrix)

def matrix_of_mutual_probabilities_x(conditional_probability_matrix, unconditional_probability):
    return np.array([conditional_probability_matrix[i] * unconditional_probability[i] for i in range(len(unconditional_probability))])
    
def matrix_of_mutual_probabilities_y(conditional_probability_matrix, unconditional_probability):
    return np.array([conditional_probability_matrix[:, i] * unconditional_probability[i] for i in range(len(unconditional_probability))])

def task_1():
    probabilities = [0.1, 0.78, 0.02, 0.05, 0.05]
    print(f'----- 1 завдання -----\nЕнтропія H(X): {round(entropy(probabilities), 3)}')
    print(f'Статистична надлишковість p(X): {round(statistical_redundancy(probabilities), 3)}')
    
def task_2():
    matrix = np.array([[0.91, 0.01, 0.02], 
                       [0.03, 0, 0.01], 
                       [0.01, 0.01, 0]])
    
    print(f'----- 2 завдання -----\nЗагальна ентропія H(X,Y): {round(general_entropy_x_y(matrix), 3)}')
    print(f'Умовна ентропія H(X): {round(x_entropy(matrix), 3)}')
    print(f'Умовна ентропія H(Y): {round(y_entropy(matrix), 3)}')
    print(f'Загальна умовна ентропія H(X|Y): {round(general_entropy_x_y(matrix) - y_entropy(matrix), 3)}')
    print(f'Загальна умовна ентропія H(Y|X): {round(general_entropy_x_y(matrix) - x_entropy(matrix), 3)}')
    print(f'Середня взаємна кількість інформації I(X,Y): {round(mutual_information(matrix), 3)}')
    print(f'Статистична надлишковість p(X): {round(statistical_redundancy(np.sum(matrix, axis=1)), 3)}')
    print(f'Статистична надлишковість p(Y): {round(statistical_redundancy(np.sum(matrix, axis=0)), 3)}')
    print(f'Джерело X має більшу надлишковість' if statistical_redundancy(np.sum(matrix, axis=1)) > statistical_redundancy(np.sum(matrix, axis=0)) else 'Джерело Y має більшу надлишковість')
    print(f'Джерела X та Y статистично незалежні' if general_entropy_x_y(matrix) == x_entropy(matrix) + y_entropy(matrix) else 'Джерела статистично залежні')
    con_matrix = conditional_probability_matrix(matrix)
    print(f'Матриця умовних ймовірностей P(Y|X):')
    for i in range(len(con_matrix)):
        print('[', end = '')
        for j in range(len(con_matrix[i])):
            print(f'{round(con_matrix[i][j], 3)}', end=' ')
        print(']')

def task_3():
    unconditional_probability = [0.17, 0.51, 0.32]
    conditional_prob_matrix = np.array([[0.01, 0.02, 0.97], 
                                        [0.03, 0.74, 0.23], 
                                        [0.17, 0.51, 0.32]])
    matrix = matrix_of_mutual_probabilities_x(conditional_prob_matrix, unconditional_probability)
    print(f'----- 3 завдання -----\nМатриця сумісних ймовірностей P(X,Y):')
    for i in range(len(matrix)):
        print('[', end = '')
        for j in range(len(matrix[i])):
            print(f'{round(matrix[i][j], 3)}', end=' ')
        print(']')
    print(f'Загальна ентропія H(X,Y): {round(general_entropy_x_y(matrix), 3)}')
    print(f'Умовна ентропія H(X): {round(x_entropy(matrix), 3)}')
    print(f'Умовна ентропія H(Y): {round(y_entropy(matrix), 3)}')
    print(f'Загальна умовна ентропія H(X|Y): {round(general_entropy_x_y(matrix) - y_entropy(matrix), 3)}')
    print(f'Загальна умовна ентропія H(Y|X): {round(general_entropy_x_y(matrix) - x_entropy(matrix), 3)}')
    print(f'Середня взаємна кількість інформації I(X,Y): {round(mutual_information(matrix), 3)}')
    print(f'Статистична надлишковість p(X): {round(statistical_redundancy(np.sum(matrix, axis=1)), 3)}')
    print(f'Статистична надлишковість p(Y): {round(statistical_redundancy(np.sum(matrix, axis=0)), 3)}')
    print(f'Джерело X має більшу надлишковість' if statistical_redundancy(np.sum(matrix, axis=1)) > statistical_redundancy(np.sum(matrix, axis=0)) else 'Джерело Y має більшу надлишковість')
    
def main():
    task_1()
    task_2()
    task_3()
    
if __name__ == "__main__":
    main()