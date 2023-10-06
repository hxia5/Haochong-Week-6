"""
ETL-Query script
"""

from mylib.lib import extract
from mylib.lib import load
import sys
import argparse
from mylib.lib import complex_query

# Extract
print("Extracting data...")
extract()

# Transform and load
print("Transforming data...")
load()

if __name__ == "__main__":
    complex_query()

