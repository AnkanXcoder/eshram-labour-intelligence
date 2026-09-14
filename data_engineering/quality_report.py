def generate_quality_report(df):
    report = {
        "total_rows": len(df),
        "total_columns": len(df.columns),
        "missing_values": int(df.isnull().sum().sum()),
        "duplicate_rows": int(df.duplicated().sum()),
        "invalid_ages": int(
            ((df["age"] < 16) | (df["age"] > 59)).sum()
        ),
        "unique_states": int(df["currentStateName"].nunique()),
        "unique_districts": int(df["currentDistrictName"].nunique()),
        "unique_occupations": int(df["primaryOccupation"].nunique()),
        "unique_education_levels": int(
            df["educationQualification"].nunique()
        )
    }

    return report