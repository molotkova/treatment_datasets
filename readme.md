# Treatment Dataset Repository

## Overview
This repository contains various datasets along with Jupyter notebooks for preprocessing. The datasets are provided in csv format for both raw and preprocessed data, and the notebooks provide preprocessing pipelines to clean, transform, and explore the data.

## Repository Structure
The `data/` folder contains a folder for each dataset consisting of 
* `data.csv` 
* `data_preprocessed.csv`
* `feature_description.md`
* `features.yaml`

The corresponding Jupyter notebooks are named after the dataset, i.e. `<dataset>.ipynb`. 

## Datasets
Each dataset is stored in the `data/` directory with a corresponding preprocessing notebook. Below is a brief description of the datasets:

* **MIMIC-III-sepsis**: This dataset is a subset of the MIMIC-III dataset and considers the data of patients that were diagnosed with "sepsis", "severe sepsis" and "septic shock". It can be used for different prediction tasks, more specifically whether a patient expires during hospitalization or after thirty days, or the length of ICU or hospital stay. 
More informations can be found [here](https://translational-medicine.biomedcentral.com/articles/10.1186/s12967-020-02620-5#additional-information).

* **COMPAS(-scores-two-years)**: This dataset contains general recidivism data. It tracks whether an individual reoffended in any way (not necessarily violent) within two years.

* **Diabetes**: The dataset represents ten years (1999-2008) of clinical care at 130 US hospitals and integrated delivery networks. Each row concerns hospital records of patients diagnosed with diabetes, who underwent laboratory, medications, and stayed up to 14 days. The goal is to determine the early readmission of the patient within 30 days of discharge.
More informations can be found [here](https://archive.ics.uci.edu/dataset/296/diabetes+130-us+hospitals+for+years+1999-2008).







