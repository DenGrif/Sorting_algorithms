# Sorting_algorithms
 Алгоритмы сортировки: 1. Пузырьковая сортировка, 2. Быстрая сортировка, 3. Сортировка выбором, 4. Сортировка вставками

DZ_main.py
Описание дополнительных задач:
Сортировка с пользовательским сравнением (compare) — позволяет сортировать элементы по любому критерию, 
например, по модулю, длине строки или другому свойству.

Сортировка строк (string_sort) — сортирует список строк по алфавиту.

Измерение производительности (measure_performance) — оценивает время выполнения алгоритма сортировки на 
заданном массиве.

Сортировка с ключом (sort_with_key) — позволяет сортировать объекты, применяя функцию key для извлечения 
значения для сравнения.

Визуализация сортировки (quick_sort_visualize) — показывает пошаговый процесс сортировки, 
что помогает понять работу алгоритма на практике.

Задания для самостоятельной работы:
Реализуйте дополнительные тесты для сравнения производительности сортировки на массивах разных размеров.
Расширьте визуализацию, добавив анимацию или цветовые акценты для различных этапов сортировки.
Реализуйте поддержку пользовательских ключей и сравнения для сложных объектов 
(например, сортировка списка словарей по определённому полю).

********************************************

DZ_main_colorama.py
Реализация визуализации, с добавлением анимации и цветовых акцентов для различных этапов сортировки.

Установка colorama:

pip install colorama

Объяснение:
Библиотека colorama:

Fore: используется для изменения цвета текста (например, Fore.BLUE для синего).
Style.RESET_ALL: сбрасывает цвет и стиль текста к стандартному.
Анимация:

Используется time.sleep() для добавления задержки между этапами сортировки, создавая эффект анимации.
Глубина рекурсии (depth):

Используется для отступов в консоли, чтобы показать уровень рекурсии.
Цвета:

Зеленый (Fore.GREEN) для возвращаемого значения.
Синий (Fore.BLUE) для текущего сортируемого массива.
Желтый (Fore.YELLOW) для разбивки массива на части.

### Задания для самостоятельной работы:
Попробуйте изменить цвета и добавьте дополнительные стили, такие как жирный шрифт или подчеркивание.
Улучшите анимацию, экспериментируя с длительностью задержки для разных этапов.
Добавьте ещё больше подробностей в визуализацию, например, количество оставшихся элементов или текущий индекс.