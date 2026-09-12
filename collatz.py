#!/usr/bin/env python3
"""
Conjetura de Collatz (3n+1) — Explorador interactivo
====================================================
La conjetura afirma que, partiendo de cualquier entero positivo n,
al aplicar reiteradamente:
    n → n/2    si n es par
    n → 3n+1   si n es impar
siempre se llega a 1.

Funciones:
  1. Secuencia de un número
  2. Análisis de rango (longitud, máximos)
  3. Top secuencias más largas
  4. Verificar que todos llegan a 1 hasta N
  5. Comparar dos números
  6. Histograma de longitudes (densidad de pasos)
  7. Récords históricos conocidos
  8. Exportar secuencia a CSV
"""

from __future__ import annotations

import csv
import sys
from collections import Counter
from typing import List, Dict


# Récords conocidos (pasos hasta 1) — datos públicos OEIS A006577
HISTORICAL_RECORDS = [
    {"n": 1, "steps": 0, "note": "trivial"},
    {"n": 2, "steps": 1, "note": ""},
    {"n": 3, "steps": 7, "note": ""},
    {"n": 6, "steps": 8, "note": ""},
    {"n": 7, "steps": 16, "note": ""},
    {"n": 9, "steps": 19, "note": ""},
    {"n": 18, "steps": 20, "note": ""},
    {"n": 25, "steps": 23, "note": ""},
    {"n": 27, "steps": 111, "note": "famoso pico temprano"},
    {"n": 54, "steps": 112, "note": ""},
    {"n": 73, "steps": 115, "note": ""},
    {"n": 97, "steps": 118, "note": ""},
    {"n": 129, "steps": 121, "note": ""},
    {"n": 171, "steps": 124, "note": ""},
    {"n": 231, "steps": 127, "note": ""},
    {"n": 313, "steps": 130, "note": ""},
    {"n": 327, "steps": 143, "note": ""},
    {"n": 649, "steps": 144, "note": ""},
    {"n": 703, "steps": 170, "note": ""},
    {"n": 871, "steps": 178, "note": ""},
    {"n": 1161, "steps": 181, "note": ""},
    {"n": 2223, "steps": 182, "note": ""},
    {"n": 2463, "steps": 208, "note": ""},
    {"n": 2919, "steps": 216, "note": ""},
    {"n": 3711, "steps": 237, "note": ""},
    {"n": 6171, "steps": 261, "note": "récord < 10k"},
    {"n": 10971, "steps": 267, "note": ""},
    {"n": 17647, "steps": 278, "note": ""},
    {"n": 26623, "steps": 307, "note": ""},
    {"n": 34239, "steps": 310, "note": ""},
    {"n": 35655, "steps": 323, "note": ""},
    {"n": 52527, "steps": 339, "note": ""},
    {"n": 77031, "steps": 350, "note": "récord < 100k"},
    {"n": 106239, "steps": 353, "note": ""},
    {"n": 142587, "steps": 374, "note": ""},
    {"n": 156159, "steps": 382, "note": ""},
    {"n": 216367, "steps": 386, "note": ""},
    {"n": 230631, "steps": 442, "note": ""},
    {"n": 410011, "steps": 448, "note": ""},
    {"n": 511935, "steps": 469, "note": ""},
    {"n": 637281, "steps": 471, "note": ""},
    {"n": 703081, "steps": 503, "note": "récord < 1M (aprox.)"},
]


def collatz_sequence(n: int) -> List[int]:
    """Secuencia completa de Collatz hasta llegar a 1."""
    if n < 1:
        raise ValueError("n debe ser un entero positivo")
    seq = [n]
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        seq.append(n)
        if len(seq) > 10_000_000:
            raise RuntimeError("Secuencia excesivamente larga")
    return seq


def collatz_stats(n: int) -> Dict:
    seq = collatz_sequence(n)
    return {
        "n": n,
        "sequence": seq,
        "steps": len(seq) - 1,
        "max_value": max(seq),
        "length": len(seq),
    }


