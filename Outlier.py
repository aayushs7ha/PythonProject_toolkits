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



# Dealing with outliers - here's how. 

from scipy.stats.mstats import winsorize
# Function to handle outliers using Winsorizing
def handle_outliers_winsorize(df, lower_limit=0.05, upper_limit=0.95):
    # Convert columns to numeric, handling non-numeric values
    #df_numeric = df.apply(pd.to_numeric, errors='coerce')
    
    # Winsorize numeric columns
    df_winsorized = df_numeric.apply(lambda x: winsorize(x, limits=(lower_limit, upper_limit)).data)
    return pd.DataFrame(df_winsorized, columns=df.columns)



# Drop outliers and reset index

print("Before: {} rows".format(len(train)))
train = train.drop(outliers_to_drop, axis = 0).reset_index(drop = True)
print("After: {} rows".format(len(train)))
