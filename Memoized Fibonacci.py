'''
Контекст проблемы

Последовательность Фибоначчи традиционно используется для объяснения рекурсии дерева.

def fibonacci(n):
    if n in [0, 1]:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

Этот алгоритм хорошо служит своей образовательной цели, но он чрезвычайно неэффективен не только из-за рекурсии, но и потому, что мы дважды вызываем функцию Фибоначчи и правую ветвь рекурсии (т.е. fibonacci(n-2)) пересчитывает все числа Фибоначчи, уже рассчитанные левой ветвью (т.е. fibonacci(n-1)).

Этот алгоритм настолько неэффективен, что времени для вычисления любого числа Фибоначчи больше 50 просто слишком много. Вы можете пойти выпить чашечку кофе или пойти вздремнуть, пока ждете ответа. Но если вы попробуете это здесь, в Code Wars, вы, скорее всего, получите тайм-аут кода перед любыми ответами.

Для этой конкретной Ката мы хотим реализовать решение для запоминания . Это будет круто, потому что позволит нам продолжать использовать алгоритм древовидной рекурсии , сохраняя при этом его достаточно оптимизированным для очень быстрого получения ответа.

Хитрость мемоизированной версии заключается в том, что мы сохраним структуру данных кеша (скорее всего, ассоциативный массив), где мы будем хранить числа Фибоначчи по мере их вычисления. Когда вычисляется число Фибоначчи, мы сначала ищем его в кеше, если его там нет, вычисляем и кладем в кеш, иначе возвращали кешированное число.

Преобразуйте функцию в рекурсивную функцию Фибоначчи, которая с помощью мемоизированной структуры данных позволяет избежать недостатков древовидной рекурсии. Можете ли вы сделать так, чтобы кеш мемоизации был приватным для этой функции?

'''

m = {0: 0, 1: 1}

def fib(n):
    if n in m:
        return m[n]
    m[n] = fib(n - 1) + fib(n - 2)
    return m[n]
print (fib(70))
print (fib(60))
print (fib(50))
