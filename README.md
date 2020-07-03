# BHTSNE
# Language: Python
# Input: CSV
# Output: CSV
# Tested with: PluMA 1.0, Python 3.6
# Dependency: numpy==1.16.0, bhtsne==0.1.9

Barnes-Hut version of tSNE (Laczny et al, 2014), which attempts to classify
sample sets into categories.

The plugin accepts as input a CSV file containing samples (rows) and data measurements.
Note: The provided example comes from the digits dataset (sklearn).

The plugin generates as output a CSV file that contains one line per sample, and
the value of principle components for each sample.
