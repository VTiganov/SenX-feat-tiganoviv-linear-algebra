from typing import List, Optional

class matrixKeeper:
    def __init__(self):
        self.matrix: Optional[List[List[float]]] = None

    def inputMatrix(self) -> None:
        """Ввод матрицы
        Первое приглашение - ввод размера матрицы n X m
        Второе приглашение - ввод самой матрицы по строчке, элементы через пробел"""
        
        try:
            n, m = map(int, input("Введите размер матрицы n x m через пробел: ").split())
            self.matrix = []
            for _ in range(n):
                row = list(map(float, input().split()))
                if len(row) != m:
                    raise ValueError("Количество элементов в строке не соответствует m.")
                self.matrix.append(row)
        except ValueError as e:
            print(f"Ошибка ввода: {e}")
            self.matrix = None

    def trace(self) -> float:
        """Поиск следа матрицы"""
        
        if self.matrix is None:
            raise ValueError("Матрица не была введена.")

        if len(self.matrix) != len(self.matrix[0]):
            raise ValueError("Матрица должна быть квадратной для вычисления следа.")

        return sum(self.matrix[i][i] for i in range(len(self.matrix)))

    def findByIndex(self, n: int, m: int) -> float:
        """Находит элемент в матрице по индексу вида n, m и выводит его"""
        
        if self.matrix is None:
            raise ValueError("Матрица не была введена.")

        if n <= 0 or m <= 0 or n > len(self.matrix) or m > len(self.matrix[0]):
            raise IndexError("Индексы выходят за пределы матрицы.")

        return self.matrix[n-1][m-1]

