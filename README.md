# Millennium Prime Numbers 🔢

Exploración computacional avanzada de números primos y la Conjetura de Riemann.

## Descripción

Este proyecto implementa algoritmos sofisticados para:

- **Pruebas de Primalidad**: Miller-Rabin, Lucas-Lehmer, AKS
- **Búsqueda de Números Primos**: Criba de Eratóstenes optimizada, números primos de Mersenne
- **Análisis de Distribución**: Función de conteo de primos π(x), Teorema del Número Primo
- **Función Zeta de Riemann**: Cálculo de ceros, visualización
- **Patrones y Conjeturas**: Conjetura de Goldbach, espacios entre primos

## Estructura del Proyecto

```
├── src/
│   ├── primality_tests.py          # Algoritmos de prueba de primalidad
│   ├── prime_generation.py         # Generación de números primos
│   ├── distribution_analysis.py    # Análisis de distribución
│   ├── riemann_zeta.py            # Función Zeta de Riemann
│   ├── conjectures.py             # Exploración de conjeturas
│   └── visualization.py           # Visualizaciones
├── tests/
│   └── test_primes.py             # Suite de pruebas
├── notebooks/
│   ├── riemann_exploration.ipynb   # Exploración interactiva
│   └── prime_patterns.ipynb        # Análisis de patrones
├── requirements.txt
└── README.md
```

## Instalación

```bash
git clone https://github.com/octacorrr/millennium-prime-numbers.git
cd millennium-prime-numbers
pip install -r requirements.txt
```

## Uso Básico

```python
from src.primality_tests import miller_rabin, aks_test
from src.prime_generation import sieve_of_eratosthenes

# Prueba de primalidad
print(miller_rabin(1000000007))  # True

# Generar primos hasta N
primes = sieve_of_eratosthenes(1000)
print(f"Hay {len(primes)} primos hasta 1000")
```

## Problemas Explorados

### 1. La Conjetura de Riemann
Investigamos la distribución de los ceros no triviales de la función zeta de Riemann en la línea crítica Re(s) = 1/2.

### 2. Conjetura de Goldbach
Todo número par mayor que 2 puede expresarse como suma de dos números primos.

### 3. Conjetura de los Números Primos Gemelos
Existen infinitos pares de números primos que difieren en 2.

## Metodología

- **Computación de alto rendimiento**: Optimizaciones numéricas y algoritmos eficientes
- **Análisis estadístico**: Distribuciones y patrones
- **Visualización**: Gráficos interactivos para identificar patrones
- **Verificación rigurosa**: Suite completa de pruebas

## Referencias

- Riemann, B. (1859). "On the Number of Primes Less Than a Given Quantity"
- Miller, G. L., & Rabin, M. O. (1976). "Probabilistic algorithm for testing primality"
- Agrawal, M., Kayal, N., & Saxena, N. (2004). "PRIMES is in P"

## Licencia

MIT License - Ver LICENSE file

## Contribuciones

Las contribuciones son bienvenidas. Por favor abre un issue o pull request.
