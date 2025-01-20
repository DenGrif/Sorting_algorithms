import sys
import time
from colorama import Fore, Style, init

# Инициализация colorama для работы с цветами в Windows и Unix
init()

# Установка лимита рекурсии (по желанию, если работа с большими массивами)
sys.setrecursionlimit(2000)

def quick_sort(arr, compare=lambda x, y: x < y):
    """Рекурсивный алгоритм быстрой сортировки с медианой из трех как опорным элементом."""
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    pivot_candidates = [arr[0], arr[mid], arr[-1]]
    pivot = sorted(pivot_candidates)[1]  # Медиана из трех

    left = list(filter(lambda x: compare(x, pivot), arr))
    center = [x for x in arr if not compare(x, pivot) and not compare(pivot, x)]
    right = list(filter(lambda x: not compare(x, pivot) and x != pivot, arr))

    return quick_sort(left, compare) + center + quick_sort(right, compare)

def quick_sort_visualize(arr, depth=0):
    """Визуализация процесса быстрой сортировки с цветами и анимацией."""
    if len(arr) <= 1:
        print(f"{'  ' * depth}{Fore.GREEN}Возвращаем: {arr}{Style.RESET_ALL}")
        time.sleep(0.5)
        return arr

    mid = len(arr) // 2
    pivot_candidates = [arr[0], arr[mid], arr[-1]]
    pivot = sorted(pivot_candidates)[1]  # Медиана из трех

    left = list(filter(lambda x: x < pivot, arr))
    center = [x for x in arr if x == pivot]
    right = list(filter(lambda x: x > pivot, arr))

    print(f"{'  ' * depth}{Fore.BLUE}Сортируем: {arr}{Style.RESET_ALL}")
    print(f"{'  ' * (depth+1)}{Fore.YELLOW}Левая часть: {left}, Центр: {center}, Правая часть: {right}{Style.RESET_ALL}")
    time.sleep(1)

    sorted_left = quick_sort_visualize(left, depth + 1)
    sorted_right = quick_sort_visualize(right, depth + 1)

    return sorted_left + center + sorted_right

def quick_sort_iterative(arr):
    """Итеративный алгоритм быстрой сортировки с использованием стека."""
    if len(arr) <= 1:
        return arr

    stack = [(0, len(arr) - 1)]
    result = arr[:]

    while stack:
        start, end = stack.pop()
        if start >= end:
            continue

        pivot = result[start]
        low, high = start, end

        while low <= high:
            while low <= high and result[low] < pivot:
                low += 1
            while low <= high and result[high] > pivot:
                high -= 1
            if low <= high:
                result[low], result[high] = result[high], result[low]
                low, high = low + 1, high - 1

        stack.append((start, high))
        stack.append((low, end))

    return result

# Примеры использования
print("Быстрая сортировка (рекурсивная):")
print(quick_sort([5, 2, 9, 0, 1, 5, 3]))

print("\nВизуализация быстрой сортировки:")
quick_sort_visualize([5, 2, 9, 0, 1, 5, 3])

print("\nБыстрая сортировка (итеративная):")
print(quick_sort_iterative([5, 2, 9, 0, 1, 5, 3]))
