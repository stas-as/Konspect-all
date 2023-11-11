import numpy as np

def get_dominant_eigenvalue_and_eigenvector(data, num_steps):
    """
    data: np.ndarray – symmetric diagonalizable real-valued matrix
    num_steps: int – number of power method steps
    
    Returns:
    eigenvalue: float – dominant eigenvalue estimation after num_steps steps
    eigenvector: np.ndarray – corresponding eigenvector estimation
    """
    ### YOUR CODE HERE
    n = data.shape[0]
    eigenvector = np.random.rand(n)
    eigenvector = eigenvector / np.linalg.norm(eigenvector)  # Нормализация вектора

    for i in range(num_steps):
        # Используйте метод степеней для оценки доминантного собственного значения и вектора
        # ваши операции с матрицами и векторами с помощью библиотеки NumPy
        
        # data.dot(eigenvector) - умножение матрицы на вектор
        # np.linalg.norm(...) - нормализация вектора
        eigenvector = data.dot(eigenvector)
        eigenvector = eigenvector / np.linalg.norm(eigenvector)  # Нормализация вектора

    # Оценка доминантного собственного значения
    eigenvalue = np.dot(eigenvector, data.dot(eigenvector))

    return float(eigenvalue),eigenvector