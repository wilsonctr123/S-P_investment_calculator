# S&P Investment Calculator

This repository includes historical S&P 500 data and a utility script to create
leveraged versions of the index.

## Leveraged Data Creation

Run the following command to generate a CSV file containing the normal VOO
values along with 2x and 3x daily leveraged series:

```bash
python3 create_leveraged_voo.py
```

The script reads `Macrotrends-s-p-500-index-daily.csv` and produces a new file
named `leveraged_voo.csv` in the same directory.
