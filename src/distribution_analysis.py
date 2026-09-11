"""
Análisis de distribución de números primos
Implementa: Función π(x), Teorema del Número Primo, Análisis estadístico
"""

import math
from collections import defaultdict
from src.prime_generation import PrimeGenerator


class DistributionAnalyzer:
    """Clase para analizar la distribución de números primos"""
    
    @staticmethod
    def prime_counting_function(n):
        """
        Calcula π(n) - cantidad de primos ≤ n
        
        Args:
            n: Límite superior
        
        Returns:
            Cantidad de primos hasta n
        """
        return len(PrimeGenerator.sieve_of_eratosthenes(n))
    
    @staticmethod
    def prime_number_theorem_approximation(n):
        """
        Aproximación del Teorema del Número Primo: π(n) ≈ n / ln(n)
        
        Args:
            n: Límite superior
        
        Returns:
            Aproximación de π(n)
        """
        if n < 2:
            return 0
        return n / math.log(n)
    
    @staticmethod
    def better_approximation(n):
        """
        Mejor aproximación: π(n) ≈ n / (ln(n) - 1)
        
        Args:
            n: Límite superior
        
        Returns:
            Aproximación mejorada de π(n)
        """
        if n < 2:
            return 0
        return n / (math.log(n) - 1)
    
    @staticmethod
    def logarithmic_integral(n):
        """
        Integral logarítmica Li(n) ≈ ∫[2,n] 1/ln(x) dx
        Aproximación muy precisa de π(n)
        
        Args:
            n: Límite superior
        
        Returns:
            Valor de la integral logarítmica
        """
        if n < 2:
            return 0
        
        # Usando aproximación de Ramanujan
        return n / math.log(n) * (1 + 1/math.log(n) + 2/(math.log(n)**2))
    
    @staticmethod
    def analyze_distribution(limit):
        """
        Análisis completo de la distribución de primos hasta limit
        
        Args:
            limit: Límite superior
        
        Returns:
            Diccionario con estadísticas de distribución
        """
        primes = PrimeGenerator.sieve_of_eratosthenes(limit)
        
        if not primes:
            return {}
        
        # Estadísticas básicas
        count = len(primes)
        average = sum(primes) / len(primes)
        
        # Densidad de primos
        density = count / limit
        
        # Desviación estándar
        variance = sum((p - average) ** 2 for p in primes) / len(primes)
        std_dev = math.sqrt(variance)
        
        # Comparación con teorema del número primo
        pnt_approx = DistributionAnalyzer.prime_number_theorem_approximation(limit)
        better_approx = DistributionAnalyzer.better_approximation(limit)
        li_approx = DistributionAnalyzer.logarithmic_integral(limit)
        
        return {
            'count': count,
            'density': density,
            'average': average,
            'std_dev': std_dev,
            'min': min(primes),
            'max': max(primes),
            'pnt_approximation': pnt_approx,
            'better_approximation': better_approx,
            'logarithmic_integral': li_approx,
            'error_pnt': abs(count - pnt_approx),
            'error_better': abs(count - better_approx),
            'error_li': abs(count - li_approx)
        }
    
    @staticmethod
    def digit_analysis(limit):
        """
        Analiza la distribución de dígitos en números primos
        
        Args:
            limit: Límite superior
        
        Returns:
            Diccionario con frecuencia de dígitos
        """
        primes = PrimeGenerator.sieve_of_eratosthenes(limit)
        digit_freq = defaultdict(int)
        
        for prime in primes:
            for digit in str(prime):
                digit_freq[int(digit)] += 1
        
        return dict(digit_freq)
    
    @staticmethod
    def last_digit_distribution(limit):
        """
        Analiza el último dígito de números primos
        Para primos > 5, solo pueden terminar en 1, 3, 7, 9
        
        Args:
            limit: Límite superior
        
        Returns:
            Diccionario con distribución de últimos dígitos
        """
        primes = PrimeGenerator.sieve_of_eratosthenes(limit)
        last_digit_freq = defaultdict(int)
        
        for prime in primes:
            last_digit = prime % 10
            last_digit_freq[last_digit] += 1
        
        return dict(sorted(last_digit_freq.items()))
    
    @staticmethod
    def first_digit_distribution(limit):
        """
        Analiza el primer dígito de números primos (Ley de Benford)
        
        Args:
            limit: Límite superior
        
        Returns:
            Diccionario con distribución de primeros dígitos
        """
        primes = PrimeGenerator.sieve_of_eratosthenes(limit)
        first_digit_freq = defaultdict(int)
        
        for prime in primes:
            first_digit = int(str(prime)[0])
            first_digit_freq[first_digit] += 1
        
        return dict(sorted(first_digit_freq.items()))
    
    @staticmethod
    def prime_gaps_analysis(limit):
        """
        Análisis estadístico de espacios entre primos consecutivos
        
        Args:
            limit: Límite superior
        
        Returns:
            Diccionario con estadísticas de espacios
        """
        primes = PrimeGenerator.sieve_of_eratosthenes(limit)
        
        if len(primes) < 2:
            return {}
        
        gaps = [primes[i+1] - primes[i] for i in range(len(primes) - 1)]
        
        # Estadísticas de espacios
        avg_gap = sum(gaps) / len(gaps)
        variance = sum((g - avg_gap) ** 2 for g in gaps) / len(gaps)
        
        return {
            'count': len(gaps),
            'average': avg_gap,
            'std_dev': math.sqrt(variance),
            'min': min(gaps),
            'max': max(gaps),
            'expected_average': math.log(limit)  # Log(n) es el espaciamiento esperado
        }
    
    @staticmethod
    def relative_prime_density(n, window_size=1000):
        """
        Analiza la densidad de primos en ventanas de tamaño window_size
        
        Args:
            n: Límite superior
            window_size: Tamaño de cada ventana
        
        Returns:
            Lista de tuplas (ventana_inicio, densidad_en_ventana)
        """
        primes = set(PrimeGenerator.sieve_of_eratosthenes(n))
        
        densities = []
        for start in range(0, n, window_size):
            end = min(start + window_size, n)
            window_primes = sum(1 for p in primes if start <= p < end)
            density = window_primes / window_size if window_size > 0 else 0
            densities.append((start, density))
        
        return densities
    
    @staticmethod
    def compare_prime_density_at_scales(limit, scales=None):
        """
        Compara la densidad de primos a diferentes escalas
        
        Args:
            limit: Límite superior
            scales: Lista de escalas a analizar
        
        Returns:
            Diccionario con densidades a diferentes escalas
        """
        if scales is None:
            scales = [100, 1000, 10000, 100000, min(1000000, limit)]
        
        results = {}
        for scale in scales:
            if scale <= limit:
                count = DistributionAnalyzer.prime_counting_function(scale)
                density = count / scale
                pnt = DistributionAnalyzer.prime_number_theorem_approximation(scale)
                results[scale] = {
                    'count': count,
                    'density': density,
                    'pnt_approximation': pnt
                }
        
        return results
    
    @staticmethod
    def benford_law_check(limit):
        """
        Verifica si los números primos siguen la Ley de Benford
        Ley de Benford predice: P(d) = log₁₀(1 + 1/d)
        
        Args:
            limit: Límite superior
        
        Returns:
            Comparación entre observado y esperado
        """
        first_digits = DistributionAnalyzer.first_digit_distribution(limit)
        total = sum(first_digits.values())
        
        benford_expected = {}
        for d in range(1, 10):
            benford_expected[d] = math.log10(1 + 1/d)
        
        comparison = {}
        for d in range(1, 10):
            observed_freq = first_digits.get(d, 0) / total if total > 0 else 0
            expected_freq = benford_expected[d]
            comparison[d] = {
                'observed': observed_freq,
                'expected': expected_freq,
                'difference': abs(observed_freq - expected_freq)
            }
        
        return comparison


# Pruebas rápidas
if __name__ == "__main__":
    print("Análisis de distribución hasta 10,000:")
    analysis = DistributionAnalyzer.analyze_distribution(10000)
    for key, value in analysis.items():
        print(f"  {key}: {value:.4f}" if isinstance(value, float) else f"  {key}: {value}")
    
    print("\nÚltimos dígitos de primos hasta 1000:")
    last_digits = DistributionAnalyzer.last_digit_distribution(1000)
    print(last_digits)
    
    print("\nPrimeros dígitos de primos (Ley de Benford):")
    first_digits = DistributionAnalyzer.first_digit_distribution(10000)
    print(first_digits)
    
    print("\nEspacios entre primos:")
    gaps = DistributionAnalyzer.prime_gaps_analysis(1000)
    for key, value in gaps.items():
        print(f"  {key}: {value:.4f}" if isinstance(value, float) else f"  {key}: {value}")
