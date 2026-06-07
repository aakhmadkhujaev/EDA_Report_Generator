def statistics_report(df):

    numerical_df = df.select_dtypes(include=['number'])
    categorical_df = df.select_dtypes(include=['object', 'category'])

    numerical_statistics = {}

    for column in numerical_df.columns:
        numerical_statistics[column] = {
            'mean': numerical_df[column].mean(),
            'median': numerical_df[column].median(),
            'std_dev': numerical_df[column].std(),
            'min': numerical_df[column].min(),
            'max': numerical_df[column].max(),
            'count': numerical_df[column].count()
        }

    categorical_statistics = {} 

    for column in categorical_df.columns:
        categorical_statistics[column] = {
            'unique_values': categorical_df[column].nunique(),
            'most_frequent': categorical_df[column].mode()[0],
            'frequency': categorical_df[column].value_counts().iloc[0]
        }

    return {
        'numerical': numerical_statistics,
        'categorical': categorical_statistics
    }