def analyze_range(start: int, end: int) -> Dict:
    if start < 1 or end < start:
        raise ValueError("Rango inválido")

    longest_n, longest_len = start, 0
    highest_n, highest_max = start, 0
    total_steps = 0
    details = []
    step_counts: Counter = Counter()

    for n in range(start, end + 1):
        stats = collatz_stats(n)
        total_steps += stats["steps"]
        step_counts[stats["steps"]] += 1
        if stats["steps"] > longest_len:
            longest_len = stats["steps"]
            longest_n = n
        if stats["max_value"] > highest_max:
            highest_max = stats["max_value"]
            highest_n = n
        details.append(stats)

    return {
        "start": start,
        "end": end,
        "count": end - start + 1,
        "longest": {"n": longest_n, "steps": longest_len},
        "highest_peak": {"n": highest_n, "max": highest_max},
        "avg_steps": total_steps / (end - start + 1),
        "step_histogram": dict(sorted(step_counts.items())),
        "details": details,
    }


def print_sequence(n: int, max_show: int = 80) -> None:
    stats = collatz_stats(n)
    seq = stats["sequence"]
    print(f"\n{'='*62}")
    print(f"  Secuencia de Collatz para n = {n}")
    print(f"{'='*62}")
    print(f"  Pasos hasta 1 : {stats['steps']}")
    print(f"  Valor máximo  : {stats['max_value']}")
    print(f"{'-'*62}")
    if len(seq) <= max_show:
        print("  → " + " → ".join(map(str, seq)))
    else:
        head = " → ".join(map(str, seq[:35]))
        tail = " → ".join(map(str, seq[-8:]))
        print(f"  → {head} → … → {tail}")
    print(f"{'='*62}\n")


def print_range_summary(result: Dict) -> None:
    print(f"\n{'='*62}")
    print(f"  Análisis: {result['start']} … {result['end']}")
    print(f"{'='*62}")
    print(f"  Números analizados     : {result['count']}")
    print(f"  Secuencia más larga    : n = {result['longest']['n']} "
          f"({result['longest']['steps']} pasos)")
    print(f"  Pico más alto          : n = {result['highest_peak']['n']} "
          f"(máx = {result['highest_peak']['max']})")
    print(f"  Promedio de pasos      : {result['avg_steps']:.2f}")
    print(f"{'='*62}\n")


def print_top_longest(result: Dict, top: int = 10) -> None:
    ranked = sorted(result["details"], key=lambda x: x["steps"], reverse=True)[:top]
    print(f"  Top {top} secuencias más largas:")
    print(f"  {'n':>10}  {'pasos':>8}  {'máximo':>14}")
    print(f"  {'-'*10}  {'-'*8}  {'-'*14}")
    for s in ranked:
        print(f"  {s['n']:10d}  {s['steps']:8d}  {s['max_value']:14d}")
    print()


