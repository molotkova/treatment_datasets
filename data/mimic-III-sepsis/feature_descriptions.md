# MIMIC-III-sepsis


## Features
* `suspected_infection_time_poe_days` : Time in days from patient admission to suspected infection  
* `positiveculture_poe` : Indicator of a positive culture result at the point of entry (POE)  
* `blood_culture_positive` : Indicator if a blood culture test returned a positive result  
* `age` : Age of the patient in years  
* `is_male` : Indicator if the patient is male (1 = male, 0 = female)  
* `race_white` : Indicator if the patient is categorized as White (1 = White, 0 = other)  
* `race_black` : Indicator if the patient is categorized as Black (1 = Black, 0 = other)  
* `race_hispanic` : Indicator if the patient is categorized as Hispanic (1 = Hispanic, 0 = other)  
* `race_other` : Indicator if the patient belongs to other racial/ethnic categories  
* `metastatic_cancer` : Indicator if the patient has metastatic cancer  
* `diabetes` : Indicator if the patient has diabetes  
* `hospital_expire_flag` : Indicator if the patient expired during hospitalization  
* `thirtyday_expire_flag` : Indicator if the patient expired within 30 days of admission  
* `icu_los` : Length of ICU stay in days  
* `hosp_los` : Length of hospital stay in days  
* `sepsis_angus` : Indicator of sepsis based on the Angus criteria  
* `sepsis_martin` : Indicator of sepsis based on the Martin criteria  
* `sepsis_explicit` : Indicator of explicitly coded sepsis diagnosis  
* `septic_shock_explicit` : Indicator of explicitly coded septic shock diagnosis  
* `severe_sepsis_explicit` : Indicator of explicitly coded severe sepsis diagnosis  
* `sepsis_nqf` : Indicator of sepsis based on National Quality Forum (NQF) definition  
* `sepsis_cdc` : Indicator of sepsis based on CDC criteria  
* `sepsis_cdc_simple` : Simplified indicator of sepsis based on CDC criteria  
* `elixhauser_hospital` : Elixhauser comorbidity score for hospital mortality risk  
* `vent` : Indicator if the patient was mechanically ventilated  
* `sofa` : Sequential Organ Failure Assessment (SOFA) score  
* `lods` : Logistic Organ Dysfunction System (LODS) score  
* `sirs` : Systemic Inflammatory Response Syndrome (SIRS) score  
* `qsofa` : Quick SOFA (qSOFA) score for sepsis severity  
* `qsofa_sysbp_score` : qSOFA component based on systolic blood pressure  
* `qsofa_gcs_score` : qSOFA component based on Glasgow Coma Scale (GCS) score  
* `qsofa_resprate_score` : qSOFA component based on respiratory rate  
* `aniongap_min` : Minimum recorded anion gap value  
* `aniongap_max` : Maximum recorded anion gap value  
* `bicarbonate_min` : Minimum recorded bicarbonate value  
* `bicarbonate_max` : Maximum recorded bicarbonate value  
* `creatinine_min` : Minimum recorded creatinine value  
* `creatinine_max` : Maximum recorded creatinine value  
* `chloride_min` : Minimum recorded chloride value  
* `chloride_max` : Maximum recorded chloride value  
* `glucose_min` : Minimum recorded glucose level  
* `glucose_max` : Maximum recorded glucose level  
* `hematocrit_min` : Minimum recorded hematocrit value  
* `hematocrit_max` : Maximum recorded hematocrit value  
* `hemoglobin_min` : Minimum recorded hemoglobin value  
* `hemoglobin_max` : Maximum recorded hemoglobin value  
* `lactate_min` : Minimum recorded lactate value  
* `lactate_max` : Maximum recorded lactate value  
* `lactate_mean` : Mean recorded lactate value  
* `platelet_min` : Minimum recorded platelet count  
* `platelet_max` : Maximum recorded platelet count  
* `potassium_min` : Minimum recorded potassium level  
* `potassium_max` : Maximum recorded potassium level  
* `inr_min` : Minimum recorded International Normalized Ratio (INR)  
* `inr_max` : Maximum recorded International Normalized Ratio (INR)  
* `sodium_min` : Minimum recorded sodium level  
* `sodium_max` : Maximum recorded sodium level  
* `bun_min` : Minimum recorded Blood Urea Nitrogen (BUN) level  
* `bun_max` : Maximum recorded Blood Urea Nitrogen (BUN) level  
* `bun_mean` : Mean recorded Blood Urea Nitrogen (BUN) level  
* `wbc_min` : Minimum recorded white blood cell (WBC) count  
* `wbc_max` : Maximum recorded white blood cell (WBC) count  
* `wbc_mean` : Mean recorded white blood cell (WBC) count  
* `heartrate_min` : Minimum recorded heart rate  
* `heartrate_max` : Maximum recorded heart rate  
* `heartrate_mean` : Mean recorded heart rate  
* `sysbp_min` : Minimum recorded systolic blood pressure  
* `sysbp_max` : Maximum recorded systolic blood pressure  
* `sysbp_mean` : Mean recorded systolic blood pressure  
* `diasbp_min` : Minimum recorded diastolic blood pressure  
* `diasbp_max` : Maximum recorded diastolic blood pressure  
* `diasbp_mean` : Mean recorded diastolic blood pressure  
* `meanbp_min` : Minimum recorded mean arterial blood pressure  
* `meanbp_max` : Maximum recorded mean arterial blood pressure  
* `meanbp_mean` : Mean recorded mean arterial blood pressure  
* `resprate_min` : Minimum recorded respiratory rate  
* `resprate_max` : Maximum recorded respiratory rate  
* `resprate_mean` : Mean recorded respiratory rate  
* `tempc_min` : Minimum recorded body temperature (°C)  
* `tempc_max` : Maximum recorded body temperature (°C)  
* `tempc_mean` : Mean recorded body temperature (°C)  
* `spo2_min` : Minimum recorded oxygen saturation (SpO2)  
* `spo2_max` : Maximum recorded oxygen saturation (SpO2)  
* `spo2_mean` : Mean recorded oxygen saturation (SpO2)  
* `glucose_mean` : Mean recorded glucose level  
* `rrt` : Indicator if the patient received renal replacement therapy (RRT)  
* `urineoutput` : Total urine output during ICU stay  
* `src_blood_culture` : Indicator if a blood culture sample was taken  
* `src_mrsa_screen` : Indicator if a MRSA screening test was performed  
* `src_urine` : Indicator if a urine sample was taken  
* `src_swab` : Indicator if a swab sample was taken  
* `src_others` : Indicator if other microbiological samples were collected  
* `fs_med` : Indicator if the patient was in a medical ICU  
* `fs_cmed` : Indicator if the patient was in a cardiac medical ICU  
* `fs_surg` : Indicator if the patient was in a surgical ICU  
* `fs_traum` : Indicator if the patient was in a trauma ICU  
* `fs_nsurg` : Indicator if the patient was in a neurosurgical ICU  
* `fs_nmed` : Indicator if the patient was in a neurological medical ICU  
* `fs_ortho` : Indicator if the patient was in an orthopedic ICU  
* `fs_omed` : Indicator if the patient was in an other medical ICU  
* `fs_others` : Indicator if the patient was in an unclassified ICU  
