"""
Generación avanzada de números primos
Implementa: Criba de Eratóstenes, Números de Mersenne, Segmented Sieve
"""

import math
from src.primality_tests import PrimalityTester


class PrimeGenerator:
    """Clase para generar números primos eficientemente"""
    
    @staticmethod
    def sieve_of_eratosthenes(limit):
        """
        Criba de Eratóstenes - O(n log log n)
        Genera todos los primos hasta 'limit'
        
        Args:
            limit: Límite superior
        
        Returns:
            Lista de números primos hasta limit
        """
        if limit < 2:
            return []
        
        # Crear array booleano, asumir que todos son primos
        is_prime = [True] * (limit + 1)
        is_prime[0] = is_prime[1] = False
        
        for i in range(2, int(math.sqrt(limit)) + 1):
            if is_prime[i]:
                # Marcar todos los múltiplos como no primos
                for j in range(i * i, limit + 1, i):
                    is_prime[j] = False
        
        return [num for num in range(2, limit + 1) if is_prime[num]]
    
    @staticmethod
    def segmented_sieve(low, high):
        """
        Criba segmentada para rangos muy grandes
        Más eficiente en memoria que Eratóstenes para rangos específicos
        
        Args:
            low: Límite inferior
            high: Límite superior
        
        Returns:
            Lista de primos entre low y high
        """
        if low < 2:
            low = 2
        
        limit = int(math.sqrt(high)) + 1
        base_primes = PrimeGenerator.sieve_of_eratosthenes(limit)
        
        is_prime = [True] * (high - low + 1)
        
        for p in base_primes:
            start = max(p * p, ((low + p - 1) // p) * p)
            for j in range(start, high + 1, p):
                is_prime[j - low] = False
        
        primes = []
        for i in range(len(is_prime)):
            if is_prime[i]:
                primes.append(low + i)
        
        return primes
    
    @staticmethod
    def sieve_of_atkin(limit):
        """
        Criba de Atkin - O(n / log log n), más rápida para límites muy grandes
        
        Args:
            limit: Límite superior
        
        Returns:
            Lista de números primos hasta limit
        """
        if limit < 2:
            return []
        
        is_prime = [False] * (limit + 1)
        is_prime[2] = is_prime[3] = True
        
        x = 1
        while x * x <= limit:
            y = 1
            while y * y <= limit:
                n = (4 * x * x) + (y * y)
                if n <= limit and n % 12 in [1, 5]:
                    is_prime[n] = not is_prime[n]
                
                n = (3 * x * x) + (y * y)
                if n <= limit and n % 12 == 7:
                    is_prime[n] = not is_prime[n]
                
                n = (3 * x * x) - (y * y)
                if x > y and n <= limit and n % 12 == 11:
                    is_prime[n] = not is_prime[n]
                
                y += 1
            x += 1
        
        # Eliminar cuadrados
        r = 5
        while r * r <= limit:
            if is_prime[r]:
                for i in range(r * r, limit + 1, r * r):
                    is_prime[i] = False
            r += 1
        
        return [num for num in range(2, limit + 1) if is_prime[num]]
    
    @staticmethod
    def generate_primes_miller_rabin(limit, k=40):
        """
        Genera primos usando Miller-Rabin (probabilístico)
        Útil para verificar números individuales grandes
        
        Args:
            limit: Límite superior
            k: Precisión de Miller-Rabin
        
        Returns:
            Lista de números primos hasta limit
        """
        primes = []
        if limit >= 2:
            primes.append(2)
        
        for num in range(3, limit + 1, 2):
            if PrimalityTester.miller_rabin(num, k):
                primes.append(num)
        
        return primes
    
    @staticmethod
    def next_prime(n):
        """
        Encuentra el siguiente número primo después de n
        
        Args:
            n: Número inicial
        
        Returns:
            El siguiente número primo
        """
        candidate = n + 1
        if candidate % 2 == 0:
            candidate += 1
        
        while not PrimalityTester.miller_rabin(candidate):
            candidate += 2
        
        return candidate
    
    @staticmethod
    def twin_primes(limit):
        """
        Encuentra todos los pares de números primos gemelos hasta limit
        Primos gemelos: pares de primos que difieren en 2 (p, p+2)
        
        Args:
            limit: Límite superior
        
        Returns:
            Lista de tuplas (p, p+2) de primos gemelos
        """
        primes = PrimeGenerator.sieve_of_eratosthenes(limit)
        prime_set = set(primes)
        
        twin_primes_list = []
        for p in primes:
            if p + 2 in prime_set:
                twin_primes_list.append((p, p + 2))
        
        return twin_primes_list
    
    @staticmethod
    def mersenne_primes(max_exponent):
        """
        Encuentra números primos de Mersenne (2^p - 1 donde p es primo)
        
        Args:
            max_exponent: Máximo exponente a verificar
        
        Returns:
            Lista de exponentes p donde 2^p - 1 es primo
        """
        primes = PrimeGenerator.sieve_of_eratosthenes(max_exponent)
        mersenne_list = []
        
        for p in primes:
            if p > 2 and PrimalityTester.lucas_lehmer(p):
                mersenne_list.append(p)
            elif p == 2:
                mersenne_list.append(2)
        
        return mersenne_list
    
    @staticmethod
    def prime_gaps(limit):
        """
        Analiza los espacios entre números primos consecutivos
        
        Args:
            limit: Límite superior
        
        Returns:
            Diccionario con estadísticas de espacios
        """
        primes = PrimeGenerator.sieve_of_eratosthenes(limit)
        
        gaps = []
        gap_freq = {}
        
        for i in range(len(primes) - 1):
            gap = primes[i + 1] - primes[i]
            gaps.append(gap)
            gap_freq[gap] = gap_freq.get(gap, 0) + 1
        
        return {
            'gaps': gaps,
            'frequency': gap_freq,
            'max_gap': max(gaps) if gaps else 0,
            'average_gap': sum(gaps) / len(gaps) if gaps else 0
        }
    
    @staticmethod
    def goldbach_conjecture(n):
        """
        Verifica la Conjetura de Goldbach para número par n
        Todo número par > 2 puede expresarse como suma de dos primos
        
        Args:
            n: Número par a verificar
        
        Returns:
            Lista de tuplas (p1, p2) donde p1 + p2 = n
        """
        if n % 2 != 0 or n < 4:
            return []
        
        primes = PrimeGenerator.sieve_of_eratosthenes(n)
        prime_set = set(primes)
        
        solutions = []
        for p in primes:
            if p > n // 2:
                break
            complement = n - p
            if complement in prime_set:
                solutions.append((p, complement))
        
        return solutions
    
    @staticmethod
    def sophie_germain_primes(limit):
        """
        Encuentra primos de Sophie Germain (p donde 2p + 1 también es primo)
        
        Args:
            limit: Límite superior
        
        Returns:
            Lista de primos de Sophie Germain
        """
        primes = PrimeGenerator.sieve_of_eratosthenes(limit)
        sg_primes = []
        
        for p in primes:
            if PrimalityTester.miller_rabin(2 * p + 1):
                sg_primes.append(p)
        
        return sg_primes
    
    @staticmethod
    def count_primes(n):
        """
        Calcula π(n) - cantidad de primos hasta n
        
        Args:
            n: Límite
        
        Returns:
            Cantidad de primos hasta n
        """
        return len(PrimeGenerator.sieve_of_eratosthenes(n))


# Pruebas rápidas
if __name__ == "__main__":
    print("Primeros 50 primos:")
    primes = PrimeGenerator.sieve_of_eratosthenes(230)
    print(primes)
    
    print("\nPrimos gemelos hasta 100:")
    twins = PrimeGenerator.twin_primes(100)
    print(twins)
    
    print("\nExponentes de Mersenne hasta 100:")
    mersenne = PrimeGenerator.mersenne_primes(100)
    print(mersenne)
    
    print("\nConjetura de Goldbach para 100:")
    goldbach = PrimeGenerator.goldbach_conjecture(100)
    print(f"Formas: {goldbach}")
    
    print("\nPrimos de Sophie Germain hasta 200:")
    sg = PrimeGenerator.sophie_germain_primes(200)
    print(sg)
