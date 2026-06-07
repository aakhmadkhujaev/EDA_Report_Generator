def duplicates(df):
    duplicates_report = df.duplicated().sum()

    duplicates_report = duplicates_report[duplicates_report > 0]
    duplicates_percent = (duplicates_report / len(df)) * 100
     
    duplicates_details = {}

    for column in duplicates_report.index:
        duplicates_details[column] = {
            "count": int(duplicates_report[column]),
            "percentage": round(float(duplicates_percent[column]), 2)
        }
    
    return {
        "duplicates": duplicates_details,
        "total_duplicates": duplicates_details["count"].sum(),
        "percentage_duplicates": round(float(duplicates_percent.sum()), 2)
    }
