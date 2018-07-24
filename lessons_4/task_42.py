#Написать два алгоритма нахождения i-го по счёту простого числа.


def eratosthenes(n):
    numbers = [k for k in range(2, 100)]
    prime = []
    i = 0
    while i < len(numbers):
        prime.append(numbers[i])
        j = i
        while i < len(numbers):
            if numbers[j] % numbers[i] == 0 and numbers[i] != numbers[j]:
                    numbers.pop(j)
            j += 1
            if j >= len(numbers):
                break
        i += 1
        if i >= len(numbers):
            break
    print(prime[n - 1])

'''
for n = 15
         880 function calls in 0.001 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
        1    0.001    0.001    0.001    0.001 task_42.py:4(eratosthenes)
        1    0.000    0.000    0.000    0.000 task_42.py:5(<listcomp>)
        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
      776    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
       25    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
       73    0.000    0.000    0.000    0.000 {method 'pop' of 'list' objects}
'''


def my_prime(number):
    prime = [2]
    k = 3
    while len(prime) < number:
        n = 0
        for j in range(2, k):
            if k % j == 0:
                n += 1
                break
        if n == 0:
            prime.append(k)
        k += 1
    print(prime[number - 1])


'''
for number = 15
         65 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 task_42.py:41(my_prime)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
       46    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
       14    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
'''
