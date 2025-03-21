-- Tabel Dimensi: dim_date
CREATE TABLE dim_date (
    date_id INTEGER PRIMARY KEY,
    week_ending DATE NOT NULL
);

-- Tabel Dimensi: dim_provider
CREATE TABLE dim_provider (
    provider_id INTEGER PRIMARY KEY,
    federal_provider_number VARCHAR(10) UNIQUE NOT NULL,
    provider_name VARCHAR(255) NOT NULL,
    provider_phone_number VARCHAR(15)
);

-- Tabel Dimensi: dim_location
CREATE TABLE dim_location (
    location_id INTEGER PRIMARY KEY,
    provider_address VARCHAR(255) NOT NULL,
    provider_city VARCHAR(100) NOT NULL,
    provider_state CHAR(2) NOT NULL,
    provider_zip_code VARCHAR(10) NOT NULL,
    county VARCHAR(100) NOT NULL
);

-- Tabel Dimensi: dim_staff
CREATE TABLE dim_staff (
    staff_id INTEGER PRIMARY KEY,
    staff_weekly_confirmed_covid_19 INTEGER NOT NULL,
    staff_total_confirmed_covid_19 INTEGER NOT NULL
);

-- Tabel Dimensi: dim_bed_capacity
CREATE TABLE dim_bed_capacity (
    bed_capacity_id INTEGER PRIMARY KEY,
    number_of_all_beds INTEGER NOT NULL,
    total_number_of_occupied_beds INTEGER NOT NULL
);

-- Tabel Fakta: fact_covid_cases
CREATE TABLE fact_covid_cases (
    fact_id INTEGER PRIMARY KEY,
    date_id INTEGER NOT NULL,
    provider_id INTEGER NOT NULL,
    location_id INTEGER NOT NULL,
    staff_id INTEGER NOT NULL,
    bed_capacity_id INTEGER NOT NULL,
    residents_weekly_confirmed_covid_19 INTEGER NOT NULL,
    residents_total_confirmed_covid_19 INTEGER NOT NULL,
    residents_weekly_all_deaths INTEGER NOT NULL,
    residents_total_all_deaths INTEGER NOT NULL,
    residents_weekly_covid_19_deaths INTEGER NOT NULL,
    residents_total_covid_19_deaths INTEGER NOT NULL,
    staff_weekly_confirmed_covid_19 INTEGER NOT NULL,
    staff_total_confirmed_covid_19 INTEGER NOT NULL,
    submitted_data CHAR(1) CHECK (submitted_data IN ('Y', 'N')),
    passed_quality_assurance_check CHAR(1) CHECK (passed_quality_assurance_check IN ('Y', 'N')),

    -- Foreign Keys
    FOREIGN KEY (date_id) REFERENCES dim_date(date_id),
    FOREIGN KEY (provider_id) REFERENCES dim_provider(provider_id),
    FOREIGN KEY (location_id) REFERENCES dim_location(location_id),
    FOREIGN KEY (staff_id) REFERENCES dim_staff(staff_id),
    FOREIGN KEY (bed_capacity_id) REFERENCES dim_bed_capacity(bed_capacity_id)
);
