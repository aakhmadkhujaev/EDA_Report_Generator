def duplicates_report(df):

    duplicate_count = df.duplicated().sum()
    duplicate_percent = (duplicate_count / len(df)) * 100

    return {
        'duplicate_count': int(duplicate_count),
        'duplicate_percent': round(float(duplicate_percent), 2)
    }
