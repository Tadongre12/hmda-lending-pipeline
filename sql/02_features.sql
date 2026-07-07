CREATE TABLE IF NOT EXISTS hmda_features AS SELECT *, 

loan_amount / income AS loan_to_income_ratio, 

CASE 
    WHEN action_taken IN(3, 7) THEN 1 
    WHEN action_taken IN (1, 2) THEN 0 
END AS is_denied, 

CASE 
    WHEN income < 50 THEN 'Low' 
    WHEN income < 100 THEN 'Medium' 
    WHEN income < 150 THEN 'High' 
    WHEN income < 200 THEN 'Very High' 
    ELSE 'Ultra High' 
END AS income_band, 

CASE 
    WHEN loan_amount < 200 THEN 'Low' 
    WHEN loan_amount < 400 THEN 'Medium' 
    WHEN loan_amount < 700 THEN 'High' 
    ELSE 'Very High' 
END AS loan_amount_band, 

CASE 
    WHEN applicant_age < 25 THEN '<25' 
    WHEN applicant_age < 32 THEN '25-32' 
    WHEN applicant_age < 45 THEN '33-45' 
    WHEN applicant_age < 65 THEN '45-65' 
    ELSE '65+' 
END AS applicant_age_band, 

debt_to_income_ratio + loan_to_value_ratio AS dti_ltv_risk

FROM hmda_clean