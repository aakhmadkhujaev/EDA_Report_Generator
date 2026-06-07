def missing_values_report(df):
    missing_report = df.isnull().sum()

    # Keep only columns with missing values
    missing_report = missing_report[missing_report > 0]

    missing_report_percent = (missing_report / len(df)) * 100

    missing_details = {}

    for column in missing_report.index:
        missing_details[column] = {
            "count": int(missing_report[column]),
            "percentage": round(float(missing_report_percent[column]), 2)
        }

    return {
        "columns_with_missing": len(missing_details),
        "missing_details": missing_details
    }
        
        