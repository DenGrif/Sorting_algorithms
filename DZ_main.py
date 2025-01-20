# Дополним домашнюю работу, добавив дополнительные методы и задачи с реализацией сортировки:
#
# Сортировка с пользовательским сравнением — позволить пользователю передать свою функцию сравнения для сортировки.
# Сортировка строк — реализовать алгоритм сортировки для списка строк.
# Измерение производительности — добавить "измерение времени выполнения сортировки" для различных размеров входного массива.
# Сортировка с использованием ключа — сортировать не только числа, но и объекты с использованием ключа для сравнения.
# Сортировка с визуализацией — добавить возможность пошаговой визуализации процесса сортировки.
import time


def quick_sort(arr, compare=lambda x, y: x < y):
    """Быстрая сортировка с поддержкой пользовательского сравнения."""

    def _quick_sort(start, end):
        if start >= end:
            return

        pivot = arr[start]
        i = start + 1
        j = end

        while True:
            while i < end and compare(arr[i], pivot):
                i += 1

            while j > start and not compare(arr[j], pivot):
                j -= 1

            if i >= j:
                break

            arr[i], arr[j] = arr[j], arr[i]

        arr[start], arr[j] = arr[j], arr[start]

        _quick_sort(start, j)
        _quick_sort(j + 1, end)

    _quick_sort(0, len(arr) - 1)
    return arr


def string_sort(arr):
    """Сортировка строк по алфавиту."""
    return quick_sort(arr, compare=lambda x, y: x < y)


def measure_performance(arr):
    """Измерение времени выполнения сортировки."""
    start_time = time.time()
    sorted_arr = quick_sort(arr)
    end_time = time.time()
    print(f"Сортировка заняла {end_time - start_time:.6f} секунд.")
    return sorted_arr


def sort_with_key(arr, key):
    """Сортировка с использованием ключа."""
    return quick_sort(arr, compare=lambda x, y: key(x) < key(y))


def quick_sort_visualize(arr):
    """Визуализация процесса быстрой сортировки."""
    if len(arr) <= 1:
        print(f"Возвращаем: {arr}")
        return arr

    pivot = arr[0]
    left = list(filter(lambda x: x < pivot, arr))
    center = [x for x in arr if x == pivot]
    right = list(filter(lambda x: x > pivot, arr))

    print(f"Сортируем: {arr}")
    print(f"Левая часть: {left}, Центр: {center}, Правая часть: {right}")

    return quick_sort_visualize(left) + center + quick_sort_visualize(right)


# 1. Сортировка чисел
print("Сортировка чисел:")
print(quick_sort([5, 2, 9, 0, 1, 5, 3]))

# 2. Сортировка строк
print("\nСортировка строк:")
print(string_sort(["apple", "banana", "cherry", "date"]))

# 3. Измерение производительности
print("\nИзмерение производительности:")
print(measure_performance([5, 2, 9, 0, 1, 5, 3]))

# 4. Сортировка с ключом
print("\nСортировка по длине строк:")
print(sort_with_key(["apple", "banana", "cherry", "date"], key=len))

# 5. Визуализация быстрой сортировки
print("\nВизуализация процесса сортировки:")
quick_sort_visualize([5, 2, 9, 0, 1, 5, 3])