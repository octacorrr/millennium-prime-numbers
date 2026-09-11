"""
Script principal para ejecutar análisis de números primos
Millennium Prime Numbers - Exploración computacional de la Conjetura de Riemann
"""

import sys
from src.primality_tests import PrimalityTester
from src.prime_generation import PrimeGenerator
from src.distribution_analysis import DistributionAnalyzer
from src.conjectures import ConjectureExplorer
from src.riemann_zeta import RiemannZeta
from src.visualization import PrimeVisualizer


def print_header():
    """Imprime encabezado del programa"""
    print("\n" + "="*70)
    print("  MILLENNIUM PRIME NUMBERS - Exploración de la Conjetura de Riemann")
    print("="*70 + "\n")


def main_menu():
    """Menú principal del programa"""
    while True:
        print_header()
        print("MENÚ PRINCIPAL")
        print("-" * 70)
        print("1. Pruebas de Primalidad")
        print("2. Generación de Números Primos")
        print("3. Análisis de Distribución")
        print("4. Conjeturas Matemáticas")
        print("5. Función Zeta de Riemann")
        print("6. Generar Visualizaciones")
        print("7. Análisis Completo")
        print("0. Salir")
        print("-" * 70)
        
        choice = input("Selecciona una opción (0-7): ").strip()
        
        if choice == "1":
            primality_tests_menu()
        elif choice == "2":
            prime_generation_menu()
        elif choice == "3":
            distribution_menu()
        elif choice == "4":
            conjectures_menu()
        elif choice == "5":
            riemann_menu()
        elif choice == "6":
            visualizations_menu()
        elif choice == "7":
            full_analysis()
        elif choice == "0":
            print("\n¡Hasta luego!\n")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")
            input("Presiona Enter para continuar...")


def primality_tests_menu():
    """Menú de pruebas de primalidad"""
    print_header()
    print("PRUEBAS DE PRIMALIDAD")
    print("-" * 70)
    
    try:
        num = int(input("Ingresa un número para probar: "))
        
        print(f"\nProbando número: {num}")
        print("-" * 70)
        
        # Miller-Rabin
        mr_result = PrimalityTester.miller_rabin(num)
        print(f"Miller-Rabin: {'PRIMO' if mr_result else 'COMPUESTO'}")
        
        # Fermat
        fermat_result = PrimalityTester.fermat_test(num)
        print(f"Fermat: {'PRIMO' if fermat_result else 'COMPUESTO'}")
        
        # Solovay-Strassen
        ss_result = PrimalityTester.solovay_strassen(num)
        print(f"Solovay-Strassen: {'PRIMO' if ss_result else 'COMPUESTO'}")
        
        print("-" * 70)
    except ValueError:
        print("Error: Debes ingresar un número válido.")
    
    input("\nPresiona Enter para continuar...")


def prime_generation_menu():
    """Menú de generación de primos"""
    print_header()
    print("GENERACIÓN DE NÚMEROS PRIMOS")
    print("-" * 70)
    
    try:
        limit = int(input("Ingresa el límite superior: "))
        
        print(f"\nGenerando primos hasta {limit}...")
        primes = PrimeGenerator.sieve_of_eratosthenes(limit)
        
        print(f"Total de primos encontrados: {len(primes)}")
        print(f"Primeros 20 primos: {primes[:20]}")
        print(f"Últimos 10 primos: {primes[-10:]}")
        
        print("\n--- Tipos especiales de primos ---")
        
        # Primos de Sophie Germain
        sg_primes = PrimeGenerator.sophie_germain_primes(limit)
        print(f"Primos de Sophie Germain: {len(sg_primes)} encontrados")
        if sg_primes:
            print(f"  Primeros: {sg_primes[:10]}")
        
        # Primos de Mersenne
        mersenne = PrimeGenerator.mersenne_primes(50)
        print(f"Exponentes de Mersenne (hasta 50): {mersenne}")
        
        print("-" * 70)
    except ValueError:
        print("Error: Debes ingresar un número válido.")
    
    input("\nPresiona Enter para continuar...")


