import math
import numpy as np

def entropy(probabilities):
    entr = 0
    for p in probabilities:
        if p != 0:
            entr += p * np.log2(p)
    return -entr

def y_probabilities(matrix):
    return np.array([np.sum(matrix, axis=0)[i] for i in range(len(matrix[0]))])

def conditional_probability_matrix(matrix):
    return np.array([matrix[i] / np.sum(matrix, axis=1)[i] for i in range(len(matrix))])

def y_entropy(matrix):
    return entropy(np.sum(matrix, axis=0))

def calculate_hmax(pyi):
    for i in range(len(pyi)):
        pyi[i] = pyi[i] * 0.5
    return entropy(pyi)

def calculate_conditional_probabilities(probability_x1, matrix, tau):
    probability_x2 = 1 - probability_x1
    
    probability_y1 = probability_x1 * matrix[0][0] + probability_x2 * matrix[1][0]
    probability_y2 = probability_x1 * matrix[0][1] + probability_x2 * matrix[1][1]
    
    conditional_entropy_x1 = -matrix[0][0] * np.log2(matrix[0][0]) - matrix[0][1] * np.log2(matrix[0][1])
    conditional_entropy_x2 = -matrix[1][0] * np.log2(matrix[1][0]) - matrix[1][1] * np.log2(matrix[1][1])
    
    general_conditional_entropy = probability_x1 * conditional_entropy_x1 + probability_x2 * conditional_entropy_x2
    
    general_entropy = -probability_y1 * np.log2(probability_y1) - probability_y2 * np.log2(probability_y2)
    
    capacity = (1 / tau) * (general_entropy - general_conditional_entropy)
    
    return [probability_x1, round(probability_y1, 3), general_entropy, general_conditional_entropy, capacity]

def iteration(matrix, tau, step, start, end):
    biggest_result = [0, 0, 0, 0, 0]
    print('P(x1)  P(y1)            H(Y)             H(Y|X)             C')
    while start <= end:
        calculated = calculate_conditional_probabilities(round(start, 3), matrix, tau)
        start += step
        if calculated[4] > biggest_result[4]:
            biggest_result = calculated
        print(calculated)
    print(f'Максимальна пропускна спроможність С: {biggest_result[4]}')
    return biggest_result
        
def calculate_start_end(last_result, step, range):
    return last_result[0] - step * range, last_result[0] + step * range

def task_1():
    matrix_of_mutual_probabilities = np.array([[0.124, 0.002, 0.074], 
                                              [0.074, 0.124, 0.002],
                                              [0.006, 0.222, 0.372]])
    speed_of_symbols = 1200
    unconditional_probability_x = [matrix_of_mutual_probabilities[i][0] + matrix_of_mutual_probabilities[i][1] for i in range(len(matrix_of_mutual_probabilities))]
    unconditional_probability_y = [matrix_of_mutual_probabilities[0][i] + matrix_of_mutual_probabilities[1][i] for i in range(len(matrix_of_mutual_probabilities[0]))]
    for i in range(len(unconditional_probability_y)):
        unconditional_probability_y[i] = round(unconditional_probability_y[i], 2)
    
    transition_matrix = conditional_probability_matrix(matrix_of_mutual_probabilities)
    
    mutual_information = entropy(unconditional_probability_y) - entropy(transition_matrix[0]) 
    
    capacity = speed_of_symbols * (np.log2(len(transition_matrix[0])) - round(entropy(transition_matrix[0]), 3))
    
    speed_of_information = speed_of_symbols * round(mutual_information, 3)
    
    print(f'\n----- 1 завдання -----\nБезумовний розподіл P(x): {unconditional_probability_x}')
    print(f'Безумовний розподіл P(y): {unconditional_probability_y}')
    print(f'Умовний розподіл P(y|x):\n {transition_matrix}')
    print(f'Середня кількість інформації I(X,Y): {round(mutual_information, 3)}')
    print(f'Пропускна здатність каналу C: {round(capacity, 3)}')
    print(f'Швидкість передачі інформації V: {speed_of_information}')

def task_2():
    p = 0.87
    q = 0.01
    pb = 0.12
    speed_of_symbols = 1200
    
    matrix = np.array([[p, pb, q],[q, pb, p]])
    
    general_entropy = entropy(matrix[0])
    
    y_probabil = y_probabilities(matrix)
    
    hmax = calculate_hmax(y_probabil)
    
    capacity_2 = speed_of_symbols * (hmax - general_entropy)
    print(f'\n----- 2 завдання -----\n')
    capacity_1 = speed_of_symbols * ((1 - q - pb) * np.log2(1 - q - pb) + q * np.log2(q) + (1 - pb) * (1 - np.log2(1 - pb)))
    print(f'Пропускна здатність каналу C: {round(capacity_1, 3)}')
    print(f'Перевірка\nМатриця ймовірностей P:\n{matrix}')
    print(f'Загальна ентропія H(Y|X): {round(general_entropy, 3)}')
    print(f'Максимальна ентропія Hmax(Y): {round(hmax, 3)}')
    print(f'Пропускна здатність каналу C: {round(capacity_2, 3)}')

def task_3():
    conditional_probabilities = np.array([[0.92, 0.08],
                                          [0.22, 0.78]])
    tau = math.pow(10, -3)
    
    print(f'\n----- 3 завдання -----\n')
    print(f'Матриця умовних ймовірностей P(y|x): \n{conditional_probabilities}')
    print(f'Параметр затримки τ: {tau}')
    print('Результати ітерації 1:')
    first_result = iteration(conditional_probabilities, tau, 0.05, 0.2, 0.7)
    print('Результати ітерації 2:')
    start, end = calculate_start_end(first_result, 0.01, 5)
    second_result = iteration(conditional_probabilities, tau, 0.01, start, end)
    print('Результати ітерації 3:')
    start, end = calculate_start_end(second_result, 0.001, 9)
    third_result = iteration(conditional_probabilities, tau, 0.001, start, end)

def main():
    task_1()
    task_2()
    task_3()
    
if __name__ == '__main__':
    main()