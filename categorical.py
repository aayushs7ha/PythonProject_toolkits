# Extract categorical columns
categorical_columns = df_service.select_dtypes(include=['object']).columns
print(categorical_columns)


# Loop through categorical columns 
for column in categorical_columns:
  print(f"Value counts of {column} : \n{df[column].value_counts()}\n")
  # Plot count plot
  plt.figure(figsize=(10, 6))
  sns.countplot(x=column, data=df_service, order=df_service[column].value_counts().index)
  plt.title(f'Count Plot for {column}')
  plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
  plt.show()
