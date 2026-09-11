"""
Exploración de conjeturas matemáticas relacionadas con números primos
Implementa: Goldbach, Primos Gemelos, Twin Prime Conjecture
"""

from src.prime_generation import PrimeGenerator
from collections import defaultdict


class ConjectureExplorer:
    """Clase para explorar conjeturas sobre números primos"""
    
    @staticmethod
    def goldbach_conjecture_verify(limit):
        """
        Verifica la Conjetura de Goldbach para todos los números pares hasta limit
        Conjetura: Todo número par > 2 es suma de dos números primos
        
        Args:
            limit: Límite superior
        
        Returns:
            Diccionario con estadísticas de verificación
        """
        primes = PrimeGenerator.sieve_of_eratosthenes(limit)
        prime_set = set(primes)
        
        verified = 0
        not_verified = []
        representations = defaultdict(list)
        
        for n in range(4, limit + 1, 2):
            found = False
            for p in primes:
                if p > n // 2:
                    break
                complement = n - p
                if complement in prime_set:
                    found = True
                    representations[n].append((p, complement))
            
            if found:
                verified += 1
            else:
                not_verified.append(n)
        
        return {
            'total_even_numbers': (limit - 2) // 2,
            'verified': verified,
            'not_verified': not_verified,
            'verification_rate': verified / ((limit - 2) // 2) if limit > 2 else 0,
            'representation_count': dict(representations)
        }
    
    @staticmethod
    def goldbach_partition_analysis(limit):
        """
        Analiza cómo los números pares se pueden expresar como suma de dos primos
        
        Args:
            limit: Límite superior
        
        Returns:
            Análisis de particiones
        """
        primes = PrimeGenerator.sieve_of_eratosthenes(limit)
        prime_set = set(primes)
        
        partition_count = defaultdict(int)
        
        for n in range(4, limit + 1, 2):
            count = 0
            for p in primes:
                if p > n // 2:
                    break
                if n - p in prime_set:
                    count += 1
            partition_count[n] = count
        
        stats = {
            'min_partitions': min(partition_count.values()) if partition_count else 0,
            'max_partitions': max(partition_count.values()) if partition_count else 0,
            'avg_partitions': sum(partition_count.values()) / len(partition_count) if partition_count else 0,
            'distribution': dict(partition_count)
        }
        
        return stats
    
    @staticmethod
    def twin_prime_conjecture_verify(limit):
        """
        Verifica la Conjetura de los Primos Gemelos hasta limit
        Conjetura: Existen infinitos pares (p, p+2) donde ambos son primos
        
        Args:
            limit: Límite superior
        
        Returns:
            Diccionario con pares de primos gemelos encontrados
        """
        twin_primes = PrimeGenerator.twin_primes(limit)
        
        gaps_between_twins = []
        if len(twin_primes) > 1:
            for i in range(len(twin_primes) - 1):
                gap = twin_primes[i+1][0] - twin_primes[i][0]
                gaps_between_twins.append(gap)
        
        return {
            'total_twin_pairs': len(twin_primes),
            'twin_pairs': twin_primes,
            'largest_twin': twin_primes[-1] if twin_primes else None,
            'gaps_between_pairs': gaps_between_twins,
            'avg_gap': sum(gaps_between_twins) / len(gaps_between_twins) if gaps_between_twins else 0,
            'density': len(twin_primes) / (limit // 2) if limit > 0 else 0
        }
    
    @staticmethod
    def cousin_primes(limit):
        """
        Encuentra primos "primos cousins" (p, p+4)
        
        Args:
            limit: Límite superior
        
        Returns:
            Lista de pares de primos cousins
        """
        primes = PrimeGenerator.sieve_of_eratosthenes(limit)
        prime_set = set(primes)
        
        cousin_pairs = []
        for p in primes:
            if p + 4 in prime_set:
                cousin_pairs.append((p, p + 4))
        
        return cousin_pairs
    
    @staticmethod
    def sexy_primes(limit):
        """
        Encuentra primos "sexy primes" (p, p+6)
        
        Args:
            limit: Límite superior
        
        Returns:
            Lista de pares de primos sexy
        """
        primes = PrimeGenerator.sieve_of_eratosthenes(limit)
        prime_set = set(primes)
        
        sexy_pairs = []
        for p in primes:
            if p + 6 in prime_set:
                sexy_pairs.append((p, p + 6))
        
        return sexy_pairs
    
    @staticmethod
    def prime_triplets(limit):
        """
        Encuentra tripletas de primos (p, p+2, p+6) o (p, p+4, p+6)
        
        Args:
            limit: Límite superior
        
        Returns:
            Diccionario con tripletas encontradas
        """
        primes = PrimeGenerator.sieve_of_eratosthenes(limit)
        prime_set = set(primes)
        
        triplets_026 = []
        triplets_046 = []
        
        for p in primes:
            if p + 2 in prime_set and p + 6 in prime_set:
                triplets_026.append((p, p + 2, p + 6))
            if p + 4 in prime_set and p + 6 in prime_set:
                triplets_046.append((p, p + 4, p + 6))
        
        return {
            'triplets_026': triplets_026,
            'triplets_046': triplets_046
        }
    
    @staticmethod
    def legendre_conjecture_verify(limit):
        """
        Verifica la Conjetura de Legendre: existe siempre un primo entre n² y (n+1)²
        
        Args:
            limit: Raíz cuadrada del límite superior
        
        Returns:
            Diccionario con resultados
        """
        primes = PrimeGenerator.sieve_of_eratosthenes((limit + 1) ** 2)
        prime_set = set(primes)
        
        verified = 0
        not_verified = []
        
        for n in range(1, limit + 1):
            found = False
            for p in range(n**2 + 1, (n+1)**2):
                if p in prime_set:
                    found = True
                    break
            
            if found:
                verified += 1
            else:
                not_verified.append(n)
        
        return {
            'total_intervals': limit,
            'verified': verified,
            'not_verified': not_verified,
            'verification_rate': verified / limit if limit > 0 else 0
        }
    
    @staticmethod
    def bertrand_postulate_verify(limit):
        """
        Verifica el Postulado de Bertrand: existe siempre un primo entre n y 2n
        
        Args:
            limit: Límite superior
        
        Returns:
            Diccionario con resultados
        """
        primes = PrimeGenerator.sieve_of_eratosthenes(2 * limit)
        prime_set = set(primes)
        
        verified = 0
        gaps = []
        
        for n in range(2, limit + 1):
            found = False
            gap_size = 0
            for p in range(n + 1, 2 * n + 1):
                if p in prime_set:
                    found = True
                    gap_size = p - n
                    break
            
            if found:
                verified += 1
                gaps.append(gap_size)
        
        return {
            'total_intervals': limit - 1,
            'verified': verified,
            'verification_rate': verified / (limit - 1) if limit > 1 else 0,
            'gaps': gaps,
            'max_gap': max(gaps) if gaps else 0,
            'avg_gap': sum(gaps) / len(gaps) if gaps else 0
        }
    
    @staticmethod
    def mersenne_conjecture_analysis():
        """
        Analiza números primos de Mersenne conocidos
        M_n = 2^p - 1 donde p es primo
        
        Returns:
            Información sobre primos de Mersenne
        """
        known_mersenne_exponents = [2, 3, 5, 7, 13, 17, 19, 31, 61, 89, 107, 127]
        
        mersenne_data = []
        for p in known_mersenne_exponents:
            mersenne_num = 2**p - 1
            mersenne_data.append({
                'exponent': p,
                'mersenne': mersenne_num,
                'digits': len(str(mersenne_num)),
                'binary_length': p
            })
        
        return {
            'known_mersenne_primes': mersenne_data,
            'total_known': len(mersenne_data),
            'largest_known': mersenne_data[-1] if mersenne_data else None
        }
    
    @staticmethod
    def prime_gap_conjecture(limit):
        """
        Analiza espacios entre primos y verifica conjeturas sobre gaps
        Cramér's conjecture: gap(p) = O((ln p)²)
        
        Args:
            limit: Límite superior
        
        Returns:
            Análisis de espacios entre primos
        """
        primes = PrimeGenerator.sieve_of_eratosthenes(limit)
        
        gaps = []
        for i in range(len(primes) - 1):
            gap = primes[i + 1] - primes[i]
            gaps.append({
                'prime': primes[i],
                'gap': gap,
                'log_squared': ((__import__('math').log(primes[i])) ** 2) if primes[i] > 1 else 0
            })
        
        cramers_violations = [g for g in gaps if g['gap'] > 2 * g['log_squared']]
        
        return {
            'total_gaps': len(gaps),
            'max_gap': max([g['gap'] for g in gaps]) if gaps else 0,
            'avg_gap': sum([g['gap'] for g in gaps]) / len(gaps) if gaps else 0,
            'cramers_violations': len(cramers_violations),
            'violation_rate': len(cramers_violations) / len(gaps) if gaps else 0,
            'largest_gaps': sorted(gaps, key=lambda x: x['gap'], reverse=True)[:10]
        }


# Pruebas rápidas
if __name__ == "__main__":
    print("Exploración de Conjeturas Matemáticas\n")
    
    print("1. Conjetura de Goldbach (hasta 1000):")
    goldbach = ConjectureExplorer.goldbach_conjecture_verify(1000)
    print(f"   Verificados: {goldbach['verified']}/{goldbach['total_even_numbers']}")
    print(f"   Tasa de verificación: {goldbach['verification_rate']:.4f}")
    
    print("\n2. Conjetura de Primos Gemelos (hasta 1000):")
    twins = ConjectureExplorer.twin_prime_conjecture_verify(1000)
    print(f"   Pares encontrados: {twins['total_twin_pairs']}")
    print(f"   Mayor par: {twins['largest_twin']}")
    
    print("\n3. Primos Cousins (p, p+4) hasta 1000:")
    cousins = ConjectureExplorer.cousin_primes(1000)
    print(f"   Pares encontrados: {len(cousins)}")
    print(f"   Primeros pares: {cousins[:5]}")
    
    print("\n4. Postulado de Bertrand (hasta 100):")
    bertrand = ConjectureExplorer.bertrand_postulate_verify(100)
    print(f"   Verificados: {bertrand['verified']}/{bertrand['total_intervals']}")
    print(f"   Tasa de verificación: {bertrand['verification_rate']:.4f}")
