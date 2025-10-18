#!/usr/bin/env -S uv run
# /// script
# requires-python = ">=3.14"
# dependencies = [
#     "matplotlib"
# ]
# ///

"""
Visualize inittab search time data as a line chart.
The script combines multiple JSON files by taking the minimum value for each key.
"""

import sys
import json
import matplotlib.pyplot as plt


def load_data(sources: list[str]) -> dict[str, int]:
    """Load data from multiple file paths."""
    all_data = []

    for source in sources:
        with open(source, "r", encoding="utf-8") as f:
            file_data = json.load(f)
            all_data.append(file_data)

    # Combine data by taking minimum value for each key
    combined_data = {}
    for data in all_data:
        for key, value in data.items():
            if key in combined_data:
                # Take the minimum value
                combined_data[key] = min(combined_data[key], value)
            else:
                combined_data[key] = value
    
    return combined_data


def plot_data(data: dict[str, int]) -> None:
    """Plot dictionary where keys look like 'inittab_ext_<N>'."""
    x = [int(k.split('_')[-1]) for k in data.keys()]
    y = list(data.values())

    # Sort by numeric index
    sorted_pairs = sorted(zip(x, y), key=lambda p: p[0])
    x, y = zip(*sorted_pairs)

    plt.figure(figsize=(10, 5))
    plt.plot(x, y, marker='o')
    plt.title("inittab_ext Values by Index")
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def main():
    if len(sys.argv) < 2:
        print("Missing input JSON files", file=sys.stderr)
        return
    sources = sys.argv[1:]
    data = load_data(sources)
    plot_data(data)


if __name__ == "__main__":
    main()
