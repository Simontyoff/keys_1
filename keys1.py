class ArrayProcessor:
    """Класс для обработки одномерного массива чисел."""

    def __init__(self, data: list):
        """
        Инициализация процессора массива.
        :param data: список чисел (исходный массив A)
        """
        self._data = list(data)
        self._sum_positive = 0
        self._count_positive = 0

    @property
    def data(self) -> list:
        """Возвращает копию массива."""
        return list(self._data)

    @property
    def size(self) -> int:
        """Возвращает размерность N массива."""
        return len(self._data)

    def compute(self) -> tuple:
        """
        Вычисляет сумму и количество положительных элементов.
        :return: кортеж (sum_positive, count_positive)
        """
        self._sum_positive = 0
        self._count_positive = 0

        for element in self._data:
            if element > 0:                     # ветвь условия
                self._sum_positive += element   # накопление суммы
                self._count_positive += 1       # подсчёт количества

        return self._sum_positive, self._count_positive

    def __str__(self) -> str:
        s, k = self.compute()
        return (f"Массив: {self._data}\n"
                f"Размерность N = {self.size}\n"
                f"Сумма положительных = {s}\n"
                f"Количество положительных = {k}")


def main():
    # Пример использования
    arr = [3, -1, 4, 0, -5, 2, 7]
    processor = ArrayProcessor(arr)
    print(processor)


if __name__ == "__main__":
    main()