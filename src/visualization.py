"""
Módulo de visualización para números primos
Genera gráficos interactivos usando matplotlib y plotly
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from collections import defaultdict
import math

from src.prime_generation import PrimeGenerator
from src.distribution_analysis import DistributionAnalyzer
from src.conjectures import ConjectureExplorer


class PrimeVisualizer:
    """Clase para visualizar datos de números primos"""
    
    @staticmethod
    def plot_prime_distribution(limit=1000, save_path='charts/distribution.png'):
        """
        Crea gráfico de distribución de primos
        
        Args:
            limit: Límite superior
            save_path: Ruta para guardar la imagen
        """
        fig, axes = plt.subplots(2, 2, figsize=(14, 10))
        
        # 1. Cantidad de primos hasta n
        points = [i*100 for i in range(1, limit//100 + 1)]
        counts = [DistributionAnalyzer.prime_counting_function(p) for p in points]
        
        axes[0, 0].plot(points, counts, 'b-', linewidth=2, label='π(n)')
        axes[0, 0].set_xlabel('n')
        axes[0, 0].set_ylabel('π(n) - Cantidad de primos')
        axes[0, 0].set_title('Función de Conteo de Primos')
        axes[0, 0].grid(True, alpha=0.3)
        axes[0, 0].legend()
        
        # 2. Comparación con Teorema del Número Primo
        pnt_approx = [DistributionAnalyzer.prime_number_theorem_approximation(p) for p in points]
        
        axes[0, 1].plot(points, counts, 'b-', linewidth=2, label='π(n) Real')
        axes[0, 1].plot(points, pnt_approx, 'r--', linewidth=2, label='n/ln(n)')
        axes[0, 1].set_xlabel('n')
        axes[0, 1].set_ylabel('Cantidad de primos')
        axes[0, 1].set_title('π(n) vs Teorema del Número Primo')
        axes[0, 1].legend()
        axes[0, 1].grid(True, alpha=0.3)
        
        # 3. Densidad de primos
        densities = [c/p if p > 0 else 0 for c, p in zip(counts, points)]
        
        axes[1, 0].plot(points, densities, 'g-', linewidth=2)
        axes[1, 0].set_xlabel('n')
        axes[1, 0].set_ylabel('Densidad (π(n)/n)')
        axes[1, 0].set_title('Densidad de Números Primos')
        axes[1, 0].grid(True, alpha=0.3)
        
        # 4. Errores de aproximación
        errors_pnt = [abs(c - p) for c, p in zip(counts, pnt_approx)]
        
        axes[1, 1].plot(points, errors_pnt, 'r-', linewidth=2)
        axes[1, 1].set_xlabel('n')
        axes[1, 1].set_ylabel('Error |π(n) - n/ln(n)|')
        axes[1, 1].set_title('Error de Aproximación del Número Primo')
        axes[1, 1].grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.savefig(save_path, dpi=150, bbox_inches='tight')
        print(f"Gráfico guardado en {save_path}")
        plt.close()
    
    @staticmethod
    def plot_prime_gaps(limit=10000, save_path='charts/gaps.png'):
        """
        Visualiza espacios entre números primos consecutivos
        
        Args:
            limit: Límite superior
            save_path: Ruta para guardar la imagen
        """
        primes = PrimeGenerator.sieve_of_eratosthenes(limit)
        gaps = [primes[i+1] - primes[i] for i in range(len(primes)-1)]
        
        fig, axes = plt.subplots(2, 2, figsize=(14, 10))
        
        # 1. Espacios vs índice
        axes[0, 0].scatter(range(len(gaps)), gaps, alpha=0.5, s=10)
        axes[0, 0].set_xlabel('Índice del primo')
        axes[0, 0].set_ylabel('Espacio al siguiente primo')
        axes[0, 0].set_title('Espacios entre Primos Consecutivos')
        axes[0, 0].grid(True, alpha=0.3)
        
        # 2. Histograma de espacios
        gap_freq = defaultdict(int)
        for gap in gaps:
            gap_freq[gap] += 1
        
        gap_sizes = sorted(gap_freq.keys())
        gap_counts = [gap_freq[g] for g in gap_sizes]
        
        axes[0, 1].bar(gap_sizes[:20], gap_counts[:20], color='steelblue')
        axes[0, 1].set_xlabel('Tamaño del espacio')
        axes[0, 1].set_ylabel('Frecuencia')
        axes[0, 1].set_title('Distribución de Espacios entre Primos')
        axes[0, 1].grid(True, alpha=0.3, axis='y')
        
        # 3. Espacios vs log(primo)
        log_primes = [math.log(p) if p > 0 else 0 for p in primes[:-1]]
        axes[1, 0].scatter(log_primes, gaps, alpha=0.5, s=10, color='green')
        axes[1, 0].set_xlabel('ln(p)')
        axes[1, 0].set_ylabel('Espacio al siguiente primo')
        axes[1, 0].set_title('Espacios vs Logaritmo del Primo')
        axes[1, 0].grid(True, alpha=0.3)
        
        # 4. Máximos espacios
        top_gaps = sorted(enumerate(gaps), key=lambda x: x[1], reverse=True)[:10]
        gap_indices = [g[0] for g in top_gaps]
        gap_values = [g[1] for g in top_gaps]
        
        axes[1, 1].barh(range(len(gap_values)), gap_values, color='coral')
        axes[1, 1].set_ylabel('Posición')
        axes[1, 1].set_xlabel('Tamaño del espacio')
        axes[1, 1].set_title('Top 10 Mayores Espacios entre Primos')
        axes[1, 1].grid(True, alpha=0.3, axis='x')
        
        plt.tight_layout()
        plt.savefig(save_path, dpi=150, bbox_inches='tight')
        print(f"Gráfico guardado en {save_path}")
        plt.close()
    
    @staticmethod
    def plot_goldbach_conjecture(limit=1000, save_path='charts/goldbach.png'):
        """
        Visualiza la Conjetura de Goldbach
        
        Args:
            limit: Límite superior
            save_path: Ruta para guardar la imagen
        """
        analysis = ConjectureExplorer.goldbach_partition_analysis(limit)
        distribution = analysis['distribution']
        
        fig, axes = plt.subplots(1, 2, figsize=(14, 5))
        
        # 1. Número de representaciones por número par
        numbers = sorted(distribution.keys())
        representations = [distribution[n] for n in numbers]
        
        axes[0].scatter(numbers, representations, alpha=0.6, s=20)
        axes[0].set_xlabel('Número par n')
        axes[0].set_ylabel('Número de representaciones como p + q')
        axes[0].set_title('Conjetura de Goldbach - Representaciones')
        axes[0].grid(True, alpha=0.3)
        
        # 2. Histograma de representaciones
        rep_freq = defaultdict(int)
        for rep_count in representations:
            rep_freq[rep_count] += 1
        
        rep_sizes = sorted(rep_freq.keys())
        rep_counts = [rep_freq[r] for r in rep_sizes]
        
        axes[1].bar(rep_sizes, rep_counts, color='steelblue', alpha=0.7)
        axes[1].set_xlabel('Número de representaciones')
        axes[1].set_ylabel('Frecuencia')
        axes[1].set_title('Distribución de Representaciones de Goldbach')
        axes[1].grid(True, alpha=0.3, axis='y')
        
        plt.tight_layout()
        plt.savefig(save_path, dpi=150, bbox_inches='tight')
        print(f"Gráfico guardado en {save_path}")
        plt.close()
    
    @staticmethod
    def plot_twin_primes(limit=10000, save_path='charts/twin_primes.png'):
        """
        Visualiza la distribución de primos gemelos
        
        Args:
            limit: Límite superior
            save_path: Ruta para guardar la imagen
        """
        twins = PrimeGenerator.twin_primes(limit)
        
        fig, axes = plt.subplots(2, 1, figsize=(14, 10))
        
        # 1. Posición de primos gemelos
        twin_positions = [t[0] for t in twins]
        
        axes[0].scatter(twin_positions, [1]*len(twin_positions), alpha=0.6, s=30, color='red')
        axes[0].set_xlabel('Valor del primo p (en par p, p+2)')
        axes[0].set_ylabel('Presencia')
        axes[0].set_title('Distribución de Primos Gemelos')
        axes[0].set_ylim([0.5, 1.5])
        axes[0].grid(True, alpha=0.3, axis='x')
        
        # 2. Densidad de primos gemelos en ventanas
        window_size = limit // 20
        windows = []
        densities = []
        
        for i in range(0, limit, window_size):
            window_end = min(i + window_size, limit)
            count = sum(1 for p, _ in twins if i <= p < window_end)
            density = count / (window_size / 1000) if window_size > 0 else 0
            windows.append(i)
            densities.append(density)
        
        axes[1].bar(windows, densities, width=window_size*0.8, color='steelblue', alpha=0.7)
        axes[1].set_xlabel('Rango')
        axes[1].set_ylabel('Densidad de pares gemelos')
        axes[1].set_title('Densidad de Primos Gemelos por Rango')
        axes[1].grid(True, alpha=0.3, axis='y')
        
        plt.tight_layout()
        plt.savefig(save_path, dpi=150, bbox_inches='tight')
        print(f"Gráfico guardado en {save_path}")
        plt.close()
    
    @staticmethod
    def plot_digit_distribution(limit=10000, save_path='charts/digits.png'):
        """
        Visualiza la distribución de dígitos en números primos
        
        Args:
            limit: Límite superior
            save_path: Ruta para guardar la imagen
        """
        fig, axes = plt.subplots(2, 2, figsize=(14, 10))
        
        # Últimos dígitos
        last_digits = DistributionAnalyzer.last_digit_distribution(limit)
        axes[0, 0].bar(last_digits.keys(), last_digits.values(), color='steelblue', alpha=0.7)
        axes[0, 0].set_xlabel('Último dígito')
        axes[0, 0].set_ylabel('Frecuencia')
        axes[0, 0].set_title('Distribución de Últimos Dígitos de Primos')
        axes[0, 0].grid(True, alpha=0.3, axis='y')
        
        # Primeros dígitos
        first_digits = DistributionAnalyzer.first_digit_distribution(limit)
        axes[0, 1].bar(first_digits.keys(), first_digits.values(), color='coral', alpha=0.7)
        axes[0, 1].set_xlabel('Primer dígito')
        axes[0, 1].set_ylabel('Frecuencia')
        axes[0, 1].set_title('Distribución de Primeros Dígitos (Ley de Benford)')
        axes[0, 1].grid(True, alpha=0.3, axis='y')
        
        # Comparación con Benford
        benford = DistributionAnalyzer.benford_law_check(limit)
        digits = sorted(benford.keys())
        observed = [benford[d]['observed'] for d in digits]
        expected = [benford[d]['expected'] for d in digits]
        
        x = range(len(digits))
        width = 0.35
        axes[1, 0].bar([i - width/2 for i in x], observed, width, label='Observado', alpha=0.7)
        axes[1, 0].bar([i + width/2 for i in x], expected, width, label='Ley de Benford', alpha=0.7)
        axes[1, 0].set_xlabel('Dígito')
        axes[1, 0].set_ylabel('Probabilidad')
        axes[1, 0].set_title('Observado vs Ley de Benford')
        axes[1, 0].set_xticks(x)
        axes[1, 0].set_xticklabels(digits)
        axes[1, 0].legend()
        axes[1, 0].grid(True, alpha=0.3, axis='y')
        
        # Todos los dígitos
        all_digits = DistributionAnalyzer.digit_analysis(limit)
        axes[1, 1].bar(all_digits.keys(), all_digits.values(), color='green', alpha=0.7)
        axes[1, 1].set_xlabel('Dígito (0-9)')
        axes[1, 1].set_ylabel('Frecuencia Total')
        axes[1, 1].set_title('Distribución de Todos los Dígitos en Primos')
        axes[1, 1].grid(True, alpha=0.3, axis='y')
        
        plt.tight_layout()
        plt.savefig(save_path, dpi=150, bbox_inches='tight')
        print(f"Gráfico guardado en {save_path}")
        plt.close()
    
    @staticmethod
    def generate_all_charts(limit=10000):
        """
        Genera todos los gráficos
        
        Args:
            limit: Límite superior para los cálculos
        """
        import os
        
        # Crear directorio si no existe
        os.makedirs('charts', exist_ok=True)
        
        print("Generando gráficos...")
        print("1. Distribución de primos...")
        PrimeVisualizer.plot_prime_distribution(limit, 'charts/distribution.png')
        
        print("2. Espacios entre primos...")
        PrimeVisualizer.plot_prime_gaps(limit, 'charts/gaps.png')
        
        print("3. Conjetura de Goldbach...")
        PrimeVisualizer.plot_goldbach_conjecture(limit, 'charts/goldbach.png')
        
        print("4. Primos gemelos...")
        PrimeVisualizer.plot_twin_primes(limit, 'charts/twin_primes.png')
        
        print("5. Distribución de dígitos...")
        PrimeVisualizer.plot_digit_distribution(limit, 'charts/digits.png')
        
        print("✓ Todos los gráficos han sido generados en la carpeta 'charts/'")


if __name__ == "__main__":
    PrimeVisualizer.generate_all_charts(10000)
