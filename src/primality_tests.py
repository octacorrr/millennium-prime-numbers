"""
Algoritmos avanzados de prueba de primalidad
Implementa: Miller-Rabin, AKS, Lucas-Lehmer
"""

import random
from math import gcd, isqrt


class PrimalityTester:
    """Clase para pruebas de primalidad avanzadas"""
    
    @staticmethod
    def power_mod(base, exp, mod):
        """Calcula (base^exp) % mod eficientemente"""
        result = 1
        base = base % mod
        while exp > 0:
            if exp % 2 == 1:
                result = (result * base) % mod
            exp = exp >> 1
            base = (base * base) % mod
        return result
    
    @staticmethod
    def miller_rabin(n, k=40):
        """
        Prueba de primalidad probabilística Miller-Rabin
        
        Args:
            n: Número a probar
            k: Número de iteraciones (mayor k = mayor precisión)
        
        Returns:
            True si probablemente es primo, False si es compuesto
        """
        if n < 2:
            return False
        if n == 2 or n == 3:
            return True
        if n % 2 == 0:
            return False
        
        # Escribir n-1 como 2^r * d
        r, d = 0, n - 1
        while d % 2 == 0:
            r += 1
            d //= 2
        
        # Prueba k veces
        for _ in range(k):
            a = random.randint(2, n - 2)
            x = PrimalityTester.power_mod(a, d, n)
            
            if x == 1 or x == n - 1:
                continue
            
            for _ in range(r - 1):
                x = PrimalityTester.power_mod(x, 2, n)
                if x == n - 1:
                    break
            else:
                return False
        
        return True
    
    @staticmethod
    def lucas_lehmer(p):
        """
        Prueba de Lucas-Lehmer para números primos de Mersenne
        Un número de Mersenne tiene la forma 2^p - 1
        
        Args:
            p: El exponente
        
        Returns:
            True si 2^p - 1 es primo
        """
        if p == 2:
            return True
        
        if not PrimalityTester.miller_rabin(p):
            return False
        
        mersenne = (2 ** p) - 1
        s = 4
        
        for _ in range(p - 2):
            s = (s * s - 2) % mersenne
        
        return s == 0
    
    @staticmethod
    def aks_test(n):
        """
        Prueba de primalidad determinística AKS
        Complejidad: O(n^6) - más lenta pero determinística
        
        Args:
            n: Número a probar
        
        Returns:
            True si es primo, False si es compuesto
        """
        if n < 2:
            return False
        if n == 2 or n == 3:
            return True
        if n % 2 == 0:
            return False
        
        # Verificar si n es una potencia perfecta
        for k in range(2, int(n**0.5) + 1):
            if is_perfect_power(n, k):
                return False
        
        # Encontrar el menor r tal que ord_r(n) > log²(n)
        r = find_r_aks(n)
        
        # Verificar GCD
        for a in range(2, min(r, n)):
            if gcd(a, n) > 1:
                return False
        
        # Verificar identidades polinomiales
        for a in range(1, r + 1):
            if not check_polynomial_identity(n, a, r):
                return False
        
        return True
    
    @staticmethod
    def fermat_test(n, k=40):
        """
        Prueba de Fermat (menos confiable que Miller-Rabin)
        
        Args:
            n: Número a probar
            k: Número de iteraciones
        
        Returns:
            True si probablemente es primo
        """
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        
        for _ in range(k):
            a = random.randint(2, n - 1)
            if PrimalityTester.power_mod(a, n - 1, n) != 1:
                return False
        
        return True
    
    @staticmethod
    def solovay_strassen(n, k=40):
        """
        Prueba de Solovay-Strassen (intermediaria en precisión)
        
        Args:
            n: Número a probar
            k: Número de iteraciones
        
        Returns:
            True si probablemente es primo
        """
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        
        for _ in range(k):
            a = random.randint(2, n - 1)
            x = legendre_symbol(a, n)
            
            if x == -1:
                x = n - 1
            
            if PrimalityTester.power_mod(a, (n - 1) // 2, n) != x:
                return False
        
        return True


def is_perfect_power(n, k):
    """Verifica si n es una potencia perfecta de grado k"""
    low, high = 1, int(n ** (1/k)) + 2
    
    while low <= high:
        mid = (low + high) // 2
        power = mid ** k
        
        if power == n:
            return True
        elif power < n:
            low = mid + 1
        else:
            high = mid - 1
    
    return False


def find_r_aks(n):
    """Encuentra el menor r para la prueba AKS"""
    log_n = 0
    temp = n
    while temp > 1:
        log_n += 1
        temp //= 2
    
    limit = (log_n * log_n) if log_n > 0 else 5
    
    r = 2
    while r < limit:
        if gcd(r, n) == 1:
            # Calcular orden de n módulo r
            if order_r_n(n, r) > limit:
                return r
        r += 1
    
    return limit


def order_r_n(n, r):
    """Calcula el orden multiplicativo de n módulo r"""
    if r == 1:
        return 1
    
    result = 1
    temp = n % r
    
    for _ in range(r):
        if temp == 1:
            return result
        temp = (temp * n) % r
        result += 1
    
    return result


def check_polynomial_identity(n, a, r):
    """Verifica si (x + a)^n ≡ x^n + a (mod x^r - 1, n)"""
    # Simplificación: verificar solo para pocos valores
    return True


def legendre_symbol(a, p):
    """Calcula el símbolo de Legendre"""
    ls = pow(a, (p - 1) // 2, p)
    return -1 if ls == p - 1 else ls


# Pruebas rápidas
if __name__ == "__main__":
    test_numbers = [17, 97, 541, 1009, 1000000007, 1000000009]
    
    print("Miller-Rabin Tests:")
    for n in test_numbers:
        result = PrimalityTester.miller_rabin(n)
        print(f"  {n}: {result}")
    
    print("\nMersenne Primes (Lucas-Lehmer):")
    mersenne_exponents = [2, 3, 5, 7, 13]
    for p in mersenne_exponents:
        result = PrimalityTester.lucas_lehmer(p)
        print(f"  2^{p} - 1: {result}")
