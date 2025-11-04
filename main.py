
import random
from algos.tri_selection import tri_selection
from algos.tri_bulles import tri_bulles
from algos.tri_insertion import tri_insertion
from algos.tri_echange import tri_echange

from utils.mesure_temps import mesurer_temps
from utils.generate_table import generate_table
from utils.generate_plot import generate_plot


def main():
    random.seed(0)
    sizes = [100, 300, 700]
    algorithms = [
        ("tri_selection", tri_selection),
        ("tri_bulles", tri_bulles),
        ("tri_insertion", tri_insertion),
        ("tri_echange", tri_echange),
    ]

    results = []
    for size in sizes:
        arr = [random.randint(0, size) for _ in range(size)]
        for name, func in algorithms:
            t, sorted_arr = mesurer_temps(func, arr)
            # quick sanity check that sorting worked
            if sorted_arr != sorted(arr):
                print(f"Warning: {name} did not sort correctly for size={size}")
            results.append({"algorithm": name, "size": size, "time": t})
            print(f"{name} size={size} time={t:.6f}s")

    csv_file = generate_table(results, filename='results.csv')
    print(f"Wrote results to {csv_file}")

    try:
        png_file = generate_plot(results, filename='results.png')
        print(f"Saved plot to {png_file}")
    except Exception as e:
        print(f"Plot generation failed: {e}. You may need matplotlib installed.")


if __name__ == '__main__':
    main()

# This is a sample Python script.

# Press Ctrl+F5 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press F9 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
