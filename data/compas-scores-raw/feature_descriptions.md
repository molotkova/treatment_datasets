# compas-scores-raw
This dataset contains COMPAS assessments used evaluating the risk of recidivism.

## Features

- `Person_ID`: A unique identifier assigned to each individual.
- `AssessmentID`: A unique identifier for each COMPAS assessment performed.
- `Case_ID`: A unique identifier for the legal case associated with the assessment.
- `Agency_Text`: The name of the agency conducting the assessment.
- `LastName`: The last name of the individual being assessed.
- `FirstName`: The first name of the individual being assessed.
- `MiddleName`: The middle name of the individual being assessed (if available).
- `Sex_Code_Text`: The gender of the individual (e.g., Male, Female).
- `Ethnic_Code_Text`: The ethnic category of the individual (e.g., African-American, Caucasian, Hispanic, etc.).
- `DateOfBirth`: The date of birth of the individual.
- `ScaleSet_ID`: A unique identifier for the set of risk assessment scales used in the COMPAS evaluation.
- `ScaleSet`: The name of the specific risk scale set used in the assessment.
- `AssessmentReason`: The reason why the assessment was conducted (e.g., pre-trial, post-conviction, parole consideration).
- `Language`: The primary language spoken by the individual.
- `LegalStatus`: The current legal status of the individual at the time of the assessment.
- `CustodyStatus`: The custody status of the individual (e.g., in custody, released).
- `MaritalStatus`: The marital status of the individual (e.g., Single, Married, Divorced).
- `Screening_Date`: The date when the COMPAS assessment was conducted.
- `RecSupervisionLevel`: The recommended supervision level assigned based on the risk assessment.
- `RecSupervisionLevelText`: A textual description of the recommended supervision level (e.g., Low, Medium, High).
- `Scale_ID`: A unique identifier for the specific risk assessment scale used.
- `DisplayText`: The name or description of the risk assessment scale.
- `RawScore`: The raw score assigned to the individual based on the COMPAS assessment.
- `DecileScore`: The risk score on a 1-10 scale, indicating the likelihood of recidivism.
- `ScoreText`: The categorical risk classification based on the decile score (e.g., Low, Medium, High).
- `AssessmentType`: The type of COMPAS assessment conducted (e.g., General Recidivism, Violent Recidivism).
- `IsCompleted`: A binary indicator (`1 = Yes`, `0 = No`) indicating whether the assessment was completed.
- `IsDeleted`: A binary indicator (`1 = Yes`, `0 = No`) indicating whether the assessment was deleted.
