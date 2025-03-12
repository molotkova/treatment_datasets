# compas-scores-two-years

This dataset contains general recidivism data. It tracks whether an individual reoffended in any way (not necessarily violent) within two years.

## Features

- `id`: A unique identifier for each individual in the dataset.
- `name`: Full name of the individual (often anonymized or pseudonymized).
- `first`: First name of the individual.
- `last`: Last name of the individual.
- `compas_screening_date`: The date when the COMPAS risk assessment was conducted.
- `sex`: The gender of the individual (e.g., Male, Female).
- `dob`: Date of birth of the individual.
- `age`: The age of the individual at the time of COMPAS assessment.
- `age_cat`: Age category of the individual (e.g., 25 and under, 26-45, 46 and older).
- `race`: The racial category of the individual (e.g., African-American, Caucasian, Hispanic, etc.).
- `juv_fel_count`: The number of juvenile felony offenses committed by the individual.
- `decile_score`: The COMPAS decile risk score (ranging from 1 to 10) predicting the likelihood of recidivism (higher scores indicate a higher risk).
- `juv_misd_count`: The number of juvenile misdemeanor offenses committed by the individual.
- `juv_other_count`: The number of other juvenile offenses not classified as felonies or misdemeanors.
- `priors_count`: The total number of prior offenses committed by the individual before the COMPAS assessment.
- `priors_count.1`: A duplicate or slightly modified version of `priors_count`, indicating the number of prior offenses.
- `days_b_screening_arrest`: The number of days between the individual's most recent arrest and the COMPAS screening date.
- `c_jail_in`: The date the individual was admitted to jail for the current case.
- `c_jail_out`: The date the individual was released from jail for the current case.
- `c_case_number`: The case number associated with the individual's most recent charge.
- `c_offense_date`: The date when the offense associated with the current case occurred.
- `c_arrest_date`: The date when the individual was arrested for the current case.
- `c_days_from_compas`: The number of days between the COMPAS screening date and the individual's current offense date.
- `c_charge_degree`: The degree of the charge for the current offense (e.g., M for misdemeanor, F for felony).
- `c_charge_desc`: A textual description of the current charge (e.g., Grand Theft, Drug Possession).
- `is_recid`: A binary indicator (`1 = Yes`, `0 = No`) of whether the individual reoffended at all (not necessarily within two years).
- `r_case_number`: The case number associated with the individual's recidivism charge (if applicable).
- `r_charge_degree`: The degree of the charge for the recidivism offense (e.g., M for misdemeanor, F for felony).
- `r_days_from_arrest`: The number of days between the individual's previous arrest and their recidivism offense (if applicable).
- `r_offense_date`: The date when the recidivism offense (if applicable) occurred.
- `r_charge_desc`: A textual description of the recidivism charge (e.g., Burglary, Drug Possession).
- `r_jail_in`: The date when the individual was admitted to jail for the recidivism charge.
- `r_jail_out`: The date when the individual was released from jail for the recidivism charge.
- `violent_recid`: A binary indicator (`1 = Yes`, `0 = No`) of whether the recidivism offense was violent.
- `is_violent_recid`: Another binary indicator (`1 = Yes`, `0 = No`) of whether the individual committed a violent recidivism offense.
- `vr_case_number`: The case number associated with the violent recidivism charge (if applicable).
- `vr_charge_degree`: The degree of the charge for the violent recidivism offense (e.g., M for misdemeanor, F for felony).
- `vr_offense_date`: The date when the violent recidivism offense (if applicable) occurred.
- `vr_charge_desc`: A textual description of the violent recidivism charge (e.g., Assault, Robbery).
- `type_of_assessment`: The type of COMPAS assessment conducted (e.g., Risk of General Recidivism).
- `decile_score.1`: The COMPAS decile score (1 to 10) associated with `type_of_assessment`.
- `score_text`: The risk category assigned based on the `decile_score` (e.g., Low, Medium, High).
- `screening_date`: The date when the COMPAS screening was conducted.
- `v_type_of_assessment`: The type of assessment related to violent recidivism risk (e.g., Risk of Violent Recidivism).
- `v_decile_score`: The COMPAS decile score (1 to 10) associated with the `v_type_of_assessment`.
- `v_score_text`: The risk category assigned based on the `v_decile_score` (e.g., Low, Medium, High).
- `v_screening_date`: The date when the COMPAS screening for violent recidivism was conducted.
- `in_custody`: The date when the individual was taken into custody.
- `out_custody`: The date when the individual was released from custody.
- `start`: The start date of the observation period for the individual's recidivism tracking.
- `end`: The end date of the observation period for tracking recidivism.
- `event`: Whether the individual reoffended (`1 = Yes`, `0 = No`) dutring the observation period (from `start` to `end`).
- `two_year_recid`: A binary indicator (`1 = Yes`, `0 = No`) of whether the individual reoffended within two years.