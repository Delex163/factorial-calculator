#!/usr/bin/env python3
"""
Программа для вычисления факториала положительного целого числа.
Поддерживает оптимизацию для больших чисел через библиотеку math.
"""

import math
import sys

def factorial_iterative(n: int) -> int:
    """
    Итеративное вычисление факториала (на случай, если нужно показать реализацию).
    Для действительно больших чисел лучше использовать math.factorial,
    который написан на C и оптимизирован.
    """
    if n < 0:
        raise ValueError("Факториал определён только для неотрицательных чисел")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def factorial_optimized(n: int) -> int:
    """
    Оптимизированное вычисление факториала с использованием встроенной библиотеки math.
    Рекомендуется для больших чисел (n > 1000).
    """
    if n < 0:
        raise ValueError("Факториал определён только для неотрицательных чисел")
    return math.factorial(n)

def get_positive_integer() -> int:
    """
    Запрашивает у пользователя ввод положительного целого числа.
    Обрабатывает все возможные ошибки ввода.
    """
    while True:
        try:
            user_input = input("Введите положительное целое число: ").strip()
            
            # Проверка на пустую строку
            if not user_input:
                print("Ошибка: Ввод не может быть пустым. Попробуйте снова.")
                continue
            
            # Попытка преобразования в целое число
            number = int(user_input)
            
            # Проверка на отрицательное значение
            if number < 0:
                print("Ошибка: Число должно быть положительным (0 или больше). Попробуйте снова.")
                continue
            
            return number
        
        except ValueError:
            print("Ошибка: Необходимо ввести целое число. Попробуйте снова.")
        except EOFError:
            print("\nОбнаружен конец ввода. Завершение программы.")
            sys.exit(0)
        except KeyboardInterrupt:
            print("\nПрограмма прервана пользователем.")
            sys.exit(0)

def main():
    """Основная функция программы."""
    print("=" * 50)
    print("   Калькулятор факториала (оптимизированная версия)")
    print("=" * 50)
    
    # Получение корректного числа от пользователя
    number = get_positive_integer()
    
    # Вычисление факториала оптимизированным способом
    try:
        # Для демонстрации используем оптимизированную версию с math.factorial
        result = factorial_optimized(number)
        
        # Вывод результата с форматированием для больших чисел
        print(f"\nРезультат вычисления факториала {number}!:")
        
        # Если число небольшое, показываем полное значение
        if number <= 20:
            print(f"{number}! = {result}")
        else:
            # Для больших чисел показываем в научном формате и количество цифр
            digits = len(str(result))
            print(f"{number}! ≈ {result:.6e}")
            print(f"(Точное значение содержит {digits} цифр)")
            print(f"Полное значение сохранено в переменной 'result'")
    
    except OverflowError:
        print(f"Ошибка: Факториал числа {number} слишком велик для вычисления.")
        print("Попробуйте число поменьше (например, до 10000).")
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")

def demo_comparison():
    """
    Дополнительная функция для сравнения производительности (опционально).
    Показывает преимущество math.factorial для больших чисел.
    """
    import time
    
    print("\n" + "=" * 50)
    print("   Сравнение производительности для n = 5000")
    print("=" * 50)
    
    n = 5000
    
    # Итеративный метод
    start = time.time()
    iter_result = factorial_iterative(n)
    iter_time = time.time() - start
    
    # Оптимизированный метод (math)
    start = time.time()
    math_result = factorial_optimized(n)
    math_time = time.time() - start
    
    print(f"Итеративный метод: {iter_time:.6f} секунд")
    print(f"math.factorial:     {math_time:.6f} секунд")
    print(f"Ускорение:          {iter_time/math_time:.2f}x")
    print(f"Результаты совпадают: {iter_result == math_result}")

if __name__ == "__main__":
    main()
    
    # Раскомментируйте следующую строку, чтобы увидеть сравнение производительности
    # demo_comparison()