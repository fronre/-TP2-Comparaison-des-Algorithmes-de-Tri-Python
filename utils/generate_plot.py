def generate_plot(results, filename='results.png'):
    """Generate a line plot (size vs time) for each algorithm and save to filename.

    results: iterable of dicts with keys: 'algorithm', 'size', 'time'
    Returns the filename written.
    """
    algos = {}
    for r in results:
        algo = r['algorithm']
        algos.setdefault(algo, []).append((int(r['size']), float(r['time'])))

    # Import matplotlib only when plotting is requested so the module is optional.
    import matplotlib.pyplot as plt

    plt.figure(figsize=(8, 5))
    for algo, pairs in algos.items():
        pairs.sort()
        sizes = [p[0] for p in pairs]
        times = [p[1] for p in pairs]
        plt.plot(sizes, times, marker='o', label=algo)

    plt.xlabel('Input size')
    plt.ylabel('Time (s)')
    plt.title('Sorting algorithms performance')
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.legend()
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()
    return filename
