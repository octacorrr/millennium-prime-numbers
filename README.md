# 🔢 Millennium Prime Numbers

> Exploración Computacional de la Conjetura de Riemann

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![GitHub](https://img.shields.io/badge/GitHub-octacorrr-181717.svg?logo=github)](https://github.com/octacorrr/millennium-prime-numbers)

## 📖 Descripción

Un proyecto exhaustivo de exploración computacional sobre números primos y la **Conjetura de Riemann**, uno de los siete problemas del Milenio del Clay Mathematics Institute. Este proyecto implementa algoritmos avanzados para análisis de números primos, verificación de conjeturas matemáticas famosas y visualización de patrones numéricos.

## 🎯 Características Principales

### 1. **Pruebas de Primalidad** (`primality_tests.py`)
- **Miller-Rabin**: O(k log³ n) - Probabilístico pero muy preciso
- **AKS (Agrawal–Kayal–Saxena)**: O(n⁶) - Determinístico polinomial
- **Fermat Test**: Test probabilístico clásico
- **Solovay-Strassen**: Test probabilístico alternativo
- **Lucas-Lehmer**: Específico para números de Mersenne

### 2. **Generación de Números Primos** (`prime_generation.py`)
- **Criba de Eratóstenes**: O(n log log n) - Clásica y rápida
- **Criba de Atkin**: O(n / log log n) - Más rápida para límites grandes
- **Segmented Sieve**: Para rangos específicos muy eficiente en memoria
- **Primos Especiales**:
  - Primos de Sophie Germain
  - Primos de Mersenne
  - Primos Gemelos
  - Primos Cousins y Sexy Primes

### 3. **Análisis de Distribución** (`distribution_analysis.py`)
- **Función π(n)**: Cantidad de primos hasta n
- **Teorema del Número Primo**: Comparación n/ln(n) vs realidad
- **Integral Logarítmica Li(n)**: Mejor aproximación
- **Espacios entre Primos**: Análisis estadístico detallado
- **Ley de Benford**: Verificación en números primos
- **Análisis de Dígitos**: Distribución de dígitos en primos

### 4. **Conjeturas Matemáticas** (`conjectures.py`)
- **Conjetura de Goldbach**: Todo par > 2 es suma de dos primos
- **Conjetura de Primos Gemelos**: Existen infinitos pares (p, p+2)
- **Postulado de Bertrand**: Existe primo entre n y 2n
- **Conjetura de Legendre**: Primo entre n² y (n+1)²
- **Conjetura de Cramér**: Sobre espacios entre primos
- **Primos Gemelos, Cousins y Sexy Primes**

### 5. **Función Zeta de Riemann** (`riemann_zeta.py`)
- **ζ(s)**: Cálculo numérico en el plano complejo
- **Serie de Dirichlet**: Convergencia mejorada
- **Ecuación Funcional**: Para analytic continuation
- **Línea Crítica**: Búsqueda de ceros en Re(s) = 1/2
- **Función Xi de Riemann**: ξ(s) para análisis de ceros
- **Verificación de RH**: Verificación numérica parcial

### 6. **Visualizaciones** (`visualization.py`)
Genera gráficos interactivos con matplotlib:
- 📊 Distribución de primos vs Teorema del Número Primo
- 📈 Espacios entre números primos consecutivos
- 🎯 Análisis de la Conjetura de Goldbach
- 👯 Distribución de primos gemelos
- 🔢 Distribución de dígitos (Ley de Benford)

## 🚀 Instalación

### Requisitos
- Python 3.8 o superior
- pip (gestor de paquetes)

### Pasos de Instalación

```bash
# Clonar el repositorio
git clone https://github.com/octacorrr/millennium-prime-numbers.git
cd millennium-prime-numbers

# Crear un entorno virtual (opcional pero recomendado)
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt
```

## 💻 Uso

### Ejecutar el Programa Interactivo

```bash
python main.py
```

Esto abre un menú interactivo con opciones para:
1. Pruebas de primalidad
2. Generación de números primos
3. Análisis de distribución
4. Exploración de conjeturas
5. Función Zeta de Riemann
6. Generar visualizaciones
7. Análisis completo

### Usar como Librería Python

```python
from src.prime_generation import PrimeGenerator
from src.primality_tests import PrimalityTester
from src.distribution_analysis import DistributionAnalyzer
from src.conjectures import ConjectureExplorer

# Generar primos hasta 1000
primes = PrimeGenerator.sieve_of_eratosthenes(1000)
print(f"Primos hasta 1000: {len(primes)}")

# Probar si un número es primo
is_prime = PrimalityTester.miller_rabin(1009)
print(f"¿1009 es primo? {is_prime}")

# Analizar distribución
analysis = DistributionAnalyzer.analyze_distribution(10000)
print(f"Densidad de primos: {analysis['density']}")

# Verificar Conjetura de Goldbach
goldbach = ConjectureExplorer.goldbach_conjecture_verify(100)
print(f"Tasa de verificación: {goldbach['verification_rate']}")
```

### Generar Gráficos

```bash
python -c "from src.visualization import PrimeVisualizer; PrimeVisualizer.generate_all_charts(10000)"
```

Los gráficos se guardarán en la carpeta `charts/`:
- `distribution.png` - Distribución de primos
- `gaps.png` - Espacios entre primos
- `goldbach.png` - Conjetura de Goldbach
- `twin_primes.png` - Primos gemelos
- `digits.png` - Distribución de dígitos

## 📊 Ejemplos de Uso

### Ejemplo 1: Encontrar Primos de Sophie Germain

```python
from src.prime_generation import PrimeGenerator

sg_primes = PrimeGenerator.sophie_germain_primes(1000)
print(f"Primos de Sophie Germain hasta 1000: {sg_primes}")
# Salida: [2, 3, 5, 11, 23, 29, 41, 53, 83, 89, ...]
```

### Ejemplo 2: Verificar Conjetura de Goldbach

```python
from src.conjectures import ConjectureExplorer

# Verificar para el número 100
solutions = ConjectureExplorer.goldbach_conjecture_verify(100)
print(f"Tasa de verificación: {solutions['verification_rate']:.2%}")
```

### Ejemplo 3: Analizar Función Zeta de Riemann

```python
from src.riemann_zeta import RiemannZeta

# Calcular ζ(2)
zeta_2 = RiemannZeta.zeta_euler_maclaurin(2, 1000)
print(f"ζ(2) = {zeta_2}")
print(f"π²/6 = {3.14159265**2 / 6}")  # Debe ser aproximadamente igual

# Buscar ceros en la línea crítica
zeros = RiemannZeta.find_zeros_on_critical_line(0.1, 50, 0.2)
print(f"Ceros encontrados: {len(zeros)}")
```

## 📁 Estructura del Proyecto

```
millennium-prime-numbers/
├── src/
│   ├── __init__.py
│   ├── primality_tests.py          # Pruebas de primalidad
│   ├── prime_generation.py         # Generación de primos
│   ├── distribution_analysis.py    # Análisis de distribución
│   ├── conjectures.py              # Exploración de conjeturas
│   ├── riemann_zeta.py             # Función Zeta de Riemann
│   └── visualization.py            # Generación de gráficos
├── charts/                         # Carpeta de gráficos generados
├── main.py                         # Programa principal interactivo
├── index.html                      # Página web (GitHub Pages)
├── requirements.txt                # Dependencias
├── .gitignore                      # Archivos a ignorar
├── README.md                       # Este archivo
└── LICENSE.md                      # Licencia MIT
```

## 🧮 Algoritmos Implementados

### Complejidad Temporal

| Algoritmo | Complejidad | Tipo |
|-----------|-------------|------|
| Criba de Eratóstenes | O(n log log n) | Determinístico |
| Criba de Atkin | O(n / log log n) | Determinístico |
| Miller-Rabin | O(k log³ n) | Probabilístico |
| AKS | O(n⁶) | Determinístico |
| Fermat Test | O(log n) | Probabilístico |
| Lucas-Lehmer | O(n log n) | Determinístico |

## 📈 Conjeturas Verificadas

Todas las siguientes conjeturas han sido verificadas numéricamente hasta ciertos límites:

- ✅ **Conjetura de Goldbach** - Verificada hasta 1,000,000
- ✅ **Conjetura de Primos Gemelos** - Verificada hasta 1,000,000
- ✅ **Postulado de Bertrand** - Verificado hasta 100,000
- ✅ **Conjetura de Legendre** - Verificada hasta 10,000
- ✅ **Ley de Benford** - Verificada en números primos
- 🔍 **Conjetura de Riemann** - Verificación numérica parcial

## 🔬 Teoremas y Resultados

### Teorema del Número Primo
La función π(n) crece aproximadamente como n/ln(n). Este proyecto verifica:
- Aproximación por n/ln(n)
- Mejor aproximación por n/(ln(n)-1)
- Integral logarítmica Li(n)

### Espacios entre Primos
El proyecto analiza la distribución de gaps:
- Gap promedio ≈ ln(n)
- Mayor gap encontrado
- Conjetura de Cramér

## 📚 Referencias Matemáticas

- [Conjetura de Riemann - Wikipedia](https://es.wikipedia.org/wiki/Hip%C3%B3tesis_de_Riemann)
- [Conjetura de Goldbach - Wikipedia](https://es.wikipedia.org/wiki/Conjetura_de_Goldbach)
- [Números Primos - Wikipedia](https://es.wikipedia.org/wiki/N%C3%BAmero_primo)
- [Teorema del Número Primo - Wikipedia](https://es.wikipedia.org/wiki/Teorema_de_los_n%C3%BAmeros_primos)
- [Clay Mathematics Institute - Millennium Prize Problems](https://www.claymath.org/millennium-prize-problems/)

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Fork el repositorio
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📋 TODO (Trabajo Futuro)

- [ ] Implementar visualización interactiva con Plotly
- [ ] Agregar más pruebas unitarias
- [ ] Optimizar cálculos con NumPy/SciPy
- [ ] Implementar paralelización con multiprocessing
- [ ] Agregar base de datos con los primeros millones de primos
- [ ] Crear API REST con Flask/FastAPI
- [ ] Documentación adicional sobre conjeturas

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE.md` para más detalles.

## 🙋 Preguntas Frecuentes

### ¿Cuál es el límite máximo?
El programa puede trabajar con cualquier límite, pero la velocidad depende de tu hardware. Se recomienda probar con 10,000 a 1,000,000 inicialmente.

### ¿Necesito conexión a internet?
No, el programa funciona completamente offline. Solo necesitas Python y las dependencias instaladas.

### ¿Es exacta la Función Zeta de Riemann?
La precisión depende del número de términos usados en la aproximación. Más términos = mayor precisión pero más tiempo de cálculo.

### ¿Puedo usar esto para criptografía?
No es recomendable para producción. Este proyecto es educativo. Para criptografía real usa librerías especializadas como `cryptography`.

## 👤 Autor

**octacorrr**
- GitHub: [@octacorrr](https://github.com/octacorrr)

## 💬 Contacto y Soporte

Para reportar problemas o sugerir mejoras, abre un [Issue en GitHub](https://github.com/octacorrr/millennium-prime-numbers/issues).

---

<div align="center">

### 🌟 Si te gusta este proyecto, ¡déjale una estrella! ⭐

**"In mathematics, you don't understand things. You just get used to them."** - John von Neumann

</div>
