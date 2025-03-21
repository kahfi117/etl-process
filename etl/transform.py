import pandas as pd

def transform_data(df):
    # Ubah tipe data
    df["week_ending"] = pd.to_datetime(df["week_ending"])
    df.fillna(0, inplace=True)

    # Membuat tabel dimensi
    dim_date = df[["week_ending"]].drop_duplicates().reset_index(drop=True)
    dim_date["date_id"] = dim_date.index + 1

    dim_provider = df[["federal_provider_number", "provider_name", "provider_phone_number"]].drop_duplicates().reset_index(drop=True)
    dim_provider["provider_id"] = dim_provider.index + 1

    dim_location = df[["provider_address", "provider_city", "provider_state", "provider_zip_code", "county"]].drop_duplicates().reset_index(drop=True)
    dim_location["location_id"] = dim_location.index + 1

    dim_staff = df[["staff_weekly_confirmed_covid_19", "staff_total_confirmed_covid_19"]].drop_duplicates().reset_index(drop=True)
    dim_staff["staff_id"] = dim_staff.index + 1

    dim_bed_capacity = df[["number_of_all_beds", "total_number_of_occupied_beds"]].drop_duplicates().reset_index(drop=True)
    dim_bed_capacity["bed_capacity_id"] = dim_bed_capacity.index + 1

    # Gabungkan ID dari dimensi ke dalam fact table
    fact_covid_cases = df.merge(dim_date, on="week_ending")\
                         .merge(dim_provider, on=["provider_name", "provider_phone_number"], how="left")\
                         .merge(dim_location, on=["provider_address", "provider_city", "provider_state", "provider_zip_code", "county"], how="left")\
                         .merge(dim_staff, on=["staff_weekly_confirmed_covid_19", "staff_total_confirmed_covid_19"], how="left")\
                         .merge(dim_bed_capacity, on=["number_of_all_beds", "total_number_of_occupied_beds"], how="left")

    fact_covid_cases = fact_covid_cases[[
        "date_id", "provider_id", "location_id", "staff_id", "bed_capacity_id",
        "residents_weekly_confirmed_covid_19", "residents_total_confirmed_covid_19",
        "residents_weekly_all_deaths", "residents_total_all_deaths",
        "residents_weekly_covid_19_deaths", "residents_total_covid_19_deaths",
        "staff_weekly_confirmed_covid_19", "staff_total_confirmed_covid_19",
        "submitted_data", "passed_quality_assurance_check"
    ]]
    
    fact_covid_cases["fact_id"] = fact_covid_cases.index + 1

    return dim_date, dim_provider, dim_location, dim_staff, dim_bed_capacity, fact_covid_cases
