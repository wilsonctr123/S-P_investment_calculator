import csv

INPUT_CSV = 'Macrotrends-s-p-500-index-daily.csv'
OUTPUT_CSV = 'leveraged_voo.csv'


def read_index_data(path):
    """Read date and closing value from the MacroTrends CSV."""
    entries = []
    with open(path, newline='') as f:
        reader = csv.reader(f)
        # skip header and disclaimer rows
        for row in reader:
            if row and row[0].startswith('Date'):
                break
        for row in reader:
            if not row:
                continue
            try:
                close = float(row[1])
            except (IndexError, ValueError):
                continue
            entries.append((row[0], close))
    return entries


def create_leveraged_series(entries, leverage):
    """Return a list with a leveraged series based on daily moves."""
    values = [entries[0][1]]
    for i in range(1, len(entries)):
        prev_close = entries[i - 1][1]
        cur_close = entries[i][1]
        daily_return = (cur_close - prev_close) / prev_close
        values.append(values[-1] * (1 + leverage * daily_return))
    return values


def main():
    data = read_index_data(INPUT_CSV)
    voo_1x = [val for _, val in data]
    voo_2x = create_leveraged_series(data, 2)
    voo_3x = create_leveraged_series(data, 3)

    with open(OUTPUT_CSV, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Date', 'VOO', 'VOO_2x', 'VOO_3x'])
        for (date, voo), v2, v3 in zip(data, voo_2x, voo_3x):
            writer.writerow([date, f'{voo:.4f}', f'{v2:.4f}', f'{v3:.4f}'])


if __name__ == '__main__':
    main()
