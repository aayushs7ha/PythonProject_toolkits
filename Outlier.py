# Function to check for outliers after Winsorizing
def check_outliers(df):
    for column in df.columns:
        # Calculate Z-scores for each column
        z_scores = np.abs((df[column] - df[column].mean()) / df[column].std())
        
        # Identify potential outliers (Z-score > 3)
        outliers = df[z_scores > 3]
        
        if not outliers.empty:
            print(f"Potential outliers in {column}:")
            print(outliers)
            print("\n")
        else:
            print(f"No potential outliers in {column}.\n")

# Check for outliers after Winsorizing
check_outliers(df_numeric)
