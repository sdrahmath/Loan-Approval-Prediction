# Loan Approval Prediction App

## Introduction

This project is an interactive web application that predicts the approval status of a loan based on various user inputs. The prediction is made using a Support Vector Machine (SVM) classifier model, which has been trained on historical loan approval data.

## Methodology

1. **Data Collection**: The historical loan approval dataset is collected, containing information about previous loan applicants along with the final loan approval decision.

2. **Data Preprocessing**: The data is preprocessed to handle missing values, encode categorical variables, and scale numerical features to a common range.

3. **Model Selection**: The Support Vector Machine (SVM) algorithm is chosen for this binary classification task due to its ability to handle both linear and non-linear decision boundaries.

4. **Model Training**: The preprocessed data is split into training and testing sets, and the SVM classifier is trained on the training data.

5. **Web App Development**: The web application is developed using Streamlit, a Python library for creating interactive web apps.

6. **Prediction**: Users can input their details, such as gender, marital status, education, income, loan amount, etc., into the web app. The SVM classifier then predicts whether the loan will be approved or not based on the provided information.

## Technology Used

- Python
- Libraries: `streamlit`, `pickle`, `numpy`, `sklearn` (for SVM model)

## Output

### Sample Screenshots

![Loan Prediction App](https://github.com/sdrahmath/Loan-Approval-Prediction/blob/main/outputs/Laon%20Prediction.gif)

## Conclusion

The Loan Approval Prediction App provides an easy-to-use interface for users to check their loan approval status based on their personal and financial information. The SVM classifier performs reasonably well in predicting loan approval outcomes. However, further improvements could be made by incorporating more data and exploring other machine learning algorithms.

## Acknowledgements

- The loan approval dataset used for training the model was sourced from Kaggle
- We would like to thank the developers of Streamlit for providing an excellent framework for creating interactive web applications.

## Future Improvements

- Incorporate more features and data sources to enhance the model's predictive capabilities.
- Experiment with different machine learning algorithms to compare their performance with the SVM classifier.
- Deploy the web app to a production environment for public use.
