def check_missing_values(df):
    return df.isnull().sum()


def check_duplicate_rows(df):
    return df.duplicated().sum()


def check_invalid_ages(df, min_age=16, max_age=59):
    return df[(df["age"] < min_age) | (df["age"] > max_age)]

def check_invalid_geographic_codes(df):
    invalid_current_state = df[df["currentStateCode"] <= 0]
    invalid_current_district = df[df["currentDistrictCode"] <= 0]
    invalid_permanent_state = df[df["permanentStateCode"] <= 0]

    return {
        "current_state": invalid_current_state,
        "current_district": invalid_current_district,
        "permanent_state": invalid_permanent_state,
    }

 
def check_state_code_consistency(df):
    current_state_mapping = (
        df.groupby("currentStateCode")["currentStateName"]
        .nunique()
    )

    permanent_state_mapping = (
        df.groupby("permanentStateCode")["permanentStateName"]
        .nunique()
    )

    return {
        "current_state": current_state_mapping,
        "permanent_state": permanent_state_mapping,
    }