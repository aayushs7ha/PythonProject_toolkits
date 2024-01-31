# import seaborn as sns
import matplotlib.pyplot as plt

def plot_individual_boxen_plots(dataframe):
    # Selecting only numerical columns
    numerical_features = dataframe.select_dtypes(include=['int64', 'float64'])

    # Setting up the matplotlib figure with individual subplots
    fig, axes = plt.subplots(nrows=len(numerical_features.columns), figsize=(12, 3 * len(numerical_features.columns)))

    # Creating individual boxen plots for each numerical feature
    for i, feature in enumerate(numerical_features.columns):
        sns.boxenplot(x=numerical_features[feature], ax=axes[i])
        axes[i].set_title(f'Boxen Plot for {feature}')

    # Adjusting layout
    plt.tight_layout()

    # Display the plots
    plt.show()

# Assuming 'df' is your DataFrame with the specified columns
plot_individual_boxen_plots(train[['CreditScore', 'Age', 'Tenure', 'Balance', 'NumOfProducts',
                                'HasCrCard', 'IsActiveMember', 'EstimatedSalary', 'Exited']])



from collections import Counter
def detect_outliers(df, n, features):
    """"
    This function will loop through a list of features and detect outliers in each one of those features. In each
    loop, a data point is deemed an outlier if it is less than the first quartile minus the outlier step or exceeds
    third quartile plus the outlier step. The outlier step is defined as 1.5 times the interquartile range. Once the 
    outliers have been determined for one feature, their indices will be stored in a list before proceeding to the next
    feature and the process repeats until the very last feature is completed. Finally, using the list with outlier 
    indices, we will count the frequencies of the index numbers and return them if their frequency exceeds n times.    
    """
    outlier_indices = [] 
    for col in features: 
        Q1 = np.percentile(df[col], 25)
        Q3 = np.percentile(df[col], 75)
        IQR = Q3 - Q1
        outlier_step = 1.5 * IQR 
        outlier_list_col = df[(df[col] < Q1 - outlier_step) | (df[col] > Q3 + outlier_step)].index
        outlier_indices.extend(outlier_list_col) 
    outlier_indices = Counter(outlier_indices)
    multiple_outliers = list(key for key, value in outlier_indices.items() if value > n) 
    return multiple_outliers

outliers_to_drop = detect_outliers(train, 2, ['CreditScore', 'Age', 'Tenure', 'Balance', 'NumOfProducts', 'HasCrCard', 'IsActiveMember', 'EstimatedSalary',])
print("We will drop these {} indices: ".format(len(outliers_to_drop)), outliers_to_drop)
