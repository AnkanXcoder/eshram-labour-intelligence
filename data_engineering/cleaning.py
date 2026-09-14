def clean_dataframe(df):
    df = df.copy()

    string_columns = [
        "gender",
        "differentlyAbledStatus",
        "educationQualification",
        "currentStateName",
        "currentDistrictName",
        "permanentStateName",
        "primaryOccupation"
    ]

    for column in string_columns:
        df[column] = df[column].str.strip()

    df["DataGovUpdateDate"] = df["DataGovUpdateDate"].astype("datetime64[us]")

    df = df.drop_duplicates()

    return df