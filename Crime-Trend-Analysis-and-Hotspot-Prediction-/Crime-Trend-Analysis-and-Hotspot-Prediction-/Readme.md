                                                                          # Crime Trend Analysis and Hotspot Prediction Using Machine Learning

## Project Overview
This project focuses on analyzing crime trends and identifying crime hotspots using machine learning techniques. 
The system processes spatial and temporal crime data through a reproducible data pipeline and applies clustering 
methods to predict high-risk areas. The entire workflow is automated using Python and Airflow.

## Dataset
- Open government crime data portals
- link = https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-Present/ijzp-q8t2/data_preview

## Research Questions
1. What are the overall crime trends over time?
2. Can crime hotspots be identified using spatial (latitude and longitude) data?
3. How does the frequency of crimes vary across different locations?
4. Are there specific time periods (days or months) with higher crime occurrences?
5. Can unsupervised machine learning techniques effectively cluster high-risk crime areas?

## How to Run the Code
```bash
pip install -r requirements.txt
python src/data_ingestion/ingest_data.py
python src/data_cleaning/clean_data.py
python src/feature_engineering/features.py
python src/modeling/train_model.py
python src/evaluation/evaluate_model.py

## How to Run the Airflow DAG

Install Apache Airflow
Place the pipeline_dag.py file inside the dags/ directory
start Airflow services
airflow standalone
Trigger the DAG named crime_analysis_pipeline from the Airflow UI

## Folder Structure Explanation

dags/ – Contains the Airflow DAG for automating the pipeline
src/ – Core Python scripts for data ingestion, cleaning, feature engineering, modeling, and evaluation
data/ – Sample input data and intermediate processed files
figures/ – visualizations (PNG/PDF)
tables/ – tables and evaluation metrics (CSV)
