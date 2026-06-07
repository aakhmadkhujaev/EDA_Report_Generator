from src.loader import load_dataset
from src.overview import overview_report
from src.missing import missing_values_report
from src.duplicates import duplicates_report
from src.report_writer import save_txt_report
from src.report_writer import save_txt_report
from src.statistics import statistics_report
from src.report_writer import save_txt_report

def main():
    # Load the dataset
    try:
       file_name = input("Enter CSV filename: ")
       file_path = f"data/{file_name}"
       
       df = load_dataset(file_path)
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return

    # Generate reports
    overview = overview_report(df)
    missing_values = missing_values_report(df)
    duplicates = duplicates_report(df)
    statistics = statistics_report(df)

    report = {
        "overview": overview,
        "missing_values": missing_values,
        "duplicates": duplicates,
        "statistics": statistics
    }
    return report

if __name__ == "__main__":
    report = main()

    if report:
        save_txt_report(report)
        print("Report saved successfully!")