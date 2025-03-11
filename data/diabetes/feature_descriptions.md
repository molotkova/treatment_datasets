# Diabetes
The dataset represents ten years (1999-2008) of clinical care at 130 US hospitals and integrated delivery networks. Each row concerns hospital records of patients diagnosed with diabetes, who underwent laboratory, medications, and stayed up to 14 days. The goal is to determine the early readmission of the patient within 30 days of discharge.

## Features
Can also be found in table 1 of https://www.hindawi.com/journals/bmri/2014/781670/

See `data/IDS_mapping.csv` for more detail on categorical features 

* `encounter_id` : Unique identifier of an encounter  
* `patient_nbr` : Unique identifier of a patient  
* `race` : Values: Caucasian, Asian, African American, Hispanic, and other 
* `gender` : Values: male, female, and unknown/invalid  
* `age` : Grouped in 10-year intervals: [0, 10), [10, 20), ..., [90, 100)  
* `weight` : Weight in pounds 
* `admission_type_id` : Integer identifier corresponding to 9 distinct values, e.g., emergency, urgent, elective, newborn, and not available  
* `discharge_disposition_id` : Integer identifier corresponding to 29 distinct values, e.g., discharged to home, expired, and not available  
* `admission_source_id` : Integer identifier corresponding to 21 distinct values, e.g., physician referral, emergency room, and transfer from a hospital  
* `time_in_hospital` : Integer number of days between admission and discharge  
* `payer_code` : Integer identifier corresponding to 23 distinct values, e.g., Blue Cross/Blue Shield, Medicare, and self-pay 
* `medical_specialty` : Integer identifier of a specialty of the admitting physician, corresponding to 84 distinct values, e.g., cardiology, internal medicine, family/general practice, and surgeon  
* `num_lab_procedures` : Number of lab tests performed during the encounter  
* `num_procedures` : Number of procedures (other than lab tests) performed during the encounter  
* `num_medications` : Number of distinct generic names administered during the encounter  
* `number_outpatient` : Number of outpatient visits of the patient in the year preceding the encounter  
* `number_emergency` : Number of emergency visits of the patient in the year preceding the encounter  
* `number_inpatient` : Number of inpatient visits of the patient in the year preceding the encounter  
* `diag_1` : The primary diagnosis (coded as first three digits of ICD9); 848 distinct values  
* `diag_2` : Secondary diagnosis (coded as first three digits of ICD9); 923 distinct values 
* `diag_3` : Additional secondary diagnosis (coded as first three digits of ICD9); 954 distinct values 
* `number_diagnoses` : Number of diagnoses entered into the system  
* `max_glu_serum` : Indicates the range of the result or if the test was not taken. Values: >200, >300, normal, and none if not measured  
* `A1Cresult` : Indicates the range of the result or if the test was not taken. Values: >8 (>8%), >7 (>7% but <8%), normal (<7%), and none if not measured  
* `metformin` : Indicates whether the drug was prescribed or there was a dosage change (Values: up, down, steady, no)  
* `repaglinide` : Indicates whether the drug was prescribed or there was a dosage change (Values: up, down, steady, no)  
* `nateglinide` : Indicates whether the drug was prescribed or there was a dosage change (Values: up, down, steady, no)  
* `chlorpropamide` : Indicates whether the drug was prescribed or there was a dosage change (Values: up, down, steady, no)  
* `glimepiride` : Indicates whether the drug was prescribed or there was a dosage change (Values: up, down, steady, no)  
* `acetohexamide` : Indicates whether the drug was prescribed or there was a dosage change (Values: up, down, steady, no)  
* `glipizide` : Indicates whether the drug was prescribed or there was a dosage change (Values: up, down, steady, no)  
* `glyburide` : Indicates whether the drug was prescribed or there was a dosage change (Values: up, down, steady, no)  
* `tolbutamide` : Indicates whether the drug was prescribed or there was a dosage change (Values: up, down, steady, no)  
* `pioglitazone` : Indicates whether the drug was prescribed or there was a dosage change (Values: up, down, steady, no)  
* `rosiglitazone` : Indicates whether the drug was prescribed or there was a dosage change (Values: up, down, steady, no)  
* `acarbose` : Indicates whether the drug was prescribed or there was a dosage change (Values: up, down, steady, no)  
* `miglitol` : Indicates whether the drug was prescribed or there was a dosage change (Values: up, down, steady, no)  
* `troglitazone` : Indicates whether the drug was prescribed or there was a dosage change (Values: up, down, steady, no)  
* `tolazamide` : Indicates whether the drug was prescribed or there was a dosage change (Values: up, down, steady, no)  
* `examide` : Indicates whether the drug was prescribed or there was a dosage change (Values: up, down, steady, no)  
* `citoglipton` : Indicates whether the drug was prescribed or there was a dosage change (Values: up, down, steady, no)  
* `insulin` : Indicates whether the drug was prescribed or there was a dosage change (Values: up, down, steady, no)  
* `glyburide-metformin` : Indicates whether the drug was prescribed or there was a dosage change (Values: up, down, steady, no)  
* `glipizide-metformin` : Indicates whether the drug was prescribed or there was a dosage change (Values: up, down, steady, no)  
* `glimepiride-pioglitazone` : Indicates whether the drug was prescribed or there was a dosage change (Values: up, down, steady, no)  
* `metformin-rosiglitazone` : Indicates whether the drug was prescribed or there was a dosage change (Values: up, down, steady, no)  
* `metformin-pioglitazone` : Indicates whether the drug was prescribed or there was a dosage change (Values: up, down, steady, no)  
* `change` : Indicates if there was a change in diabetic medications (Values: change, no change)  
* `diabetesMed` : Indicates if there was any diabetic medication prescribed (Values: yes, no)  
* `readmitted` : Days to inpatient readmission (Values: <30, >30, No)  