def distribution_menu():
    """Menú de análisis de distribución"""
    print_header()
    print("ANÁLISIS DE DISTRIBUCIÓN DE PRIMOS")
    print("-" * 70)
    
    try:
        limit = int(input("Ingresa el límite superior: "))
        
        print(f"\nAnalizando distribución hasta {limit}...")
        analysis = DistributionAnalyzer.analyze_distribution(limit)
        
        print(f"\nEstadísticas:")
        print(f"  Cantidad de primos: {analysis['count']}")
        print(f"  Densidad: {analysis['density']:.6f}")
        print(f"  Promedio: {analysis['average']:.2f}")
        print(f"  Desv. Estándar: {analysis['std_dev']:.2f}")
        
        print(f"\nAproximaciones del Teorema del Número Primo:")
        print(f"  π({limit}) real: {analysis['count']}")
        print(f"  n/ln(n): {analysis['pnt_approximation']:.2f} (error: {analysis['error_pnt']:.2f})")
        print(f"  n/(ln(n)-1): {analysis['better_approximation']:.2f} (error: {analysis['error_better']:.2f})")
        print(f"  Li(n): {analysis['logarithmic_integral']:.2f} (error: {analysis['error_li']:.2f})")
        
        # Análisis de espacios
        gaps = DistributionAnalyzer.prime_gaps_analysis(limit)
        print(f"\nEspacios entre primos consecutivos:")
        print(f"  Promedio: {gaps['average']:.2f}")
        print(f"  Mínimo: {gaps['min']}")
        print(f"  Máximo: {gaps['max']}")
        print(f"  Esperado (ln n): {gaps['expected_average']:.2f}")
        
        print("-" * 70)
    except ValueError:
        print("Error: Debes ingresar un número válido.")
    
    input("\nPresiona Enter para continuar...")


