# Por Brando Matute

def fibonacci(n: int) -> list[int]:
    if n <= 0:
        return []
    if n == 1:
        return [0]

    secuencia = [0, 1]
    while len(secuencia) < n:
        secuencia.append(secuencia[-1] + secuencia[-2])
    return secuencia


if __name__ == "__main__":
    n = 10
    print(f"Secuencia de Fibonacci con {n} términos:")
    print(fibonacci(n))
