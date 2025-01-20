# необходимо установить: pip install colorama
import time
from colorama import Fore, Style, init

# Инициализация colorama для работы с цветами в Windows и Unix
init()

def quick_sort_visualize(arr, depth=0):
    """Визуализация процесса быстрой сортировки с цветами и анимацией."""
    if len(arr) <= 1:
        print(f"{'  ' * depth}{Fore.GREEN}Возвращаем: {arr}{Style.RESET_ALL}")
        time.sleep(0.5)
        return arr

    pivot = arr[0]
    left = list(filter(lambda x: x < pivot, arr))
    center = [x for x in arr if x == pivot]
    right = list(filter(lambda x: x > pivot, arr))

    print(f"{'  ' * depth}{Fore.BLUE}Сортируем: {arr}{Style.RESET_ALL}")
    print(f"{'  ' * (depth+1)}{Fore.YELLOW}Левая часть: {left}, Центр: {center}, Правая часть: {right}{Style.RESET_ALL}")
    time.sleep(1)

    sorted_left = quick_sort_visualize(left, depth + 1)
    sorted_right = quick_sort_visualize(right, depth + 1)

    return sorted_left + center + sorted_right

# Пример использования
print("Визуализация процесса сортировки:")
quick_sort_visualize([5, 2, 9, 0, 1, 5, 3])
