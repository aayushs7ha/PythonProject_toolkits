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

    # Check for disparities between dtypes and actual values
    dtypes_disparities = {}
    for col in df.columns:
        unique_values = df[col].unique()
        dtype = df[col].dtype
        unique_types = set(type(value).__name__ for value in unique_values)
        if len(unique_types) > 1:
            dtypes_disparities[col] = {"dtype": dtype, "unique_types": list(unique_types)}

    results["dtypes_disparities"] = dtypes_disparities

    # Unique values and counts
    for col in df.columns:
        results[f"unique_values_{col}"] = df[col].unique()

    if verbose:
        for key, value in results.items():
            print(f"\n{key}:\n{value}")

    return results
