from src import statistics


def save_txt_report(report):
    with open("reports/report.txt", "w") as f:

        overview = report["overview"]

        f.write("EDA REPORT\n")
        f.write("=" * 40 + "\n\n")

        f.write("OVERVIEW\n")
        f.write("-" * 20 + "\n")
        f.write(f"Rows: {overview['num_rows']}\n")
        f.write(f"Columns: {overview['num_columns']}\n\n")

        duplicates = report["duplicates"]

        f.write("DUPLICATES\n")
        f.write("-" * 20 + "\n")
        f.write(f"Duplicate Rows: {duplicates['duplicate_count']}\n")
        f.write(f"Duplicate Percentage: {duplicates['duplicate_percent']}%\n")

        missing_values = report["missing_values"]
        f.write("\nMISSING VALUES\n")
        f.write("-" * 20 + "\n")                
        f.write(f"Columns With Missing Values: {missing_values["columns_with_missing"]}\n")

        if missing_values["columns_with_missing"] == 0:
            f.write("No missing values detected.\n")
        else:
            missing_details = missing_values["missing_details"]
            for col, details in missing_details.items():
                f.write(f"\nColumn: {col}\n")
                f.write(f"Missing Count: {details['count']}\n")
                f.write(f"Missing Percentage: {details['percentage']}%\n")

        statistics = report["statistics"]
        numerical_stats = statistics["numerical"]   
        f.write("\nSTATISTICS\n")
        f.write("-" * 20 + "\n")

        f.write("NUMERICAL STATISTICS:\n")
        for col, stats in numerical_stats.items():
            f.write(f"\nColumn: {col}\n")
            f.write(f"Mean: {stats['mean']}\n")
            f.write(f"Median: {stats['median']}\n")
            f.write(f"Standard Deviation: {stats['std_dev']}\n")
            f.write(f"Min: {stats['min']}\n")
            f.write(f"Max: {stats['max']}\n")
            f.write(f"Count: {stats['count']}\n")
            f.write("\n")
        
        f.write("CATEGORICAL STATISTICS:\n")
        categorical_stats = statistics["categorical"]
        for col, stats in categorical_stats.items():
            f.write(f"\nColumn: {col}\n")
            f.write(f"Unique Values: {stats['unique_values']}\n")
            f.write(f"Most Frequent Value: {stats['most_frequent']}\n")
            f.write(f"Frequency: {stats['frequency']}\n")
            f.write("\n")