import numpy as np
import pandas as pd
from scipy import stats

# Generate some sample data
data = np.random.normal(loc=50, scale=10, size=1000)

# Mean, Median, Mode
mean = np.mean(data)
median = np.median(data)
mode = stats.mode(data)

# Variance, Standard Deviation
variance = np.var(data)
std_deviation = np.std(data)

# Quartiles and Interquartile Range (IQR)
quartiles = np.percentile(data, [25, 50, 75])
iqr = quartiles[2] - quartiles[0]

# Skewness and Kurtosis
skewness = stats.skew(data)
kurtosis = stats.kurtosis(data)

print("Mean:", mean)
print("Median:", median)
print("Mode:", mode[0])
print("Variance:", variance)
print("Standard Deviation:", std_deviation)
print("25th Percentile (Q1):", quartiles[0])
print("50th Percentile (Q2/Median):", quartiles[1])
print("75th Percentile (Q3):", quartiles[2])
print("Interquartile Range (IQR):", iqr)
print("Skewness:", skewness)
print("Kurtosis:", kurtosis)
print("\n\n")

# Generate some sample data
group1 = np.random.normal(loc=50, scale=10, size=100)
group2 = np.random.normal(loc=55, scale=10, size=100)

# Perform independent t-test
t_stat, p_value = stats.ttest_ind(group1, group2)

print("T-statistic:", t_stat)
print("P-value:", p_value)

print("\n\n")
from scipy.stats import pearsonr, spearmanr
# Generate some sample data
x = np.random.normal(loc=50, scale=10, size=100)
y = np.random.normal(loc=50, scale=10, size=100)

# Compute Pearson correlation coefficient
pearson_corr, _ = pearsonr(x, y)

# Compute Spearman's rank correlation coefficient
spearman_corr, _ = spearmanr(x, y)

print("Pearson Correlation Coefficient:", pearson_corr)
print("Spearman's Rank Correlation Coefficient:", spearman_corr)