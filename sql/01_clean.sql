CREATE TABLE IF NOT EXISTS hmda_clean AS SELECT action_taken, loan_type, loan_purpose, lien_status, loan_amount, loan_to_value_ratio, interest_rate, income, debt_to_income_ratio, property_value, applicant_age, state_code, county_code, derived_race, derived_ethnicity, derived_sex, "denial_reason-1"
FROM hmda_raw
WHERE action_taken IN (1, 2, 3, 7)
AND loan_amount IS NOT NULL
AND income IS NOT NULL
AND loan_to_value_ratio IS NOT NULL
AND interest_rate IS NOT NULL
AND debt_to_income_ratio IS NOT NULL
AND property_value IS NOT NULL
AND loan_type IS NOT NULL
AND loan_purpose IS NOT NULL
AND lien_status IS NOT NULL
AND applicant_age IS NOT NULL
AND state_code IS NOT NULL
AND county_code IS NOT NULL