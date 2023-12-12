import pandas as pd

def diagnose_dataframe(df, verbose=True):
  """
  Performs various initial inspections on a pandas dataframe and provides details.

  Args:
    df: The pandas dataframe to diagnose.
    verbose: Whether to print details for each inspection.

  Returns:
    A dictionary containing the results of the inspections.
  """

  results = {}

  # Basic information
  results["shape"] = df.shape
  results["columns"] = list(df.columns)
  results["dtypes"] = df.dtypes.to_dict()
  results["null_counts"] = df.isnull().sum().to_dict()

  # Descriptive statistics
  results["describe"] = df.describe(include='all')

  # Unique values and counts
  for col in df.columns:
    results[f"unique_values_{col}"] = df[col].unique()
    results[f"value_counts_{col}"] = df[col].value_counts().to_dict()

  # Missing value analysis
  missing_values_pct = (df.isnull().sum() / df.shape[0]) * 100
  results["missing_values_pct"] = missing_values_pct.to_dict()
  missing_values_threshold = 0.5  # Set a threshold for high missing value percentage
  high_missing_values = missing_values_pct[missing_values_pct > missing_values_threshold]
  results["high_missing_values"] = list(high_missing_values.index)

  # Duplicate rows
  duplicate_rows = df[df.duplicated()]
  results["duplicate_rows_count"] = len(duplicate_rows)

  # Outlier analysis
  # ... (implement your own outlier analysis strategy)

  if verbose:
    for key, value in results.items():
      print(f"\n{key}:\n{value}")

  return results