def conjectures_menu():
    """Menú de conjeturas"""
    print_header()
    print("EXPLORACIÓN DE CONJETURAS MATEMÁTICAS")
    print("-" * 70)
    
    try:
        limit = int(input("Ingresa el límite superior: "))
        
        print(f"\nVerificando conjeturas hasta {limit}...")
        
        # Goldbach
        print("\n1. CONJETURA DE GOLDBACH")
        print("-" * 70)
        goldbach = ConjectureExplorer.goldbach_conjecture_verify(limit)
        print(f"Números pares verificados: {goldbach['verified']}/{goldbach['total_even_numbers']}")
        print(f"Tasa de verificación: {goldbach['verification_rate']:.4f}")
        if goldbach['not_verified']:
            print(f"No verificados: {goldbach['not_verified']}")
        
        # Primos Gemelos
        print("\n2. CONJETURA DE PRIMOS GEMELOS")
        print("-" * 70)
        twins = ConjectureExplorer.twin_prime_conjecture_verify(limit)
        print(f"Pares de primos gemelos: {twins['total_twin_pairs']}")
        print(f"Mayor par: {twins['largest_twin']}")
        print(f"Densidad: {twins['density']:.6f}")
        
        # Postulado de Bertrand
        print("\n3. POSTULADO DE BERTRAND")
        print("-" * 70)
        bertrand = ConjectureExplorer.bertrand_postulate_verify(limit // 2)
        print(f"Intervalos verificados: {bertrand['verified']}/{bertrand['total_intervals']}")
        print(f"Tasa de verificación: {bertrand['verification_rate']:.4f}")
        print(f"Mayor gap: {bertrand['max_gap']}")
        
        print("-" * 70)
    except ValueError:
        print("Error: Debes ingresar un número válido.")
    
    input("\nPresiona Enter para continuar...")


def riemann_menu():
    """Menú de función Zeta de Riemann"""
    print_header()
    print("FUNCIÓN ZETA DE RIEMANN - CONJETURA DE RIEMANN")
    print("-" * 70)
    
    print("1. Calcular ζ(s) en un punto específico")
    print("2. Buscar ceros en la línea crítica")
    print("3. Verificar la Conjetura de Riemann")
    print("0. Volver al menú principal")
    
    choice = input("\nSelecciona una opción: ").strip()
    
    if choice == "1":
        try:
            real = float(input("Parte real de s: "))
            imag = float(input("Parte imaginaria de s: "))
            s = complex(real, imag)
            
            result = RiemannZeta.zeta_euler_maclaurin(s)
            print(f"\nζ({real} + {imag}i) = {result}")
        except ValueError:
            print("Error: Debes ingresar números válidos.")
    
    elif choice == "2":
        print("\nBuscando ceros en la línea crítica Re(s) = 1/2...")
        zeros = RiemannZeta.find_zeros_on_critical_line(0.1, 30, 0.2)
        print(f"Ceros encontrados (primeros 10): {zeros[:10]}")
        print(f"Total de ceros encontrados: {len(zeros)}")
    
    elif choice == "3":
        print("\nVerificando la Conjetura de Riemann...")
        verification = RiemannZeta.verify_riemann_hypothesis(30, 0.2)
        print(f"Ceros encontrados: {verification['zeros_found']}")
        print(f"Verificados: {verification['zeros_verified']}")
        print(f"Tasa de verificación: {verification['verification_rate']:.2%}")
    
    input("\nPresiona Enter para continuar...")


def visualizations_menu():
    """Menú de visualizaciones"""
    print_header()
    print("GENERAR VISUALIZACIONES")
    print("-" * 70)
    
    try:
        limit = int(input("Ingresa el límite superior para los gráficos: "))
        
        print(f"\nGenerando gráficos hasta {limit}...")
        PrimeVisualizer.generate_all_charts(limit)
        
        print("\n✓ Los gráficos han sido guardados en la carpeta 'charts/'")
        print("  - distribution.png: Distribución de primos y teorema del número primo")
        print("  - gaps.png: Espacios entre números primos consecutivos")
        print("  - goldbach.png: Análisis de la Conjetura de Goldbach")
        print("  - twin_primes.png: Distribución de primos gemelos")
        print("  - digits.png: Análisis de dígitos (Ley de Benford)")
        
        print("-" * 70)
    except ValueError:
        print("Error: Debes ingresar un número válido.")
    
    input("\nPresiona Enter para continuar...")


def full_analysis():
    """Realiza análisis completo"""
    print_header()
    print("ANÁLISIS COMPLETO DEL PROYECTO")
    print("=" * 70)
    
    limit = 10000
    print(f"Analizando números hasta {limit}...")
    
    # Generación
    print("\n1. GENERANDO NÚMEROS PRIMOS...")
    primes = PrimeGenerator.sieve_of_eratosthenes(limit)
    print(f"   ✓ {len(primes)} primos encontrados")
    
    # Distribución
    print("\n2. ANALIZANDO DISTRIBUCIÓN...")
    analysis = DistributionAnalyzer.analyze_distribution(limit)
    print(f"   ✓ Densidad: {analysis['density']:.6f}")
    print(f"   ✓ Error en n/ln(n): {analysis['error_pnt']:.2f}")
    
    # Goldbach
    print("\n3. VERIFICANDO CONJETURA DE GOLDBACH...")
    goldbach = ConjectureExplorer.goldbach_conjecture_verify(limit)
    print(f"   ✓ Tasa de verificación: {goldbach['verification_rate']:.2%}")
    
    # Primos Gemelos
    print("\n4. ANALIZANDO PRIMOS GEMELOS...")
    twins = ConjectureExplorer.twin_prime_conjecture_verify(limit)
    print(f"   ✓ {twins['total_twin_pairs']} pares encontrados")
    
    # Visualizaciones
    print("\n5. GENERANDO VISUALIZACIONES...")
    PrimeVisualizer.generate_all_charts(limit)
    print("   ✓ Gráficos generados")
    
    print("\n" + "=" * 70)
    print("¡Análisis completo finalizado!")
    print("=" * 70 + "\n")
    
    input("Presiona Enter para volver al menú principal...")


if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print("\n\n¡Hasta luego!\n")
        sys.exit(0)
