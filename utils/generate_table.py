import csv

def generate_table(results, filename='results.csv'):
    """Write timing results to a CSV file.

    results: iterable of dicts with keys: 'algorithm', 'size', 'time'
    Returns the filename written.
    """
    fieldnames = ['algorithm', 'size', 'time']
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for r in results:
            writer.writerow({k: r.get(k, '') for k in fieldnames})
    return filename