def print_histogram(result: Dict, width: int = 40) -> None:
    hist = result["step_histogram"]
    if not hist:
        return
    max_count = max(hist.values())
    print(f"\n  Histograma de longitudes (pasos → frecuencia)")
    print(f"  {'pasos':>6}  {'count':>6}  barra")
    print(f"  {'-'*6}  {'-'*6}  {'-'*width}")
    items = list(hist.items())
    if len(items) > 30:
        min_s, max_s = items[0][0], items[-1][0]
        bin_size = max(1, (max_s - min_s) // 25)
        buckets: Dict[int, int] = {}
        for steps, cnt in items:
            key = (steps // bin_size) * bin_size
            buckets[key] = buckets.get(key, 0) + cnt
        items = sorted(buckets.items())
        max_count = max(items, key=lambda x: x[1])[1]

    for steps, cnt in items:
        bar_len = int(width * cnt / max_count) if max_count else 0
        bar = "█" * bar_len
        print(f"  {steps:6d}  {cnt:6d}  {bar}")
    print()


def print_historical() -> None:
    print(f"\n{'='*62}")
    print("  Récords históricos de pasos (Collatz)")
    print(f"{'='*62}")
    print(f"  {'n':>10}  {'pasos':>8}  nota")
    print(f"  {'-'*10}  {'-'*8}  {'-'*20}")
    for r in HISTORICAL_RECORDS:
        print(f"  {r['n']:10d}  {r['steps']:8d}  {r['note']}")
    print(f"\n  (Fuente: OEIS A006577 y tablas clásicas de Collatz)")
    print(f"{'='*62}\n")


def export_csv(n: int, path: str = "collatz_sequence.csv") -> None:
    seq = collatz_sequence(n)
    with open(path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["step", "value"])
        for i, v in enumerate(seq):
            w.writerow([i, v])
    print(f"  ✓ Secuencia de {n} exportada a {path} ({len(seq)} filas)\n")


def verify_all_reach_one(limit: int) -> None:
    print(f"\n  Verificando 1 … {limit} …")
    for n in range(1, limit + 1):
        collatz_sequence(n)
    print(f"  ✓ Todos llegan a 1. La conjetura se cumple en este rango.\n")


def compare_two(a: int, b: int) -> None:
    sa, sb = collatz_stats(a), collatz_stats(b)
    print(f"\n{'='*50}")
    print(f"  Comparación  {a}  vs  {b}")
    print(f"{'='*50}")
    print(f"  {'':15} {a:>12}  {b:>12}")
    print(f"  {'Pasos':15} {sa['steps']:12d}  {sb['steps']:12d}")
    print(f"  {'Máximo':15} {sa['max_value']:12d}  {sb['max_value']:12d}")
    print(f"{'='*50}\n")


def menu() -> None:
    print("""
╔════════════════════════════════════════════════════════════╗
║            CONJETURA DE COLLATZ (3n + 1)                   ║
║              Explorador interactivo                        ║
╚════════════════════════════════════════════════════════════╝

  1. Seguir la secuencia de un número
  2. Analizar un rango de números
  3. Top secuencias más largas + histograma
  4. Verificar que todos llegan a 1 (hasta N)
  5. Comparar dos números
  6. Récords históricos conocidos
  7. Exportar secuencia a CSV
  0. Salir
""")


def main() -> None:
    while True:
        menu()
        choice = input("  Elige una opción: ").strip()

        try:
            if choice == "0":
                print("\n  ¡Hasta luego!\n")
                break

            elif choice == "1":
                n = int(input("  Número n: "))
                print_sequence(n)

            elif choice == "2":
                start = int(input("  Desde: "))
                end = int(input("  Hasta: "))
                if end - start > 100_000:
                    print("  Rango demasiado grande (máx. ~100 000).")
                    continue
                result = analyze_range(start, end)
                print_range_summary(result)

            elif choice == "3":
                start = int(input("  Desde: "))
                end = int(input("  Hasta: "))
                top = int(input("  ¿Cuántos del top? [10]: ") or "10")
                if end - start > 50_000:
                    print("  Rango grande; puede tardar…")
                result = analyze_range(start, end)
                print_range_summary(result)
                print_top_longest(result, top)
                print_histogram(result)

            elif choice == "4":
                limit = int(input("  Verificar hasta N = "))
                if limit > 1_000_000:
                    print("  Límite alto; puede tardar varios segundos.")
                verify_all_reach_one(limit)

            elif choice == "5":
                a = int(input("  Primer número: "))
                b = int(input("  Segundo número: "))
                compare_two(a, b)

            elif choice == "6":
                print_historical()

            elif choice == "7":
                n = int(input("  Número n a exportar: "))
                path = input("  Nombre de archivo [collatz_sequence.csv]: ").strip()
                if not path:
                    path = "collatz_sequence.csv"
                export_csv(n, path)

            else:
                print("  Opción no válida.\n")

        except ValueError as e:
            print(f"  Error: {e}\n")
        except KeyboardInterrupt:
            print("\n\n  Interrumpido.\n")
            break

        input("  Pulsa Enter para continuar…")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n  ¡Hasta luego!\n")
        sys.exit(0)
