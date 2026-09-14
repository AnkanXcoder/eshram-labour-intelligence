from ingestion.api_client import fetch_data

import pandas as pd

from data_engineering.cleaning import clean_dataframe
from data_engineering.quality_report import generate_quality_report

from data_engineering.validation import (
    check_missing_values,
    check_duplicate_rows,
    check_invalid_ages,
    check_invalid_geographic_codes,
    check_state_code_consistency
)


def run_pipeline():

    limit = 100
    all_records = []

    for page in range(3):

        offset = page * limit

        print(f"\nFetching page {page + 1}")
        print(f"Offset: {offset}")

        data = fetch_data(
            limit=limit,
            offset=offset
        )

        if data is None:
            print("Pipeline stopped: no data received.")
            return

        records = data

        all_records.extend(records)

        print("Records received:", len(records))

    print("\nTotal records collected:", len(all_records))

    df = pd.DataFrame(all_records)

    df = clean_dataframe(df)

    quality_report = generate_quality_report(df)

    print("\nData Quality Report:")

    for key, value in quality_report.items():
        print(f"{key}: {value}")

    print("\nCleaned DataFrame shape:", df.shape)

    print("\nData types:")
    print(df.dtypes)

    print("\nMissing values:")
    print(check_missing_values(df))

    print("\nUnique values:")

    print("\nGender:")
    print(df["gender"].unique())

    print("\nEducation:")
    print(df["educationQualification"].unique())

    print("\nOccupation:")
    print(df["primaryOccupation"].unique())

    print("\nDataFrame shape:", df.shape)

    print("\nColumns:")
    print(df.columns.tolist())

    print("\nDuplicate rows:")
    print(check_duplicate_rows(df))

    print("\nAge statistics:")
    print(df["age"].describe())

    print("\nInvalid ages:")
    print(check_invalid_ages(df))

    print("\nInvalid geographic codes:")

    geo_results = check_invalid_geographic_codes(df)

    for name, invalid_rows in geo_results.items():
        print(f"{name}: {len(invalid_rows)}")

    print("\nState code consistency:")

    state_results = check_state_code_consistency(df)

    for name, mapping in state_results.items():
        inconsistent = mapping[mapping > 1]
        print(f"{name}: {len(inconsistent)} inconsistent codes")

    return df


if __name__ == "__main__":
    run_pipeline()