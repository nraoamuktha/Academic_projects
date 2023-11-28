# Airbnb Data Analysis and Predictive Modeling

## Project Overview
This project focuses on analyzing Airbnb listing data and predicting high booking rates using various machine learning techniques. The aim is to provide insights into factors influencing booking rates and enhance the decision-making process for hosts and the Airbnb platform.

## Data Sources
- **Airbnb Data**: Comprises of listings' details such as location, price, amenities, host information, etc.
- **External Data**: Includes additional datasets like population by zip code to enrich the analysis.

## Features
- **Data Loading and Cleaning**: The script includes comprehensive data loading, cleaning, and preprocessing steps to prepare the dataset for analysis.
- **Feature Engineering**: Extensive feature engineering to extract meaningful attributes from the dataset, including text mining from unstructured fields and integration of external data.
- **Predictive Modeling**: Implementation of various machine learning models such as Logistic Regression, Decision Trees, Random Forest, Ridge and Lasso Regression, K-Nearest Neighbors (KNN), and Boosting (XGBoost) to predict high booking rates.
- **Model Evaluation**: Detailed evaluation of each model's performance using metrics like accuracy and AUC-ROC, along with visualization of results.
- **Hyperparameter Tuning**: Techniques for optimizing model parameters to enhance prediction accuracy.

## Libraries Used
- `tidyverse`, `caret`, `tree`, `randomForest`, `gbm`, `splitstackshape`, `text2vec`, `tm`, `SnowballC`, `vip`, `pROC`, `ROCR`, `glmnet`, `naivebayes`, `ranger`, `xgboost`, `textdata`, `tidytext`, `quanteda`, `Matrix`, `modeest`, `stringr`, `stats`, `car`, `openxlsx`, `ggplot2`, `factoextra`.

## Key Functions and Methods
- **Data Merging and Transformation**: Techniques for merging external datasets and transforming features.
- **Text Mining and Sentiment Analysis**: Utilization of text data from listing descriptions to extract features and conduct sentiment analysis.
- **Clustering**: Application of k-means clustering for geographical data analysis.
- **Visualization**: Generating various plots and charts for exploratory data analysis.

## Results
- **Insights**: Provides insights into the relationship between different factors such as property type, room type, host response time, and their impact on booking rates.
- **Model Selection**: The script concludes with the selection of the most effective model based on performance metrics.

## Usage
- **Input Data**: The script expects CSV files containing Airbnb listing details and external datasets.
- **Execution**: Run the script in an R environment with the necessary libraries installed. Modify paths to data files as needed.
