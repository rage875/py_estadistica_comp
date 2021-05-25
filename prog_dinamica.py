def fibonacci_recursivo(n):
    if n == 0 or n == 1:
        return 1

    return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)

def fibonacci_dinamico_dict(n, memo = {}):
    if n == 0 or n == 1:
        return 1
    
    try:
        return memo[n]
    except KeyError:
        memo[n] = fibonacci_dinamico_dict(n - 1, memo) + fibonacci_dinamico_dict(n - 2, memo)
        return memo[n]

def fibonacci_dinamico_list(n, memo = [1]):
    if n == 0 or n == 1:
        return 1

    try:
        return memo[n - 1]
    except IndexError:
        memo.append(fibonacci_dinamico_list(n - 1) + fibonacci_dinamico_list(n - 2))

    return memo[n - 1]

if __name__ == '__main__':
    print(fibonacci_recursivo(8))
    print(fibonacci_dinamico_dict(50))
    print(fibonacci_dinamico_list(50))