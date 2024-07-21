
## Web Link

https://resale-price-prediction-cv3e.onrender.com/
# Project Title

Singapore Resale Flat Prices Prediction

Welcome to the Singapore Resale Flat Prices Prediction project! This project involves the development of a machine learning model to predict resale prices of flats in Singapore. By leveraging historical transaction data, the goal is to assist potential buyers and sellers in estimating the resale value of a flat.




## Packages

Python

import Pandas

import pickle

import streamlit as st,
from streamlit_option_menu import option_menu
## Intro

The Singapore resale flat market is known for its competitiveness, making it challenging for individuals to accurately gauge the resale value of their property. This project aims to address this challenge by employing machine learning techniques to provide users with reliable resale price predictions based on various influential factors.
## Demo




## Scope of Work

1. Data Collection and Preprocessing:

Collect and clean historical resale flat transaction data from the Singapore Housing and Development Board (HDB).

2. Feature Engineering:

Extract relevant features such as town, flat type, storey range, floor area, flat model, and lease commence date. Create additional features to improve prediction accuracy.

3. Model Selection and Training:

Choose a suitable regression model and train it on the historical dataset.

4. Model Evaluation:

Assess the model's predictive performance using regression metrics like MAE, MSE, RMSE, and R2 Score.

5. Streamlit Web Application:

Develop an intuitive web application using Streamlit, allowing users to input flat details for price predictions.

6. Deployment on Render:

Deploy the Streamlit application on the Render platform or any cloud platform for online accessibility.

7. Testing and Validation:

Thoroughly test the deployed application to ensure accurate predictions and seamless functionality.
## Deployment

Take all the relevant data from the repository, like py file and all pickle files which are trained models file and load it in the appropariate variable in the py file.


To deploy this project run in command prompt

```bash
streamlit run app.py
```

check demo video...
## Note

All the manual enter values should be in numbers to perform the model correctly.

The Prediction model is with 98% accuracy.

Thanks...