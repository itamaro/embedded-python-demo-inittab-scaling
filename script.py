#!/usr/bin/env python3
"""
Benchmarking script for embedded Python extension modules using inittab.
"""

import argparse
import sys
import time

def benchmark_imports(num_extensions: int = 10) -> None:
    """
    Benchmark the import times of extension modules.
    """
    for n in range(num_extensions):
        module_name = f"inittab_ext_{n}"
        start_time = time.perf_counter()
        __import__(module_name)
        end_time = time.perf_counter()
        import_time_us = (end_time - start_time) * 1_000_000  # Convert to microseconds
        if n % 100 == 0 or n == num_extensions - 1:
            print(f"  {module_name}: {import_time_us:.1f} μs")

def main():
    """
    Main benchmarking function.
    """
    parser = argparse.ArgumentParser(
        description="Benchmark embedded Python extension module import times",
    )
    parser.add_argument(
        '--extensions', '-e',
        type=int,
        default=10,
        help='Number of extension modules to benchmark (default: 10)'
    )
    args = parser.parse_args()
    print("Embedded Python Extension Module Import Benchmark")
    print("=" * 60)

    print(f"Starting benchmark: {args.extensions} extensions")
    print("=" * 60)
    print("{", file=sys.stderr)
    # Run benchmark
    start_total = time.perf_counter()
    benchmark_imports(args.extensions)
    end_total = time.perf_counter()
    print("}", file=sys.stderr)
    
    # Final summary
    total_time = end_total - start_total
    print(f"\n{'='*60}")
    print("BENCHMARK COMPLETE")
    print(f"{'='*60}")
    print(f"Total benchmark time: {total_time:.3f} seconds")
    print(f"Extensions tested: {args.extensions}")

if __name__ == "__main__":
    main()
